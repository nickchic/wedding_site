from __future__ import unicode_literals

from django.db import models

class GuestValidations(models.Manager):
    def user_validate(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 1:
            errors['first_name'] = "First Name must not be blank"
        if len(postdata['last_name']) < 1:
            errors['last_name'] = "Last Name must not be blank"
        return errors

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    attending = models.BooleanField()
    staying = models.BooleanField()
    color_war = models.BooleanField()
    rehearsal = models.BooleanField()
    rsvp = models.BooleanField()
    shirt_size = models.CharField(max_length=5, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GuestValidations()

class Invite(models.Model):
    guest_1 = models.ForeignKey(Guest, related_name="invites_1")
    guest_2 = models.ForeignKey(Guest, related_name="invites_2", null=True)
    greeting = models.CharField(max_length=255)
    passcode = models.CharField(max_length=4)
    opened = models.BooleanField()
    completed = models.BooleanField()
    form_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
