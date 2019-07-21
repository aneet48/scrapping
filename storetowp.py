from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client

import json
import random
from datetime import datetime
import colorer,logging
import urllib.request


# toScrap = 'http://wp.test/'
# username = 'admin'
# password = 'redefine123'

toScrap = 'http://localhost/wordpress/'
username = 'admin'
password = 'admin'
# connect withe admin user of wordpress site
client = Client(toScrap+'/xmlrpc.php', username, password)
data = []
offset = 0
increment = 100
while True:
        wp_posts = client.call(posts.GetPosts(
            {'post_type': 'quotes','number': increment, 'offset': offset}))
        if len(wp_posts) == 0:
                break  # no more posts returned
        for post in wp_posts:
                data.append(post.title)
        offset = offset + increment
q_authors = ','.join(data)

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
    print (bcolors.OKGREEN + \
        "/---------------------------------------------------------------------------/")
    print( bcolors.WARNING+"                   "+msg + bcolors.OKGREEN)
    print( "/---------------------------------------------------------------------------/"+bcolors.ENDC)


def getQuotesFromJson():
    # print(bcolors.WARNING+"*** Getting links list from file ***"+bcolors.ENDC)
    filePath = './main-quotes-id.json'
    url_list = ''
    # print ("getting list from file")
    with open(filePath, 'r') as filehandle:
            url_list = json.load(filehandle)
    return url_list
def createQuote(url):
    tags="random"
    name = str(random.randint(100, 10000))+'.png'
    attachment_id=''
    idata = {
            'name': name,
            'type': 'image/png',  # mimetype
    }
    if(url['categories']):
        categories = ','.join(url['categories'])
    res =urllib.request.urlretrieve('https://source.unsplash.com/800x400/?'+categories, "./img-quote/"+name)
    if(res):
        with open('./img-quote/'+name, 'rb') as img:
            idata['bits'] = xmlrpc_client.Binary(img.read())
        response = client.call(media.UploadFile(idata))
        attachment_id=response['attachment_id']

    print( bcolors.OKBLUE + " creating post " + bcolors.ENDC)
    postDate = datetime.now()
    post = WordPressPost()
    post.title = url['id']
    post.post_type = 'quotes'
    post.content = url['quote']
    post.post_status = "publish"
    post.author = "admin"
    post.date = postDate
    post.thumbnail = attachment_id
    post.terms_names = {
        'quotes_category': url['categories'],
    }
    post.custom_fields = []
    post.custom_fields.append({
        'key': 'q_author',
        'value':url['author-id']
    })
    addpost = client.call(posts.NewPost(post))
    if(addpost):
        print (bcolors.OKGREEN + "post created " + bcolors.ENDC)

def find_a(json_object, name):
        return [obj for obj in json_object if obj['author']==name]

def main():
    # printMsg('Starting Scrapping')
    q_list = getQuotesFromJson()
    for url in q_list:
        if(url['id'] not in q_authors):
            print('storing '+url['id'])
            createQuote(url)

if __name__ == '__main__':
    main()

