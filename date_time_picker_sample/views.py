from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from date_time_picker_sample.forms import ItemForm, ItemModalForm
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


class ItemCreateModalView(BSModalCreateView):
    model = Item
    form_class = ItemModalForm
    template_name = 'date_time_picker_sample/item_modal_form.html'
    success_url = reverse_lazy('list')
