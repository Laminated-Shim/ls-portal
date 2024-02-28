from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional
from datetime import datetime


class Aoperate(BaseModel):
    ao_order_num: Optional[str] = Field(max_length=12, default=None)
    ao_op_num: Optional[Decimal] = None
    ao_type: Optional[str] = Field(max_length=1, default=None)
    ao_mach_code: Optional[str] = Field(max_length=5, default=None)
    ao_suhr: Optional[Decimal] = None
    ao_sur: Optional[Decimal] = None
    ao_su: Optional[Decimal] = None
    ao_gp: Optional[Decimal] = None
    ao_pop: Optional[Decimal] = None
    ao_np: Optional[Decimal] = None
    ao_hpu: Optional[Decimal] = None
    ao_hr: Optional[Decimal] = None
    ao_cpu: Optional[Decimal] = None
    ao_note: Optional[str] = Field(max_length=2147483647, default=None)
    ao_current: Optional[Decimal] = None
    ao_attend: Optional[Decimal] = None
    ao_queue: Optional[Decimal] = None
    ao_dist_code: Optional[str] = Field(max_length=2, default=None)
    ao_supp_code: Optional[str] = Field(max_length=6, default=None)
    ao_unit_cost: Optional[Decimal] = None
    ao_quantity: Optional[Decimal] = None
    ao_ext_cost: Optional[Decimal] = None
    ao_mark_up: Optional[Decimal] = None
    ao_tot_cost: Optional[Decimal] = None
    ao_distrib: Optional[bool] = False
    ao_cost1: Optional[Decimal] = None
    ao_cost2: Optional[Decimal] = None
    ao_cost3: Optional[Decimal] = None
    ao_cost4: Optional[Decimal] = None
    ao_cost5: Optional[Decimal] = None
    ao_cost6: Optional[Decimal] = None
    ao_cost7: Optional[Decimal] = None
    ao_cost8: Optional[Decimal] = None
    ao_cost9: Optional[Decimal] = None
    ao_cost10: Optional[Decimal] = None
    ao_recalc: Optional[bool] = False
    ao_tsu: Optional[Decimal] = None
    ao_hrs_od: Optional[Decimal] = None
    ao_hrs_td: Optional[Decimal] = None
    ao_hrs_totd: Optional[Decimal] = None
    ao_hrs_av: Optional[Decimal] = None
    ao_p_prod: Optional[Decimal] = None
    ao_p_bad: Optional[Decimal] = None
    ao_p_good: Optional[Decimal] = None
    ao_qty_bal: Optional[Decimal] = None
    ao_hrs_prod: Optional[Decimal] = None
    ao_hrs_set: Optional[Decimal] = None
    ao_scrap: Optional[Decimal] = None
    ao_rework: Optional[Decimal] = None
    ao_qty_prod: Optional[Decimal] = None
    ao_qty_inv: Optional[Decimal] = None
    ao_act_phr: Optional[Decimal] = None
    ao_adj_phr: Optional[Decimal] = None
    ao_go_eff: Optional[Decimal] = None
    ao_p_eff: Optional[Decimal] = None
    ao_su_eff: Optional[Decimal] = None
    ao_perc_comp: Optional[Decimal] = None
    ao_num_mach: Optional[Decimal] = None
    ao_qty_ord: Optional[Decimal] = None
    ao_incl_su: Optional[str] = Field(max_length=100, default=None)
    ao_end_date: Optional[str] = Field(max_length=2147483647, default=None)
    ao_sc_off: Optional[str] = Field(max_length=100, default=None)
    ao_labors: Optional[Decimal] = None
    ao_burdens: Optional[Decimal] = None
    ao_laborp: Optional[Decimal] = None
    ao_burdenp: Optional[Decimal] = None
    ao_force_mach: Optional[str] = Field(max_length=100, default=None)
    ao_sched_qty: Optional[str] = Field(max_length=2147483647, default=None)
    ao_in_invent: Optional[str] = Field(max_length=30, default=None)
    ao_out_invent: Optional[str] = Field(max_length=30, default=None)
    ao_sched: Optional[bool] = False
    ao_force: Optional[bool] = False
    ao_rewflag: Optional[bool] = False
    ao_g_code: Optional[str] = Field(max_length=10, default=None)
    ao_review: Optional[Decimal] = None
    ao_move_stock: Optional[bool] = False
    ao_complete: Optional[bool] = False
    ao_master_id: Optional[int] = None
    ao_parent_id: Optional[int] = None
    ao_oplib_note: Optional[str] = Field(max_length=2147483647, default=None)
    ao_il_id: Optional[str] = Field(max_length=10, default=None)
    ao_ib_id: Optional[str] = Field(max_length=10, default=None)
    ao_pagebreak: Optional[bool] = False
    ao_min_charge: Optional[Decimal] = None
    ao_infin_max: Optional[Decimal] = None
    ao_enforce_usage: Optional[bool] = False
    ao_setup_master: Optional[bool] = False
    ao_setup_count: Optional[Decimal] = None
    ao_aggregate_op: Optional[Decimal] = None
    ao_last_prod_op: Optional[bool] = False
    ao_split: Optional[bool] = False
    ao_il_id_in: Optional[str] = Field(max_length=10, default=None)
    ao_ib_id_in: Optional[str] = Field(max_length=10, default=None)
    ao_optype: Optional[Decimal] = None
    ao_down: Optional[Decimal] = None
    ao_pc_lbs: Optional[bool] = False
    ao_pc_cost: Optional[Decimal] = None
    ao_aw_order_num: Optional[str] = Field(max_length=8, default=None)
    ao_unit_type: Optional[str] = Field(max_length=4, default=None)
    ao_infstart_date: Optional[datetime] = None
    ao_infend_date: Optional[datetime] = None
    ao_statnotes: Optional[str] = Field(max_length=2147483647, default=None)
    ao_minqty: Optional[Decimal] = None
    ao_hpp: Optional[Decimal] = None
    ao_mpp: Optional[Decimal] = None
    ao_spp: Optional[Decimal] = None
    ao_burden: Optional[Decimal] = None
    ao_exclude: Optional[bool] = False
    ao_comp_date: Optional[datetime] = None
    ao_sl: Optional[str] = Field(max_length=2147483647, default=None)
    ao_pc_per_unit: Optional[Decimal] = None
    ao_unit_rate: Optional[Decimal] = None
    ao_need_qty: Optional[Decimal] = None
    ao_surcharge: Optional[Decimal] = None
    ao_simple_calc: Optional[bool] = False
    ao_lossperc: Optional[Decimal] = None
    ao_load_time: Optional[Decimal] = None
    ao_rpm: Optional[int] = None
    ao_spindgear: Optional[str] = Field(max_length=15, default=None)
    ao_changegear: Optional[str] = Field(max_length=15, default=None)
    ao_threadgear: Optional[str] = Field(max_length=15, default=None)
    ao_st_id: Optional[str] = Field(max_length=10, default=None)
    ao_significant: Optional[bool] = False
    ao_post_pc: Optional[bool] = False
    ao_sa_id: Optional[str] = Field(max_length=10, default=None)
    ao_donotorder: Optional[bool] = False
    ao_casting_op: Optional[bool] = False
    ao_spindle_rpm: Optional[Decimal] = None
    ao_feed_rpm: Optional[Decimal] = None
    ao_eff_thread_rpm: Optional[Decimal] = None
    ao_mtsc: Optional[Decimal] = None
    ao_opqty: Optional[Decimal] = None
    ao_freightmin: Optional[Decimal] = None
    ao_freightcost: Optional[Decimal] = None
    ao_lotqty: Optional[Decimal] = None
    ao_infstart_datetime: Optional[datetime] = None
    ao_infend_datetime: Optional[datetime] = None
    ao_act_pph: Optional[Decimal] = None
