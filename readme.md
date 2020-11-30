# Django Async Task Handler

This is a sample app to demonstrate how async tasks can be handled using django and celery task queue, it provides abilities to

  - Initiate a task 
  - Pause a task
  - Resume a task
  - Cancel a task

### Installation

It requires [django](https://www.djangoproject.com/) and [celery](https://docs.celeryproject.org/en/stable/) to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd atlan
$ pip install -r requirements.txt
$ python manage.py runserver
```
In another console start the celery worker
```sh
$ celery -A atlan worker
```

Api endpoints are
  - Initiate a task -> /processor/create
  - Pause a task -> /processor/pause
  - Resume a task -> /processor/resume
  - Cancel a task -> /processor/cancel
  - Get a task -> /processor/get



