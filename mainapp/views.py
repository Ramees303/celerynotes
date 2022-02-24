from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func

from django_celery_beat.models import PeriodicTask,CrontabSchedule
# Create your views here.

def test(request):
#calling function to allocate task to celery
    test_func.delay()
    return HttpResponse("Done")

#installing redis:-pip install redis
#for starting celery worker we have a commad
#celery -A django_celery_project(projectname).celery worker --pool=solo  -l info

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Done")

# for making task dynamic   ie   adding and removing task dynamically
def schedule_mail(request):
    schedule,created = CrontabSchedule.objects.get_or_create(hour = 1 , minute = 10)
    # The other fields default are * (ie *-all)
    task = PeriodicTask.objects.create(crontab=schedule,name="schedule_mail_task_" + "1",task = 'send_mail_app.tasks.send_email_func')
    # we are creating an instance of periodictask and name must be unique and also mention task
    return HttpResponse('Ok')






