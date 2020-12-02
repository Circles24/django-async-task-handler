from django.urls import path
from .views import (create_task, get_task, pause_task, resume_task, cancel_task)

urlpatterns = [
    path('create', create_task, name='create task'),
    path('get', get_task, name='get task'),
    path('pause', pause_task, name='pause task'),
    path('resume', resume_task, name='resume task'),
    path('cancel', cancel_task, name='cancel task'),
]

import threading
from .worker import bootstrap_workers

worker_thread = threading.Thread(target=bootstrap_workers, daemon=True)
worker_thread.start()
