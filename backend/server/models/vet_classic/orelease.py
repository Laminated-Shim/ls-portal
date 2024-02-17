from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime
from typing import Optional


class Orelease(BaseModel):
    ol_order_num: str = Field(max_length=12)
    ol_rel_date: datetime
    ol_rel_number: Decimal
    ol_rel_qty: Decimal
    ol_rel_prod: Decimal
    ol_rel_bal: Decimal
    ol_rel_sch: Decimal
    ol_rel_ship: Decimal
    ol_quantity: Decimal
    ol_priority: Decimal
    ol_il: Decimal
    ol_end_date: datetime
    ol_fi: str = Field(max_length=1)
    ol_start_date: datetime
    ol_po_num: str = Field(max_length=25)
    ol_sch_qty: Decimal
    ol_sch_method: str = Field(max_length=1)
    ol_lead_time: Decimal
    ol_ph: str = Field(max_length=1)
    ol_track_num: str = Field(max_length=15)
    ol_proj_start: datetime
    ol_rel_stat: str = Field(max_length=1)
    ol_sched: bool = False
    ol_comp_date: datetime
    ol_lock: bool = False
    ol_cont_cnt: str = Field(max_length=10)
    ol_cont_type: str = Field(max_length=10)
    ol_cont_desc: str = Field(max_length=20)
    ol_cont_weight: str = Field(max_length=10)
    ol_lot: str = Field(max_length=20)
    ol_insp_date: datetime
    ol_released: bool = False
    ol_notes: str = Field(max_length=2147483647)
    ol_fab_date: datetime
    ol_shipby_date: datetime
    ol_planning_date: datetime
    ol_ordstatus: str = Field(max_length=10)
    ol_expedite: str = Field(max_length=10)
    ol_owner: str = Field(max_length=5)
    ol_status1: str = Field(max_length=50)
    ol_status2: str = Field(max_length=50)
    ol_matverify: bool = False
