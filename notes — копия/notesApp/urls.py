from django.urls import path, include
from . import views
from .views import add_note
from .views import save_note
from django.contrib import admin


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', add_note, name='add_note'),
    path('save/', save_note, name='save_note'),
    #path('admin/', admin.site.urls),
    #path('add/', add_note, name='add_note'),
    #path('success/', TemplateView.as_view(template_name='success.html'), name='success'),  # Страница успешного завершения
]
