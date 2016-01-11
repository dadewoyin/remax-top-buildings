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
    return render(request, 
        "remax_homepage/show_neighborhood_"+ neighborhood +".html", 
        {"original": neighborhood,
         "dir": "images/LG/" + neighborhood + ".png", 
         "neighborhood": neighborhood.title().replace("-", " ")})

def top_buildings_main(request):
    return render(request, "remax_homepage/top_buildings_main.html", {})

def show_top_buildings(request, neighborhood):
    return render(request ,
        "remax_homepage/show_top_buildings_"+neighborhood+".html", 
        {"neighborhood" : neighborhood.title().replace("-", " ")
        })

def show_building_profile(request, neighborhood, rank):
    return render(request, 
        "remax_homepage/show_building_profile_"+neighborhood+"-"+rank+".html", 
        {"rank": rank,
         "neighborhood": neighborhood.title().replace("-", " ")})

def contact_page(request):
    return render(request, "remax_homepage/contact_page.html", {})