from django import forms
from . models import Subscribers, MailMessage, Country, Statutworkplan, Outputworkplan,Kpi, GsmWorkplan,Toptask, Operworkplan, KpiAchieve, IndividualReport,SurveyProject, SurveyDataset,DocSave,Feature,Units, ReportSave,MeetingProject,MeetingDiscussion,TypeMeeting,BriefingProject, BriefingBackground, RiskIdentification
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions
from django.contrib.admin import widgets
from django.db.models import CheckConstraint, Q, F



class DateInput(forms.DateInput):
    input_type = 'date'
   
class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['name_subscriber', 'email_subscriber']
        
class MailMessageForm(forms.ModelForm):
    class Meta:
        model =  MailMessage
        fields = '__all__'
        
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
        'country_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the country code'}),
        'country_name': forms.TextInput(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the country name'})
    }
        
class StatutForm(forms.ModelForm):
    class Meta:
        model = Statutworkplan
        fields = '__all__'

class UnitsForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = '__all__'
        widgets = {
        'unit_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the unit code'}),
        'unit_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the unit description'})
    }
        
class OutputForm(forms.ModelForm):
    class Meta:
        model = Outputworkplan
        fields = '__all__'
        widgets = {
        'output_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the output code'}),
        'output_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the output description'})
    }
        
class KpiForm(forms.ModelForm):
    class Meta:
        model = Kpi
        fields = '__all__'
        widgets = {
        'expected_result': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the expected result'}),
        'kpi_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the kpi code'}),
        'kpi_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the kpi description'}),
        'kpi_country_level': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the kpi description at country level'}),
        'data_description':forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the data description'}),
        'data_source': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the data source'}),
        'collection_methods': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the collection methods'}),
        'data_frequency': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the frequency'}), 
        'kpi_link': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the reference'}),   
        'unit': forms.Select(attrs={'class': 'form-control', 'label':'Unit'})   
    }
        
class KpiAchieveForm(forms.ModelForm):
    class Meta:
        model = KpiAchieve
        fields = '__all__'
        widgets = {
        'kpi': forms.Select(attrs={'class': 'form-control', 'label':'kpi name'}), 
        'kpi_baseline':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the kpi baseline'}),
        'kpi_target': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the kpi target'}),
        'report_date': DateInput(), 
        'report_resut':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the report of the result'}),
        'report_comment': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the comment of the result'})         
    }
          
class ToptaskForm(forms.ModelForm):
    class Meta:
        model = Toptask
        fields = ['unit','output','kpi','top_task', 'top_task_short','top_task_description']
        widgets = {
        'unit': forms.Select(attrs={'class': 'form-control', 'label':'Unit'}),
        'output': forms.Select(attrs={'class': 'form-control', 'label':'output'}),
        'kpi': forms.Select(attrs={'class': 'form-control', 'label':'kpi'}),
        'top_task': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the top task number'}),
        'top_task_short': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the top task short'}),       
        'top_task_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the top task description'}),
       
    }
             
class GsmwpForm(forms.ModelForm):
    class Meta:
        model = GsmWorkplan
        fields = [
             'toptask',
         #   'unit',
         #   'output',
         #   'kpi',
         #   'top_task',
         #   'top_task_short',
         #   'top_task_description', 
            'lowest_task', 
            'lowest_task_short',
            'lowest_task_description' ]
        widgets = {
         'toptask': forms.Select(attrs={'class': 'form-control', 'label':'Top task'}),
    #    'unit': forms.Select(attrs={'class': 'form-control', 'label':'Unit'}),
    #    'output': forms.Select(attrs={'class': 'form-control', 'label':'output'}),
    #    'kpi': forms.Select(attrs={'class': 'form-control', 'label':'kpi'}),
    #    'top_task': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the top task number'}),
    #    'top_task_short': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the top task short'}),       
    #    'top_task_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the top task description'}),
        'lowest_task': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the lowest task number'}),
        'lowest_task_short': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the lowest task short'}),       
        'lowest_task_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the lowest task description'})
    }    
                   
