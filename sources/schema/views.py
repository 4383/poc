from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from schema.models import Warehouse
from schema.models import Schema
import schema.converters as converters


def ordonate_sections(a, b):
	sections = {}
	for el in a.all():
		if el.name not in sections:
			sections.update({el.name: [el]})
			continue
		sections[el.name].append(el)
	for el in b.all():
		if el.name not in sections:
			sections.update({el.name: [el]})
			continue
		sections[el.name].append(el)
	return sections


def get_schema(id):
	schema = Schema.objects.filter(id=id)[0]
	data = {'schema': schema, 'zones': []}
	for zone in schema.zones.all():
		data['zones'].append({
			'zone': zone,
			'sections': ordonate_sections(
				zone.global_sections,
				zone.global_user
			)
		})
	return data


@login_required(login_url='/admin/login/')
def index(request):
	warehouse = Warehouse.objects.filter(user=request.user, active=True)
	return render(request, 'schema/index.html', {'data': warehouse})


@login_required(login_url='/admin/login/')
def edit(request, id):
	return render(request, 'schema/edit.html', get_schema(id))


@login_required(login_url='/admin/login/')
def download(request, id):
	data = get_schema(id)
	json = str(converters.to_json(data)).replace("'",'"')
	yaml = converters.to_yaml(data)
	return render(request, 'schema/download.html', {'json': json, 'yaml': yaml})
