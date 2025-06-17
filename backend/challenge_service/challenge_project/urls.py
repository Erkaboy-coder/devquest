from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('challange/admin/', admin.site.urls),
    path('challange/api/', include('challenges.urls')),
]
