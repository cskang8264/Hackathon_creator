from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import Place_create
from .models import Place

# Create your views here.
def place(request):
    places = Place.objects
    return render(request, 'place.html', {'places':places})

def place_new(request):
    return render(request, 'place_new.html')

def place_detail(request, place_id):
    place_detail = get_object_or_404(Place, pk=place_id)
    return render(request, 'place_detail.html', {'place': place_detail})

def summary(self):
    return self.body[:100]

def place_create(request, place=None):
    if request.method == 'POST':
        form = Place_create(request.POST, request.FILES, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.pub_date = timezone.now()
            place.save()
            form.save_m2m()
            return redirect('place')
    else:
        form = PlaceForm(instance=place)
        return render(request, 'place_new.html', {'form': form})
    # place = Place()
    # place.title = request.GET['title']
    # place.body = request.GET['body']
    # place.pub_date = timezone.datetime.now()
    # place.save()
    # return redirect('/place/' + str(place.id))

# def placeform(request, place=None):       
#     if request.method == 'POST':
#         form = PlaceForm(request.POST, request.FILES, instance=place)
#         if form.is_valid():
#             place = form.save(commit=False)
#             place.pub_date = timezone.now()
#             place.save()
#             form.save_m2m()
#             return redirect('place')
#     else:
#         form = PlaceForm(instance=place)
#         return render(request, 'place_new.html', {'form': form})

# Edit
def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return place_create(request, place)

# Delete
def place_remove(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.delete()
    return redirect('place')