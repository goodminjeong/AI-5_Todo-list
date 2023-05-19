from django.urls import path
from lists import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list_view'),
    path('<int:todo_id>/', views.TodoView.as_view(), name='todo_view'),
    path('<int:todo_id>/complete/',
         views.TodoCompletionView.as_view(), name='todo_view'),
]
