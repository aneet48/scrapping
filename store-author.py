import json

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client
import random 

import urllib.request

toScrap = 'https://arbites.in/qoutes'
username = 'admin'
password = 'takerisk48'
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
                data.append(post.title)
        offset = offset + increment
existingPosts = ','.join(data)

# toScrap = 'http://wp.test/'
# username = 'admin'
# password = 'redefine123'

# get authors from quotes list and store it saparetly
# filePath = './main-quotes.json'
# url_list = ''
# author=[]
# tmp_author=[]
# with open(filePath, 'r') as filehandle:
#     a_list = json.load(filehandle)
# for a in a_list:
#     if(a['author'] not in tmp_author):
#         tmp_author.append(a['author'])
#         author.append({'author':a['author'],'image':''})
# print(author)
# with open('./author.json', 'w') as filehandle:
#     json.dump(author,filehandle)
# data = {
#         'name': 'picture.jpg',
#         'type': 'image/jpeg',  # mimetype
# }
# with open('./images/local-filename.jpg', 'rb') as img:
#         data['bits'] = xmlrpc_client.Binary(img.read())
# response = client.call(media.UploadFile(data))
# print(response)
filePath = './author.json'
with open(filePath, 'r') as filehandle:
    a_list = json.load(filehandle)

if(len(a_list)):
    for a in a_list:
        if(a['author'] not in existingPosts):
            print('storing author '+ a['author'])
            attachment_id=''
            tags=[]
            if(a['featured']):
                tags.append('Featured')
            if(a['image']):
                num = str(random.randint(100, 25000))
                name = num +a['author']+ '.png'
                data = {
                        'name': name,
                        'type': 'image/png',  # mimetype
                }
                res =urllib.request.urlretrieve(a['image'], "./images/"+name)
                if(res):
                    with open('./images/'+name, 'rb') as img:
                        data['bits'] = xmlrpc_client.Binary(img.read())
                    response = client.call(media.UploadFile(data))
                    attachment_id=response['attachment_id']
            if a['author'] and len(a['author'])>= 1:
                # try:
                   
                    post = WordPressPost()
                    post.title = a['author']
                    post.post_type = 'q_author'
                    post.post_status = "publish"
                    post.terms_names = {
                        'post_tag':tags
                    }                
                    post.thumbnail = attachment_id
                    addpost = client.call(posts.NewPost(post))
                # except:
                #     exit()
                #     pass
           