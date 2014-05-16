from django.shortcuts import render
from django.http import HttpResponse
import urlparse
import urllib2
import hashlib
import json
import base64
import urllib

from django.views.decorators.csrf import csrf_exempt

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
  r['SupportsUpdate'] = True
  r['UserCanWrite'] = True
  r['SupportsLocks'] = True
  return HttpResponse(json.dumps(r), content_type="application/json")

@csrf_exempt
def contents(request,fileid=None):
  print 'request to contents'
  if request.method == 'GET':
    f = urllib2.urlopen(fileid_to_url(fileid)) 
    stuff = f.read()
    return HttpResponse(stuff,content_type="application/octet-stream")
  elif request.method == 'POST':
    #put the file back on box
    print "Got hit to POST"
    box_url = 'https://upload.box.com/api/2.0/files/content'
    files = {'filename':(fileid+'1',request.body)}
    data = { 'folder_id':'1919107407' }
    headers = {'Authorization':"Bearer azNbv38wYbxpbl3luS9Ucuwycd0AdFRC"}
    resp = requests.post(url, params=data, files=files, headers=headers)
    print resp

def get_wopi_url(request,fileid=None):
  r = {}
  wopi_url = 'http://wopi-playground.herokuapp.com/stuff/wopi/files/{}'.format(fileid)
  encoded_params= urllib.urlencode( [('WOPISrc',wopi_url),('access_token','12345')] )
  urls = []
  if fileid.endswith('xlsx'):
    urls.append('http://hlabows01.contoso.com/x/_layouts/xlviewerinternal.aspx?'+encoded_params) 
    urls.append('http://hlabows01.contoso.com/x/_layouts/xlviewerinternal.aspx?edit=1'+encoded_params) 
  r['get_info_url'] = wopi_url
  r['get_file_url'] = wopi_url+'/contents'
  r['urls'] = urls
  return render(request,'geturl.html',r)
