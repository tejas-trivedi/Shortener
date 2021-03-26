from django.db import models
class URL_Short(models.Model):
    short_url = models.CharField(max_length=20, unique=True)
    long_url = models.URLField("URL", unique=True)

    def __str__(self):
        return self.long_url