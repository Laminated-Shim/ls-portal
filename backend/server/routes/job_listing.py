from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import date
import json
import requests
import asyncio
import aiohttp
import time

from server.models.job_listing import JobListing

router = APIRouter()

url = "http://192.168.0.147:81/api/v2/VETquery"


# @router.get("/orelease", response_description="get orelease")
async def get_orelease(
    start_date: date, end_date: date, status: List[str] = Query(None)
) -> List[JobListing.Orelease]:
    try:
        # if len(status) > 1:
        #     raise HTTPException(status_code=400, detail=f"Bad status code '{status}'")
        status_list = ",".join(
                [f"'{_status}'" for _status in status]
            )

        sql = f"SELECT ol_order_num, ol_rel_date, ol_shipby_date, ol_sch_qty, ol_rel_number, ol_rel_stat \
                    FROM [orelease] \
                    WHERE (orelease.ol_rel_date >= {{^{start_date}}} AND orelease.ol_rel_date <= {{^{end_date}}}) \
                    AND  INLIST (orelease.ol_rel_stat, {status_list}) \
                    ORDER BY orelease.ol_rel_date;"

        payload = json.dumps(sql)
        headers = {"Content-Type": "application/json"}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=payload, ssl=False
            ) as response:
                data = await response.json()
                return data["data"]["value"]

    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Bad request if date format is incorrect
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )  # Internal server error for other issues


# @router.post("/orders", response_description="get orders")
async def get_orders(job_numbers: List[str]) -> List[JobListing.Order]:
    try:
        list = []
        chunk_size = 25
        order_number_chunks = [
            job_numbers[i : i + chunk_size]
            for i in range(0, len(job_numbers), chunk_size)
        ]

        headers = {"Content-Type": "application/json"}

        async def fetch_data(order_number_chunk):
            code_list = ",".join(
                [f"'{order_number}'" for order_number in order_number_chunk]
            )

            sql = f"""
                SELECT or_order_num, or_cust_code, or_po_num, or_part_num, or_sord_num, or_cpu, or_quote_num, or_stat_notes
                FROM [order]
                WHERE INLIST (or_order_num, {code_list})"""

            payload = json.dumps(sql)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, headers=headers, data=payload, ssl=False
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["data"]["value"]
                    else:
                        raise HTTPException(
                            status_code=response.status, detail=response.text
                        )

        tasks = [
            fetch_data(order_number_chunk) for order_number_chunk in order_number_chunks
        ]
        results = await asyncio.gather(*tasks)

        for result in results:
            list.extend(result)

        return list

    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Bad request if date format is incorrect
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )  # Internal server error for other issues


# @router.post("/operations", response_description="get job operations")
async def get_operations(job_numbers: List[str]) -> List[JobListing.Operation]:
    try:
        list = []
        chunk_size = 25
        order_number_chunks = [
            job_numbers[i : i + chunk_size]
            for i in range(0, len(job_numbers), chunk_size)
        ]

        headers = {"Content-Type": "application/json"}

        async def fetch_data(order_number_chunk):
            code_list = ",".join(
                [f"'{order_number}'" for order_number in order_number_chunk]
            )

            sql = f"""
                SELECT a.ao_order_num, a.ao_mach_code, a.ao_complete, a.ao_comp_date, b.mt_de_id, b.mt_mach_desc, c.de_desc
                FROM [aoperate] AS a
                JOIN [mach_typ] AS b ON a.ao_mach_code = b.mt_mach_code
                JOIN [ac_dept] AS c ON b.mt_de_id = c.de_id
                WHERE INLIST (a.ao_order_num, {code_list})
                    AND a.ao_exclude = 0
                GROUP BY a.ao_order_num, a.ao_mach_code, b.mt_de_id, b.mt_mach_desc, c.de_desc
                ORDER BY a.ao_op_num;
                """

            payload = json.dumps(sql)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, headers=headers, data=payload, ssl=False
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["data"]["value"]
                    else:
                        raise HTTPException(
                            status_code=response.status, detail=response.text
                        )

        tasks = [
            fetch_data(order_number_chunk) for order_number_chunk in order_number_chunks
        ]
        results = await asyncio.gather(*tasks)

        for result in results:
            list.extend(result)

        return list

    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Bad request if date format is incorrect
    except aiohttp.ClientError as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )  # Internal server error for other issues


