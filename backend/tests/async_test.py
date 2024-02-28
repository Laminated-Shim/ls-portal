import asyncio
import time
import aiohttp


async def get_list():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://lsp.api.local/joblisting/orelease?start_date=2021-02-28&end_date=2024-05-28&status=O",
            ssl=False,
        ) as response:
            return await response.json()


async def func1(jobs):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://lsp.api.local/joblisting/orders", json=jobs, ssl=False
        ) as response:
            result = await response.json()
            return result


async def func2(jobs):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://lsp.api.local/joblisting/operations", json=jobs, ssl=False
        ) as response:
            result = await response.json()
            return result


async def func3(jobs):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://lsp.api.local/joblisting/jobcards", json=jobs, ssl=False
        ) as response:
            result = await response.json()
            return result


async def func4(customers):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://lsp.api.local/joblisting/csrs", json=customers, ssl=False
        ) as response:
            result = await response.json()
            return result


async def main():
    tic = time.perf_counter()
    jobs = await get_list()
    job_list = [job["ol_order_num"] for job in jobs]

    # Create tasks to execute the functions concurrently
    task1 = func1(job_list)
    task2 = func2(job_list)
    task3 = func3(job_list)

    # Wait for all tasks to complete
    orders, operations, jobcards = await asyncio.gather(task1, task2, task3)

    customer_codes = []
    for order in orders:
        if order["or_cust_code"] not in customer_codes:
            customer_codes.append(order["or_cust_code"])
    task4 = func4(customer_codes)
    customers = await asyncio.gather(task4)

    for job in jobs:
        for order in orders:
            if "cu_cust_code" not in job:
                for customer in customers[0]:
                    if order["or_cust_code"] == customer["cu_cust_code"]:
                        job.update(customer)
                        break
            if job["ol_order_num"] == order["or_order_num"]:
                job.update(order)
                break
        for operation in operations:
            if job["ol_order_num"] == operation["ao_order_num"]:
                if "operations" not in job:
                    job["operations"] = []
                job["operations"].append(operation)
        for jobcard in jobcards:
            if job["ol_order_num"] == jobcard["jc_order_num"]:
                if "job_cards" not in job:
                    job["job_cards"] = []
                job["job_cards"].append(jobcard)

    toc = time.perf_counter()
    #print(jobs[50])
    print(f"task {toc - tic:0.4f} seconds.")


# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
