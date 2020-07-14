from django.shortcuts import render
from chart.models import KidInstance, Kids, Reward, Rules
# Create your views here.

def index(request):
    """
    view function for site homepage. Stuff below will be subject to change if I don't like how it looks
    """
    kids_list = Kids.objects.all()

    rules_list = Rules.objects.all()

    context = {
        'kids_list' : kids_list,
        'rules_list' : rules_list,
    }

    return render(request, 'index.html', context=context)