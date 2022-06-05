from django.urls import path
from IAPS_app.h_officer_views import IndexView,Prisoner_View,Add_Health_Details,View_Health,View_Update_Health

urlpatterns = [

    path('',IndexView.as_view()),
    path('view_prisoner',Prisoner_View.as_view()),
    path('add_health_details',Add_Health_Details.as_view()),
    path('view_health',View_Health.as_view()),
    path('view_update_health',View_Update_Health.as_view())

    ]
def urls():
    return urlpatterns, 'health_officer', 'health_officer'