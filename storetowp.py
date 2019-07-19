from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client

import requests
import os.path
from bs4 import BeautifulSoup
import json
import random
from datetime import datetime
import colorer,logging
from PIL import Image
from io import BytesIO

toScrap = 'http://wp.test/'
username = 'admin'
password = 'redefine123'

# connect withe admin user of wordpress site
client = Client(toScrap+'/xmlrpc.php', username, password)
data = []
offset = 0
increment = 100
while True:
        wp_posts = client.call(posts.GetPosts(
            {'post_type': 'q_author','number': increment, 'offset': offset}))
        if len(wp_posts) == 0:
                break  # no more posts returned
        for post in wp_posts:
                data.append({'id':post.id,'title':post.title})
        offset = offset + increment
# q_authors = ','.join(data)
print(data)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'

def validate(html):
    # check if post title exist
    hasPageTitle = html.find('h2', attrs={'class', 'pageTitle'})
    if hasPageTitle:
        # check if post with title already exists
        if hasPageTitle.text in existingPosts:
            print (bcolors.OKBLUE+"Already Exist"+bcolors.ENDC)
            return False
        return True
    return False


def printMsg(msg):
    print ""
    print bcolors.OKGREEN + \
        "/---------------------------------------------------------------------------/"
    print bcolors.WARNING+"                   "+msg + bcolors.OKGREEN
    print "/---------------------------------------------------------------------------/"+bcolors.ENDC
    print ""


def getQuotesFromJson():
    print(bcolors.WARNING+"*** Getting links list from file ***"+bcolors.ENDC)
    filePath = './main-quotes.json'
    url_list = ''
    print ("getting list from file")
    with open(filePath, 'r') as filehandle:
            url_list = json.load(filehandle)
    return url_list
def createQuote(url):
    print( bcolors.OKBLUE + " creating post " + bcolors.ENDC)
    postDate = datetime.now()
    post = WordPressPost()
    post.title = 'Quote #'+str(random.randint(100, 10000))
    post.post_type = 'quotes'
    post.content = url['quote']
    post.post_status = "publish"
    post.author = "admin"
    post.date = postDate
    # post.thumbnail = postImg
    post.terms_names = {
        'quotes_category': url['categories'],
    }
    post.custom_fields = []
    post.custom_fields.append({
        'key': 'q_author',
        'value':url['author']
    })
    addpost = client.call(posts.NewPost(post))
    if(addpost):
        print (bcolors.OKGREEN + "post created " + bcolors.ENDC)
    exit()

def find_a(json_object, name):
        return [obj for obj in json_object if obj['author']==name]

def main():
    printMsg('Starting Scrapping')
    q_list = getQuotesFromJson()
    for url in q_list:
        res = find_a(data, url['author'])
        print(res)
        # createQuote(url)
        exit()

if __name__ == '__main__':
    main()

