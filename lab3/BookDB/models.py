from django.db import models
#111111111111
#222222222222
#333333333333
class Book(models.Model):
    ISBN = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    AuthorID = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
class Book0(models.Model):
    #ISBN = models.CharField(max_length=100)
    #Title = models.CharField(max_length=100)
    #AuthorID = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
class Author(models.Model):
    AuthorID = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
