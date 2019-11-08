from newscrawler import NewsCrawler
from flask import jsonify
import requests
import json

def newsupdate(request):
#     crawler = NewsCrawler(storage='bigquery')
#     crawler.collect()
#     crawler.crawl('reuters', 'investing.com', 'cnn')
#     crawler.record()
#     crawler.report(using='sendgrid')
    
    resp = requests.get('https://us-central1-global-news-crawl.cloudfunctions.net/test').text
    print(json.loads(resp))
    return 'success'


def test(request):
    data = {'a':1, 'b':2, 'c':3}
    return jsonify(**data)