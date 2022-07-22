# Attempt to comply with PEP8
# Standard modules, no need to include in requirements.
import sys
from datetime import datetime
from time import sleep

# Third party modules installed with pip.
import requests

checkstring = 'login'

def page_lister():
    '''Reads from file list of urls, removes unnecessary newlines,
    returns list of urls.
    '''
    url_list = []
    url_strings = []

    try:
        url_filename = sys.argv[1]
        url_file = open(url_filename, 'r')
        url_strings = url_file.readlines()
        url_file.close()

        for url in url_strings:
            url = url.replace('\n', '')
            url_list.append(url)
        
        if len(url_list) != 0:
            return url_list
        else:
            print('File is empty!')
            return None
    except IndexError:
        print('No file name given!')
        return None

def response_getter(url):
    '''Takes list of urls, makes page requests,
    returns log strings.
    '''
    resultstring = ''

    try:
        response = requests.get(url)
        resultstring = content_checker(checkstring, response)
    except requests.exceptions.ConnectionError:
        resultstring = '{0} {1}: page does not exsist\n'.format(
            datetime.now(), url)
    except:
        resultstring = '{0} {1}: incorrect URL format\n'.format(
            datetime.now(), url)

    return resultstring

def content_checker(checkstring, content):
    '''Takes content of requested pages and checkstring as parameters,
    performes checks, returns result strings.
    '''
    content = content
    resultstring = '{0} {1}: Status: {2} --- Response time:{3}s'.format(
        datetime.now(), content.url, 
        content.status_code, content.elapsed)

    if content.status_code == 200:
        if checkstring in content.text:
            return '{0} --- Checkstring: {1}\n'.format(resultstring, 'YES')
        else:
            return '{0} --- Checkstring: {1}\n'.format(resultstring, 'Nope')
    else:
        return resultstring + '\n'

def process_looper(url_list):
    '''Loops process, writes logs to file, breaks on empty file.'''
    url_list = url_list
    
    if url_list:
        while True:
            for url in url_list:
                logs = open('logs.txt', 'a')
                log = response_getter(url)
                print(log)
                logs.write(log)
                logs.close()

            try:
                sleep(int(sys.argv[2]))
            except IndexError:
                sleep(5)

process_looper(page_lister())