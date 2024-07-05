from django.db import models

# Create your models here.
## For Home page _01
class Feature(models.Model):
    name = models.CharField(max_length = 200)
    details = models.CharField(max_length = 500)
    mostinfo = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name   

## For Home page _02
class Subscribers(models.Model):
    name_subscriber = models.CharField(max_length = 50, unique = True)
    email_subscriber = models.EmailField(null = True)
    date_subscriber = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.email_subscriber

class MailMessage(models.Model):
    title_mail = models.CharField('Title', max_length = 100, null = True)
    message_mail = models.TextField('Message', null = True)
    
    def __str__(self):
        return self.title_mail
   
class Statutworkplan(models.Model):
    statut_name =  models.CharField('Statut name', max_length = 30)

    def __str__(self):
            return self.statut_name 

class Outputworkplan(models.Model):
    output_code =  models.CharField('Output code', max_length = 10)
    output_description =  models.CharField('Output description', max_length = 200)

    def __str__(self):
            return self.output_code
      
class Country(models.Model):
    country_code =  models.CharField('Country code', max_length = 10)
    country_name =  models.CharField('Country name', max_length = 100)
    
    def __str__(self):
            return self.country_code
   
class Units(models.Model):
    unit_code =models.CharField('Unit code', max_length = 10)
    unit_description = models.CharField('Unit description', max_length = 250)
    
    def __str__(self):
        return self.unit_code   
    
class Kpi(models.Model):
    expected_result =  models.CharField('Expected result',max_length = 250, null = True)
    kpi_code =  models.CharField('Kpi code',max_length = 30)
    kpi_description =  models.CharField('Kpi Description',max_length = 250)
    kpi_country_level =  models.CharField('Kpi country level',max_length = 250, null = True)
    data_description =  models.CharField('Data description', max_length = 250, null = True)
    data_source =  models.CharField('Data source',max_length = 250, null = True)
    collection_methods =  models.CharField('Collection methods', max_length = 250, null = True)
    data_frequency =  models.CharField('Data frequency',max_length = 250, null = True)
    kpi_link = models.CharField('Kpi link',max_length = 100, null = True)
    unit = models.ForeignKey(Units, on_delete = models.SET_NULL, null = True, related_name='units_kpi')

    def __str__(self):
            return self.kpi_code
        
class KpiAchieve(models.Model):
    kpi = models.ForeignKey(Kpi, on_delete = models.SET_NULL, null = True,related_name='kpis_kpiAchive') 
    kpi_baseline =  models.CharField('Baseline of the KPI', max_length = 100)
    kpi_target =  models.CharField('Target of the KPI', max_length = 30)
    report_date =  models.DateField('Report date', blank=True, null=True)
    report_resut =  models.CharField('Result of the KPI', max_length = 250)
    report_comment =  models.CharField('Comment', max_length = 250) 

    def __str__(self):
            return self.report_comment
        

       
class Toptask(models.Model):    
    output = models.ForeignKey(Outputworkplan, on_delete = models.SET_NULL, null = True, related_name='outputs_toptask') 
    kpi = models.ForeignKey(Kpi, on_delete = models.SET_NULL, null = True, related_name='kpis_toptask') 
    top_task = models.IntegerField('Top task', null = True, blank = True)
    top_task_short = models.CharField('Top task short name',max_length = 100)
    top_task_description = models.CharField('Top task short description',max_length = 250)
    unit = models.ForeignKey(Units, on_delete = models.CASCADE, related_name='units_toptask')
    
    def __str__(self) -> str:
        return self.top_task_description

        
class GsmWorkplan(models.Model):    
  #  output = models.ForeignKey(Outputworkplan, on_delete = models.SET_NULL, null = True, related_name='outputs_gsmWorkplan') 
    toptask = models.ForeignKey(Toptask, on_delete = models.SET_NULL, null = True, related_name='toptask_gsmWorkplan') 
  #  kpi = models.ForeignKey(Kpi, on_delete = models.SET_NULL, null = True, related_name='kpis_gsmWorkplan') 
  #  top_task = models.IntegerField('Top task', null = True, blank = True)
  #  top_task_short = models.CharField('Top task short name',max_length = 100)
  #  top_task_description = models.CharField('Top task short description',max_length = 250)
    lowest_task = models.CharField('Lowest task', max_length = 50)
    lowest_task_short = models.CharField('Lowest task short name',max_length = 100)
    lowest_task_description = models.CharField('Lowest task short description',max_length = 250)
   # unit = models.ForeignKey(Units, on_delete = models.CASCADE, related_name='units_gsmWorkplan')
    
    def __str__(self) -> str:
        return self.lowest_task_description
    
       
