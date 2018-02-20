from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^guest_form_zero', views.guest_form_zero),
    url(r'^guest_form_one', views.guest_form_one),
    url(r'^guest_form_two', views.guest_form_two),
    url(r'^guest_form_three', views.guest_form_three),
    url(r'^guest_form_four', views.guest_form_four),
    url(r'^passcode', views.passcode),
    url(r'^all_guests', views.guest_view),
    url(r'^form', views.form),
    url(r'^edit/guest/(?P<guest_id>[0-9]+)', views.edit_guest_page),
    url(r'^edit_action/guest/(?P<guest_id>[0-9]+)', views.edit_guest),
    url(r'^edit/invite/(?P<invite_id>[0-9]+)', views.edit_invite_page),
    url(r'^edit_action/invite/(?P<invite_id>[0-9]+)', views.edit_invite),
]
