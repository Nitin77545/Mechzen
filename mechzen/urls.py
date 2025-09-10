from django.contrib import admin
from django.urls import path, include  # <-- include imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  # your app urls
]
