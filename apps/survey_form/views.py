from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_form/index.html')

def display_result(request):
    return render(request, 'survey_form/result.html')

def process_form(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['name'] = request.POST['name']
    print request.session['name']
    request.session['location'] = request.POST['location']
    print request.session['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    request.session['tries'] += 1
    return redirect('/result')
