from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from chart.models import KidInstance, Kid, Reward, Rule
# Create your views here.

@login_required
def index(request):
    """
    view function for site homepage. Stuff below will be subject to change if I don't like how it looks
    """
    kids_list = Kid.objects.all()

    rules_list = Rule.objects.all()

    context = {
        'kids_list' : kids_list,
        'rules_list' : rules_list,
    }

    return render(request, 'index.html', context=context)

class KidListView(generic.ListView):
    model = Kid

class KidDetailView(generic.DetailView):
    model = Kid

class RuleListView(generic.ListView):
    model = Rule

class RuleDetailView(generic.DetailView):
    model = Rule