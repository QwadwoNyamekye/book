from django.shortcuts import render


def index(request):
    name = "kwame"
    return render(request, "base.html", {"name": name})
