import requests
from bs4 import BeautifulSoup

#爬取一页Pull Request的标题
def get_aria_labels(url):

    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    blocks = soup.select('div>div>a.d-block')
    
    aria_labels_local = []
    for block in blocks:
        aria_labels_local.append(block['aria-label'][15:])
    return aria_labels_local

def get_StackOverFlow_QA(url):
    cookie ='prov=548bf8e0-bbd3-2f92-f314-145d3888f3e6; __qca=P0-1324908065-1593929000356; _ga=GA1.2.172973307.1594087955; _gid=GA1.2.802337396.1603621559; usr=p=%5b160%7c%3bNewest%3b%5d%5b10%7c50%5d; acct=t=dm8MuA5EeBu1qCb%2fwDidPAPbep%2b4VNl7&s=hJKM%2fVHDOzNpecdcONtfLjQim71oTN3W; _gat=1'
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    ,'Cookie' : cookie
    }
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.select('div.result-link h3 a')
    
    questions = []
    for item in items:
        questions.append(item['title'])
    return questions
#将一个列表的内容写到txt文件中
def write2file(filename, datas):
    with open(filename, 'a') as file:
        for data in datas:
            try:
                file.write(data + '\n')
            except:
                pass

if __name__ == '__main__':
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    #爬取Pull Requests
    '''for i in range(1, 11):
        url = 'https://github.com/microsoft/vscode/pulls?page=' + str(i) + '&q=is%3Apr+is%3Aopen'
        write2file('PullRequestTitles.txt', get_aria_labels(url))'''
    #爬取issues
    '''for i in range(1, 214):
        url = 'https://github.com/microsoft/vscode/issues?page=' + str(i) + '&q=is%3Aissue+is%3Aopen'
        write2file('VSCodeIssues.txt', get_aria_labels(url))'''
    '''#爬取Stack Overflow上关于vscode extend的问题
    for i in range(1, 19):
        url = 'https://stackoverflow.com/search?page=' + str(i) + '&tab=Relevance&q=vscode%20extend'
        write2file('VSCodeQuestions.txt', get_StackOverFlow_QA(url))'''
    #爬取Stack Overflow上关于ide的问题
    for i in range(920, 4347):
        url = 'https://stackoverflow.com/search?page=' + str(i) + '&tab=Relevance&pagesize=50&q=ide'
        write2file('IDEQuestions.txt', get_StackOverFlow_QA(url))

