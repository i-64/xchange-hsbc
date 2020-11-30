from django.shortcuts import render
from data.models import *
from django.http import HttpResponse
import os
from django.views.decorators.csrf import csrf_exempt

def home(request):

    return render(request, 'index.html', {'title': 'Home'})


def upload(request):

    title = request.POST['title']
    text_content = request.POST['text_content']

    data_item = DataItem(title = title)
    data_item.save()
    file_name = str(data_item.id) + '.txt'
    f = open('./data/static/' + file_name, 'a+')
    f.write(text_content)
    f.close()

    # error_msg = 'An error occured :/'

    return render(request, 'index.html', {'title': 'Home', 'success_msg': 'success'});

def file_list(request):

    data_items_list = os.listdir('./data/static')
    return render(request, 'file-list.html', {'data_items': data_items_list})


@csrf_exempt
def file_download(request):

    file_name = './data/static/' + request.GET['file_name']
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    print('tesjfs' + file_content)
    return HttpResponse(file_content)
