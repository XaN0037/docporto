from django.urls import path

from dashboard.v1.patient.views import PatientViews

urlpatterns = [

    path("patient/", PatientViews.as_view()),

    # path("doctor/", DoctorViews.as_view()),
    #
    # path("new/", NewViews.as_view()),

]