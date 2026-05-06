from django.db import models
from django.core.validators import FileExtensionValidator

class Lecture(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(
        upload_to="lectures/",
        validators=[FileExtensionValidator(["pdf"])],
        blank=True,
    )

    def __str__(self):
        return self.title


class Practice(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(
        upload_to="practice/",
        validators=[FileExtensionValidator(["pdf"])],
        blank=True,
    )

    def __str__(self):
        return self.title


class Resource(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(
        upload_to="resources/",
        validators=[FileExtensionValidator(["pdf"])],
        blank=True,
    )

    def __str__(self):
        return self.title