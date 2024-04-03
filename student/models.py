from django.db import models


class Auther(models.Model):
    firth_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firth_name} {self.last_name}"


class Student(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FileField()
    count = models.IntegerField(default=1)
    auther = models.ForeignKey(auther, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.price}"
