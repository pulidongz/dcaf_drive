from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery import shared_task

from celery.decorators import task, periodic_task
from celery.schedules import crontab
from django.utils.crypto import get_random_string

@periodic_task(
    run_every=(crontab(minute="*")),
    name="add",
    ignore_result=True
)
def add():
	return 5 + 5

@shared_task
def mul(x, y):
	return x * y


@shared_task
def xsum(numbers):
	return sum(numbers)