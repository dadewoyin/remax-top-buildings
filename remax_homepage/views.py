from django.shortcuts import render

def home_page(request):
    return render(request, "remax_homepage/home_page.html", {})

def about_page(request):
    return render(request, "remax_homepage/about_page.html", {})

def blog_page(request):
    return render(request, "remax_homepage/blog_page.html", {})

def neighborhoods_page(request):
    return render(request, "remax_homepage/neighborhoods_page.html", {})

def show_neighborhood(request, neighborhood):
    return render(request, "remax_homepage/show_neighborhood.html", {
        "dir": "images/" + neighborhood + ".png", 
        "neighborhood": neighborhood.title().replace("-", " ")})

def top_buildings_main(request):
    return render(request, "remax_homepage/top_buildings_main.html", {})