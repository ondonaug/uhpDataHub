from django.contrib import admin

from myUHP.models import Feature, Subscribers, MailMessage,Statutworkplan,Outputworkplan,Country,Units,GsmWorkplan,Operworkplan,Kpi,KpiAchieve, IndividualReport, SurveyDataset, DocSave, ReportSave, TypeMeeting,MeetingProject, MeetingDiscussion,BriefingProject,BriefingBackground,RiskIdentification, Toptask
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Feature)
admin.site.register(Subscribers)
admin.site.register(MailMessage)
admin.site.register(Country)
admin.site.register(Statutworkplan)
admin.site.register(Outputworkplan)
admin.site.register(Units)
admin.site.register(GsmWorkplan)
admin.site.register(Operworkplan, ImportExportModelAdmin)
admin.site.register(Kpi)
admin.site.register(KpiAchieve)
admin.site.register(IndividualReport)
admin.site.register(TypeMeeting)
admin.site.register(MeetingProject)
admin.site.register(MeetingDiscussion)
admin.site.register(BriefingProject)
admin.site.register(BriefingBackground)
admin.site.register(RiskIdentification)
admin.site.register(Toptask)
admin.site.register(SurveyDataset, ImportExportModelAdmin)

class SurveyDatasetAdmin(ImportExportModelAdmin):
    list_display = ('title_surv','start_date', 'end_date','location_survey', 'quest_code', 'question', 'response_text','response_num')

admin.site.register(DocSave, ImportExportModelAdmin)
admin.site.register(ReportSave, ImportExportModelAdmin)
