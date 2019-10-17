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
                    'nit': '87654321',
                },
        )
        results = response.json()
        
        context = {
            'results': results['results'],
        }
        return render(request, self.template_name, context=context)

class AddressingProgramView(View):
    template_name = 'addressing/addressing_program.html'

    def get(self, request, *args, **kwargs):
        print('REQUEST OF PROGRAMMING>>>>', request)
        return render(request, self.template_name, context={})
    
    def post(self, request, *args, **kwargs):
        print('ID User', self.request.POST.get('ID', None))
        ID = self.request.POST.get('ID', None)
        numAddressing = self.request.POST.get('numAddressing', None)
        TipoTec = self.request.POST.get('TipoTec', None)
        ConTec = self.request.POST.get('ConTec', None)
        NoIdPaciente = self.request.POST.get('NoIdPaciente', None)
        NoEntrega = self.request.POST.get('NoEntrega', None)
        NoSubEntrega = self.request.POST.get('NoSubEntrega', None)
        TipoIDProv = self.request.POST.get('TipoIDProv', None)
        NoIDProv = self.request.POST.get('NoIDProv', None)
        CodMunEnt = self.request.POST.get('CodMunEnt', None)
        FecMaxEnt = self.request.POST.get('FecMaxEnt', None)
        CantTotAEntregar = self.request.POST.get('CantTotAEntregar', None)
        DirPaciente = self.request.POST.get('DirPaciente', None)
        CodTecAEntregar = self.request.POST.get('CodTecAEntregar', None)
        response = requests.put(
            choices.programming,
            data = {
                "id": ID,
                "FecMaxEnt": FecMaxEnt,
                "TipoIDSedeProv": TipoIDProv,
                "NoIDSedeProv": NoIDProv,
                "CodSedeProv": CodMunEnt,
                "CodTecAEntregar": CodTecAEntregar,
                "CantTotAEntregar": CantTotAEntregar,
            },
            headers = {
                'token': '5368651fbd70ce21d335e005dcb139faa0ada834',
                'nit': '87654321',
            },
        )
        print('\n\n\n')
        print('!!!!!!!!!!!!::::::::::::::::', response)
        results = response.json()
        context = {
            'results': results,
            'numAddressing': numAddressing,
            'TipoTec': TipoTec,
            'ConTec': ConTec,    
            'NoIdPaciente': NoIdPaciente,
            'NoEntrega': NoEntrega,
            'NoSubEntrega': NoSubEntrega,
            'TipoIDProv': TipoIDProv,
            'NoIDProv': NoIDProv,
            'CodMunEnt': CodMunEnt,
            'FecMaxEnt': FecMaxEnt,
            'CantTotAEntregar': CantTotAEntregar,
            'DirPaciente': DirPaciente,
            'CodTecAEntregar': CodTecAEntregar
        }
        return render(request, self.template_name, context=context)
