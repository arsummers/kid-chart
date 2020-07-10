from django.shortcuts import render
from chart.models import KidInstance, Kid, Reward, Rule
# Create your views here.

def index(request):
    """
    view function for site homepage. Stuff below will be subject to change if I don't like how it looks
    """
    num_kids = Kid.objects.all().count()

    num_rules = Rule.objects.all().count()

    context = {
        'num_kids' : num_kids,
        'num_rules' : num_rules,
    }

    return render(request, 'index.html', context=context)