class Operworkplan(models.Model):
    TRAVEL_CHOICES = (
        ('yes', 'Yes',),
        ('no', 'No',)     
    )
  #  COUNTRY = [ (country.country_code, country.country_name())
  #          for country in Country.objects.all() ]
    gsmWorkplan = models.ForeignKey(GsmWorkplan, on_delete = models.SET_NULL, null = True,  related_name='gsmWorkplan_operw') 
    sub_activity = models.CharField('Sub activity', max_length = 250)
    country = models.ManyToManyField(Country, related_name='countries_operwork') 
    travel_required = models.CharField('Travel required', max_length=5, choices=TRAVEL_CHOICES)
    consultants = models.IntegerField('Number of consultants', null = True, blank = True, default=0)
    duration_days = models.IntegerField('Duration days', null = True, blank = True, default=0)
    staff_amount = models.FloatField('Staff amount', null = True, blank = True, default=0)
    travel_amount = models.FloatField('Travel amount', null = True, blank = True, default=0)
    procurment_amount = models.FloatField('Procurment amount', null = True, blank = True, default=0)
    service_amount = models.FloatField('Service amount', null = True, blank = True, default=0)
    flexible_amount = models.FloatField('Flexible amount', null = True, blank = True, default=0)
    vc_amount = models.FloatField('VC amount', null = True, blank = True, default=0)
    responsable = models.CharField('Responsible', max_length = 250)
    coworkers = models.CharField('Coworkers', max_length = 250)
    expected_result = models.CharField('Expected result', max_length = 250)
    indicator_measuring = models.CharField('Indicator measuring', max_length = 250)
    collect_method = models.CharField('Collect method', max_length = 250)
    completion_date = models.DateField('Completion date', blank=True)
    statut_name = models.ForeignKey(Statutworkplan, on_delete = models.SET_NULL, null = True, related_name='statuts_operwork')
    comments = models.CharField('Comments', max_length = 250)
   
   # country = models.CharField(choices = COUNTRY)
    def __str__(self) -> str:
        return self.sub_activity
    
class IndividualReport(models.Model):    
    unit = models.ForeignKey(Units, on_delete = models.SET_NULL, null = True, related_name='units_indReport')
    staff_name = models.CharField('Staff Full Name',max_length = 250)
    email_staff = models.EmailField()
    supervisor = models.CharField('Supervisor Full Name',max_length = 250)
    email_sup = models.EmailField()
    start_date = models.DateField('Start date', blank=True)
    end_date = models.DateField('End date', blank=True)
    Question_1 = models.CharField('What output would you like to focus on during this period?',max_length = 500)
    Question_2 = models.CharField('Specify tasks you would like to lead (1 or 2)',max_length = 500)
    Question_3 = models.CharField('What support (tools, skills, training, office environment) would you like to receive from your supervisor/other experienced staff in performing your duties?',max_length = 500)
    Question_4 = models.CharField('What are your 2 or 3 main achievements during this reporting period? To be completed at the end of the performance period and discussed with the supervisor and cluster director',max_length = 500)
    Question_5 = models.CharField('Final comments',max_length = 500)
     
    def __str__(self) -> str:
        return self.staff_name
       
    
class DocSave(models.Model):
    name_doc =models.CharField('File name',max_length=200, null = True, blank=True)
    file_doc = models.ImageField(upload_to='static/images/demo', null=True)
    
    def __str__(self):
        return self.name_doc
    
class ReportSave(models.Model):
    title_rep =models.CharField('Report title',max_length=200, null = True, blank=True)
    author_rep =models.CharField('Organization responsible for the report',max_length = 500, null = True, blank=True)
    date_rep = models.DateField('Date', blank=True)
    summary_rep = models.CharField('Summary report', max_length = 500)
    file_rep = models.FileField(upload_to='static/report/pdf', null=True)
    img_cp_rep = models.ImageField(upload_to='static/report/imgs', null=True)
    
    def __str__(self):
        return self.title_rep
        
