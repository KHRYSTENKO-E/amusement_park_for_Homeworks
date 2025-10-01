from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import AttractionForm
from main.models import Attractions


class AttractionDetailView(DetailView):
    model = Attractions
    template_name = "my_administrator/attractions/detail_view.html"
    context_object_name = "attractions"

class AttractionUpdateView(UpdateView):
    model = Attractions
    template_name = "my_administrator/attractions/update.html"
    form_class = AttractionForm
    success_url = ".."

class AttractionDeleteView(DeleteView):
    model = Attractions
    template_name = "my_administrator/attractions/delete.html"
    success_url = ".."

def show_administrator_main_page(request):
    return render(request, "my_administrator/main_page.html")

def show_attractions(request):
    all_attractions = Attractions.objects.all()
    sort_field = request.GET.get("sort", "id")
    direction = request.GET.get("dir", "asc")

    if request.method == 'POST':
        filters_fields = ['id', 'time', 'name', 'min_age', 'zone']
        filters = {}
        for i in filters_fields:
            value = request.POST.get(f"filter_{i}")
            if value:
                filters[i] = value
        all_attractions = Attractions.objects.filter(**filters)

    if direction == 'desc':
        all_attractions = all_attractions.order_by(f"-{sort_field}")
    else:
        all_attractions = all_attractions.order_by(sort_field)

    return render(request, "my_administrator/attractions/show.html", {'all_attractions' : all_attractions, 'sort_field':sort_field, 'direction' : direction})

def add_attraction(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(".")

    form = AttractionForm
    return render(request, "my_administrator/attractions/add.html", {'form' : form})


