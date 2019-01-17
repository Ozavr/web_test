from django.db import models
from django.utils import timezone


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    STATUS_CHOICES = (
        ('In Queue', 'In Queue'),
        ('Run', 'Run'),
        ('Completed', 'Completed')
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, 
        default='In Queue', blank=False, null=False, verbose_name='Status')
    create_time = models.DateTimeField(blank=False, null=False, 
        default=timezone.now, verbose_name='create_time')
    start_time = models.DateTimeField(blank=True, null=False, 
        verbose_name='start_time')
    exec_time = models.DateTimeField(blank=True, null=False, 
        verbose_name='exec_time')


class TaskState(models.Model):
    """
    various states associated with this application, 
    created primarily to switch queues
    """
    key = models.CharField(max_length=32, blank=False, null=False, 
        unique=True, db_index=True, verbose_name='Key')
    value = models.CharField(max_length=32, blank=False, null=False, 
        verbose_name='Value')