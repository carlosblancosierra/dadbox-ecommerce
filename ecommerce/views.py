from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
    context = {
        "title":"Hellow World",
        "content":"Welcome to the hompage",
    }

    if request.user.is_authenticated():
        context["premiun_content"] = "yeahhhh"
    return render(request,"home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":"Welcome to the About Page"
    }
    return render(request,"home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Welcome to the Contact Page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message":"Gracias por su mensaje, le responderemos en la brevedad posible"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     # print (request.POST)
    #     print (request.POST.get('fullname'))
    #     print (request.POST.get('email'))
    #     print (request.POST.get('content'))

    return render(request,"contact/view.html", context)















