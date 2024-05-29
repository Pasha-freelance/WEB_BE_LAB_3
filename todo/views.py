from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
import uuid

from todo.models import Todo
from todo.serializers import UserSerializer, ToDoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]


# AUTHENTICATION
# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(request.data['password'])  # Make sure to handle password hashing
#         user.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO
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
    data = request.data.copy()  # Copy request data
    data['identifier'] = str(uuid.uuid4())
    serializer = ToDoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_todo(request, identifier):
    try:
        todo = Todo.objects.get(identifier=identifier)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ToDoSerializer(todo, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_todo(request, identifier):
    todo = Todo.objects.get(identifier=identifier)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
