#must remember to run in pyth3. Unicode is a bitch.
import sys
from datetime import datetime
from time import sleep
import requests

#interval = sys.argv[1]
checkstring = "login"

def pageLister():
    pagelist = []
    pages = open('pages.txt', 'r')
    pagestrings = pages.readlines()
    pages.close()

    for page in pagestrings:
        page = page.replace('\n', '')
        pagelist.append(page)

    return pagelist

def responseGetter(pagelist):
    logs = open('logs.txt', 'a')

    for page in pagelist:
        try:
            response = requests.get(page)
            logs.write(contentChecker(checkstring, response))
        except:
            logs.write('{0} {1}: incorrect URL format\n'.format(datetime.now(), page))
    
    logs.close()

def contentChecker(checkstring, content):
    content = content
    logline = '{0} {1}: Status: {2} --- Response time:{3}s'.format(datetime.now(), content.url, content.status_code, content.elapsed)

    if content.status_code == 200:
        if checkstring in content.text:
            return '{0} --- Checkstring: {1}\n'.format(logline, 'YES')
        else:
            return '{0} --- Checkstring: {1}\n'.format(logline, 'Nope')
    else:
        return logline + '\n'
    
    

def processLooper():

    while True:
        responseGetter(pageLister())
        sleep(5)

processLooper()