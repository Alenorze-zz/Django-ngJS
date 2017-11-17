from django.db import models


class RestangElements(models.Model):
    restang_text = models.CharField(max_length=200)
    done = models.BooleanField()