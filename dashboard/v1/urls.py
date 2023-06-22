from django.urls import path

from dashboard.v1.diagnoz.views import DiagnozViews
from dashboard.v1.files.views import FileViews
from dashboard.v1.patient.views import PatientViews
from dashboard.v1.retseps.views import RetsepViews

urlpatterns = [

    path("patient/", PatientViews.as_view()),

    path('files/', FileViews.as_view()),

    path('retsep/', RetsepViews.as_view()),

    path('diagnoz/', DiagnozViews.as_view()),



]