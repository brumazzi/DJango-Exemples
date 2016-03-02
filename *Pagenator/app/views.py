from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Article

def index(request, page=1):
    p = Paginator(Article.objects.all(),3)
    try:
        res = p.page(page)
    except PageNotAnInteger:
        res = p.page(1)
    except EmptyPage:
        res = p.page(p.num_pages)

    return render(request, 'index.html',{
            'article': res.object_list,
            'paginator':res,
            'page_now':page,
        })
