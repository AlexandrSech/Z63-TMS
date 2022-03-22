from .views import TaskViewSet, TaskStatusesViewSet, TaskCommentsViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'comments', TaskStatusesViewSet)
router.register(r'statuses', TaskCommentsViewSet)

urlpatterns = router.urls
