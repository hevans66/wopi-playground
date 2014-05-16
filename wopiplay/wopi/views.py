from django.shortcuts import render
from django.http import HttpResponse
import urlparse
import urllib2
import hashlib
import json
import base64
import urllib

def fileid_to_url(fileid):
  if fileid == 'test2.docx':
    return 'https://app.box.com/shared/static/oif4oljhrdk9zrm0f8z8.docx'
  elif fileid == 'test4.xlsx':
    return 'https://app.box.com/shared/static/dcrv1hljglo53fy6nvaj.xlsx'
 
# Create your views here.
def info(request,fileid=None):
  f = urllib2.urlopen(fileid_to_url(fileid)) 
  stuff = f.read()
  r = {}
  r['BaseFileName'] = fileid
  r['OwnerId'] = 'lovezors'
  r['Size'] = len(stuff)
  dig = hashlib.sha256(stuff).digest()
  r['SHA256'] = base64.b64encode(dig).decode()
  r['Version'] = '1'
  return HttpResponse(json.dumps(r), content_type="application/json")

def contents(request,fileid=None):
  f = urllib2.urlopen(fileid_to_url(fileid)) 
  #f = urllib2.urlopen('https://app.box.com/shared/static/z5uvek60a8r0q1q2wpca.xlsx') 
  stuff = f.read()
  return HttpResponse(stuff,content_type="application/octet-stream")

def get_wopi_url(request,fileid=None):
  r = {}
  wopi_url = 'http://wopi-playground.herokuapp.com/stuff/wopi/files/{}'.format(fileid)
  encoded_params= urllib.urlencode( [('WOPISrc',wopi_url),('access_token','12345')] )
  urls = []
  if fileid.endswith('xlsx'):
    urls.append('http://hlabows01.contoso.com/x/_layouts/xlviewerinternal.aspx?'+encoded_params) 
  r['urls'] = urls
  return render(request,'geturl.html',r)
