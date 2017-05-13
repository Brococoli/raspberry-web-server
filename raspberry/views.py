from django.shortcuts import render
from .models import detail

# Create your views here.

def index(request):
	pi_list = detail.objects.all()
	context = [('')]
	return render(request, 'raspberry/index.html', context = {
			'pi_list' : pi_list,
		})