class SurveyProject(models.Model):
    responsible =  models.CharField('Organization responsible for the survey',max_length = 500, null = True, blank=True)
    title_surv = models.CharField('Survey title', max_length=350, null = True, blank=True)
    start_date = models.DateField('Start date', blank=True)
    end_date = models.DateField('End date', blank=True)
    location_survey =  models.CharField('Survey location',max_length = 500, null = True, blank=True)

    def __str__(self):
            return self.title_surv

class SurveyDataset(models.Model):
    surveyProject = models.ForeignKey(SurveyProject, on_delete = models.SET_NULL, null = True,related_name='project_surveyData') 
    quest_code= models.CharField('Question code', max_length=250,null = True, blank=True)
    question =  models.CharField('Questions',max_length = 1000)
    response_text = models.CharField('Response in text format',max_length = 1000, null = True, blank=True)
    response_num = models.FloatField('Response in integer format', null = True, blank = True)
    level_1 = models.CharField('First area of data',max_length = 500, null = True, blank=True)
    level_2 = models.CharField('Seconde area of data',max_length = 500, null = True, blank=True)
    
    def __str__(self):
        return f"{self.quest_code} {self.question}"
        


class TypeMeeting(models.Model):
    group_meeting =  models.CharField('Statut name', max_length = 250)
    
    def __str__(self):
            return self.group_meeting
    
    
class MeetingProject(models.Model):
    output = models.ManyToManyField(Outputworkplan, related_name='outputs_meetingProject') 
    kpi = models.ManyToManyField(Kpi, related_name='kpis_meetingProject') 
    date_meeting=models.DateField('Date of meeting', blank=True)
    name_meeting = models.CharField('Name', max_length=500, null = True, blank=True)
    type_meeting = models.ForeignKey(TypeMeeting, on_delete = models.SET_NULL, null = True, related_name='typemeeting_meetingProject')
    objective_meeting =  models.CharField('Objective',max_length = 500, null = True, blank=True)
    taking_place =  models.CharField('Taking place',max_length = 500, null = True, blank=True)
    chair_name =  models.CharField('Chair Name',max_length = 500, null = True, blank=True)
    note_taker  =  models.CharField('NoteTaker Name',max_length = 500, null = True, blank=True)
    participants_list  =  models.CharField('Participants list',max_length = 500, null = True, blank=True)
    
    def __str__(self):
            return self.name_meeting


class MeetingDiscussion(models.Model):
    STATUS_CHOICES = (
        ('NoStart', 'No start',),
        ('Ongoing', 'Ongoing',) ,
        ('Done', 'Done',)      
    )
    meetingProject = models.ForeignKey(MeetingProject, on_delete = models.SET_NULL, null = True,  related_name='meetingProject_discussion') 
    topic_discussion =  models.CharField('Topics for discussion ',max_length = 500, null = True, blank=True)
    summary_discussion =  models.CharField('Summary of discussion ',max_length = 500, null = True, blank=True)
    recommandation =  models.CharField('Recommandations ',max_length = 500, null = True, blank=True)
    actions_points =  models.CharField('Actions points ',max_length = 500, null = True, blank=True)
    responsible =  models.CharField('Responsible',max_length = 500, null = True, blank=True)
    action_deadlines=models.DateField('Deadlines', blank=True)
    action_status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES)
    feedback_discussion =  models.CharField('Feedback of discussion ',max_length = 500, null = True, blank=True)

    def __str__(self):
            return self.topic_discussion
    
class BriefingProject(models.Model):
    briefing_title = models.CharField('Title', max_length=500, null = True, blank=True)
    unit = models.ForeignKey(Units, on_delete = models.SET_NULL, null = True, related_name='units_briefingNote')
    start_date=models.DateField('Start date', blank=True)
    end_date=models.DateField('End date', blank=True)
    reporting_date=models.DateField('Reporting date', blank=True)

    def __str__(self):
            return self.briefing_title 

