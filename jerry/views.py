from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


# class IndexView(generic.ListView):
#     template_name = 'jerry/index.html'
#
#     def get_queryset(self):
#         """Return the last five published questions."""

def homePage(request):
    return render(request, 'jerry/index.html')


def aboutPage(request):
    return render(request, 'jerry/about.html')


def servicePage(request):
    return render(request, 'jerry/service.html')


def contactPage(request):
    return render(request, 'jerry/contact.html')


# class AboutView(generic.DetailView):
#     template_name = 'jerry/about.html'
#
#
# class ResultsView(generic.DetailView):
#     template_name = 'jerry/results.html'
