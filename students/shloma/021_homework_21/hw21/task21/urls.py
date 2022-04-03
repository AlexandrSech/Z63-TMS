from django.urls import path
from . import views


urlpatterns = [
   path(r'', views.index, name='index'),
   path(r'person/<person_id>', views.show_one_person, name='person_detail'),
   path(r'edit/<person_id>', views.edit_person, name='person_edit'),
   path(r'delete/<person_id>', views.delete_person, name='person_delete'),
]
