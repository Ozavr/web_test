from rest_framework import serializers
from tasks.models import Task


class TaskCreateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Task
        fields = ('id',)

    def get_success_response(self):
        data = {}
        data['status'] = True
        data['task_id'] = self.data['id']
        return data
    
    def get_invalid_response(self):
        data = {}
        data['status'] = False
        data['exception'] = self.errors
        return data

    def get_error_response(self, error):
        data = {}
        data['status'] = False
        data['exception'] = error
        return data


class TaskGetSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'