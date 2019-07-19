import json

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client


toScrap = 'http://wp.test/'
username = 'admin'
password = 'redefine123'
client = Client(toScrap+'/xmlrpc.php', username, password)


filePath = './main-quotes.json'
url_list = ''
author=[]
with open(filePath, 'r') as filehandle:
    a_list = json.load(filehandle)
    
for a in a_list:
    if(a['author'] not in author):
        author.append(a['author'])

if(len(author)):
    for a in author:
        if a and len(a)>= 1:
            try:
                print('storing author'+a)
                post = WordPressPost()
                post.title = a
                post.post_type = 'q_author'
                post.post_status = "publish"
                addpost = client.call(posts.NewPost(post))
            except:
                pass
           