import requests
from bs4 import BeautifulSoup


class Spider:
    url_header = 'https://stackoverflow.com'
    keyword_vscode_extend = 'https://stackoverflow.com/search?q=vscode+extend'
    keyword_ide = 'https://stackoverflow.com/search?q=ide'
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    #获取每一页问答链接
    def getQurls(self, url):
        res = requests.get(url, headers = self.headers)
        print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        questions = soup.select('div>h3>a')
        
        return [self.url_header + question['href'] for question in questions]
    
if __name__ == '__main__':
    spider = Spider()
    print(spider.getQurls(spider.keyword_ide))
