from django.urls import path

from api.v1.contacts.views import ContactViews
from api.v1.doctors.views import DoctorViews
from api.v1.news.views import NewViews

urlpatterns = [

    path("contact/", ContactViews.as_view()),

    path("doctor/", DoctorViews.as_view()),

    path("new/", NewViews.as_view()),

]