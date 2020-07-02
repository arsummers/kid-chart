from django.db import models

# Create your models here.


class Rule(models.Model):
    name = models.CharField(max_length=50, help_text='Enter rule', default=None)
    weight = models.IntegerField(default=0, max_length=2)
    description = models.TextField(max_length=250, help_text='Enter description of rule')

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'Rule: {self.name} \n Points worth: {self.weight} \n Description: {self.description}'

class Kid(models.Model):
    name = models.CharField(max_length=20, help_text='Enter kid name', default=None)
    points = models.IntegerField(default=0, max_length=3)
    rules = models.ManyToManyField(Rule)
    # https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/

    class Meta:
        ordering = ['-points']

    # methods
    def __str__(self):
        return f'Name: {self.name}\n Points total: {self.points} \n Rules assigned: {self.rules}'

class Reward(models.Model):
    name = models.CharField(max_length=50, help_text='Enter reward', default=None)
    points_needed = models.IntegerField(default=0, max_length=2)
    description = models.TextField(max_length=250, help_text='Enter description of reward')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Name: {self.name} \n Unlocks at: {self.points_needed} points \n Description: {self.description}'

