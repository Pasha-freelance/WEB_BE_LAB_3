from django.urls import path

from todo.views import all_todos, add_todo, remove_todo, edit_todo

urlpatterns = [
    path('all-todos/', all_todos),
    path('add-todo/', add_todo),
    path('edit/<str:identifier>/', edit_todo, name='edit_todo'),
    path('delete/<str:identifier>/', remove_todo, name='remove_todo'),
]