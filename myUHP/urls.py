from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name='index'), 
    
      # For USER ACCOUNT 
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name ='activate'),
    #path('', views.base, name='base'),
    # For SEND EMAIL TO THE NEWSLETTERS SUBSCRIBERS
    path('subscribers', views.subscribers, name ='subscribers'),
    path('mail_letter', views.mail_letter, name ='mail_letter'),
    path('counter',views.counter, name='counter'),
    path('subscribers_views', views.subscribers_views, name ='subscribers_views'),
    path('add_subscribers', views.add_subscribers, name ='add_subscribers'),
    path('edit_subscribers/<int:pk>', views.edit_subscribers, name = 'edit_subscribers'),
    path('delete_subscribers/<int:pk>', views.delete_subscribers, name = 'delete_subscribers'),
        
    # For DASHBOARD VIEW 
    path('dashboard', views.dashboard, name = 'dashboard'),
    # For GENERAL INFO SETTING 
    path('general_info', views.general_info, name = 'general_info'),
    # For COUNTRY
    path('countryList', views.countryList, name = 'countryList'),
    path('edit_country/<int:pk>', views.edit_country, name = 'edit_country'),
    path('delete_country/<int:pk>', views.delete_country, name = 'delete_country'),
    # For STATUT
    path('statutList', views.statutList, name = 'statutList'),
    path('edit_statut/<int:pk>', views.edit_statut, name = 'edit_statut'),
    path('delete_statut/<int:pk>', views.delete_statut, name = 'delete_statut'),
        
        # For UNIT
    path('add_units', views.add_units, name = 'add_units'),
    path('edit_unit/<int:pk>', views.edit_unit, name = 'edit_unit'),
    path('delete_unit/<int:pk>', views.delete_unit, name = 'delete_unit'),
    
    
    # For OUTPUT
    path('add_output', views.add_output, name = 'add_output'),
    path('edit_output/<int:pk>', views.edit_output, name = 'edit_output'),
    path('delete_output/<int:pk>', views.delete_output, name = 'delete_output'),
    # For KPI
    path('add_kpi', views.add_kpi, name = 'add_kpi'),
    path('edit_kpi/<int:pk>', views.edit_kpi, name = 'edit_kpi'),
    path('delete_kpi/<int:pk>', views.delete_kpi, name = 'delete_kpi'),
    path('load_kpi', views.load_kpi, name = 'load_kpi'),    
    path('index_kpi', views.kpi_achieve_index, name = 'index_kpi'),
    path('kpi_report', views.kpi_report, name = 'kpi_report'),
    path('single_kpi_page/<int:pk>', views.single_kpi_page, name='single_kpi_page'),
    
    # For TOP TASK
    path('add_toptask', views.add_toptask, name = 'add_toptask'),
    path('edit_lowest/<int:pk>', views.edit_lowest, name = 'edit_lowest'),
    path('delete_lowest/<int:pk>', views.delete_lowest, name = 'delete_lowest'), 
    
    
    # For Lowest task
    path('add_lowest', views.add_lowest, name = 'add_lowest'),
    path('edit_toptask/<int:pk>', views.edit_toptask, name = 'edit_toptask'),
    path('delete_toptask/<int:pk>', views.delete_toptask, name = 'delete_toptask'), 
    # For sub activity
    
    path('workplans', views.sub_activity_view, name = 'workplans'),
    #path('workplans', views.workplansView.as_view(), name = 'workplans'),
    path('workplan/new', views.add_new_workplan_view, name = 'add_new_workplan'),
    path('edit_workplan/<int:pk>/update', views.edit_workplan_view, name = 'edit_workplan') ,
    path('delete_workplan/<int:pk>', views.delete_workplan_view, name = 'delete_workplan'),
    path('edit_op_wp/<int:pk>', views.edit_op_wp, name = 'edit_op_wp'),
    
    path('workplan_fiche', views.fiche_workplan, name = 'workplan_fiche'),
    path('sub_activity_report', views.sub_activity_report, name = 'sub_activity_report'),
    path('single_sub_activity_page/<str:unit_code>', views.single_sub_activity_page, name='single_sub_activity_page'),
    
    # For individual annual report
    path('indiv_report', views.individual_report, name = 'indiv_report'),
    path('add_indivReport', views.add_indivReport, name='add_indivReport'),
    path('single_report_page/<str:name>', views.single_report_page, name='single_report_page'),
    path('single_report_page/edit_indivReport/<int:pk>', views.edit_indivReport, name = 'edit_indivReport'),
    
    # For events calendar
    path('events', views.events_cluster, name = 'events'),
    
    # For import and export survey
    
    path('upload_survey', views.simple_upload, name = 'upload_survey'),
    
    # For add new project  into the survey table
    path('project_survey', views.survey_add_project, name = 'project_survey'),
    # For add new dataset into the survey table
    path('index_survey', views.survey_add_data, name = 'index_survey'),
    path('survey_report', views.survey_report, name = 'survey_report'),
    path('single_survey_page/<int:pk>', views.single_survey_page, name='single_survey_page'),
    
    # For upload image file into the system to disply in cover page
    path('doc_import', views.docSave_upload, name = 'doc_import'),
    
    # For items in cover page Index
    path('cover_list', views.cover_list, name = 'cover_list'),
    path('add_items_covertPages', views.add_items_cover_page, name = 'add_items_covertPages'),
    path('edit_items_covertPages/<int:pk>', views.edit_items_cover_page, name = 'edit_items_covertPages'),
    path('delete_cover_page/<int:pk>', views.delete_items_cover_page, name = 'delete_cover_page'),
    
    # For export to Excel file
    path('export_project/', views.export_project_survey, name='export_project_survey'),
        
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('export_survey_page/<int:pk>', views.export_survey_page, name='export_survey_page'),
    
    path('export_kpi_excel/<int:pk>', views.export_kpi_excel, name='export_kpi_excel'),
    path('export_listKpi_excel', views.export_listKpi_excel, name='export_listKpi_excel'),
    
    path('export_listOutput_excel', views.export_listOutput_excel, name='export_listOutput_excel'),
    
    path('export_subactivity_excel', views.export_subactivity_excel, name='export_subactivity_excel'),
        
        
    # Export dashboard to pdf
    # METHOD TO GENERATE SUMMARY OF KPI ON PDF FORMAT
    path('render_pdf_view', views.render_pdf_view, name='render_pdf_view'),
    
    path('render_lowestTask_view', views.render_pdf_activities, name='render_lowestTask_view'),
    
    path('che_lowestTask_view', views.CHE_pdf_activities, name='che_lowestTask_view'),

    # For upload report file into the system to backup
    path('report_upload', views.report_upload, name = 'report_upload'),
    # Method for views all reports upload in the system
    path('views_report', views.views_report, name = 'views_report'),
    #Method to put  into the table all reports upload in the system
    path('index_report', views.index_report, name = 'index_report'),
    
    #Method to edit reports upload in the system
    path('edit_report/<int:pk>', views.editReport, name = 'edit_report'),
    
    path('reporting_indicator', views.shiny_dashboard_ind, name = 'reporting_indicator'),
    
    # DISPLAY MONITORING PERFORMANCE OF WORKPLAN BY UNIT AND BUY COMPLETION DATE 
    path('sub_activity_level', views.unit_sub_activity_view, name = 'sub_activity_level'),
    path('single_sub_activity_page/<str:unit_code>', views.single_sub_activity_page, name='single_sub_activity_page'),
    
    # DOWNLOAD MONITORING PERFORMANCE OF WORKPLAN BY UNIT AND BUY COMPLETION DATE 
    path('download_monitoring', views.download_monitoring_progress, name = 'download_monitoring'),
        
        #Method to generate the pdf for VID unit sub activities views from html
        
    path('vid_lowestTask_view', views.VID_pdf_activities, name='vid_lowestTask_view'),
    
    #Method to generate the pdf for HPD unit sub activities views from html

    path('hpd_lowestTask_view', views.HPD_pdf_activities, name='hpd_lowestTask_view'),
    #Method to generate the pdf for UHU unit sub activities views from html

    path('uhu_lowestTask_view', views.UHU_pdf_activities, name='uhu_lowestTask_view'),
    #Method to generate the pdf for NUT unit sub activities views from html

    path('nut_lowestTask_view', views.NUT_pdf_activities, name='nut_lowestTask_view'),
    #Method to generate the pdf for TNR unit sub activities views from html

    path('tnr_lowestTask_view', views.TNR_pdf_activities, name='tnr_lowestTask_view'),
    # For add new project  into the meeting table
    path('project_meeting', views.meeting_add_project, name = 'project_meeting'),
        # For add new dataset into the survey table
    path('index_meeting', views.meeting_add_data, name = 'index_meeting'),
    
    
    path('export_all_meeting/', views.export_meeting_to_excel, name='export_all_meeting'),
    ## METHOD TO DISPLAY ALL MEETING REPORT SUBMITTED
    path('meeting_report', views.meeting_report, name = 'meeting_report'),
    #METHOD TO VIEW SINGLE PAGE FOR  MEETING REPORT  
    path('single_meeting_page/<int:pk>', views.single_meeting_page, name='single_meeting_page'),
    #METHOD TO EXPORT MEETING REPORT AND DETAILS TO EXCEL FILE 
    path('export_meeting_page/<int:pk>', views.export_meeting_page, name='export_meeting_page'),
    
    # METHODE TO EXPORT MEETING REPORT TO WORD FILE
    path('meeting_doc_report/<int:pk>', views.meeting_doc_report, name = 'meeting_doc_report'),
    
    path('pdf', views.pdf, name = 'pdf'),
    
    # FOR ADD NEW PROJECT INTO THE BRIEFING TABLE
    path('project_briefing', views.briefing_add_project, name = 'project_briefing'),
    # FOR ADD NEW BACKGROUND INTO THE BRIEFING TABLE
    path('index_briefing', views.briefing_add_data, name = 'index_briefing'),
    #METHOD TO EXPORT BRIEFING DATASET ALL DATA ON EXCEL FILE
    path('export_all_briefing/', views.export_briefingNote_to_excel, name='export_all_briefing'),
    # METHOD TO DISPLAY ALL BRIEFING REPORT SUBMITTED
    path('briefing_report', views.briefing_report, name = 'briefing_report'),
    #METHOD TO VIEW SINGLE PAGE FOR  MEETING REPORT  
    path('single_briefing_page/<int:pk>', views.single_briefing_page, name='single_briefing_page'),
        #METHOD TO EXPORT BRIEFING BACKGROUND AND DETAILS TO EXCEL FILE 
    path('export_briefing_page/<int:pk>', views.export_briefing_page, name='export_briefing_page'),
    # METHODE TO EXPORT BRIEFING NOTES TO WORD FILE
    path('briefing_doc_report/<int:pk>', views.briefing_doc_report, name = 'briefing_doc_report'),
    
    #FOR ADD NEW PROJECT INTO THE BRIEFING TABLE
    path('risk_register', views.risk_identification_add, name = 'risk_register'),
    path('export_risk_to_excel/', views.export_risk_to_excel, name = 'export_risk_to_excel'),
        ## METHOD TO DISPLAY ALL RISK MANAGEMENT SUBMITTED
    path('risk_report', views.risk_report, name = 'risk_report'),
    #METHOD TO VIEW SINGLE UNIT PAGE FOR  RISK REGISTET  
    path('unit_risk_page/<int:pk>', views.unit_risk_page, name='unit_risk_page'),
    path('export_unit_risk/<int:pk>', views.export_unit_risk, name = 'export_unit_risk'),
    
    # METHODE TO EXPORT UNIT RISK REGISTER TO WORD FILE
    path('risk_doc_report/<int:pk>', views.riskRegister_doc_report, name = 'risk_doc_report'),
    
    path('sub_activity_wkpl', views.wpkl_subActivities_add, name = 'sub_activity_wkpl'),
    
    # METHOD TO EXPORT OPERATIONNAL WORKPLAN TO WORD FILE
    path('subActivities_doc_report/<str:unit_code>', views.subActivities_doc_report, name = 'subActivities_doc_report'),
    
    # METHOD TO EXPORT KPI RESULT TO WORD FILE
    path('download_kpi_result/<int:pk>', views.download_kpi_result, name='download_kpi_result'),
    
    # METHOD TO EXPORT WORKPLAN FOR EACH UNIT IN EXCEL FORMAT
    path('export_to_excel_workplan/<str:by_unit>/<str:end_date>', views.export_to_excel_workplan, name='export_to_excel_workplan'),
    
    ## METHOD TO EXPORT KPI RESULTS FOR EACH UNIT IN EXCEL FORMAT
    path('export_to_excel_kpiResults/<str:by_unit>/<str:end_date>', views.export_to_excel_kpiResults, name='export_to_excel_kpiResults'),
    
    # METHOD TO EXPORT RISK REGISTER FOR EACH UNIT IN EXCEL FORMAT
    
    path('export_to_excel_riskRegister/<str:by_unit>/<str:end_date>', views.export_to_excel_riskRegister, name='export_to_excel_riskRegister'),


    # METHOD TO EXPORT SURVEY DATASET FOR EACH UNIT IN EXCEL FORMAT
    path('export_to_excel_survey_dataset/<str:by_survey>/<str:end_day>', views.export_to_excel_survey_dataset, name='export_to_excel_survey_dataset'),
    
    
]

