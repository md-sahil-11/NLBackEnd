from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.applications.models import App, Category, Task
from apps.applications.api.serializers import AppSerializer, CategorySerializer, TaskSerializer

from apps.applications.permissions import AppActionBasedPermission


class AppViewSet(viewsets.ModelViewSet):
    # queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [AppActionBasedPermission,]

    def get_queryset(self):
        queryset = App.objects.all()

        completed = self.request.query_params.get("completed", None)
        if completed is not None:

            app_ids = Task.objects.filter(user=self.request.user).values_list("app_id", flat=True)
            if completed in ["true", "True", "1", True, 1]:
                queryset = queryset.filter(id__in=app_ids)
            else:
                queryset = queryset.exclude(id__in=app_ids)
    
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated,]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
        