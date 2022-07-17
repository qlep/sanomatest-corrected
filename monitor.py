
import sys
from datetime import datetime
from time import sleep
import requests

#interval = sys.argv[1]
checkstring = "login"
urlfilename = 'pagess.txt'

def pageLister():
    '''reads from file list of urls, removes unnecessary newlines'''

    urllist = []
    urlfile = open(urlfilename, 'r')
    urlstrings = urlfile.readlines()
    urlfile.close()

    for url in urlstrings:
        url = url.replace('\n', '')
        urllist.append(url)

    return urllist

def responseGetter(urllist):
    '''takes list of urls as parameter, makes page requests, returns logs'''

    log = ''

    if len(urllist) != 0:
        for url in urllist:
            try:
                response = requests.get(url)
                log = contentChecker(checkstring, response)
            except:
                log = '{0} {1}: incorrect URL format\n'.format(datetime.now(), url)
    else:
        log = 'Hey, file is empty!\n'
    
    print(log)

    return log

def contentChecker(checkstring, content):
    '''takes content of requested pages and checkstring as parameters, performes checks, returns result strings'''
    content = content
    resultstring = '{0} {1}: Status: {2} --- Response time:{3}s'.format(datetime.now(), content.url, content.status_code, content.elapsed)

    if content.status_code == 200:
        if checkstring in content.text:
            return '{0} --- Checkstring: {1}\n'.format(resultstring, 'YES')
        else:
            return '{0} --- Checkstring: {1}\n'.format(resultstring, 'Nope')
    else:
        return resultstring + '\n'

def processLooper():
    '''loops process, writes logs to file, breaks on empty file'''

    run = True

    while run:
        logs = open('logs.txt', 'a')
        log = responseGetter(pageLister())

        if 'file is empty' in log:
            run = False

        logs.writelines(log)
        logs.close()

        sleep(5)

processLooper()