# url = 'https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1378&q=80'
url='https://bloximages.newyork1.vip.townnews.com/gwinnettdailypost.com/content/tncms/assets/v3/editorial/0/8d/08d2fd5e-266c-11e9-8f3b-b7c534b784e5/5c54c039c0e53.image.jpg?resize=602%2C494'
# url='https://source.unsplash.com/400x400/?life'
import urllib

res =urllib.urlretrieve(url, "local-filename.jpg")
print(res)