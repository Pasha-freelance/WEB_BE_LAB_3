from django.urls import path

from todo.views import all_todos, todos_count, add_todo

urlpatterns = [
    path('todos-count/', todos_count),
    path('all-todos/', all_todos),
    path('add-todo/', add_todo)
]