class WorkplanForm(forms.ModelForm):
    country = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all()
    )
    class Meta:
        model = Operworkplan
        fields = ['gsmWorkplan', 'sub_activity', 'country','travel_required', 'consultants', 'duration_days', 'staff_amount','travel_amount', 'procurment_amount', 'service_amount',
                  'flexible_amount', 'vc_amount', 'responsable', 'coworkers', 'expected_result', 'indicator_measuring', 'collect_method', 'completion_date', 'statut_name',
                  'comments']   
        widgets = {
        'gsmWorkplan': forms.Select(attrs={'class': 'form-control', 'label':'Lowest task from GSM'}),
        'sub_activity': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the sub activity description'}),
        'country': forms.SelectMultiple(attrs={'class': 'form-control', 'required': True}),
        'travel_required': forms.Select(attrs={'class': 'form-control'}),
        'consultants': forms.NumberInput(attrs={'class': 'form-control'}),
        'duration_days': forms.NumberInput(attrs={'class': 'form-control'}),
        'staff_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'travel_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'procurment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'service_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'flexible_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'vc_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'responsable': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the responsible name'}),
        'coworkers': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the list name of coworkers'}),
        'expected_result': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the expected result description'}),
        'indicator_measuring': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the name of indicator'}),
        'collect_method': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the collect data description'}),
        'completion_date': DateInput(),
       # 'completion_date': forms.forms.DateInput(attrs={'type': 'date'})
        'statut_name': forms.Select(attrs={'class': 'form-control', 'style': 'border-color: orange;'}),
        'comments': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter some comments or observations'})
    }
        
    def __init__(self, *args, **kwargs):
       
        super(WorkplanForm, self).__init__(*args, **kwargs)
   #     selected_country = kwargs.pop('selected_country', None)   ##queryset returned from function
   #     self.fields['country'].queryset = selected_country
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['completion_date'].widget.attrs['class'] = 'datepicker'
      #  self.helper.add_input()
      #  self.helper.add_input()
        self.helper.layout = Layout(
            Row(
                Column('gsmWorkplan', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sub_activity', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('country', css_class='form-group col-md-6 mb-0'),
                Column('consultants', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('travel_amount', css_class='form-group col-md-3 mb-0'),
                Column('travel_required', css_class='form-group col-md-3 mb-0'),
                Column('duration_days', css_class='form-group col-md-3 mb-0'),
                Column('staff_amount', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('procurment_amount', css_class='form-group col-md-3 mb-0'),
                Column('service_amount', css_class='form-group col-md-3 mb-0'),
                Column('flexible_amount', css_class='form-group col-md-3 mb-0'),
                Column('vc_amount', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('responsable', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('coworkers', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('expected_result', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('indicator_measuring', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('collect_method', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('completion_date', css_class='form-group col-md-6 mb-0'),
                Column('statut_name', css_class='form-group col-md-- mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('comments', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('Save_sub_activity', 'Save sub activity'),
                Submit('Cancel', 'Cancel', css_class='ml-4 btn btn-danger')
            )
        )
        
class OperworkplanSearchForm(forms.ModelForm):
    class Meta:
        model = Operworkplan
        fields = ['gsmWorkplan']   
        widgets = {
        'gsmWorkplan': forms.Select(attrs={'class': 'form-control', 'label':'Lowest task from GSM'})
        
    }
        
class IndivReportForm(forms.ModelForm):
    class Meta:
        model = IndividualReport
        fields = ['unit', 'staff_name', 'email_staff','supervisor', 'email_sup', 'start_date', 'end_date','Question_1', 'Question_2', 'Question_3',
                  'Question_4', 'Question_5', ]   
        widgets = {
        'unit': forms.Select(attrs={'class': 'form-control'}),
        'staff_name': forms.TextInput(attrs={'class': 'form-control'}),
      #  'email_staff': forms.EmailField(),
        'supervisor': forms.TextInput(attrs={'class': 'form-control'}),
      #  'email_sup': forms.EmailField(),
        'start_date': DateInput(),
        'end_date': DateInput(),
        'Question_1': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the answers here'}),
        'Question_2': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the answers here'}),
        'Question_3': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the answers here'}),
        'Question_4': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the answers here'}),
        'Question_5': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the answers here'}),       
    }
          
class DocSaveForm(forms.ModelForm):
    class Meta:
        model = DocSave
        fields =['name_doc','file_doc']
        widgets = {
        'name_doc': forms.TextInput(attrs={'class': 'form-control', 'label':'Name'})#, 
      #  'file_doc':forms.ImageField()      
    }
 
class CoverPageForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields =['name','details']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'label':'Name'}), 
        'details': forms.TextInput(attrs={'class': 'form-control', 'label':'details'})#,   
    }

class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(end__gt=F('start')), 
                name = 'check_start',
            ),
        ]

class ReportSaveForm(forms.ModelForm):
    class Meta:
        model = ReportSave
        fields =['title_rep','author_rep','date_rep','summary_rep','file_rep','img_cp_rep']
        widgets = {
        'title_rep': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the title here'}),
        'author_rep': forms.TextInput(attrs={'class': 'form-control', 'label':'Author'}), 
        'date_rep': DateInput(),  
        'summary_rep': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the summary here'})
        #'file_rep': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':False}))     
    }
        


       
class SurveyProjectForm(forms.ModelForm):
    class Meta:
        model = SurveyProject
        fields = '__all__'
        widgets = {
        'responsible': forms.TextInput(attrs={'class': 'form-control', 'label':'Responsible'}), 
        'title_surv':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the title'}),
        'start_date': DateInput(), 
        'end_date': DateInput(), 
        'location_survey':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the Survey location'})
    }
        constraints = [
            CheckConstraint(
                check = Q(end_date__gt=F('start_date')), 
                name = 'check_start_date',
            ),
        ]
        
class SurveyDatasetForm(forms.ModelForm):
    class Meta:
        model = SurveyDataset
        fields = '__all__'
        widgets = {
        'surveyProject': forms.Select(attrs={'class': 'form-control', 'label':'Project name'}), 
        'quest_code':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the Question code'}),
        'question':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the Question'}),
        'response_text':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the Response in text format'}),
        'response_num': forms.NumberInput(attrs={'class': 'form-control'}),
        'level_1':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the First Geographical area '}),
        'level_2':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter the Second Geographical area '})
    }
        
        

class SelectUnitForm(forms.Form):
    UNIT_CHOICES =( 
    ("CHE", "CHE"), 
    ("HPD", "HPD"), 
    ("NUT", "NUT"), 
    ("TNR", "TNR"), 
    ("VID", "VID"),
    ("UHU", "UHU")) 
    
    by_unit =  forms.ChoiceField(choices = UNIT_CHOICES,  label=('Please select unit'))
   # start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label=('Completion date'))
    def __init__(self, *args, by_unit=None):
        super().__init__(*args)
        self.by_unit = by_unit
        
    
        
class TypeMeetingForm(forms.ModelForm):
    class Meta:
        model = TypeMeeting
        fields = '__all__'
     
class MeetingProjectForm(forms.ModelForm):
    output = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Outputworkplan.objects.all()        
    )
    kpi = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Kpi.objects.all()
    )
    
    class Meta:
        model = MeetingProject
        fields = '__all__'
        widgets = {
        'output': forms.SelectMultiple(attrs={'class': 'form-control', 'label':'Link to output'}),
        'kpi': forms.SelectMultiple(attrs={'class': 'form-control', 'label':'Link to kpi'}),
        'date_meeting': DateInput(), 
        'name_meeting': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the Meeting Name'}),
        'type_meeting': forms.Select(attrs={'class': 'form-control'}),
        'objective_meeting': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Objective'}),
       # 'agenda': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Agenda of meeting'}),
        'taking_place': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Where is the meeting taking place'}),
        'chair_name': forms.TextInput(attrs={'class': 'form-control', 'label':'Chair Name'}), 
        'note_taker': forms.TextInput(attrs={'class': 'form-control', 'label':'NoteTaker Name'}),
        'participants_list': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Participants list'})  
    }
        
        
class MeetingDiscussionForm(forms.ModelForm):
    class Meta:
        model = MeetingDiscussion
        fields = '__all__'
        widgets = {
        'meetingProject': forms.Select(attrs={'class': 'form-control', 'label':'Meeting project'}), 
        'topic_discussion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Topics for discussion'}),
        'summary_discussion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Summary of discussion'}),  
        'recommandation': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Recommandations'}), 
        'actions_points': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Actions points'}), 
        'responsible':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Responsible'}),
        'action_deadlines': DateInput(), 
        'action_status': forms.Select(attrs={'class': 'form-control', 'label':'Status'}), 
        'feedback_discussion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Feedback of discussion'})
    }
 
        
