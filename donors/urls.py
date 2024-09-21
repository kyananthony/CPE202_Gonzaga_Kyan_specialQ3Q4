from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from donors import views as donors_views
urlpatterns = [
    path('donors/', views.donor_list, name='donor_list'),
    path('requests/', views.request_list, name='requests_list'),
    path('admin/', admin.site.urls),
    path('donors/', include('donors.urls')),
    path('', donors_views.home, name='home'),
]
