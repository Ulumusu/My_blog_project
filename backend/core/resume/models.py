from django.db import models
from datetime import datetime

now = datetime.now()
type_of_choice = (
    (1, 'Job'),
    (2, 'Certificate'),
    (3, 'Education'),
    (4, 'Hobby'),
)


class Resume(models.Model):
    main_photo = models.ImageField(blank=False, upload_to='resumeImage/' + now.strftime("%Y/%m/%d/%H:%M:%S"))
    name_surname = models.CharField(max_length=25)
    email_info = models.CharField(blank=False, max_length=25)


class Competence(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='competences')
    competence_number = models.IntegerField()
    choice = models.PositiveIntegerField(choices=type_of_choice, blank=False)
    title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    details = models.TextField(max_length=250)

    class Meta:
        unique_together = ['resume', 'competence_number']
        ordering = ['competence_number']
