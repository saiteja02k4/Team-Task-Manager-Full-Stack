from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from projects.views import ProjectViewSet
from tasks.views import dashboard
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include(router.urls)),
    path('api/dashboard/', dashboard),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

