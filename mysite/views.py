from django.shortcuts import render
from loja.models import Pet

def home(request):

 project = Pet.objects.all()
 context = {
 'rows': project
 }
 return render(request, 'index.html', context)
