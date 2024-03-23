from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('beranda.urls')),
    path('app/', include('app.urls')),

]
