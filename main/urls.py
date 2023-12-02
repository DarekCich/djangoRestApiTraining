from django.urls import path, include

urlpatterns = [
  path('normal/', include('normal.urls')),
  path('protected/', include('protected.urls'))
]
