from django.db import models
from datetime import datetime

now = datetime.now()


# Create your models here.
class AboutMe(models.Model):
    beginning = models.TextField()


class Part(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='parts')
    part_number = models.IntegerField()
    text = models.TextField()
    picture = models.ImageField(blank=True, upload_to='partImages/' + now.strftime("%Y/%m/%d/%H:%M:%S"))

    class Meta:
        unique_together = ['about', 'part_number']
        ordering = ['part_number']

