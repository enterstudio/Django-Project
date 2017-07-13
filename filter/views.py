from django.http import HttpResponse
from django.template import loader
from filter.models import Post


# Create your views here.


def index(request):
    template = loader.get_template('filter_index.html')
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
