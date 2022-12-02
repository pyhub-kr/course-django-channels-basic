from django.shortcuts import render


def echo_page(request):
    return render(request, "app/echo_page.html")
