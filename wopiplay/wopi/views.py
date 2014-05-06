from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import hashlib
import json

# Create your views here.
def info(request):
  f = urllib2.urlopen('https://app.box.com/shared/static/oif4oljhrdk9zrm0f8z8.docx') 
  stuff = f.read()
  r = {}
  r['BaseFileName'] = 'test.docx'
  r['OwnerId'] = 'lovezors'
  r['Size'] = len(stuff)
  r['SHA256'] = hashlib.sha256(stuff).hexdigest() 
  r['Version'] = '1'
  return HttpResponse(json.dumps(r), content_type="application/json")

def contents(request):
  f = urllib2.urlopen('https://app.box.com/shared/static/oif4oljhrdk9zrm0f8z8.docx') 
  stuff = f.read()
  return HttpResponse(stuff,content_type="application/octet-stream")
