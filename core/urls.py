from rest_framework import routers
from .views import ClientViewSet, AddictOperationViewSet, SubtractOperationViewSet

router = routers.SimpleRouter()
router.register('user', ClientViewSet, basename='user')
router.register('add', AddictOperationViewSet, basename='add')
router.register('sub', SubtractOperationViewSet, basename='sub')

urlpatterns = []
urlpatterns += router.urls
