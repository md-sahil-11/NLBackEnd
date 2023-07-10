from rest_framework.routers import DefaultRouter

from . import views

app_name = "applications"

router = DefaultRouter(trailing_slash=False)

router.register("apps", views.AppViewSet, basename="apps")
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("tasks", views.TaskViewSet, basename="tasks")

urlpatterns = router.urls
