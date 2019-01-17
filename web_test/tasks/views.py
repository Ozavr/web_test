import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_rq
from tasks.serializers import TaskCreateSerializer, TaskGetSerializer
from tasks.models import Task
from tasks.tests import execute_task


class TaskCreateApi(APIView):
    def __init__(self, **options):
        super(TaskCreateApi, self).__init__(**options)
        self.serializer = TaskCreateSerializer
        self.queue = django_rq.get_queue('tasks_queue', is_async=True)

    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        try:
            response = self.create_task(serializer)
        except Exception as error:
            response = self.get_error_response(serializer, error)
        return response

    def create_task(self, serializer):
        if serializer.is_valid():
            response = self.save_task(serializer) 
        else:
            response = self.get_invalid_response(serializer)
        return response

    def save_task(self, serializer):
        serializer.save()
        self.queue.enqueue(execute_task, serializer.data['id'])
        response_data = serializer.get_success_response()
        response =  Response(response_data, status=status.HTTP_201_CREATED)
        return response

    def get_invalid_response(self, serializer):
        response_data = serializer.get_invalid_response()
        response = Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        return response

    def get_error_response(self, serializer, error):
        response_data = serializer.get_error_response(error)
        response = Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response


class TaskGetApi(APIView):
    serializer = TaskGetSerializer
    model = Task

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = self.serializer(task)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            data = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            data = {}
        return data