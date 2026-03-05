from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    state = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
