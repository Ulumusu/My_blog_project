from .models import AboutMe, Part
from .serializers import AboutMeSerializer, PartSerializer
from rest_framework import viewsets


class Part_detail_view(viewsets.ReadOnlyModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class About_me_details_view(viewsets.ReadOnlyModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer