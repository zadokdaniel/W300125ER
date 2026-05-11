from django.db import models
import django.core.validators as v

# Create your models here.


def validate_not_length_11(value):
    if len(value) == 11:
        raise v.ValidationError("Content length cannot be 11 characters long.")


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, error_messages={
        'unique': "unique error",
        'blank': "blank field please fill"
    })
    content = models.TextField(
        validators=[
            v.MinLengthValidator(5, message='Content is too short'),
            validate_not_length_11
        ]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
