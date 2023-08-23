from rest_framework import generics
from rest_framework.response import Response
from .models import TodoTask
from .serializers import TodoTaskSerializer


class TodoTaskListCreateView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer


class TodoTaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        action = request.data.get('action')

        if action == 'mark_complete':
            task.completed = True
            task.save()
            return Response({"message": "Task marked as complete"}, status=200)
        elif action == 'schedule':
            # Implement scheduling logic here
            return Response({"message": "Task scheduled successfully"}, status=200)
        elif action == 'reschedule':
            # Implement rescheduling logic here
            return Response({"message": "Task rescheduled successfully"}, status=200)
