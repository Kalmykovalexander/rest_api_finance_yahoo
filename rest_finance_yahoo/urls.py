from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel path
    path('admin/', admin.site.urls),
    # API path
    path('api/', include('historical_data.urls')),
]
