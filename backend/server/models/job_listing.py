from pydantic import BaseModel, Field, computed_field
from decimal import Decimal
from datetime import datetime, timedelta
from typing import Optional, List


class JobListing(BaseModel):
    class Settings:
        name = "Job Listing"

    class Orelease(BaseModel):
        ol_order_num: Optional[str] = Field(max_length=12, default=None)
        ol_rel_date: Optional[datetime] = None
        ol_shipby_date: Optional[datetime] = None
        ol_sch_qty: Optional[Decimal] = None
        ol_rel_number: Optional[Decimal] = None

    class Order(BaseModel):
        or_order_num: Optional[str] = Field(max_length=12, default=None)
        or_cust_code: Optional[str] = Field(max_length=6, default=None)
        or_po_num: Optional[str] = Field(max_length=25, default=None)
        or_part_num: Optional[str] = Field(max_length=30, default=None)
        or_sord_num: Optional[str] = Field(max_length=7, default=None)
        or_cpu: Optional[Decimal] = None
        or_quote_num: Optional[str] = Field(max_length=15, default=None)
        or_stat_notes: Optional[str] = Field(max_length=2147483647, default=None)

    class Operation(BaseModel):
        ao_order_num: Optional[str] = Field(max_length=12, default=None)
        ao_mach_code: Optional[str] = Field(max_length=5, default=None)
        ao_complete: Optional[bool] = False
        ao_comp_date: Optional[datetime] = None
        mt_de_id: Optional[str] = Field(max_length=2, default=None)
        mt_mach_desc: Optional[str] = Field(max_length=20, default=None)
        de_desc: Optional[str] = Field(max_length=30, default=None)

    class JobCard(BaseModel):
        aj_run_date: Optional[datetime] = None
        aj_time1: Optional[str] = Field(max_length=10, default=None)
        mt_mach_desc: Optional[str] = Field(max_length=20, default=None)
        em_emp_name: Optional[str] = Field(max_length=20, default=None)
        aj_tot_time: Optional[Decimal] = None
        jc_order_num: Optional[str] = Field(max_length=12, default=None)

        @computed_field
        @property
        def aj_tot_time_formatted(self) -> Decimal:
            if self.aj_tot_time is not None:
                hour = int(self.aj_tot_time)
                minute = (self.aj_tot_time * 60) % 60
                second = (self.aj_tot_time * 3600) % 60
                return "%02d:%02d:%02d" % (hour, minute, second)
            else:
                return "%02d:%02d:%02d" % (0, 0, 0)

        @computed_field
        @property
        def aj_run_date_aj_time1(self) -> datetime:
            if self.aj_time1 is not None:
                time_tuple = self.aj_time1.split(":")
                hour = int(time_tuple[0])
                minute = int(time_tuple[1])
                second = int(time_tuple[2])
                return self.aj_run_date + timedelta(
                    hours=hour, minutes=minute, seconds=second
                )
            else:
                return None

    class Csr(BaseModel):
        cu_cust_code: Optional[str] = Field(max_length=6, default=None)
        em_emp_id: Optional[str] = Field(max_length=5, default=None)
        em_emp_name: Optional[str] = Field(max_length=20, default=None)

    orelease: Orelease = None
    order: Order = None
    operations: List[Operation] = []
    job_cards: List[JobCard] = []
    csr: Csr = None
