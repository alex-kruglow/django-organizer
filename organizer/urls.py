from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account_app.urls')),
    path('', include('calendar_app.urls')),
]
