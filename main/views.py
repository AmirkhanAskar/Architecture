from django.shortcuts import render, get_object_or_404, redirect
from .models import MyBlogs
from .models import Interiors
from .models import Exteriors
from .models import InteriorImage
from .models import ExteriorImage
from .models import Kitchens
from .models import KitchenImage
from .models import PrivateHouses
from .models import PrivateHouseImage
from .forms import CommentForm
from itertools import chain
import random


def index(request):
    interiors = Interiors.objects.all()
    exteriors = Exteriors.objects.all()
    kitchens = Kitchens.objects.all()
    privateHouses = PrivateHouses.objects.all()

    combined_projects = list(chain(interiors, exteriors, kitchens, privateHouses))
    random.shuffle(combined_projects)  # Перемешивание списка проектов

    return render(request, 'main/index.html', {'combined_projects': combined_projects})


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def contact(request):
    return render(request, 'main/contact.html')


# def interior(request):
#     return render(request, 'main/projects.html')


def exterior(request):
    return render(request, 'main/exterior.html')


def blog_page(request):
    blog_entries = MyBlogs.objects.all()
    return render(request, 'main/blog.html', {'blog_entries': blog_entries})


def blog_detail(request, blog_id):
    blog = get_object_or_404(MyBlogs, pk=blog_id)
    comments = blog.comments.all()
    return render(request, 'main/eachBlog.html', {'blog': blog, 'comments': comments})



def add_comment(request, blog_id):
    blog = get_object_or_404(MyBlogs, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()

    return render(request, 'main/eachBlog.html', {'blog': blog, 'form': form})


def interior_page(request):
    interior_entries = Interiors.objects.all()
    return render(request, 'main/projects.html', {'interior_entries': interior_entries})



def interior_detail(request, interior_id):
    interior = get_object_or_404(Interiors, pk=interior_id)
    interior_images = InteriorImage.objects.filter(interior=interior)
    return render(request, 'main/projectSignle.html', {'interior': interior, 'interior_images': interior_images})


def exterior_page(request):
    exterior_entries = Exteriors.objects.all()
    return render(request, 'main/exterior.html', {'exterior_entries': exterior_entries})


def exterior_detail(request, exterior_id):
    exterior = get_object_or_404(Exteriors, pk=exterior_id)
    exterior_images = ExteriorImage.objects.filter(exterior=exterior)
    return render(request, 'main/projectExterior.html', {'exterior': exterior, 'exterior_images': exterior_images})


def kitchen_page(request):
    kitchen_entries = Kitchens.objects.all()
    return render(request, 'main/kitchens.html', {'kitchen_entries': kitchen_entries})


def kitchen_detail(request, kitchen_id):
    kitchen = get_object_or_404(Kitchens, pk=kitchen_id)
    kitchen_images = KitchenImage.objects.filter(kitchen=kitchen)
    return render(request, 'main/projectKitchen.html', {'kitchen': kitchen, 'kitchen_images': kitchen_images})



def privateHouse_page(request):
    privateHouse_entries = PrivateHouses.objects.all()
    return render(request, 'main/privateHouses.html', {'privateHouse_entries': privateHouse_entries})


def privateHouse_detail(request, privateHouse_id):
    privateHouse = get_object_or_404(PrivateHouses, pk=privateHouse_id)
    privateHouse_images = PrivateHouseImage.objects.filter(PrivateHouse=privateHouse)
    return render(request, 'main/projectPrivateHouse.html', {'privateHouse': privateHouse, 'privateHouse_images': privateHouse_images})


def mixed_projects(request):
    interior_entries = Interiors.objects.all()
    exterior_entries = Exteriors.objects.all()
    kitchen_entries = Kitchens.objects.all()
    privateHouse_entries = PrivateHouses.objects.all()

    # Объединяем все записи в один список
    combined_entries = list(chain(interior_entries, exterior_entries, kitchen_entries, privateHouse_entries))
    
    # Перемешиваем список
    random.shuffle(combined_entries)

    return render(request, 'main/mixed_projects.html', {'combined_entries': combined_entries})