# -*- coding: utf-8 -*-
# !/usr/bin/python3

"""

Translate english word from command-line to russian:
    $ python translate_en_ru.py monday
    понедельник
    $ python translate_en_ru.py earth
    Земля

"""

import sys
import re
import gzip
import io
from urllib import request
from urllib import parse
from urllib.error import HTTPError
import argparse


# parser command-line
parser = argparse.ArgumentParser(description='Get translation english/russian word by Google Translator')
parser.add_argument('word', type=str, nargs='+', help='english or russian word')
parser.add_argument('-r', action='store_true', help='translate from russian to english')
args = parser.parse_args()

# get word for translation
word = args.word[0]
word = parse.quote(word)

# support only for translation Eng->Rus or inverse
if args.r is True:
    raise NotImplementedError('Support for translation from russian to english in not completed for now')
    LANG_FROM = 'ru'
    LANG_TO = 'en'
else:
    LANG_FROM = 'en'
    LANG_TO = 'ru'

# URL to googleapis
url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format(
    LANG_FROM, LANG_TO, word
)

# create a request
request_ = request.Request(url)
request_.headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Slavic browser',
}

# try made request, if return response wuth code 403
# most likely neew try again because it is nonofficial way to Google API
try:
    response = request.urlopen(request_, timeout=5000)
except HTTPError as err:
    if err.code == 403:
        print('Same problems. Try again.')
        sys.exit()

# if something wrong
if response.status != 200:
    print('Unexpected response "{}" with status {}'.format(response.reason, response.status))
    sys.exit()

# data returned if encoding supported for gzip,
# so use additional methods for decode data
gzip_content = response.read()
buffer_ = io.BytesIO(gzip_content)
content = gzip.GzipFile(fileobj=buffer_).read()
content = content.decode('utf-8')

# get only translation from example
# [[["понедельник","monday",,,1]],,"en"]
matches = re.match(r'\[{3}"(\w+)","(\w+)"', content, re.UNICODE)
print(matches.group(1))
