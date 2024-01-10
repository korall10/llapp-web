from django.urls import path
from rest_framework.routers import DefaultRouter
from note.views import NoteViewSet

router = DefaultRouter()
router.register('', NoteViewSet)

paths = []

urlpatterns = router.urls + paths
