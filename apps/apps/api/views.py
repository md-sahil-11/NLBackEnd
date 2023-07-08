from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.apps.models import App, Category, Task
from apps.apps.api.serializers import AppSerializer, CategorySerializer, TaskSerializer

from apps.apps.permissions import AppActionBasedPermission


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [AppActionBasedPermission,]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated,]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        queryset = Task.objects.all()
        completed = self.request.query_params.get("completed", None)
        if completed is not None:
            if completed in ["true", "True", "1", True, 1]:
                queryset = queryset.filter(is_completed=True)
            else:
                queryset = queryset.filter(is_completed=False)
    
        return queryset
        