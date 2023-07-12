from django.urls import path

from todo_list.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name='todo_list'),
]
