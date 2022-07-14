from http.client import responses
import sys
import requests

#pagurl = sys.argv[1]
#checkstring = sys.argv[2]

def listPages():
    pagelist = []
    pages = open('pages.txt', 'r')
    pagestrings = pages.readlines()
    pages.close()

    for page in pagestrings:
        page = page.replace('\n', '')
        pagelist.append(page)

    return pagelist

def getPageResponse(page):
    try:
        response = requests.get(page)
    except:
        response = page
    
    return response

def pageChecker(checkstring):
    for page in listPages():
        content = getPageResponse(page)
        try:
            if checkstring in content.text:
                print(content.url + '---' + str(content.status_code) + '---' + str(content.elapsed) + 's' + '---' + 'YASS!!1')
            else:
                print(content.url + '---' + str(content.status_code) + '---' + str(content.elapsed) + '---' + 'YATSI!!1')
        except:
            print('incorrect URF format: ' + page)

pageChecker('login')