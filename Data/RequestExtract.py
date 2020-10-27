def include(word, sentence):
    return word in sentence or word.title() in sentence or word.upper() in sentence

def extract(filename, words):
    extract_words = []
    with open(filename, 'a') as text_file:
        for line in text_file.readlines():
            for word in words:
                if include(word, line) and not include('fix', line):
                    if line not in extract_words:
                        extract_words.append(line)
    
    with open('Extract' + filename, 'a') as extract_text_file:
        extract_text_file.writelines(extract_words)
        
if __name__ == '__main__':
    extract('PullRequestTitles.txt', ['add', 'extension', 'support', 'allow', 'update', 'remove', 'provise', 'show', 'new', 'replace', 'variable'])