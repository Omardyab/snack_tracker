from django.views.generic import ListView,DetailView
from .models import Snacks

# Create your views here.
class Snackslistview(ListView):
    template_name='snacks_list.html'
    model=Snacks

class Snacksdetailview(DetailView):
    template_name='snacks_detail.html'
    model=Snacks



