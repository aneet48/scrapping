import json

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client
import random 

import urllib.request

toScrap = 'http://localhost/wordpress/'
username = 'admin'
password = 'admin'
client = Client(toScrap+'/xmlrpc.php', username, password)

# postsAll = client.call(posts.GetPosts())
data = []
offset = 0
increment = 20
while True:
        wp_posts = client.call(posts.GetPosts(
            {'post_type':'q_author','number': increment, 'offset': offset}))
        if len(wp_posts) == 0:
                break  # no more posts returned
        for post in wp_posts:
                data.append({'id':post.id,'title':post.title})
                # data.append(post.title)
        offset = offset + increment
# existingPosts = ','.join(data)

filePath = './main-quotes.json'
with open(filePath, 'r') as filehandle:
    a_list = json.load(filehandle)

def findauthor(json_object, title):
    for dict in json_object:
        if dict['title'] == title:
            return dict['id']

new_list=[]

if(len(a_list)):
    for a in a_list:
        res = findauthor(data,a['author'])
        a['author-id'] = res
        new_list.append(a)
        print(res)
print(new_list)
with open('./main-quotes-id.json', 'w') as filehandle:
    json.dump(new_list,filehandle)
