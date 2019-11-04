from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from newscrawler import NewsCrawler

# Create your views here.

def update(request):
    crawler = NewsCrawler(storage='bigquery')
    collect_result = crawler.collect()
    print(collect_result[0])
    return HttpResponse('testtest')
