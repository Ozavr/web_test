import django_rq
from tasks.models import TaskState


class QueueManager:
    """
    queue switching implementation
    """
    def __init__(self):
        self.key = 'current_tasks_queue'
        self.default_value = '1'
        self.queues = self.get_dict_queues()

    def get_dict_queues(self):
        queue_1 = django_rq.get_queue('tasks_queue_1')
        queue_2 = django_rq.get_queue('tasks_queue_2')
        queues = {}
        queues['1'] = queue_1
        queues['2'] = queue_2
        return queues

    def get_queue(self):
        state_obj = self.get_state_obj()
        state_obj = self.refresh_state_obj(state_obj)
        current_tasks_queue = state_obj.value
        queue = self.queues[current_tasks_queue]
        return queue

    def get_state_obj(self):
        try:
            state_obj = TaskState.objects.get(key=self.key)
        except:
            state_obj = self.create_state_object()
        return state_obj

    def create_state_object(self):
        state_obj = TaskState.objects.create(key=self.key, value=self.default_value)
        return state_obj
        
    def refresh_state_obj(self, state_obj):
        if state_obj.value == '1':
            state_obj.value = '2'
        elif state_obj.value == '2':
            state_obj.value = '1'
        else:
            state_obj.value = '1'
        state_obj.save()
        return state_obj
