from django.shortcuts import render


def index(request):
    content = "some test words"
    return render(request, 'static_pages/index.html', {'content': content})

