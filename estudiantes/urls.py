
from rest_framework.routers import DefaultRouter

from estudiantes.views import StudentViewSet, SubjectViewSet

router = DefaultRouter()
router.register('estudiantesRest', StudentViewSet)
router.register('materiasRest', SubjectViewSet)

urlpatterns = router.urls
