from django.urls.base import reverse_lazy
from .models import ImagePost, Location
from .forms import ImageForm, ImageUpdateForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = ImagePost
    template_name = 'home.html'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = ImagePost
    template_name = 'post_details.html'

class AddPost(LoginRequiredMixin, CreateView):
    model = ImagePost
    form_class = ImageForm
    template_name = 'add_post.html' 

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = ImagePost
    form_class = ImageUpdateForm
    template_name = 'update_post.html' 

class DeletePost(LoginRequiredMixin, DeleteView):
    model = ImagePost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

@login_required
def post_by_location(request, locale):

    pictures = ImagePost.objects.filter(image_location = locale).all()
    location = Location.objects.get(id = locale)
    title = f'Photos taken in {location}'
    return render(request, 'post_location.html', {'pictures': pictures, 'title': title, 'location': location})

@login_required
def search_results(request):  

    if 'search_category' in request.GET and request.GET["search_category"]:
        search_term = request.GET.get("search_category")
        searched_photos = ImagePost.search_by_category(search_term)
        message = f"{search_term}"
        title = search_term
        return render(request, 'search_results.html',{"message": message, "pictures": searched_photos, 'title': title})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message": message})


    