class BriefingProjectForm(forms.ModelForm):   
    class Meta:
        model = BriefingProject
        fields = '__all__'
        widgets = {
        'briefing_title': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Please enter the Title'}),
        'unit': forms.Select(attrs={'class': 'form-control', 'label':'Unit'}),
        'start_date': DateInput(), 
        'end_date': DateInput(), 
        'reporting_date': DateInput()
    }
        
       
class BriefingBackgroundForm(forms.ModelForm):
    output = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Outputworkplan.objects.all()        
    )
    kpi = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Kpi.objects.all()
    )
    class Meta:
        model = BriefingBackground
        fields = '__all__'
        widgets = {
        'briefingProject': forms.Select(attrs={'class': 'form-control', 'label':'Briefing project'}),
        'subject_background': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Subject'}),
        'specific_topic': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Specific topic'}),
        'accomplished_last_period': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Activities accomplished last period'}), 
        'planned_next_steps': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Activities planned current month'}), 
        'output': forms.SelectMultiple(attrs={'class': 'form-control', 'label':'Link to output'}),
        'kpi': forms.SelectMultiple(attrs={'class': 'form-control', 'label':'Link to kpi'}),
        'comment_background': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Comments'})
    }
     
class RiskIdentificationForm(forms.ModelForm):
    class Meta:
        model = RiskIdentification
        fields = '__all__'
        widgets = {
        'unit': forms.Select(attrs={'class': 'form-control', 'label':'Unit'}),
        'toptask': forms.Select(attrs={'class': 'form-control', 'label':'Top task'}),
        'risk_name': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Risk identification'}),
        'risk_cause': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Cause'}),  
        'risk_impact': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Risk consequence'}),
        'risk_category': forms.Select(attrs={'class': 'form-control', 'label':'Risk Category'}),
        'risk_status': forms.Select(attrs={'class': 'form-control', 'label':'Risk Status'}),
        'risk_occuring': forms.Select(attrs={'class': 'form-control', 'label':'Probability of Risk Occuring'}),
        'risk_rating': forms.Select(attrs={'class': 'form-control', 'label':'Risk Impact Rating'}),
        'risk_criticality': forms.Select(attrs={'class': 'form-control', 'label':'Risk Criticality'}),
        'response_decision': forms.Select(attrs={'class': 'form-control', 'label':'Response Decision'}),
        'risk_action': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Risk Response Plan'}),
        'budget': forms.NumberInput(attrs={'class': 'form-control'}),
        'response_date': DateInput(),
        'review_plan': forms.Select(attrs={'class': 'form-control', 'label':'Review of Existing Response Plans'}),
        'comments': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder': 'Comment'}),
        'responsible':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Responsible'}),
        'monitoring': forms.NumberInput(attrs={'class': 'form-control'}),
        'risk_criticality_after': forms.Select(attrs={'class': 'form-control', 'label':'After preventive actions'})
    }
    


class SelectSurveyForm(forms.Form):
    SURVEY_TITLES = SurveyProject.objects.all().values_list('id','title_surv').order_by('title_surv').distinct() 
    
    by_survey =  forms.ChoiceField(choices = SURVEY_TITLES,  label=('Please select survey title'))
   # start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label=('End date of survey'))
    


class SelectMeetingForm(forms.Form):
    MEETING_TITLES = MeetingProject.objects.all().values_list('id','name_meeting').order_by('name_meeting').distinct() 
    
    by_name_meeting =  forms.ChoiceField(choices = MEETING_TITLES,  label=('Please select name meeting'))
   # start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label=('Date of meeting'))

   

   
    