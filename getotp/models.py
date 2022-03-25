#!/usr/bin/env python
# $Id$
#
# Copyright (c) 2021 Lalokalabs Inc

__author__ = "Surya Banerjee <surya@xoxzo.com>"

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class OTP(models.Model):
    otp_id = models.CharField(max_length=100, unique=True)
    link = models.URLField()
    otp_secret = models.CharField(max_length=100)
    status = models.CharField(max_length=200, default="initiated")
    callback_time = models.DateTimeField(null=True, blank=True)
    creation_time = models.DateTimeField(default=timezone.now, blank=True)
    email = models.CharField(max_length=255, default="")
    phone_sms = models.CharField(max_length=255, default="")
    phone_voice = models.CharField(max_length=255, default="")
    metadata = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.otp_id


    def verify(self, age=60*10):
        age = datetime.timedelta(seconds=age)
        expiry_time = self.creation_time + age
        if expiry_time > datetime.datetime.now():
            return self.status == "verified"

        return False
