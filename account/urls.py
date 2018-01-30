from rest_framework import routers

from account.views import UserViewSet


router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls
