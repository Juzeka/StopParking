from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class CustomHomeView(LoginRequiredMixin, TemplateView): ...


class CustomListView(LoginRequiredMixin, ListView): ...


class CustomCreateView(LoginRequiredMixin, CreateView): ...


class CustomUpdateView(LoginRequiredMixin, UpdateView): ...


class CustomDetailView(LoginRequiredMixin, DetailView): ...


class CustomDeleteView(LoginRequiredMixin, DeleteView): ...