#must remember to run in pyth3. Unicode is a bitch.
import sys
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

    for page in pageLister():
        content = responseGetter(page)
        try:
            if checkstring in content.text:
                logs.writelines('{0}: Status:{1} --- Response time:{2}s --- Check:{3}\n'.format(content.url, content.status_code, content.elapsed, "YAS!1"))
            else:
                logs.writelines('{0}: Status:{1} --- Response time:{2}s --- Check:{3}\n'.format(content.url, content.status_code, content.elapsed, "NOPE"))
        except:
            logs.writelines('incorrect URL format: "{}"\n'.format(page))

    logs.close()

pageChecker('login')
