from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kuponi


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def kupons(request):
    kupons = Kuponi.objects.order_by('title')
    return render(request, 'main/kupons.html', {'kupons': kupons})

def profile(request):
    return render(request, 'main/profile.html')

class KuponDetailView(DetailView):
    model = Kuponi
    template_name = 'main/detail_view.html'
    context_object_name = 'kupon'

class SearchResultsView(ListView):
    model = Kuponi
    template_name = 'main/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Kuponi.objects.filter(
            Q(title=query)
        )
        return object_list
