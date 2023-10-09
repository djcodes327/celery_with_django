from celery import shared_task


@shared_task(bind=True)
def test_task(self):
    # Operations
    for i in range(5):
        print(i)
    return "Done"
