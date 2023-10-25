from django.urls import path, include
from rest_framework import routers
from shipping import views

#api versioning
router = routers.DefaultRouter()
router.register(r'clients',views.ClientView, 'clients')
router.register(r'products',views.ProductView, 'products')
router.register(r'drivers',views.DriverView, 'drivers')
router.register(r'trucks',views.TruckView, 'trucks')
router.register(r'containers',views.ContainerView, 'containers')
router.register(r'customs',views.CustomView, 'containers')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]


# this code generate GET,POST,PUT,DELETE