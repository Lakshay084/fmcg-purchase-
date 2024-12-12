from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit-tender/', views.submit_tender, name='submit_tender'),
    path('login/', views.supplier_login, name='supplier_login'),
    path('track-progress/', views.track_progress, name='track_progress'),
    path('vendor-login/', views.vendor_login, name='vendor_login'),
]
