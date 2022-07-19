
import sys
from datetime import datetime
from time import sleep
import requests

checkstring = 'login'

def pageLister():
    '''reads from file list of urls, removes unnecessary newlines'''

    urllist = []
    urlstrings = []

    try:
        urlfilename = sys.argv[1]
        urlfile = open(urlfilename, 'r')
        urlstrings = urlfile.readlines()
        urlfile.close()

        for url in urlstrings:
            url = url.replace('\n', '')
            urllist.append(url)
        
        if len(urllist) != 0:
            return urllist
        else:
            print('File is empty!')
            return None
    except IndexError:
        print('No file name given!')
        return None

def responseGetter(url):
    '''takes list of urls as parameter, makes page requests, returns logs'''
    
    resultstring = ''

    try:
        response = requests.get(url)
        resultstring = contentChecker(checkstring, response)
    except requests.exceptions.ConnectionError:
        resultstring = '{0} {1}: page does not exsist\n'.format(datetime.now(), url)
    except:
        resultstring = '{0} {1}: incorrect URL format\n'.format(datetime.now(), url)

    return resultstring

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
    
    if urllist:
        while True:
            for url in urllist:
                logs = open('logs.txt', 'a')
                log = responseGetter(url)
                print(log)
                logs.write(log)
                logs.close()

            try:
                sleep(int(sys.argv[2]))
            except IndexError:
                sleep(5)

processLooper(pageLister())