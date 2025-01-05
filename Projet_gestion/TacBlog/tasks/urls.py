from tkinter.font import names

from django.contrib import admin
from django.urls import path

from .views import info_personnel, do_tache, modifier_tache, do_tache_all

urlpatterns = [
    path('', info_personnel, name="info_personnel"),
    path('do/<int:id>/', do_tache, name="do_tache"),
    path('modifier/<int:id>/', modifier_tache, name="modifier_tache"),
    path('tasks/del_all/', do_tache_all, name='do_tache_all'),
]