from django.db import models



class Continent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    languages = models.ManyToManyField('Language')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
