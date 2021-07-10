from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Hotel
# Create your views here.
def hotel_image_view(request):
    if request.method == "POST":
        form=HotelForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/display')

    else:
        form=HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})

def display_img(request):
    if request.method=="GET":

        Hotels=Hotel.objects.all()
        return render(request, 'display_hotel_images.html',{'hotel_images':Hotels})
