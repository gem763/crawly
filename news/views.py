from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from newscrawler import NewsCrawler
#from background_task import background

# Create your views here.

# @background(schedule=0)
# def crawl_and_update():
#     crawler = NewsCrawler(storage='bigquery')
#     crawler.collect()
#     crawler.crawl()
#     crawler.record()
#     crawler.report()

def newscrawl_and_bigquerize(request):
# def update(request):
    try:
        crawler = NewsCrawler(storage='bigquery')
        crawler.collect()
        crawler.crawl()
        crawler.record()
        crawler.report()
        # print('**************************************')
        return JsonResponse({'result':crawler.crawl_summary.to_html()})

    except ConnectionAbortedError as e:
        print('connection aborted')

    except Exception as e:
        return JsonResponse({'result':e})


def update(request):
    return render(request, 'news/update.html')


def test(request):
    return HttpResponse('ok')
