import os
import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'xmlparser/home.html')


def record(request):
    return render(request, 'xmlparser/recorded.html')


def output(request):
    return render(request, 'xmlparser/record.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'xmlparser/record.html', {
        'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'xmlparser/record.html')


file = 'box2.xml'
file_path = os.path.abspath(os.path.join('data', file))
dom = ET.parse(file_path)
details = dom.findall('issue')
CONFIG_PROPERTIES = {}
c = 0
f = open('xmlparser/record.html', 'w')
for d in details:
    c = c+1
    name = d.find('name').text
    severity = d.find('severity').text
    confidence = d.find('confidence').text
    host = d.find('host').text
    request = d.find('path').text
    CONFIG_PROPERTIES = c, name, severity, confidence, host+request
    f.write(' {}, {}, {}, {}, {} '.format(
        c, name, severity, confidence, host+request
    ))
    f.close
