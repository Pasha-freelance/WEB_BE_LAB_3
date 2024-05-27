from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view

from todo.models import Todo
from todo.serializers import UserSerializer, ToDoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def todos_count(request):
    total = Todo.objects.all().count()
    return JsonResponse({'total': total})


@api_view(['GET'])
def all_todos(request):
    result = []
    for todo in Todo.objects.all():
        result.append({
            "id": todo.identifier,
            "description": todo.description,
            "deadline": todo.deadline
        })

    return JsonResponse({'result': result})


@api_view(['POST'])
def add_todo(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)