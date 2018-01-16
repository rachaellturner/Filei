from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Retrotransposons

import random


# Create your views here.

# template based views #
class ExampleFunctions(TemplateView):
    template_name = 'example_functions.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(ExampleFunctions, self).get_context_data(*args, **kwargs)
        
        positive_nums = []

        for x in range(0,10):
            num = random.randint(0,100)
            if num%2 == 0:
                positive_nums.append(num)
        
        context = {
            "nums": positive_nums
        }
        return context
