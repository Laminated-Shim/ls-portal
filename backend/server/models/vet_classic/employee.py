from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date


class Employee(BaseModel):
    class Settings:
        name = "employee.dbf"

    class Config:
        json_schema_extra = {
            "example": {
                "em_emp_id": "0536 ",
                "em_emp_name": "ANDREW MOLYNEAUX    ",
                "em_position": "GENERAL MANAGER               ",
                "em_hrly_rate": -99.99,
                "em_dept_code": "00",
                "em_shift": "1 ",
                "em_salespers": True,
                "em_picture": "K:\\COMPANY\\EMPLOYEES BIRTHDAYS AND ANNIVERSARIES\\ANDREW MOLYNEAUX-05-15-15.JPG                                                                                                                                                                                ",
                "em_ci": "07:00:00",
                "em_co": "03:30:00",
                "em_lo": "12:30:00",
                "em_li": "01:00:00",
                "em_r_limit": 0,
                "em_jc_use": True,
                "em_tc_use": True,
                "em_minlunch": 30,
                "em_gl_number": "            ",
                "em_last_name": "MOLYNEAUX           ",
                "em_first_name": "ANDREW         ",
                "em_middle_name": "JOHN        ",
                "em_address_1": "                                   ",
                "em_address_2": "                                   ",
                "em_city": "                    ",
                "em_state": "  ",
                "em_zip_code": "          ",
                "em_phone": "              ",
                "em_soc_sec": "                    ",
                "em_birth_date": "01/01/2124          ",
                "em_sex": " ",
                "em_marital": " ",
                "em_exempts_fd": 0,
                "em_pay_type": " ",
                "em_pay_freq": " ",
                "em_date_hired": "1899-12-30T00:00:00",
                "em_date_left": "1899-12-30T00:00:00",
                "em_reason_left": "",
                "em_notes": "",
                "em_ad_tax_fd": 0,
                "em_ad_tax_st": 0,
                "em_ad_tax_lc1": 0,
                "em_adv_rec": 0,
                "em_st_id_st": "  ",
                "em_tt_id_sii": "          ",
                "em_tx_id_lc1": "          ",
                "em_tx_id_lc2": "          ",
                "em_vac_avail": 0,
                "em_vac_used": 0,
                "em_vac_remain": 0,
                "em_pto_avail": 0,
                "em_pto_used": 0,
                "em_pto_remain": 0,
                "em_fax": "              ",
                "em_email": "Amolyneaux@laminatedshim.com                      ",
                "em_benefit_date": "1899-12-30T00:00:00",
                "em_vac_annual": 0,
                "em_pto_annual": 0,
                "em_ad_tax_lc2": 0,
                "em_use_tcards": False,
                "em_w2_stat_emp": False,
                "em_w2_942_emp": False,
                "em_w2_def_comp": False,
                "em_w2_legal_rep": False,
                "em_w2_pension": False,
                "em_w2_deceased": False,
                "em_as_fica": False,
                "em_as_medicare": False,
                "em_as_futa": False,
                "em_as_suta": False,
                "em_vac_basis": " ",
                "em_vac_accrual": " ",
                "em_pto_basis": " ",
                "em_pto_accrual": " ",
                "em_exempts_st": 0,
                "em_exempts_lc1": 0,
                "em_exempts_lc2": 0,
                "em_filing_fd": "N",
                "em_filing_st": "N",
                "em_filing_lc1": "N",
                "em_filing_lc2": "N",
                "em_st_id_lc1": "  ",
                "em_st_id_lc2": "  ",
                "em_vac_accrued": 0,
                "em_pto_accrued": 0,
                "em_electronic": False,
                "em_no_etr": False,
                "em_fed_res_no": "                              ",
                "em_inactive": False,
                "em_supp_code": "      ",
                "em_use_jcards": False,
                "em_supervisor": True,
                "em_emp_id_sup": "0177 ",
                "em_commission": 0,
                "em_shift_over": False,
                "em_vac_escrow": 0,
                "em_pto_escrow": 0,
                "em_w2_3rd_sick_pay": False,
                "em_use_scards": False,
                "em_sell_rate": 0,
                "em_ad_calc_fd": False,
                "em_ad_calc_st": False,
                "em_ad_calc_lc1": False,
                "em_ad_calc_lc2": False,
                "em_sc_dow": 0,
                "em_temporary": False,
                "em_pe_code": "      ",
                "em_use_rcards": False,
                "em_ex_gain_share": False,
                "em_production": True,
                "em_signature": "C:\\SIGNATURE.jpg                        ",
                "em_fit_py_gl": "            ",
                "em_fica_py_gl": "            ",
                "em_fica_ex_gl": "            ",
                "em_mc_py_gl": "            ",
                "em_mc_ex_gl": "            ",
                "em_futa_py_gl": "            ",
                "em_futa_ex_gl": "            ",
                "em_suta_py_gl": "            ",
                "em_suta_ex_gl": "            ",
                "em_sii_py_gl": "            ",
                "em_sii_ex_gl": "            ",
                "em_sit_py_gl": "            ",
                "em_sit_ex_gl": "            ",
                "em_lit1_py_gl": "            ",
                "em_lit1_ex_gl": "            ",
                "em_lit2_py_gl": "            ",
                "em_lit2_ex_gl": "            ",
                "em_tax_override": False,
                "em_suponly": False,
                "em_spec_req_acts": False,
                "em_inspector": False,
                "em_trans_code": "  ",
                "em_routing_no": "         ",
                "em_account_no": "                                   ",
                "em_tc_notes": "HI ANDREW",
                "em_mgr_quality": False,
                "em_mgr_pm": False,
                "em_mgr_engineering": False,
                "em_app_requisitions": False,
                "em_spouse_name": "                    ",
                "em_unattend": False,
                "em_exp_dept": "      ",
                "em_exp_code": "        ",
                "em_hr_notes": "",
                "em_da_notes": "",
                "em_pr_notes": "",
                "em_pr_next_date": "1899-12-30T00:00:00",
                "em_ps_id": "          ",
                "em_hours_allotted": 0,
                "em_cert_train": False,
                "em_filing_eic": "N",
                "em_eic_rc_gl": "            ",
                "em_setup": False,
                "em_emerg_name": "                         ",
                "em_emerg_phone": "              ",
                "em_can_issue_docs": False,
                "em_can_assign": False,
                "em_as_sother": False,
                "em_sot_py_gl": "            ",
                "em_sot_ex_gl": "            ",
                "em_filing_so": "N",
                "em_federal": False,
                "em_state_1": False,
                "em_local_1": False,
                "em_local_2": False,
                "em_arbitrator": False,
                "em_ex_holidays": False,
                "em_split_perc": 0,
                "em_electronic2": False,
                "em_trans_code2": "  ",
                "em_routing_no2": "         ",
                "em_account_no2": "                                   ",
                "em_split_perc2": 0,
                "em_split_type": 1,
                "em_split_amt": 0,
                "em_split_amt2": 0,
                "em_requisition": False,
                "em_lc_id_lc1": "          ",
                "em_lc_id_lc2": "          ",
                "em_as_lother1": False,
                "em_as_lother2": False,
                "em_lot1_py_gl": "            ",
                "em_lot1_ex_gl": "            ",
                "em_lot2_py_gl": "            ",
                "em_lot2_ex_gl": "            ",
                "em_srt_py_gl": "            ",
                "em_srt_ex_gl": "            ",
                "em_depends_fd": 0,
                "em_inside": False,
                "em_id_code": "          ",
                "em_qualified": False,
                "em_sell_rate_ot": 0,
                "em_sell_rate_dot": 0,
                "em_gl_com_exp": "            ",
                "em_check_memo": "                              ",
                "em_gl_com_pay": "            ",
                "em_passwrd": "       ",
                "em_approve_qa": False,
                "em_car_resp": False,
                "em_1099": False,
                "em_1099box": "  ",
                "em_lm_user_id": "     ",
                "em_lm_date_time": "1899-12-30T00:00:00",
                "em_email_pay_stub": False,
                "em_portalonly": False,
                "em_birth_date2": "                    ",
                "em_soc_sec2": "           ",
                "em_numofmachines": 0,
                "em_prevent_clockin": False,
                "em_pdf_pay_stub": False,
                "em_pdf_directory": "                                        ",
                "em_aca_fte_basis": 0,
                "em_account_no_ue": "                 ",
                "em_account_no2_ue": "                 ",
                "em_sp_basis": "X",
                "em_sp_accrual": "X",
                "em_sp_annual": 0,
                "em_sp_per_pay": 0,
                "em_vac_per_pay": 0,
                "em_pto_per_pay": 0,
                "em_reqapprover": "     ",
                "em_reqmeonly": False,
                "em_w4_2020_later": False,
                "em_w4_step_2_c": False,
            }
        }

    em_emp_id: str = Field(max_length=5)
    em_emp_name: str = Field(max_length=20)
    em_position: str = Field(max_length=30)
    em_hrly_rate: Decimal
    em_dept_code: str = Field(max_length=2)
    em_shift: str = Field(max_length=2)
    em_salespers: bool
    em_picture: str = Field(max_length=254)
    em_ci: str = Field(max_length=8)
    em_co: str = Field(max_length=8)
    em_lo: str = Field(max_length=8)
    em_li: str = Field(max_length=8)
    em_r_limit: Decimal
    em_jc_use: bool
    em_tc_use: bool
    em_minlunch: Decimal
    em_gl_number: str = Field(max_length=12)
    em_last_name: str = Field(max_length=20)
    em_first_name: str = Field(max_length=15)
    em_middle_name: str = Field(max_length=12)
    em_address_1: str = Field(max_length=35)
    em_address_2: str = Field(max_length=35)
    em_city: str = Field(max_length=20)
    em_state: str = Field(max_length=2)
    em_zip_code: str = Field(max_length=10)
    em_phone: str = Field(max_length=14)
    em_soc_sec: str = Field(max_length=20)
    em_birth_date: str = Field(max_length=20)
    em_sex: str = Field(max_length=1)
    em_marital: str = Field(max_length=1)
    em_exempts_fd: Decimal
    em_pay_type: str = Field(max_length=1)
    em_pay_freq: str = Field(max_length=1)
    em_date_hired: date
    em_date_left: date
    em_reason_left: str = Field(max_length=2147483647)
    em_notes: str = Field(max_length=2147483647)
    em_ad_tax_fd: Decimal
    em_ad_tax_st: Decimal
    em_ad_tax_lc1: Decimal
    em_adv_rec: Decimal
    em_st_id_st: str = Field(max_length=2)
    em_tt_id_sii: str = Field(max_length=10)
    em_tx_id_lc1: str = Field(max_length=10)
    em_tx_id_lc2: str = Field(max_length=10)
    em_vac_avail: Decimal
    em_vac_used: Decimal
    em_vac_remain: Decimal
    em_pto_avail: Decimal
    em_pto_used: Decimal
    em_pto_remain: Decimal
    em_fax: str = Field(max_length=14)
    em_email: str = Field(max_length=50)
    em_benefit_date: date
    em_vac_annual: Decimal
    em_pto_annual: Decimal
    em_ad_tax_lc2: Decimal
    em_use_tcards: bool
    em_w2_stat_emp: bool
    em_w2_942_emp: bool
    em_w2_def_comp: bool
    em_w2_legal_rep: bool
    em_w2_pension: bool
    em_w2_deceased: bool
    em_as_fica: bool
    em_as_medicare: bool
    em_as_futa: bool
    em_as_suta: bool
    em_vac_basis: str = Field(max_length=1)
    em_vac_accrual: str = Field(max_length=1)
    em_pto_basis: str = Field(max_length=1)
    em_pto_accrual: str = Field(max_length=1)
    em_exempts_st: Decimal
    em_exempts_lc1: Decimal
    em_exempts_lc2: Decimal
    em_filing_fd: str = Field(max_length=1)
    em_filing_st: str = Field(max_length=1)
    em_filing_lc1: str = Field(max_length=1)
    em_filing_lc2: str = Field(max_length=1)
    em_st_id_lc1: str = Field(max_length=2)
    em_st_id_lc2: str = Field(max_length=2)
    em_vac_accrued: Decimal
    em_pto_accrued: Decimal
    em_electronic: bool
    em_no_etr: bool
    em_fed_res_no: str = Field(max_length=30)
    em_inactive: bool
    em_supp_code: str = Field(max_length=6)
    em_use_jcards: bool
    em_supervisor: bool
    em_emp_id_sup: str = Field(max_length=5)
    em_commission: Decimal
    em_shift_over: bool
    em_vac_escrow: Decimal
    em_pto_escrow: Decimal
    em_w2_3rd_sick_pay: bool
    em_use_scards: bool
    em_sell_rate: Decimal
    em_ad_calc_fd: bool
    em_ad_calc_st: bool
    em_ad_calc_lc1: bool
    em_ad_calc_lc2: bool
    em_sc_dow: Decimal
    em_temporary: bool
    em_pe_code: str = Field(max_length=6)
    em_use_rcards: bool
    em_ex_gain_share: bool
    em_production: bool
    em_signature: str = Field(max_length=40)
    em_fit_py_gl: str = Field(max_length=12)
    em_fica_py_gl: str = Field(max_length=12)
    em_fica_ex_gl: str = Field(max_length=12)
    em_mc_py_gl: str = Field(max_length=12)
    em_mc_ex_gl: str = Field(max_length=12)
    em_futa_py_gl: str = Field(max_length=12)
    em_futa_ex_gl: str = Field(max_length=12)
    em_suta_py_gl: str = Field(max_length=12)
    em_suta_ex_gl: str = Field(max_length=12)
    em_sii_py_gl: str = Field(max_length=12)
    em_sii_ex_gl: str = Field(max_length=12)
    em_sit_py_gl: str = Field(max_length=12)
    em_sit_ex_gl: str = Field(max_length=12)
    em_lit1_py_gl: str = Field(max_length=12)
    em_lit1_ex_gl: str = Field(max_length=12)
    em_lit2_py_gl: str = Field(max_length=12)
    em_lit2_ex_gl: str = Field(max_length=12)
    em_tax_override: bool
    em_suponly: bool
    em_spec_req_acts: bool
    em_inspector: bool
    em_trans_code: str = Field(max_length=2)
    em_routing_no: str = Field(max_length=9)
    em_account_no: str = Field(max_length=35)
    em_tc_notes: str = Field(max_length=2147483647)
    em_mgr_quality: bool
    em_mgr_pm: bool
    em_mgr_engineering: bool
    em_app_requisitions: bool
    em_spouse_name: str = Field(max_length=20)
    em_unattend: bool
    em_exp_dept: str = Field(max_length=6)
    em_exp_code: str = Field(max_length=8)
    em_hr_notes: str = Field(max_length=2147483647)
    em_da_notes: str = Field(max_length=2147483647)
    em_pr_notes: str = Field(max_length=2147483647)
    em_pr_next_date: date
    em_ps_id: str = Field(max_length=10)
    em_hours_allotted: Decimal
    em_cert_train: bool
    em_filing_eic: str = Field(max_length=1)
    em_eic_rc_gl: str = Field(max_length=12)
    em_setup: bool
    em_emerg_name: str = Field(max_length=25)
    em_emerg_phone: str = Field(max_length=14)
    em_can_issue_docs: bool
    em_can_assign: bool
    em_as_sother: bool
    em_sot_py_gl: str = Field(max_length=12)
    em_sot_ex_gl: str = Field(max_length=12)
    em_filing_so: str = Field(max_length=1)
    em_federal: bool
    em_state_1: bool
    em_local_1: bool
    em_local_2: bool
    em_arbitrator: bool
    em_ex_holidays: bool
    em_split_perc: Decimal
    em_electronic2: bool
    em_trans_code2: str = Field(max_length=2)
    em_routing_no2: str = Field(max_length=9)
    em_account_no2: str = Field(max_length=35)
    em_split_perc2: Decimal
    em_split_type: Decimal
    em_split_amt: Decimal
    em_split_amt2: Decimal
    em_requisition: bool
    em_lc_id_lc1: str = Field(max_length=10)
    em_lc_id_lc2: str = Field(max_length=10)
    em_as_lother1: bool
    em_as_lother2: bool
    em_lot1_py_gl: str = Field(max_length=12)
    em_lot1_ex_gl: str = Field(max_length=12)
    em_lot2_py_gl: str = Field(max_length=12)
    em_lot2_ex_gl: str = Field(max_length=12)
    em_srt_py_gl: str = Field(max_length=12)
    em_srt_ex_gl: str = Field(max_length=12)
    em_depends_fd: Decimal
    em_inside: bool
    em_id_code: str = Field(max_length=10)
    em_qualified: bool
    em_sell_rate_ot: Decimal
    em_sell_rate_dot: Decimal
    em_gl_com_exp: str = Field(max_length=12)
    em_check_memo: str = Field(max_length=30)
    em_gl_com_pay: str = Field(max_length=12)
    em_passwrd: str = Field(max_length=7)
    em_approve_qa: bool
    em_car_resp: bool
    em_1099: bool
    em_1099box: str = Field(max_length=2)
    em_lm_user_id: str = Field(max_length=5)
    em_lm_date_time: date
    em_email_pay_stub: bool
    em_portalonly: bool
    em_birth_date2: str = Field(max_length=20)
    em_soc_sec2: str = Field(max_length=11)
    em_numofmachines: int
    em_prevent_clockin: bool
    em_pdf_pay_stub: bool
    em_pdf_directory: str = Field(max_length=40)
    em_aca_fte_basis: Decimal
    em_account_no_ue: str = Field(max_length=17)
    em_account_no2_ue: str = Field(max_length=17)
    em_sp_basis: str = Field(max_length=1)
    em_sp_accrual: str = Field(max_length=1)
    em_sp_annual: Decimal
    em_sp_per_pay: Decimal
    em_vac_per_pay: Decimal
    em_pto_per_pay: Decimal
    em_reqapprover: str = Field(max_length=5)
    em_reqmeonly: bool
    em_w4_2020_later: bool
    em_w4_step_2_c: bool
