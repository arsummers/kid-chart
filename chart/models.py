from django.db import models

# Create your models here.


class Rule(models.Model):
    name = models.CharField(max_length=50, help_text='Enter rule, default='')
    weight = models.IntegerField(default=0, max_length=2)
    description = models.TextField(max_length=250, help_text='Enter description of rule')

    class Meta:
        pass

    # methods
    def __str__(self):
        pass

class Kid(models.Model):
    name = models.CharField(max_length=20, help_text='Enter kid name', default='')
    points = models.IntegerField(default=0, max_length=3)
    rules = models.ManyToManyField(Rule)
    # https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/

    class Meta:
        ordering = ['-points']

    # methods
    def __str__(self):
        pass