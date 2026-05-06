from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Project.objects.all()

        return Project.objects.filter(members=user)
