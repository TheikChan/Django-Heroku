from django.db import models


class ProjectHistory(models.Model):
    title = models.CharField(max_length=255, default='')