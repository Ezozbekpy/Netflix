from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Muci app uchun AIP docs',
        default_version='v1',
        description='api da hamma narsa batafsil korsatilgan ! ',
        contact= openapi.Contact(email='ezozbek@gmail.com'),
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    path('doc/', schema_view.with_ui('swagger', ), name='swagger-doc'),
    path('redoc/', schema_view.with_ui('redoc', ), name='redoc-doc'),
]
