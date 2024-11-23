# Create your views here.
from rest_framework import viewsets
from .models import Hymn
from .serializers import HymnSerializer

class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer


