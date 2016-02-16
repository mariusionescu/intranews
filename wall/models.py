from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('html', 'HTML'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('script', 'Script'),
        ('iframe', 'Iframe')
    )

    title = models.CharField(max_length=256, null=True)
    component_type = models.CharField(max_length=32, choices=TYPES, null=False, default='html')
    value = models.TextField(null=False)
    parent = models.ForeignKey('Component', null=True)


class Comment(models.Model):
    component = models.ForeignKey('Component')
    user = models.ForeignKey(User, null=True)
    value = models.TextField()



