from django.http import HttpResponse
from django.template import loader

from home.models import Post


# Create your views here.


def home(request):
    template = loader.get_template('index.html')
    context = {
        'items': Post.objects.all()
    }
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template('search.html')
    query = request.GET['search'].lower()
    context = {
        'items': Post.objects.filter(tags__name__in=[query]),
        'query': query,
    }
    return HttpResponse(template.render(context, request))
