from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional
from datetime import datetime


class Mach_typ(BaseModel):
    mt_mach_code: Optional[str] = Field(max_length=5, default=None)
    mt_mach_desc: Optional[str] = Field(max_length=20, default=None)
    mt_caltype: Optional[str] = Field(max_length=1, default=None)
    mt_cut_off: Optional[Decimal] = None
    mt_rate: Optional[Decimal] = None
    mt_setup_rate: Optional[Decimal] = None
    mt_max_speed: Optional[Decimal] = None
    mt_max_feed: Optional[Decimal] = None
    mt_notes: Optional[str] = Field(max_length=2147483647, default=None)
    mt_cycle: Optional[str] = Field(max_length=1, default=None)
    mt_def_hrs: Optional[Decimal] = None
    mt_location: Optional[str] = Field(max_length=10, default=None)
    mt_mach_group: Optional[str] = Field(max_length=10, default=None)
    mt_sched: Optional[bool] = False
    mt_burd_rate: Optional[Decimal] = None
    mt_pop: Optional[Decimal] = None
    mt_de_id: Optional[str] = Field(max_length=2, default=None)
    mt_sell_rate: Optional[Decimal] = None
    mt_cb_rate: Optional[Decimal] = None
    mt_usenote: Optional[bool] = False
    mt_infinite: Optional[bool] = False
    mt_position: Optional[Decimal] = None
    mt_nowork: Optional[bool] = False
    mt_il_id: Optional[str] = Field(max_length=10, default=None)
    mt_queue: Optional[Decimal] = None
    mt_ib_id: Optional[str] = Field(max_length=10, default=None)
    mt_is_sub: Optional[bool] = False
    mt_supp_code: Optional[str] = Field(max_length=6, default=None)
    mt_dist_code: Optional[str] = Field(max_length=2, default=None)
    mt_workcell: Optional[bool] = False
    mt_useburden: Optional[bool] = False
    mt_il_id_wip: Optional[str] = Field(max_length=10, default=None)
    mt_secondary: Optional[bool] = False
    mt_unattend_burd: Optional[Decimal] = None
    mt_line: Optional[Decimal] = None
    mt_spindles: Optional[int] = None
    mt_fixed_asset_no: Optional[str] = Field(max_length=40, default=None)
    mt_mincharge: Optional[Decimal] = None
    mt_features: Optional[str] = Field(max_length=20, default=None)
    mt_inactive: Optional[bool] = False
    mt_id_code: Optional[str] = Field(max_length=10, default=None)
    mt_packaging: Optional[bool] = False
    mt_prod_code: Optional[str] = Field(max_length=2, default=None)
    mt_sortby: Optional[Decimal] = None
    mt_barend_len: Optional[Decimal] = None
    mt_bufferhours: Optional[Decimal] = None
    mt_partcounter: Optional[Decimal] = None
    mt_hourscounter: Optional[Decimal] = None
    mt_virtual_type: Optional[Decimal] = None
    mt_emp_id: Optional[str] = Field(max_length=5, default=None)
    mt_useinjc: Optional[bool] = False
    mt_setup_qty: Optional[Decimal] = None
    mt_maneng_id: Optional[str] = Field(max_length=5, default=None)
    mt_assigned_emp_id: Optional[str] = Field(max_length=5, default=None)
    mt_type: Optional[int] = None
    mt_assigned_emp_id2: Optional[str] = Field(max_length=5, default=None)
    mt_assigned_emp_id3: Optional[str] = Field(max_length=5, default=None)
    mt_mmexport: Optional[bool] = False
    mt_minmax: Optional[Decimal] = None
    mt_usecounters: Optional[bool] = False
