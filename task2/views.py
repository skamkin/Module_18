from django.shortcuts import render
from django.views.generic import TemplateView



def task2_func_view(request):
    return render(request, 'second_task/func_template.html')


class ViewByClass(TemplateView):
    template_name = 'second_task/class_template.html'


# Create your views here.
