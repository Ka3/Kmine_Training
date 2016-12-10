from django.shortcuts import render
from django.template import Context
from models import mas_company_profile
# Create your views here.

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView


def add_Company(request):
    '''
    athlete_list = [
                    { 'Name' : 'Usain Bolt', 'Country' : 'Jamaica' , },
                    
                    { 'Name' : 'Michael Jordan','Country' : 'US' },
                    
                    { 'Name' : 'Saina','Country' : 'India' },
                    
                    ]
    '''
    Company_list = mas_company_profile.objects.filter(State__state_name='Maharashtra')
    context = Context(
                      {'Company_list'  : Company_list}
                      )
    return render(request,'Company_info/add_Company.html',context)

