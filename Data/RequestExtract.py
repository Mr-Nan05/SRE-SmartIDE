def include(word, sentence):
    return word in sentence or word.title() in sentence or word.upper() in sentence

def select(sentence):
    flag = True
    word_list = ['json','what','NetBeans','can\'t','best','difference','error', 'why', 'how', 'cnanot', 'visual','eclipse','java','selenium','studio','android','netbean','python']
    for word in word_list:
        flag = flag and (not include(word, sentence))
    return flag

def extract(filename, words):
    extract_words = []
    with open(filename, 'r') as text_file:
        for line in text_file.readlines():
            for word in words:
                if include(word, line) and select(line):
                    if line not in extract_words:
                        extract_words.append(line)
    
    with open('Extract' + filename[7:-4] + '2' + '.txt', 'a') as extract_text_file:
        extract_text_file.writelines(extract_words)
        
if __name__ == '__main__':
    #extract('PullRequestTitles.txt', ['add', 'extension', 'support', 'allow', 'update', 'remove', 'provise', 'show', 'new', 'replace', 'variable'])
    #extract('VSCodeIssuesTitle.txt', ['shortcut','remote','launch','sync','keyboard','markdown','link','variable','auto','integrate','replace','match','mode','ui','context','button','keybind','save','css','filter'])
    #extract('VSCodeQuestions.txt', ['extend','extension','eslint','angular','show','html','add','plugin','generic','property','document'])
    #extract('IDEQuestions.txt', ['applicable','import','plugin','find','app','html','web','connect','variable','server','show','text','library','generic','tool','add'])
    extract('ExtractIDEQuestions.txt', ['use','file','run','project','text','work','class','develop'])
    extract('ExtractVSCodeIssuesTitle.txt', ['support','open','allow','link','use','menu','code','window'])
    