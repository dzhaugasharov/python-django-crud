from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True)
    isbn = models.CharField(max_length=150, null=True)
    print_year = models.SmallIntegerField(null=True)
    read_already = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', null=True)

    def __str__(self):
        return self.title

    def is_already_read(self):
        return self.read_already == 1;
