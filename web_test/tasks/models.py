from django.db import models
from datetime import datetime


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    STATUS_CHOICES = (
        ('In Queue', 'In Queue'),
        ('Run', 'Run'),
        ('Completed', 'Completed')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='In Queue', blank=False, null=False, verbose_name='Status')
    create_time = models.DateTimeField(blank=False, null=False, default=datetime.utcnow(), verbose_name='create_time')
    start_time = models.DateTimeField(blank=True, null=False, verbose_name='start_time')
    exec_time = models.DateTimeField(blank=True, null=False, verbose_name='exec_time')