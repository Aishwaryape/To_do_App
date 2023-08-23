from django.urls import path

from .views import TodoTaskListCreateView, TodoTaskRetrieveUpdateDeleteView

urlpatterns = [
    path('tasks/', TodoTaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TodoTaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    path('tasks/<int:pk>/complete/', TodoTaskRetrieveUpdateDeleteView.as_view(), name='task-mark-complete'),
    path('tasks/<int:pk>/schedule/', TodoTaskRetrieveUpdateDeleteView.as_view(), name='task-schedule'),
    path('tasks/<int:pk>/reschedule/', TodoTaskRetrieveUpdateDeleteView.as_view(), name='task-reschedule'),
    path('tasks/<int:pk>/reminder/', TodoTaskRetrieveUpdateDeleteView.as_view(), name='task-send-reminder'),

]
