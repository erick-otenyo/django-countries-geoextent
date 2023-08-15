from django.shortcuts import render

from sandbox.home.models import Home


def home(request):
    home = Home.objects.first()

    return render(request, template_name="home.html", context={}, )
