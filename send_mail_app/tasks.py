from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_celery_project import  settings

from celery import shared_task
# for using timezone in django
from django.utils import timezone
from datetime import timedelta



@shared_task(bind=True)
# we can create any function that we need to allocate(move) to  celery
def send_mail_func(self):
    # sending mail to all users if  we want to send mail to specific person 
    # we can use filter to filter the user 
    users=get_user_model().objects.all()
    # if we have date_time in our db to connect with our time to datetime we use timezone.localtime
    # for performing calculation we use timedelta eg:adding 2 days 
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "hi subject name"
        message = "content of message  that need to snd "
        to_email = user.email
        #sending the email to the users
        send_mail(
            subject=mail_subject'
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
            # if sending of mail failures to one user it doesnt affect the other user 

        )
        return 'Done'







        
         