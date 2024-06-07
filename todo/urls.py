from django.urls import path

from todo.views import all_todos, add_todo, remove_todo, edit_todo, register_user, login_user

urlpatterns = [
    path('all-todos/<str:profile_id>', all_todos),
    path('add-todo/<str:profile_id>', add_todo),
    path('edit/<str:identifier>/', edit_todo, name='edit_todo'),
    path('delete/<str:identifier>/', remove_todo, name='remove_todo'),
    path('auth/register/', register_user),
    path('auth/login/', login_user)
]