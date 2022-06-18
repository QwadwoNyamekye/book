from django.shortcuts import render


def index(request):
    name = "kwame"
    return render(request, "base.html", {"name": name})


def search(request):
    searched_value = request.GET.get('search')
    return render(request, "search_result.html", {'search': searched_value})
