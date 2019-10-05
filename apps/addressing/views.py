import json
import requests

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from apps.core import choices


# Create your views here.
class AddressingDateView(View):
    template_name = 'addressing/addressing_date.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
    
    def post(self, request, *args, **kwargs):
        date = self.request.POST.get('date', None)
        response = requests.get(choices.addressing_date,
        headers={'date': date,
                'token': '5368651fbd70ce21d335e005dcb139faa0ada834',
                # 'nit': '555555221'
                'nit': '87654321',
            },
        )
        
        results = response.json()
        context = {
            'results': results['results'],
        }
        return render(request, self.template_name, context=context)
