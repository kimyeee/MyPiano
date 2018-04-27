# coding: utf-8
from rest_framework.routers import SimpleRouter

from piano.views import PianoViewSet

router = SimpleRouter()

router.register('', PianoViewSet)

urlpatterns = router.urls
