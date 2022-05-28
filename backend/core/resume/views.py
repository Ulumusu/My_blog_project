from .models import Resume, Competence
from .serializers import CompetenceSerializer, ResumeSerializer
from rest_framework import viewsets


class Competence_detail_view(viewsets.ReadOnlyModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class Resume_details_view(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer