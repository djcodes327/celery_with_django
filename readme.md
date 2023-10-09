## Commands Used in this Project

#### Start the Celery

Celery -A app_name(App Name).celery worker -l (log) info (Log Level)

`celery -A celery_with_django.celery worker --pool=solo -l info`

To Start Celery Beat

`celery -A celery_with_django beat -l info`

`--pool` decides who will perform the tasks i.e. threads,process,worker,etc

`--concurrency` will decide the size of pool. Note max = Number of Cores in system

`--autoscale` you can specify this for auto-scaling the pool size min and max values can be set here to manage load of pool.

```python
# Example Below

celery -A celery_with_django.celery worker --pool=solo --concurrency=5 --autoscale=10,3 -l info
```

#### Execution Pool can have below different options
1. Pre-fork (Multi-processing) [default]
2. Solo
3. Threads (Multi-threading)
4. eventlet
5. gevent

**Basic Setup Below**


Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_with_django.settings')

```python
app = Celery('celery_with_django')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
```

Using a string here means the worker doesn't have to serialize
the configuration object to child processes.
namespace='CELERY' means all celery-related configuration keys
should have a `CELERY_` prefix.

`app.config_from_object('django.conf:settings', namespace='CELERY')
`
#### Celery Beat Settings

```python
app.conf.beat_schedule = {
    'send-mail-everyday-at-8': {
        'task': 'send_emails.tasks.send_user_email',
        'schedule': crontab(hour=8, minute=0),
    }
}
```

Load task modules from all registered Django apps.

`app.autodiscover_tasks()`

#### To Show Debug Output statements in Celery's Terminal

```python
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

#### Sample Test Task below

```python
@shared_task(bind=True)
def test_task(self):
    # Operations
    for i in range(5):
        print(i)
    return "Done"
```

### Calling the above task in view

```python
def index(request, *args, **kwargs):
    test_task.delay()
    return HttpResponse("Done")
```

`.delay()` is used to call the task. This will not send the data to celery worker to process the task further
