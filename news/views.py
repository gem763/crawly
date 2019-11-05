from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from newscrawler import NewsCrawler
from background_task import background

# Create your views here.

@background(schedule=0)
def crawl_and_update():
    crawler = NewsCrawler(storage='bigquery')
    crawler.collect()
    crawler.crawl()
    #print(crawler.crawl_summary)
    crawler.record()
    crawler.report()


def update(request):
    try:
        crawl_and_update()
        return HttpResponse('requested')
    except Exception as e:
        return HttpResponse(e)


def test(request):
    return HttpResponse('ok')
