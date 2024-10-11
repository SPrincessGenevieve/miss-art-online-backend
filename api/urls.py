from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_app.urls')),
    path('customer/', include('customer_app.urls')),
    path('order/', include('order_app.urls')),
]