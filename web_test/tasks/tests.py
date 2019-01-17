import time
import random
from django_rq import job
from django.shortcuts import get_object_or_404
from django.utils import timezone
from tasks.models import Task


@job('tasks_queue')
def execute_task(task_id):
    update_status_task(task_id, status='Run')
    time.sleep(random.randint(0,10))
    print('Task completed', task_id)
    update_status_task(task_id, status='Completed')


def update_status_task(task_id, status):
    task = get_object_or_404(Task, pk=task_id)
    task.status = status
    if status == 'Run':
        task.start_time = timezone.now()
    elif status == 'Completed':
        task.exec_time = timezone.now()
    task.save()
