from django.urls import path, re_path, include
from . import views
from .views import add_note, move_2_bin, save_note, test_page, get_info, search

#from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', add_note, name='add_note'),
    path('save/', save_note, name='save_note'),
    path('test/', test_page, name='test_page'),
    path('note/xml/<int:id>/', get_info, name='get_info'),
    path('search/', search, name='search'),
    path('move2bin/<int:id>/<int:is_in_bin>/', move_2_bin, name='move_2_bin'),

    #path('admin/', admin.site.urls),
    #path('add/', add_note, name='add_note'),
    #path('success/', TemplateView.as_view(template_name='success.html'), name='success'),  # Страница успешного завершения
]
