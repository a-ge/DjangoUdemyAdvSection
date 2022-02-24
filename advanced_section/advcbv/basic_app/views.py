from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, DeleteView,
                                UpdateView)
from . import models

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolListView(ListView): # Gives list of every record in School model
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School
    # school_list in school_list.html
    # ListView object we are inheriting from creates context dict and returns for you
    # takes ".School", lowercases, adds _list

class SchoolDetailView(DetailView): # Show details for a specific entry in School db, includes students of that school
    # DV returns: takes ".School" from models, lowercases
    context_object_name = 'school_details'
    model = models.School
    #LV, DV are related to TemplateView,
    # in the fact that they can take the same class object attribute template_name
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    # once deleted, go back to list and show all schools- no longer there
    # reverse_lazy: dont want evaluated completely to run py file. wait until called as success
    success_url = reverse_lazy("basic_app:list")





# class In/
# # Gritty. more manual way to do CBV
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")


# # Create your views here.
#### function-based view. learned at beginning of tutorial
# def index(request):
#     return render(request, 'index.html')