# @router.post("/jobcards", response_description="get job cards")
async def get_job_cards(job_numbers: List[str]) -> List[JobListing.JobCard]:
    try:
        list = []
        chunk_size = 25
        chunks = [
            job_numbers[i : i + chunk_size]
            for i in range(0, len(job_numbers), chunk_size)
        ]

        headers = {"Content-Type": "application/json"}

        async def fetch_data(chunk):
            code_list = ",".join([f"'{order_number}'" for order_number in chunk])

            sql = f"""
            SELECT ajcard.aj_run_date, ajcard.aj_time1, mach_typ.mt_mach_desc, employee.em_emp_name, ajcard.aj_tot_time, jcardman.jc_order_num
            FROM jcardman 
                INNER JOIN (ajcard 
                INNER JOIN employee 
                    ON ajcard.aj_emp_id = employee.em_emp_id) 
                    ON jcardman.jc_aj_id = ajcard.aj_id
                INNER JOIN mach_typ ON ajcard.aj_mach_code = mach_typ.mt_mach_code
            WHERE INLIST (jcardman.jc_order_num, {code_list})
            GROUP BY ajcard.aj_run_date, ajcard.aj_time1, mach_typ.mt_mach_desc, employee.em_emp_name, ajcard.aj_tot_time, jcardman.jc_order_num
            ORDER BY ajcard.aj_run_date;
            """

            payload = json.dumps(sql)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, headers=headers, data=payload, ssl=False
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["data"]["value"]
                    else:
                        raise HTTPException(
                            status_code=response.status, detail=response.text
                        )

        tasks = [fetch_data(chunk) for chunk in chunks]
        results = await asyncio.gather(*tasks)

        for result in results:
            list.extend(result)

        return list

    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Bad request if date format is incorrect
    except aiohttp.ClientError as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )  # Internal server error for other issues


# @router.post("/csrs", response_description="get customer sales reps")
async def get_csr(customer_codes: List[str]) -> List:
    try:
        list = []
        chunk_size = 25
        chunks = [
            customer_codes[i : i + chunk_size]
            for i in range(0, len(customer_codes), chunk_size)
        ]

        headers = {"Content-Type": "application/json"}

        async def fetch_data(chunk):
            code_list = ",".join([f"'{customer_codes}'" for customer_codes in chunk])

            sql = f"SELECT cu.cu_cust_code, e.em_emp_name, e.em_emp_id \
                FROM [q_cust] AS cu \
                JOIN [employee] AS e ON cu.cu_emp_id = e.em_emp_id \
                WHERE INLIST (cu.cu_cust_code , {code_list});"

            payload = json.dumps(sql)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, headers=headers, data=payload, ssl=False
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["data"]["value"]
                    else:
                        raise HTTPException(
                            status_code=response.status, detail=response.text
                        )

        tasks = [fetch_data(chunk) for chunk in chunks]
        results = await asyncio.gather(*tasks)

        for result in results:
            list.extend(result)

        return list

    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Bad request if date format is incorrect
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )  # Internal server error for other issues



# https://lsp.api.local/joblisting?start_date=2023-02-28&end_date=2024-05-28&status=O
@router.get("", response_description="Get Job Listing Data")
async def get_job_listings(
    start_date: date, end_date: date, status: List[str] = Query(None)
) -> List[JobListing]:
    tic = time.perf_counter()

    # Fetch data
    orelease: List[JobListing.Orelease] = await get_orelease(
        start_date, end_date, status
    )
    job_list: List[str] = [job["ol_order_num"] for job in orelease]

    get_orders_task = get_orders(job_list)
    get_operations_task = get_operations(job_list)
    get_job_cards_task = get_job_cards(job_list)

    orders, operations, jobcards = await asyncio.gather(
        get_orders_task, get_operations_task, get_job_cards_task
    )

    # Fetch customer codes
    customer_codes = set(order["or_cust_code"] for order in orders)
    get_csrs_task = get_csr(list(customer_codes))
    customers = await asyncio.gather(get_csrs_task)

    # Index orders by order number
    orders_index = {
        order["or_order_num"]: JobListing.Order(**order) for order in orders
    }

    # Index customers by customer code
    customers_index = {
        customer["cu_cust_code"]: JobListing.Csr(**customer)
        for customer in customers[0]
    }

    job_listings = []

    for job in orelease:
        job_listing = JobListing()
        job_listing.orelease = job

        # Find corresponding order and customer using indexes
        order = orders_index.get(job["ol_order_num"])
        if order:
            job_listing.order = order

            customer_code = order.or_cust_code
            customer = customers_index.get(customer_code)
            if customer:
                job_listing.csr = customer

        # Populate operations using list comprehension
        job_listing.operations.extend(
            [
                JobListing.Operation(**operation)
                for operation in operations
                if job["ol_order_num"] == operation["ao_order_num"]
            ]
        )

        # Populate job cards using list comprehension
        job_listing.job_cards.extend(
            [
                JobListing.JobCard(**jobcard)
                for jobcard in jobcards
                if job["ol_order_num"] == jobcard["jc_order_num"]
            ]
        )

        job_listings.append(job_listing)

    toc = time.perf_counter()
    print(f"task {toc - tic:0.4f} seconds.")

    return job_listings
