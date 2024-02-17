from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date


class Order(BaseModel):
    or_order_num: str = Field(max_length=12)
    or_ord_date: date
    or_quote_num: str = Field(max_length=15)
    or_unit_type: str = Field(max_length=4)
    or_po_num: str = Field(max_length=25)
    or_ord_status: str = Field(max_length=1)
    or_part_num: str = Field(max_length=30)
    or_rev_num: str = Field(max_length=6)
    or_part_desc: str = Field(max_length=50)
    or_pmemo: str = Field(max_length=2147483647)
    or_cust_code: str = Field(max_length=6)
    or_emp_id: str = Field(max_length=5)
    or_scomm: Decimal
    or_runs: Decimal
    or_lastop: Decimal
    or_ord_notes: str = Field(max_length=2147483647)
    or_up_date: date
    or_qty_ord: Decimal
    or_qty_car: Decimal
    or_qty_ret: Decimal
    or_qty_ship: Decimal
    or_qty_prod: Decimal
    or_qty_bal: Decimal
    or_qty_inv: Decimal
    or_ht: Decimal
    or_pl: Decimal
    or_tool: Decimal
    or_misc: Decimal
    or_ov: Decimal
    or_ottool: Decimal
    or_otgage: Decimal
    or_otcollet: Decimal
    or_otmisc: Decimal
    or_ht_notes: str = Field(max_length=2147483647)
    or_pl_notes: str = Field(max_length=2147483647)
    or_ppbar1: Decimal
    or_act_ppb1: Decimal
    or_tsu1: Decimal
    or_tsu2: Decimal
    or_tsu3: Decimal
    or_tsu4: Decimal
    or_tsu5: Decimal
    or_tsu6: Decimal
    or_tsu7: Decimal
    or_tsu8: Decimal
    or_tsu9: Decimal
    or_tsu10: Decimal
    or_cpu: Decimal
    or_weight: Decimal
    or_change_ord: str = Field(max_length=15)
    or_qtq: Decimal
    or_require_ty: Decimal
    or_buyer: str = Field(max_length=20)
    or_spec_po: str = Field(max_length=2147483647)
    or_cust_s_ins: bool
    or_n_des_ts: bool
    or_n_des_no: str = Field(max_length=2147483647)
    or_os_proc_sp: str = Field(max_length=2147483647)
    or_spec_pk_sh: str = Field(max_length=2147483647)
    or_cert_req: str = Field(max_length=2147483647)
    or_mat_spec: str = Field(max_length=2147483647)
    or_os_pr_spec: str = Field(max_length=2147483647)
    or_spec_mark: str = Field(max_length=2147483647)
    or_dt_r_po: date
    or_po_type: Decimal
    or_cor_bp_rev: bool
    or_dt_pb_rq: date
    or_mat_on_hnd: bool
    or_dt_moh_o: date
    or_dt_moh_d: date
    or_sketch_ava: bool
    or_rout_book: bool
    or_dt_prg_a: date
    or_dt_tol_o: date
    or_dt_tol_d: date
    or_dt_gag_o: date
    or_dt_gag_d: date
    or_dt_rel_p: date
    or_reviewedby: str = Field(max_length=30)
    or_dt_rev: date
    or_mat: Decimal
    or_lot: str = Field(max_length=20)
    or_induct_s: Decimal
    or_induct_i: Decimal
    or_shard_s: str = Field(max_length=25)
    or_shard_i: str = Field(max_length=25)
    or_toteff_s: Decimal
    or_toteff_i: Decimal
    or_case_s: str = Field(max_length=10)
    or_case_i: str = Field(max_length=10)
    or_core_s: str = Field(max_length=10)
    or_core_i: str = Field(max_length=10)
    or_plen_s: str = Field(max_length=10)
    or_plen_i: str = Field(max_length=10)
    or_note_s: str = Field(max_length=40)
    or_note_i: str = Field(max_length=2147483647)
    or_ins_by: str = Field(max_length=40)
    or_app_by: str = Field(max_length=25)
    or_ins_date: date
    or_app_date: date
    or_qty_extra: Decimal
    or_mat_code: str = Field(max_length=6)
    or_prod_code: str = Field(max_length=2)
    or_invent_num: str = Field(max_length=30)
    or_raw_num: str = Field(max_length=30)
    or_sord_num: str = Field(max_length=7)
    or_line_num: Decimal
    or_est_mat_cost: Decimal
    or_lo_code: str = Field(max_length=10)
    or_comp_date: date
    or_draw_num: str = Field(max_length=30)
    or_draw_rev: str = Field(max_length=6)
    or_non_bill: bool
    or_internal: bool
    or_misc_cost: Decimal
    or_scrap_amt: Decimal
    or_scrap_wgt: Decimal
    or_scrap_val: Decimal
    or_parent_order: str = Field(max_length=12)
    or_extatrb1: str = Field(max_length=30)
    or_extatrb2: str = Field(max_length=30)
    or_extatrb3: str = Field(max_length=30)
    or_extatrb4: str = Field(max_length=30)
    or_extatrb5: str = Field(max_length=30)
    or_extatrb6: str = Field(max_length=30)
    or_extatrb7: str = Field(max_length=30)
    or_extatrb8: str = Field(max_length=30)
    or_extatrb9: str = Field(max_length=30)
    or_extatrb10: str = Field(max_length=30)
    or_contact: str = Field(max_length=25)
    or_is_lot: Decimal
    or_cont_cnt: str = Field(max_length=10)
    or_cont_type: str = Field(max_length=10)
    or_cont_desc: str = Field(max_length=20)
    or_cont_weight: str = Field(max_length=10)
    or_aggregate: bool
    or_user_id: str = Field(max_length=5)
    or_last_mod: date
    or_serialize: bool
    or_op_last_changed_by: str = Field(max_length=30)
    or_op_rev: str = Field(max_length=3)
    or_op_last_changed_date: date
    or_doc_type: str = Field(max_length=10)
    or_dpas: str = Field(max_length=10)
    or_rev_stepup: Decimal
    or_wipinfg: bool
    or_freeze: bool
    or_ser_type: Decimal
    or_ser_stepup: Decimal
    or_serial_no: str = Field(max_length=20)
    or_printed: date
    or_rework: bool
    or_rev_level: str = Field(max_length=3)
    or_markup: Decimal
    or_labor_code: bool
    or_continuous_jc: bool
    or_loctimedate: date
    or_sl_id: str = Field(max_length=10)
    or_print_date: date
    or_originator_id: str = Field(max_length=5)
    or_st_id: str = Field(max_length=2)
    or_lc_id: str = Field(max_length=10)
    or_external: bool
    or_adj_date: date
    or_mat_mu: Decimal
    or_display_labor: bool
    or_display_mats: bool
    or_mat_memo: str = Field(max_length=2147483647)
    or_override: bool
    or_project_type: Decimal
    or_proj_sales_suffix: str = Field(max_length=1)
    or_tag_num: Decimal
    or_proj_stepup: str = Field(max_length=3)
    or_df_id: str = Field(max_length=10)
    or_stat_notes: str = Field(max_length=2147483647)
    or_useopqty: bool
    or_splitparent: str = Field(max_length=12)
    or_warranty: bool
    or_scrap_ca_code: str = Field(max_length=12)
    or_hidecomplete: bool
    or_jobnote: str = Field(max_length=2147483647)
    or_jobstoppedbynote: bool
    or_sigma_stat: Decimal
    or_keepzero: bool
    or_excludepaperless: bool
    or_price_color_red: bool
    or_track_stepup: Decimal
