from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(
        request,
        "home.html",
        {"dynamic_content": "This is dynamic content passed from the view."},
    )
