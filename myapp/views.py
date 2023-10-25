from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import OrderForm
from .models import Order, Meal, Gallery, Review, Contactform, About
from django.utils import timezone 

# Create your views here.

def index(request):
    
    if request.method == 'POST':

        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank You For Choosing Naija Restaurant, Your Booking Is Successful !')
            return render(request, 'index.html')
            
        name = request.POST.get('name')      
        email = request.POST.get('email')        
        subject = request.POST.get('subject') 
        message = request.POST.get('message')            
                       
        print(name, email, subject, message)            
        Contactform.objects.create(name=name, email=email, subject=subject, message=message,)
        messages.success(request, f'Your Message Has Been Sent Successfully !')       
        return redirect('index')

    else:
        form = OrderForm

    meals = Meal.objects.all()
    gallerys = Gallery.objects.all()
    reviews = Review.objects.all()
    abouts = About.objects.all()

    return render(request, 'index.html', {'form': form, "meals": meals, "gallerys": gallerys, "reviews": reviews, "abouts": abouts})

 

def donate(request):

    return render(request, 'donate.html')


def inner_page(request):

    return render(request, 'inner_page.html')

 



        


