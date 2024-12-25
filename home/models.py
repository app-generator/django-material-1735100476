# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Adminuser(models.Model):

    #__Adminuser_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)

    #__Adminuser_FIELDS__END

    class Meta:
        verbose_name        = _("Adminuser")
        verbose_name_plural = _("Adminuser")


class Church(models.Model):

    #__Church_FIELDS__
    location = models.CharField(max_length=255, null=True, blank=True)

    #__Church_FIELDS__END

    class Meta:
        verbose_name        = _("Church")
        verbose_name_plural = _("Church")


class Member(models.Model):

    #__Member_FIELDS__
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    #__Member_FIELDS__END

    class Meta:
        verbose_name        = _("Member")
        verbose_name_plural = _("Member")



#__MODELS__END
