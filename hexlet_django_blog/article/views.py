#from django.shortcuts import render
from django.http import HttpResponse

def index(request, tags, article_id):
    #return render(request, "articles/index.html", context={"app_name": "Article"})
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")