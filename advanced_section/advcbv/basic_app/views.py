from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Gritty. more manual way to do CBV
class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")


# # Create your views here.
#### function-based view. learned at beginning of tutorial
# def index(request):
#     return render(request, 'index.html')
