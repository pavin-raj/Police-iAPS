from django.urls import path
from IAPS_app.warden_views import IndexView, Add_Prisoner, View_Prisoner, View_Details, Add_Complaints, View_Actions, \
    Parole_Request, Parole_Request_View, Add_Task, View_Task, Add_Attendance, Salary_View, Attendance_View, \
    Add_Schedule, View_Schedule, Update_Schedule, \
    View_Scheduled_Task, Update_Task, update_view_details, date_wise_view, Remove_Prisoner

urlpatterns = [

    path('',IndexView.as_view()),
    path('add_prisoner',Add_Prisoner.as_view()),
    path('view_prisoner',View_Prisoner.as_view()),
    path('view_details',View_Details.as_view()),
    path('complaints',Add_Complaints.as_view()),
    path('view_action',View_Actions.as_view()),
    path('parole_request',Parole_Request.as_view()),
    path('parole_request_view',Parole_Request_View.as_view()),
    path('add_task',Add_Task.as_view()),
    path('view_task',View_Task.as_view()),
    path('add_attendance',Add_Attendance.as_view()),
    path('salary_view',Salary_View.as_view()),
    path('attendance_view',Attendance_View.as_view()),
    path('add_schedule',Add_Schedule.as_view()),
    path('view_schedule',View_Schedule.as_view()),
    path('update_schedule',Update_Schedule.as_view()),
    path('view_schedule_task',View_Scheduled_Task.as_view()),
    path('update_task',Update_Task.as_view()),
    path('update_view_details',update_view_details.as_view()),
    path('date_wise_view',date_wise_view.as_view()),
    path('prison_remove',Remove_Prisoner.as_view())

]
def urls():
    return urlpatterns, 'warden', 'warden'