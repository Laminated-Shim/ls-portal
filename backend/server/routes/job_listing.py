from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import json
import requests

from server.models.vet_classic import orelease

router = APIRouter()

url = "http://192.168.0.147:81/api/v2/VETquery"

@router.get("/", response_description="get orelease")
async def get_orelease(start_date: str, end_date: str, status: str) -> List[orelease.Orelease]:
    start_date_object = datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date_object = datetime.strptime(end_date, '%m-%d-%Y').date()
    start_date_string = f"{{^{start_date_object.year}-{start_date_object.month}-{start_date_object.day}}}"
    end_date_string = f"{{^{end_date_object.year}-{end_date_object.month}-{end_date_object.day}}}"

    sql = f"SELECT ol_order_num, ol_rel_date, ol_shipby_date, ol_sch_qty, ol_rel_number \
                        FROM [orelease] \
                        WHERE (orelease.ol_rel_date >= {start_date_string} AND orelease.ol_rel_date <= {end_date_string}) \
                        AND (orelease.ol_rel_stat = '{status}') \
                        ORDER BY orelease.ol_rel_date;"
    
    payload = json.dumps(sql)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data['data']['value']
    else:
        return HTTPException(status_code = response.status_code, detail = response.reason)
   