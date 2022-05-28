from rest_framework import serializers
from .models import Resume, Competence


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ['competence_number','choice','title', 'start_date', 'end_date', 'company', 'type', 'details']


class ResumeSerializer(serializers.ModelSerializer):
    competences = CompetenceSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'main_photo', 'name_surname', 'email_info', 'competences']
