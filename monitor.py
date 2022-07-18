
import sys
from datetime import datetime
from time import sleep
import requests

interval = int(sys.argv[1])
checkstring = "login"
urlfilename = 'pages.txt'

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

def responseGetter(url):
    '''takes list of urls as parameter, makes page requests, returns logs'''
    log = ''
    try:
        response = requests.get(url)
        log = contentChecker(checkstring, response)
    except:
        log = '{0} {1}: incorrect URL format\n'.format(datetime.now(), url)

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

def processLooper(urllist):
    '''loops process, writes logs to file, breaks on empty file'''
    
    urllist = urllist
    if len(urllist) == 0:
        print('File is empty!')
    else:
        while True:
            for url in urllist:
                logs = open('logs.txt', 'a')
                log = responseGetter(url)
                print(log)

                logs.write(log)
                logs.close()

            sleep(interval)

processLooper(pageLister())