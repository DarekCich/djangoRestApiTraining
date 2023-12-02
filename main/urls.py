from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Szkolenie z REST API w Django",
        default_version='v1',
        description="Proste api do przeznaczone do zapoznania zespołu z tworzeniem REST API w Django",
        contact=openapi.Contact(email="dariusz.c01@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
  path('normal/', include('normal.urls')),
  path('protected/', include('protected.urls'))
]
