from django.shortcuts import render
from .models import Restaurant,Review,Video,Vlog,Blog,Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from review.models import Model

# Create your views here.

def home(request):
    restaurants=Restaurant.objects.all()[:3][::-1]
    reviews=Review.objects.all()[:3][::-1]
    videos=Video.objects.all()[:3][::-1]
    vlogs=Vlog.objects.all()[:3][::-1]
    blogs=Blog.objects.all()[:3][::-1]
    recipes=Recipe.objects.all()[:3][::-1]
    pinned=list(Restaurant.objects.filter(pinned=True))+list(Review.objects.filter(pinned=True))+list(Video.objects.filter(pinned=True))+list(Vlog.objects.filter(pinned=True))+list(Blog.objects.filter(pinned=True)) +list(Recipe.objects.filter(pinned=True))
    pinned=pinned[:6][::-1]
    return render(request,"home.html",{"restaurants":restaurants,"reviews":reviews,"videos":videos,"vlogs":vlogs,"blogs":blogs,"recipes":recipes,"pinned":pinned})


def restaurants(request):
    restaurants=Restaurant.objects.all()
    return render(request,"restaurants.html",{"restaurants":restaurants})

def restaurantdishes(request,id):
    restauarnt=Restaurant.objects.get(id=id)
    dish=restauarnt.dish_set.all()
    return render(request,"dishes.html",{"dish":dish,"restauarnt":restauarnt})

def reviews(request):
    reviews=Review.objects.all()
    return render(request,"reviews.html",{"reviews":reviews})

def reviewdetail(request,id):
    reviews=Review.objects.get(id=id)
    img=reviews.reviewimage_set.all()
    return render(request,"reviewsdetail.html",{"reviews":reviews,"img":img})

def videos(request):
    videos=Video.objects.all()
    return render(request,"videos.html",{"videos":videos})

def videodetail(request,id):
    video=Video.objects.get(id=id)
    return render(request,"videodetail.html",{"video":video})

def vlogs(request):
    vlogs=Vlog.objects.all()
    return render(request,"vlogs.html",{"vlogs":vlogs})

def vlogdetail(request,id):
    vlog=Vlog.objects.get(id=id)
    return render(request,"vlogdetail.html",{"vlog":vlog})

def blogs(request):
    blogs=Blog.objects.all()
    return render(request,"blogs.html",{"blogs":blogs})

def blogdetail(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,"blogdetail.html",{"blog":blog})

def recipes(request):
    recipes=Recipe.objects.all()
    return render(request,"recipes.html",{"recipes":recipes})

def recipedetail(request,id):
    recipe=Recipe.objects.get(id=id)
    return render(request,"recipedetail.html",{"recipe":recipe})



class modelCreateView(LoginRequiredMixin, CreateView):
    model = Model
    template_name = 'create.html'
    fields = ["title","text","image","images","desc","video","pinned","rating","category"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(modelCreateView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Model.objects.all()
        return context

def models(request):
    models=Model.objects.all()
    return render(request,"models.html",{"models":models})

def modeldetail(request,id):
    model=Model.objects.get(id=id)
    return render(request,"modeldetail.html",{"model":model})
