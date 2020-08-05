from django.db import models

# Create your models here.
class Rule(models.Model):
    """
    Model representing a base class for rules. Weight field is how much you want the rule to be worth. The same rule can be applied to multiple kids, and a single kid can be assigned multiple rules.
    """
    name = models.CharField(max_length=50, help_text='Enter rule', default=None)
    weight = models.IntegerField(default=0)
    description = models.TextField(max_length=250, help_text='Enter description of rule')

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'Rule: {self.name} \n Points worth: {self.weight} \n Description: {self.description}'

    def get_absolute_url(self):
        """
        url to gain access to one Rule
        """

        return reverse('rule-detail', args=[str(self.id)])


class RuleInstance(models.Model):
    """
    Model representing all the rules
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this rule')
    rules = models.ForeignKey(Rule, on_delete=models.SET_NULL, null=True)