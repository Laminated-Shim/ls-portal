from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional
from datetime import datetime


class Order(BaseModel):
    or_order_num: Optional[str] = Field(max_length=12, default=None)
    or_ord_date: Optional[datetime] = None
    or_quote_num: Optional[str] = Field(max_length=15, default=None)
    or_unit_type: Optional[str] = Field(max_length=4, default=None)
    or_po_num: Optional[str] = Field(max_length=25, default=None)
    or_ord_status: Optional[str] = Field(max_length=1, default=None)
    or_part_num: Optional[str] = Field(max_length=30, default=None)
    or_rev_num: Optional[str] = Field(max_length=6, default=None)
    or_part_desc: Optional[str] = Field(max_length=50, default=None)
    or_pmemo: Optional[str] = Field(max_length=2147483647, default=None)
    or_cust_code: Optional[str] = Field(max_length=6, default=None)
    or_emp_id: Optional[str] = Field(max_length=5, default=None)
    or_scomm: Optional[Decimal] = None
    or_runs: Optional[Decimal] = None
    or_lastop: Optional[Decimal] = None
    or_ord_notes: Optional[str] = Field(max_length=2147483647, default=None)
    or_up_date: Optional[datetime] = None
    or_qty_ord: Optional[Decimal] = None
    or_qty_car: Optional[Decimal] = None
    or_qty_ret: Optional[Decimal] = None
    or_qty_ship: Optional[Decimal] = None
    or_qty_prod: Optional[Decimal] = None
    or_qty_bal: Optional[Decimal] = None
    or_qty_inv: Optional[Decimal] = None
    or_ht: Optional[Decimal] = None
    or_pl: Optional[Decimal] = None
    or_tool: Optional[Decimal] = None
    or_misc: Optional[Decimal] = None
    or_ov: Optional[Decimal] = None
    or_ottool: Optional[Decimal] = None
    or_otgage: Optional[Decimal] = None
    or_otcollet: Optional[Decimal] = None
    or_otmisc: Optional[Decimal] = None
    or_ht_notes: Optional[str] = Field(max_length=2147483647, default=None)
    or_pl_notes: Optional[str] = Field(max_length=2147483647, default=None)
    or_ppbar1: Optional[Decimal] = None
    or_act_ppb1: Optional[Decimal] = None
    or_tsu1: Optional[Decimal] = None
    or_tsu2: Optional[Decimal] = None
    or_tsu3: Optional[Decimal] = None
    or_tsu4: Optional[Decimal] = None
    or_tsu5: Optional[Decimal] = None
    or_tsu6: Optional[Decimal] = None
    or_tsu7: Optional[Decimal] = None
    or_tsu8: Optional[Decimal] = None
    or_tsu9: Optional[Decimal] = None
    or_tsu10: Optional[Decimal] = None
    or_cpu: Optional[Decimal] = None
    or_weight: Optional[Decimal] = None
    or_change_ord: Optional[str] = Field(max_length=15, default=None)
    or_qtq: Optional[Decimal] = None
    or_require_ty: Optional[Decimal] = None
    or_buyer: Optional[str] = Field(max_length=20, default=None)
    or_spec_po: Optional[str] = Field(max_length=2147483647, default=None)
    or_cust_s_ins: Optional[bool] = False
    or_n_des_ts: Optional[bool] = False
    or_n_des_no: Optional[str] = Field(max_length=2147483647, default=None)
    or_os_proc_sp: Optional[str] = Field(max_length=2147483647, default=None)
    or_spec_pk_sh: Optional[str] = Field(max_length=2147483647, default=None)
    or_cert_req: Optional[str] = Field(max_length=2147483647, default=None)
    or_mat_spec: Optional[str] = Field(max_length=2147483647, default=None)
    or_os_pr_spec: Optional[str] = Field(max_length=2147483647, default=None)
    or_spec_mark: Optional[str] = Field(max_length=2147483647, default=None)
    or_dt_r_po: Optional[datetime] = None
    or_po_type: Optional[Decimal] = None
    or_cor_bp_rev: Optional[bool] = False
    or_dt_pb_rq: Optional[datetime] = None
    or_mat_on_hnd: Optional[bool] = False
    or_dt_moh_o: Optional[datetime] = None
    or_dt_moh_d: Optional[datetime] = None
    or_sketch_ava: Optional[bool] = False
    or_rout_book: Optional[bool] = False
    or_dt_prg_a: Optional[datetime] = None
    or_dt_tol_o: Optional[datetime] = None
    or_dt_tol_d: Optional[datetime] = None
    or_dt_gag_o: Optional[datetime] = None
    or_dt_gag_d: Optional[datetime] = None
    or_dt_rel_p: Optional[datetime] = None
    or_reviewedby: Optional[str] = Field(max_length=30, default=None)
    or_dt_rev: Optional[datetime] = None
    or_mat: Optional[Decimal] = None
    or_lot: Optional[str] = Field(max_length=20, default=None)
    or_induct_s: Optional[Decimal] = None
    or_induct_i: Optional[Decimal] = None
    or_shard_s: Optional[str] = Field(max_length=25, default=None)
    or_shard_i: Optional[str] = Field(max_length=25, default=None)
    or_toteff_s: Optional[Decimal] = None
    or_toteff_i: Optional[Decimal] = None
    or_case_s: Optional[str] = Field(max_length=10, default=None)
    or_case_i: Optional[str] = Field(max_length=10, default=None)
    or_core_s: Optional[str] = Field(max_length=10, default=None)
    or_core_i: Optional[str] = Field(max_length=10, default=None)
    or_plen_s: Optional[str] = Field(max_length=10, default=None)
    or_plen_i: Optional[str] = Field(max_length=10, default=None)
    or_note_s: Optional[str] = Field(max_length=40, default=None)
    or_note_i: Optional[str] = Field(max_length=2147483647, default=None)
    or_ins_by: Optional[str] = Field(max_length=40, default=None)
    or_app_by: Optional[str] = Field(max_length=25, default=None)
    or_ins_date: Optional[datetime] = None
    or_app_date: Optional[datetime] = None
    or_qty_extra: Optional[Decimal] = None
    or_mat_code: Optional[str] = Field(max_length=6, default=None)
    or_prod_code: Optional[str] = Field(max_length=2, default=None)
    or_invent_num: Optional[str] = Field(max_length=30, default=None)
    or_raw_num: Optional[str] = Field(max_length=30, default=None)
    or_sord_num: Optional[str] = Field(max_length=7, default=None)
    or_line_num: Optional[Decimal] = None
    or_est_mat_cost: Optional[Decimal] = None
    or_lo_code: Optional[str] = Field(max_length=10, default=None)
    or_comp_date: Optional[datetime] = None
    or_draw_num: Optional[str] = Field(max_length=30, default=None)
    or_draw_rev: Optional[str] = Field(max_length=6, default=None)
    or_non_bill: Optional[bool] = False
    or_internal: Optional[bool] = False
    or_misc_cost: Optional[Decimal] = None
    or_scrap_amt: Optional[Decimal] = None
    or_scrap_wgt: Optional[Decimal] = None
    or_scrap_val: Optional[Decimal] = None
    or_parent_order: Optional[str] = Field(max_length=12, default=None)
    or_extatrb1: Optional[str] = Field(max_length=30, default=None)
    or_extatrb2: Optional[str] = Field(max_length=30, default=None)
    or_extatrb3: Optional[str] = Field(max_length=30, default=None)
    or_extatrb4: Optional[str] = Field(max_length=30, default=None)
    or_extatrb5: Optional[str] = Field(max_length=30, default=None)
    or_extatrb6: Optional[str] = Field(max_length=30, default=None)
    or_extatrb7: Optional[str] = Field(max_length=30, default=None)
    or_extatrb8: Optional[str] = Field(max_length=30, default=None)
    or_extatrb9: Optional[str] = Field(max_length=30, default=None)
    or_extatrb10: Optional[str] = Field(max_length=30, default=None)
    or_contact: Optional[str] = Field(max_length=25, default=None)
    or_is_lot: Optional[Decimal] = None
    or_cont_cnt: Optional[str] = Field(max_length=10, default=None)
    or_cont_type: Optional[str] = Field(max_length=10, default=None)
    or_cont_desc: Optional[str] = Field(max_length=20, default=None)
    or_cont_weight: Optional[str] = Field(max_length=10, default=None)
    or_aggregate: Optional[bool] = False
    or_user_id: Optional[str] = Field(max_length=5, default=None)
    or_last_mod: Optional[datetime] = None
    or_serialize: Optional[bool] = False
    or_op_last_changed_by: Optional[str] = Field(max_length=30, default=None)
    or_op_rev: Optional[str] = Field(max_length=3, default=None)
    or_op_last_changed_date: Optional[datetime] = None
    or_doc_type: Optional[str] = Field(max_length=10, default=None)
    or_dpas: Optional[str] = Field(max_length=10, default=None)
    or_rev_stepup: Optional[Decimal] = None
    or_wipinfg: Optional[bool] = False
    or_freeze: Optional[bool] = False
    or_ser_type: Optional[Decimal] = None
    or_ser_stepup: Optional[Decimal] = None
    or_serial_no: Optional[str] = Field(max_length=20, default=None)
    or_printed: Optional[datetime] = None
    or_rework: Optional[bool] = False
    or_rev_level: Optional[str] = Field(max_length=3, default=None)
    or_markup: Optional[Decimal] = None
    or_labor_code: Optional[bool] = False
    or_continuous_jc: Optional[bool] = False
    or_loctimedate: Optional[datetime] = None
    or_sl_id: Optional[str] = Field(max_length=10, default=None)
    or_print_date: Optional[datetime] = None
    or_originator_id: Optional[str] = Field(max_length=5, default=None)
    or_st_id: Optional[str] = Field(max_length=2, default=None)
    or_lc_id: Optional[str] = Field(max_length=10, default=None)
    or_external: Optional[bool] = False
    or_adj_date: Optional[datetime] = None
    or_mat_mu: Optional[Decimal] = None
    or_display_labor: Optional[bool] = False
    or_display_mats: Optional[bool] = False
    or_mat_memo: Optional[str] = Field(max_length=2147483647, default=None)
    or_override: Optional[bool] = False
    or_project_type: Optional[Decimal] = None
    or_proj_sales_suffix: Optional[str] = Field(max_length=1, default=None)
    or_tag_num: Optional[Decimal] = None
    or_proj_stepup: Optional[str] = Field(max_length=3, default=None)
    or_df_id: Optional[str] = Field(max_length=10, default=None)
    or_stat_notes: Optional[str] = Field(max_length=2147483647, default=None)
    or_useopqty: Optional[bool] = False
    or_splitparent: Optional[str] = Field(max_length=12, default=None)
    or_warranty: Optional[bool] = False
    or_scrap_ca_code: Optional[str] = Field(max_length=12, default=None)
    or_hidecomplete: Optional[bool] = False
    or_jobnote: Optional[str] = Field(max_length=2147483647, default=None)
    or_jobstoppedbynote: Optional[bool] = False
    or_sigma_stat: Optional[Decimal] = None
    or_keepzero: Optional[bool] = False
    or_excludepaperless: Optional[bool] = False
    or_price_color_red: Optional[bool] = False
    or_track_stepup: Optional[Decimal] = None
