from rest_framework import serializers
from .models import Task
from atlan.celery import app
from .tasks import process_task

class TaskMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def start_async_processing(self):
        process_task.delay(self.data['id'])

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    operation = serializers.CharField()

    def validate_id(self, id):
        queryset = Task.objects.filter(pk=id)
        if len(queryset) == 0:
            raise serializers.ValidationError('no such task')
        
        return id

    def validate(self, data):
        task = Task.objects.filter(pk=data['id']).first()
        if data['operation'] != 'get' and task.is_completed == True:
            raise serializers.ValidationError('task already completed')
        elif data['operation'] == 'pause' and task.is_paused == True:
            raise serializers.ValidationError('task already paused')
        elif data['operation'] == 'resume' and task.is_paused == False:
            raise serializers.ValidationError("task isn't paused")
        return data

    def get_task(self):
        return Task.objects.filter(pk=self.validated_data['id']).first()

    def pause(self):
        task = self.get_task()
        task.is_paused = True
        task.save()

    def resume(self):
        task = self.get_task()
        task.is_paused = False
        task.save()

    def cancel(self):
        task = self.get_task()
        task.is_cancelled = True
        task.save()



