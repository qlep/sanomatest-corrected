#must remember to run in pyth3. Unicode is a bitch.
import sys
from datetime import datetime
from time import sleep
import requests

#interval = sys.argv[1]
now = datetime.now()
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

    for page in pagelist:
        try:
            response = requests.get(page)
            contentChecker(checkstring, response)

        except:
            print('{0} {1}: incorrect URL format\n'.format(now, page))

def contentChecker(checkstring, content):
    logs = open('logs.txt', 'a')
    content = content
    logline = '{0} {1}: Status: {2} --- Response time:{3}s'.format(now, content.url, content.status_code, content.elapsed)

    if checkstring in content.text:
        logs.write('{0} --- Checkstring: {1}\n'.format(logline, 'YES'))
    else:
        logs.write('{0} --- Checkstring: {1}\n'.format(logline, 'Nope'))
    
    logs.close()

def processLooper():

    while True:
        responseGetter(pageLister())
        #sleep(interval)

#processLooper()

responseGetter(pageLister())