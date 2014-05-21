# Create your views here.
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response,redirect
import sae.kvdb

def index(request):
	kv = sae.kvdb.KVClient()
	kv_info = kv.get_info()
	path = request.path
	prefix = request.GET.get('prefix','')
	limit = request.GET.get('limit',20)
	prev_marker = request.GET.get('prev_marker','')
	marker = str(request.GET.get('marker',''))
	if not len(prev_marker):
		prev_marker = None
	results = list(kv.get_by_prefix(str(prefix),int(limit),marker))
	if results and len(results):
		marker = results[-1][0]
	#results = [('test','test'),('test2','test2')]
	if prev_marker is None:
		prev_marker = ''
	return render_to_response('kvpanel/index.html', {'kv_info':kv_info,'results':results,'prefix':prefix,'pre_marker':prev_marker,'marker':marker,'path':path,'limit':limit}, context_instance=RequestContext(request))

def set(request):
	key = request.POST.get('key')
	val = request.POST.get('val')
	if key and val:
		kv = sae.kvdb.KVClient()
		kv.set(str(key),str(val))
	return HttpResponse('',mimetype="text/plain")

def delete(request):
	key = request.POST.get('key')
	if key:
		kv = sae.kvdb.KVClient()
		kv.delete(str(key))
	return HttpResponse('',mimetype="text/plain")

def get(request):
	key = request.GET.get('key')
	ans = ''
	if key:
		kv = sae.kvdb.KVClient()
		ans = str(kv.get(str(key)))
	return HttpResponse(ans,mimetype="text/plain")