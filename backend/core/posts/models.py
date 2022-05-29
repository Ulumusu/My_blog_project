from django.db import models
from datetime import datetime

now = datetime.now()


class Post(models.Model):
    title = models.CharField(max_length=250)
    beginning = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_picture = models.ImageField(blank=False, upload_to='postImages/' + now.strftime("%Y/%m/%d/%H:%M:%S"))
    main_text = models.TextField()


class Text(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='texts')
    text_number = models.IntegerField()
    picture = models.ImageField(blank=False, upload_to='postImages/' + now.strftime("%Y/%m/%d/%H:%M:%S"))
    text = models.TextField()

    class Meta:
        unique_together = ['post', 'text_number']
        ordering = ['text_number']

    