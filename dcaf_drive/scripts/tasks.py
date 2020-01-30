from __future__ import absolute_import, unicode_literals
from django.conf import settings
from .scripts import *

from celery import shared_task
from celery.decorators import task, periodic_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                       7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command_to_execute
# or check crontab.guru

#run on the 1st and 15th of the month, once @midnight
#0 0 1,15 * * echo 'Hello' >> /tmp/test.txt

#interval every 10mins
#/10 * * * * echo...

#range - run every hour from midnight to 5AM
#0 0-5 * * * echo...


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