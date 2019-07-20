# url = 'https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1378&q=80'
url='https://source.unsplash.com/1600x900/?nature,water'
# url='https://source.unsplash.com/400x400/?life'
import urllib.request

res =urllib.request.urlretrieve(url, "./img-quote/local-filename.jpg")
print(res)