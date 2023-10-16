from django.shortcuts import render
import requests

def index(request):
    f=requests.get('http://api.mediastack.com/v1/news?access_key=50cf4b745ceeccd057b1b5a8c5b406b5&countries=in')
    res=f.json()
    data = res['data']
    title = []
    description = []
    image = []
    category = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        category.append(i['category'])
        url.append(i['url'])
    final = zip(title,description,image,category,url)
    return render(request, 'newsapp/index.html', {'final': final})    
        

# Create your views here.
