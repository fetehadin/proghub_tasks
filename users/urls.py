from django.urls import path
from .views import user_list, user_create, user_delete

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/create/', user_create, name='user-create'),
    path('users/delete/<int:id>/', user_delete, name='user-delete'),
]