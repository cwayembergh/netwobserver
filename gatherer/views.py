from os import listdir
from os.path import isfile,join, splitext
from threading import Thread
from datetime import timedelta

from django.core.context_processors import csrf
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gatherer.log.logParser import parser
from gatherer.snmp.getter import getAllAP
from gatherer.models import RadiusEvent, DHCPEvent, WismEvent, MobileStation, AccessPoint, RogueAccessPoint, BadLog
from gatherer.tasks import snmpRAPDaemon, snmpMSDaemon, snmpAPDaemon

from django.conf import settings

TMPFILE=settings.MEDIA_ROOT
SEVERITYMEANING = ['Emergency: System is unusable','Alert: Action must be taken immediately', 'Critical: Critical conditions', 'Error: Error conditions', 'Warning: Warning conditions', 'Notice: Normal but significant condition', 'Informational: Informational messages', 'Debug: Debug-level messages']

def index(request):
	context = {}
	context['app'] = 'gatherer'
	context['logFiles'] = [ f for f in listdir(TMPFILE) if isfile(join(TMPFILE,f)) and not f.startswith(".") and not f.endswith('.badLogs')]
	context.update(csrf(request))

	if request.method == 'POST':
		if 'selectLogFile' in request.POST:
			if request.POST.get('selectLogFile','') in context["logFiles"]:
				Thread(target=parser, args=(join(TMPFILE,request.POST.get('selectLogFile','')),) ).start()
				#parser(join(TMPFILE,request.POST.get('selectLogFile','')))

	return render(request, "gatherer/index.html", context)

def wismlogs(request, page=1, perpage=100, filters={}):
	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'wism'

	context['sevMeaning'] = SEVERITYMEANING
	tmpQuery = WismEvent.objects.order_by('-date','-microsecond')
	
	p = Paginator(tmpQuery,perpage)
	try:
		context['wismEvent'] = p.page(page)
	except PageNotAnInteger:
		context['wismEvent'] = p.page(1)
	except EmptyPage:
		context['wismEvent'] = p.page(p.num_pages)

	return render(request, "gatherer/wismlogs.html", context)



def radiuslogs(request, page=1, perpage=100, filters={}):
	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'radius'

	tmpQuery = RadiusEvent.objects.order_by('-date','-microsecond')
	p = Paginator(tmpQuery,perpage)
	try:
		context['radiusEvent'] = p.page(page)
	except PageNotAnInteger:
		context['radiusEvent'] = p.page(1)
	except EmptyPage:
		context['radiusEvent'] = p.page(p.num_pages)

	return render(request, "gatherer/radiuslogs.html", context)

def dhcplogs(request, page=1, perpage=100, filters={}):
	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'dhcp'

	tmpQuery = DHCPEvent.objects.order_by('-date','-microsecond')
		
	if "filterDate" in filters:
		tmpQuery = tmpQuery.filter(date__gte=filters['filterDate'][0])
		tmpQuery = tmpQuery.filter(date__gte=filters['filterDate'][1])
	if 'filterIP' in filters:
		tmpQuery = tmpQuery.filter(ip__exact=filters['filterIP'])
	if 'filterType' in filters:
		tmpQuery = tmpQuery.filter(dhcpType__exact=filters['filterType'])
	if 'filterDevice' in filters:
		tmpQuery = tmpQuery.filter(device_macAddress=filters['filterDevice'])
	
	p = Paginator(tmpQuery,perpage)
	try:
		context['dhcpEvent'] = p.page(page)
	except PageNotAnInteger:
		context['dhcpEvent'] = p.page(1)
	except EmptyPage:
		context['dhcpEvent'] = p.page(p.num_pages)


	return render(request, "gatherer/dhcplogs.html", context)

def apsnmpRefresh(request):
	snmpAPDaemon.delay()
	return apsnmp(request)

def apsnmp(request, page=1, perpage=100):
	AUTHORIZED_ORDER = ["name", "-name", "macAddress", "-macAddress", "ip", "-ip", "ethernetLinkSpeed", "-ethernetLinkSpeed"]

	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'ap'

	tmpQuery = AccessPoint.objects.areUp()
	if "order" in request.GET and request.GET["order"] in AUTHORIZED_ORDER:
		context["order"] = request.GET["order"]
		tmpQuery = tmpQuery.order_by(request.GET["order"])
	else:
		tmpQuery = tmpQuery.order_by('name')
		context["order"] = "name"

	p = Paginator(tmpQuery,perpage)
	try:
		context['ap'] = p.page(page)
	except PageNotAnInteger:
		context['ap'] = p.page(1)
	except EmptyPage:
		context['ap'] = p.page(p.num_pages)

	return render(request, "gatherer/apsnmp.html", context)

def mssnmpRefresh(request):
	snmpMSDaemon.delay()
	return mssnmp(request)

def mssnmp(request, page=1, perpage=100):
	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'ms'

	tmpQuery = MobileStation.objects.areAssociated().order_by('macAddress')
	p = Paginator(tmpQuery,perpage)
	try:
		context['ms'] = p.page(page)
	except PageNotAnInteger:
		context['ms'] = p.page(1)
	except EmptyPage:
		context['ms'] = p.page(p.num_pages)

	return render(request, "gatherer/mssnmp.html", context)

def rapsnmpRefresh(request):
	snmpRAPDaemon.delay()
	return rapsnmp(request)

def rapsnmp(request, page=1, perpage=100):
	context = {}
	context['app'] = 'gatherer'
	context['cat'] = 'rap'

	tmpQuery = RogueAccessPoint.objects.order_by('-nbrOfClients','ssid')
	p = Paginator(tmpQuery,perpage)
	try:
		context['rap'] = p.page(page)
	except PageNotAnInteger:
		context['rap'] = p.page(1)
	except EmptyPage:
		context['rap'] = p.page(p.num_pages)

	return render(request, "gatherer/rapsnmp.html", context)

