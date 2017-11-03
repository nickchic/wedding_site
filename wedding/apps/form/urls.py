from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^guest_form_one', views.guest_form_one),
    url(r'^passcode', views.passcode),
    url(r'^all_guests', views.guest_view),
    url(r'^form', views.form),
]
