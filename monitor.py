#must remember to run in pyth3. Unicode is a bitch.
import sys
from datetime import datetime
import requests

#interval = sys.argv[1]

def pageLister():
    pagelist = []
    pages = open('pages.txt', 'r')
    pagestrings = pages.readlines()
    pages.close()

    for page in pagestrings:
        page = page.replace('\n', '')
        pagelist.append(page)

    return pagelist

def responseGetter(page):
    try:
        response = requests.get(page)
    except:
        response = page
    return response

def pageChecker(checkstring):
    logs = open('logs.txt', 'a')
    now = datetime.now()

    for page in pageLister():
        try:
            content = responseGetter(page)

            if checkstring in content.text:
                logs.write('{0} {1}: Status:{2} --- Response time:{3}s --- Check:{4}\n'.format(now, content.url, content.status_code, content.elapsed, "YAS!1"))
            else:
                logs.write('{0} {1}: Status:{2} --- Response time:{3}s --- Check:{4}\n'.format(now, content.url, content.status_code, content.elapsed, "NOPE"))
        except:
            logs.write('{0} {1}: incorrect URL format\n'.format(now, page))

    logs.close()

pageChecker('login')
