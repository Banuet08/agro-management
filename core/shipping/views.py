from rest_framework import viewsets
from shipping.serializer import ClientSerializer,ProductSerializer,DriverSerializer,TruckSerializer,ContainerSerializer,CustomSerializer
from shipping.models import Client,Product,Driver,Truck,Container,Custom
from rest_framework.permissions import IsAuthenticated

class BaseViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

# Create your views here.
class ClientView(BaseViewset):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    

class ProductView(BaseViewset):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class DriverView(BaseViewset):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

class TruckView(BaseViewset):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

class ContainerView(BaseViewset):
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()

class CustomView(BaseViewset):
    serializer_class = CustomSerializer
    queryset = Custom.objects.all()
