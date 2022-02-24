#we can create tasks for our required app

from celery import shared_task

@shared_task(bind=True)
# we can create any function that we need to allocate(move) to  celery
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return "Done"

