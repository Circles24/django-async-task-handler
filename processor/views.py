from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskMSerializer, TaskSerializer
from .models import Task
from traceback import print_exc

@api_view(['POST'])
def create_task(request):
    try:
        serializer = TaskMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.start_async_processing()
            return Response({'msg':'operation successful'}, 200)
        else :
            return Response(serializer.errors, 400)
    except Exception as ex:
        print_exc()
        return Response({'msg':'internal server error'}, 500)

@api_view(['GET'])
def get_task(request):
    try:
        data = dict(request.data)
        data['operation'] = 'get'
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer = TaskMSerializer(serializer.get_task())
            return Response(serializer.data, 200)
        else :
            return Response(serializer.error, 400)
    except Exception as ex:
        print_exc()
        return Response({'msg':'internal server error'}, 500)


@api_view(['POST'])
def pause_task(request):
    try:
        data = dict(request.data)
        data['operation'] = 'pause'
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.pause()
            return Response({'msg':'operation successful'}, 200)
        else :
            return Response(serializer.errors, 400)
    except Exception as ex:
        print_exc()
        return Response({'msg':'internal server error'}, 500)


@api_view(['POST'])
def resume_task(request):
    try:
        data = dict(request.data)
        data['operation'] = 'resume'
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.resume()
            return Response({'msg':'operation successful'}, 200)
        else :
            return Response(serializer.errors, 400)
    except Exception as ex:
        print_exc()
        return Response({'msg':'internal server error'}, 500)


@api_view(['POST'])
def cancel_task(request):
    try:
        data = dict(request.data)
        data['operation'] = 'cancel'
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.cancel()
            return Response({'msg':'operation successful'}, 200)
        else :
            return Response(serializer.errors, 400)
    except Exception as ex:
        print_exc()
        return Response({'msg':'internal server error'}, 500)
