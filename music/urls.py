from django.urls import path, include
from .views import ActorAPIView, MovieAPIView, MovieViewSet, ActorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actor', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('actor_list/', ActorAPIView.as_view(), name='actor'),
    path('movi_list/', MovieAPIView.as_view(), name='movie'),
    # path('movis/',MovieViewSet.as_view, name='maw')
]

