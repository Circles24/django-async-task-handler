from queue import Queue
from .models import Task
import time
from django.utils import timezone
import threading

WORKER_THREADS = 10
task_queue = Queue()

def process_task(task_id):
    # dummy loop to demonstrate large operation consisting of multiple atomic operations
    
    print(f'task::{task_id} starting processing')
    op_completed = 0
    while op_completed < 30:
        t = Task.objects.filter(pk=task_id).first()
        if t.is_paused:
           print(f'task::{task_id} paused')
           time.sleep(60)
        elif t.is_cancelled:
            print(f'task::{task_id} cancelled')
            print(f'task::{task_id} rolling back')
            print(f'task::{task_id} rolled_back')
            break
        else:
            print(f'task::{task_id} processing op::{op_completed}')
            time.sleep(10)
            op_completed += 1
    t = Task.objects.filter(pk=task_id).first()
    t.completed_at = timezone.now()
    t.is_completed = True
    t.save()
    print(f'task::{task_id} completed')


def task_assigner():
    while True:
        task_id = task_queue.get()
        process_task(task_id)

def bootstrap_workers():
    for i in range(WORKER_THREADS):
        worker_thread = threading.Thread(target=task_assigner, daemon=True)
        worker_thread.start()