class BriefingBackground(models.Model):
    briefingProject = models.ForeignKey(BriefingProject, on_delete = models.SET_NULL, null = True,  related_name='briefingProject_background') 
    subject_background =  models.CharField('Subject ',max_length = 500, null = True, blank=True)
    specific_topic =  models.CharField('Specific topic ',max_length = 500, null = True, blank=True)
    accomplished_last_period = models.CharField('Activities accomplished last period ',max_length = 700, null = True, blank=True)
    planned_next_steps =  models.CharField('Activities planned current month',max_length = 700, null = True, blank=True)
    output = models.ManyToManyField(Outputworkplan, related_name='outputs_briefingProject') 
    kpi = models.ManyToManyField(Kpi, related_name='kpis_briefingProject') 
    comment_background =  models.CharField('Comments ',max_length = 500, null = True, blank=True)

    def __str__(self):
            return self.subject_background  

class RiskIdentification(models.Model):
    CATEGORY_CHOICES = (
        ('Financial', 'Financial'),
        ('Political_governance', 'Political or governance') ,
        ('Reputational', 'Reputational'),
        ('Staff_Systems_Structures', 'Staff, Systems & Structures'),
        ('Strategic', 'Strategic'), 
        ('Technical', 'Technical or Public Health')       
    )
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Existing', 'Existing') ,
        ('closed', 'To be closed')    
    )
    PROBABILITY_CHOICES = (
        ('Very_High', 'Very High'),
        ('High', 'High') ,
        ('Medium', 'Medium'),
        ('Low', 'Low')      
    )
    RATING_CHOICES = (
        ('Severe', 'Severe'),
        ('Major', 'Major') ,
        ('Medium', 'Medium'),
        ('Minor', 'Minor')      
    )
    CRITICALITY_CHOICES = (
        ('Moderate', 'Moderate'),
        ('Critical', 'Critical') ,
        ('Very_critical', 'Very critical')     
    )
    DECISION_CHOICES = (
        ('Accept_Tolerate', 'Accept or Tolerate'),
        ('Mitigate', 'Mitigate') ,
        ('Transfer', 'Transfer'),
        ('Avoid', 'Avoid'),  
        ('Exploit', 'Exploit')       
    )
    REVIEW_CHOICES = (
        ('Relevant_Effective', 'Relevant and Effective'),
        ('Needs_revised', 'Needs to be revised') ,
        ('Not_started', 'Not started'),
        ('Closed', 'To be closed')
    )
    unit = models.ForeignKey(Units, on_delete = models.SET_NULL, null = True, related_name='units_risk')   
    toptask = models.ForeignKey(Toptask, on_delete = models.SET_NULL, null = True, related_name='toptask_risk')   
    risk_name = models.CharField('Risk identification', max_length=500, null = True, blank=True)
    risk_cause = models.CharField('Cause', max_length=500, null = True, blank=True)
    risk_impact = models.CharField('Risk consequence', max_length=500, null = True, blank=True)
    risk_category = models.CharField('Risk Category', max_length=100, choices=CATEGORY_CHOICES)
    risk_status = models.CharField('Risk Status', max_length=100, choices=STATUS_CHOICES)
    risk_occuring = models.CharField('Probability of Risk Occuring', max_length=100, choices=PROBABILITY_CHOICES)
    risk_rating = models.CharField('Risk Impact Rating', max_length=100, choices=RATING_CHOICES)
    risk_criticality = models.CharField('Risk Criticality', max_length=100, choices=CRITICALITY_CHOICES)
    response_decision = models.CharField('Response Decision', max_length=100, choices=DECISION_CHOICES)
    risk_action = models.CharField('Risk Response Plan', max_length=500, null = True, blank=True)
    budget = models.FloatField('Budget Implication', null = True, blank = True)
    response_date = models.DateField('Response Date', blank=True)
    review_plan = models.CharField('Review of Existing Response Plans', max_length=100, choices=REVIEW_CHOICES)
    comments = models.CharField('Comment', max_length=500, null = True, blank=True)
    responsible = models.CharField('Responsible Person', max_length=500, null = True, blank=True)
    monitoring = models.FloatField('Monitoring percent', null = True, blank = True)
    risk_criticality_after = models.CharField('After preventive actions', max_length=100, choices=CRITICALITY_CHOICES)
    
    def __str__(self):
            return self.risk_name
 