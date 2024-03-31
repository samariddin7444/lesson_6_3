from django.db import models


class Student(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FileField()
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.price}"
