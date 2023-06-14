from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from date_time_picker_sample.forms import ItemForm
from date_time_picker_sample.models import Item


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('list')


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('list')
