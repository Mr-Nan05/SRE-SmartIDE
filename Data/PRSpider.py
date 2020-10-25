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

#爬取github上vscode的issues
def get_issues():
    pass

def get_onepage_issues(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    
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
    '''for i in range(1, 11):
        url = 'https://github.com/microsoft/vscode/pulls?page=' + str(i) + '&q=is%3Apr+is%3Aopen'
        write2file('PullRequestTitles.txt', get_aria_labels(url))'''
        
    for i in range(1, 214):
        url = 'https://github.com/microsoft/vscode/issues?page=' + str(i) + '&q=is%3Aissue+is%3Aopen'
        write2file('VSCodeIssues.txt', get_aria_labels(url))
        

