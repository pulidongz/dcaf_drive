from __future__ import absolute_import, unicode_literals
from django.conf import settings
from .scripts import *

from celery import shared_task
from celery.decorators import task, periodic_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# @periodic_task(
#     run_every=(crontab(minute="*")),
#     name="add",
#     ignore_result=True
# )
# def add():
# 	return 5 + 5

@shared_task
def mul(x, y):
	return x * y


@shared_task
def xsum(numbers):
	return sum(numbers)

@periodic_task(
	run_every=(crontab(minute="*")),
    name="create_file",
    ignore_result=True
)
def create_file():
	CreateFile()
	logger.info("Created tiff file.")