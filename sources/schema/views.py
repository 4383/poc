from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from schema.models import Warehouse

# Create your views here.
@login_required(login_url='/admin/login/')
def index(request):
	warehouse = Warehouse.objects.filter(user=request.user, active=True)
	return render(request, 'schema/index.html', {'data': warehouse})
