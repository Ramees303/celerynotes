from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')
#we must write the name of projectfolder.settings

app = Celery('django_celery_project')
app.conf.enable_utc = False

# the timezone is currently set the timezone as utc we must change it into our timezone 
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings,namespace = 'CELERY')

#Celery Beat Settings:- it is used for performing a schedule task/periodic task
#pip install django_celery_beat
#so we add task and it perform at the time we are given
#In periodic task we mention interval after the interval it will happen again and again
#cmd for celery beat:- celery -A django_celery_project(project name) beat -l INFO
app.conf.beat_schedule = {
    
    # in here celery beat is allocating tasks rather than django
    # enter the task that want to be schedule here 
    # celery beat will send the task to  broker(redis) and it will send to celery worker at given particular time

    'send-mail-every-day-at-8':{
        'task':'send_mail_app.tasks.send_mail_func',
        #task:appname.tasks.function name inside task
        # for scheduling task at particular time we use corn tab
        'schedule': crontab(hour=1,minute=0),
        # if we want to send one time we can add day_of_month,month_of_year inside crontab
        # crontab(hour=1,minute=5,day_of_month=12,month_of_year=2)
        # when we can change the time in crontab () the databases are modified
        # if we want to pass data we can use args

    }
    




 }









app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')





