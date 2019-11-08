from newscrawler import NewsCrawler
from flask import Flask


app = Flask(__name__)


@app.route('/newsupdate')
def newsupdate():
    crawler = NewsCrawler(storage='bigquery')
    crawler.collect()
    crawler.crawl()
    crawler.record()
    crawler.report(using='sendgrid')
    return 'updated'


@app.route('/test')
def test():
    return 'hello'

    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)