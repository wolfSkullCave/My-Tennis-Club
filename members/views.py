from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
    mydata2 = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()

    # order by
    orderBy_name = Member.objects.all().order_by('firstname').values()
    orderBy_nameReverse = Member.objects.all().order_by('-firstname').values()
    multi_orderBy = Member.objects.all().order_by('lastname','-id').values()

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
        'mymembers2': mydata2,
        'names': orderBy_name,
        'namesReverse': orderBy_nameReverse,
        'multiOrderBy': multi_orderBy,
    }
    return HttpResponse(template.render(context, request))
