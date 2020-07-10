from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Rule(models.Model):
    """
    Model representing a base class for rules. Weight field is how much you want the rule to be worth.
    """
    name = models.CharField(max_length=50, help_text='Enter rule', default=None)
    weight = models.IntegerField(default=0)
    description = models.TextField(max_length=250, help_text='Enter description of rule')

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'Rule: {self.name} \n Points worth: {self.weight} \n Description: {self.description}'
        
class Kid(models.Model):
    """
    Model representing a base class for kids. Each kid will be represented by name with a primary key. Rules can be assigned to individual kids.
    """
    name = models.CharField(max_length=20, help_text='Enter kid name', default=None)
    rules = models.ManyToManyField(Rule, help_text='Select a rule to give to this kid')
    # https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'Name: {self.name}\n Points total: {self.points} \n Rules assigned: {self.rules}'

    def get_absolute_url():
        """
        url to gain access to one Kid
        """
        return reverse('kid-detail', args=[str(self.id)])

class KidInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this kid')
    kid = models.ForeignKey('Kid', on_delete=models.SET_NULL, null=True)
    points = models.IntegerField(default=0)
    rules = models.ManyToManyField(Rule, help_text='Select a rule to give to this kid')

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return f'{self.id}, {self.kid.name}'

class Reward(models.Model):
    name = models.CharField(max_length=50, help_text='Enter reward', default=None)
    points_needed = models.IntegerField(default=0)
    description = models.TextField(max_length=250, help_text='Enter description of reward')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Name: {self.name} \n Unlocks at: {self.points_needed} points \n Description: {self.description}'

