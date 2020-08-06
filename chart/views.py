from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

# I will need to pass all of the rules assigned to this view and template as well, so the user can easily see what they've assigned to that kid
class KidDetailView(generic.DetailView):
    model = Kid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['rules_list'] = Rule.objects.all()

        return context


class KidCreate(CreateView):
    model = Kid
    fields = '__all__'

class KidUpdate(UpdateView):
    model = Kid
    fields = '__all__'

class KidDelete(DeleteView):
    model = Kid
    success_url = reverse_lazy('kids')

class RuleListView(generic.ListView):
    model = Rule

class RuleDetailView(generic.DetailView):
    model = Rule

class RuleCreate(CreateView):
    model = Rule
    fields = '__all__'

class RuleUpdate(UpdateView):
    model = Rule
    fields = '__all__'

class RuleDelete(DeleteView):
    model = Rule
    success_url = reverse_lazy('rules')