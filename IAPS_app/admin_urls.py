from django.urls import path
from IAPS_app.admin_views import IndexView,Warden_Approvel,ApproveView,RejectView,Warden_View,Medical_Approve,Medical_View,Complaint_View, \
    View_Prisoner,Prisoner_Details,Parole_Request_View,View_Health,View_Health_Details

urlpatterns = [

    path('',IndexView.as_view()),
    path('warden_approvel',Warden_Approvel.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('warden_view',Warden_View.as_view()),
    path('medical_approve',Medical_Approve.as_view()),
    path('medical_view',Medical_View.as_view()),
    path('view_complaint',Complaint_View.as_view()),
    path('prisoner_view',View_Prisoner.as_view()),
    path('prisoner_details',Prisoner_Details.as_view()),
    path('parole_request_view',Parole_Request_View.as_view()),
    path('view_health',View_Health.as_view()),
    path('view_health_details',View_Health_Details.as_view())
    # path('action',Action.as_view())

    ]
def urls():
    return urlpatterns, 'admin', 'admin'