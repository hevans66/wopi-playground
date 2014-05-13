from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import hashlib
import json
import base64

# Create your views here.
def info(request):
  f = urllib2.urlopen('https://app.box.com/shared/static/oif4oljhrdk9zrm0f8z8.docx') 
  #f = urllib2.urlopen('https://app.box.com/shared/static/z5uvek60a8r0q1q2wpca.xlsx') 
  stuff = f.read()
  r = {}
  r['BaseFileName'] = 'test.docx'
  r['OwnerId'] = 'lovezors'
  r['Size'] = len(stuff)
  dig = hashlib.sha256(stuff).digest()
  r['SHA256'] = base64.b64encode(dig).decode()
  r['Version'] = '1'
  return HttpResponse(json.dumps(r), content_type="application/json")

def contents(request):
  f = urllib2.urlopen('https://app.box.com/shared/static/oif4oljhrdk9zrm0f8z8.docx') 
  #f = urllib2.urlopen('https://app.box.com/shared/static/z5uvek60a8r0q1q2wpca.xlsx') 
  stuff = f.read()
  return HttpResponse(stuff,content_type="application/octet-stream")

