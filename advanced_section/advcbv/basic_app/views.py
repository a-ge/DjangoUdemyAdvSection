from django.shortcuts import render
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    # template_name: class object attribute
    template_name = 'index.html'

    # use context dict with TemplateView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

# # Gritty. more manual way to do CBV
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")


# # Create your views here.
#### function-based view. learned at beginning of tutorial
# def index(request):
#     return render(request, 'index.html')
