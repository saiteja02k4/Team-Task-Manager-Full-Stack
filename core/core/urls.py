from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, dashboard
from projects.views import ProjectViewSet
from .views import home

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 🔥 ADD HERE
admin.site.site_header = "Smart Invitation Admin"
admin.site.site_title = "Smart Invitation"
admin.site.index_title = "Welcome to Smart Invitation Dashboard"

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/dashboard/', dashboard),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

