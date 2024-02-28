from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional
from datetime import datetime


class Orelease(BaseModel):
    ol_order_num: Optional[str] = Field(max_length=12, default=None)
    ol_rel_date: Optional[datetime] = None
    ol_rel_number: Optional[Decimal] = None
    ol_rel_qty: Optional[Decimal] = None
    ol_rel_prod: Optional[Decimal] = None
    ol_rel_bal: Optional[Decimal] = None
    ol_rel_sch: Optional[Decimal] = None
    ol_rel_ship: Optional[Decimal] = None
    ol_quantity: Optional[Decimal] = None
    ol_priority: Optional[Decimal] = None
    ol_il: Optional[Decimal] = None
    ol_end_date: Optional[datetime] = None
    ol_fi: Optional[str] = Field(max_length=1, default=None)
    ol_start_date: Optional[datetime] = None
    ol_po_num: Optional[str] = Field(max_length=25, default=None)
    ol_sch_qty: Optional[Decimal] = None
    ol_sch_method: Optional[str] = Field(max_length=1, default=None)
    ol_lead_time: Optional[Decimal] = None
    ol_ph: Optional[str] = Field(max_length=1, default=None)
    ol_track_num: Optional[str] = Field(max_length=15, default=None)
    ol_proj_start: Optional[datetime] = None
    ol_rel_stat: Optional[str] = Field(max_length=1, default=None)
    ol_sched: Optional[bool] = False
    ol_comp_date: Optional[datetime] = None
    ol_lock: Optional[bool] = False
    ol_cont_cnt: Optional[str] = Field(max_length=10, default=None)
    ol_cont_type: Optional[str] = Field(max_length=10, default=None)
    ol_cont_desc: Optional[str] = Field(max_length=20, default=None)
    ol_cont_weight: Optional[str] = Field(max_length=10, default=None)
    ol_lot: Optional[str] = Field(max_length=20, default=None)
    ol_insp_date: Optional[datetime] = None
    ol_released: Optional[bool] = False
    ol_notes: Optional[str] = Field(max_length=2147483647, default=None)
    ol_fab_date: Optional[datetime] = None
    ol_shipby_date: Optional[datetime] = None
    ol_planning_date: Optional[datetime] = None
    ol_ordstatus: Optional[str] = Field(max_length=10, default=None)
    ol_expedite: Optional[str] = Field(max_length=10, default=None)
    ol_owner: Optional[str] = Field(max_length=5, default=None)
    ol_status1: Optional[str] = Field(max_length=50, default=None)
    ol_status2: Optional[str] = Field(max_length=50, default=None)
    ol_matverify: Optional[bool] = False
