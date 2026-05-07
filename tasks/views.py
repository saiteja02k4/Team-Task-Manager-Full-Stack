from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.timezone import now

from .models import Task
from .serializers import TaskSerializer


# ✅ Task ViewSet (THIS WAS MISSING / DELETED)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Task.objects.all()

        return Task.objects.filter(assigned_to=user)


# ✅ Dashboard API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user

    if user.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user)

    total = tasks.count()
    completed = tasks.filter(status='done').count()
    pending = tasks.filter(status='pending').count()
    overdue = tasks.filter(due_date__lt=now().date()).exclude(status='done').count()

    return Response({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "overdue_tasks": overdue
    })
