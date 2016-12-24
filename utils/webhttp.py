
import re
import warnings
import json
import urllib.request
from urllib.parse import urlparse
import base64
from http.client import HTTPSConnection
from functools import partial


def get(url, username, password):
    """

    """

    # create a request by url
    request = urllib.request.Request(url)

    # add a header with authentication
    auth_encode = base64.b64encode(bytes('{}:{}'.format(username, password), 'ascii'))
    request.add_header('Authorization', 'Basic {}'.format(auth_encode.decode('utf-8')))

    # get response and it`s content
    response = urllib.request.urlopen(request)
    content = response.read()
    content = content.decode('utf-8')

    # return data in json
    content = json.loads(content)
    return content


def get2(url, username, password, user_agent=''):
    """

    """

    urlparse_result = urlparse(url)

    connection = HTTPSConnection(urlparse_result.netloc)

    auth_encode = base64.b64encode(bytes('{}:{}'.format(username, password), 'ascii'))

    headers = {
        'User-Agent': user_agent,
        'Authorization': 'Basic {}'.format(auth_encode.decode('utf-8')),
    }

    try:
        connection.request('GET', urlparse_result.path, headers=headers)
        response = connection.getresponse()
        content = response.read()
    except Exception:
        raise
    else:
        content = content.decode('utf-8')
        return json.loads(content)
    finally:
        response.close()
        connection.close()


def get3(url, username, password):
    """ """

    warnings.warn('For some reason does not working authorization')

    # add password
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    #
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)

    # get response and return content as json
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return json.loads(content)


def get_info_github_following_of_user():

    username = 'setivolkylany'
    password = 'totheend7525'

    get_ = partial(get, username=username, password=password)

    github_api_user_url = 'https://api.github.com/user'

    response_user = get_(github_api_user_url)
    following_url = response_user['following_url']
    following_url = re.sub(r'{(.*)}', '', following_url)
    response_following = get_(following_url)

    response_following = response_following[:1]
    for following in response_following:
        response_following_user = get_(following['url'])
        response_following_user['avatar_url'],
        response_following_user['login'],
        response_following_user['location'],
        response_following_user['following'],
        response_following_user['blog'],
        response_following_user['bio'],
        response_following_user['public_repos'],
        response_following_user['url'],
        response_following_user['followers'],
        response_following_user['created_at'],

        repos_url = response_following_user['repos_url']

        response_other_user_repos = get_(repos_url)

        for repo in response_other_user_repos:
            print(
                repo['name'],
                repo['created_at'],
                repo['language'],
                repo['description'],
                repo['forks'],
                repo['fork'],
                repo['forks_count'],
                repo['private'],
                repo['url'],
            )


# get_info_github_following_of_user()
# print(get('https://api.anaconda.org', None, None))
