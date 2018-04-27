from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import  Mylife
# Create your views here.
def index(request):
	mylife = Mylife.objects.all()
	return render_to_response('cms/chiao.html', locals())