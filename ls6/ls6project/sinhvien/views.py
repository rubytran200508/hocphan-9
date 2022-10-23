from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Name
# Create your views here.
# def index(request):
#     response= HttpResponse()
#     response.write("<h1>Hello world- Welcome </h1>")
#     response.write("This is a student app abcd")
#     return response
def index(request):
    Myname=Name.objects.all().values()
    template = loader.get_template('sinhvien/base.html')
    context = {
        'Myname': Myname
    }
    return HttpResponse(template.render(context, request))
def add(request):
    template= loader.get_template('add.html')
    return HttpResponse(template.render({}, request))
def addrecord(request):
    y=request.POST('Ten_hs')
    sinhvien=Name(Ten_hs=y)
def delete (request, id):
    sinhvien=Name.objects.get(id=id)
    sinhvien=delete()
    return HttpResponseRedirect(reverse('index'))

