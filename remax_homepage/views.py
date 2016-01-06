from django.shortcuts import render

def home_page(request):
    return render(request, "remax_homepage/home_page.html", {})

def about_page(request):
    return render(request, "remax_homepage/about_page.html", {})

def blog_page(request):
    return render(request, "remax_homepage/blog_page.html", {})

def neighborhoods_page(request):
    return render(request, "remax_homepage/neighborhoods_page.html", {})