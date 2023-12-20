from django.db import models


class BaseCustomAuthModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True