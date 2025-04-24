from django.urls import path
from . import views
from .views import add_note, move_2_bin, save_note, test_page, get_info, search


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', add_note, name='add_note'),
    path('save/', save_note, name='save_note'),
    path('test/', test_page, name='test_page'),
    path('note/xml/<int:id>/', get_info, name='get_info'),
    path('search/', search, name='search'),
    path('move2bin/<int:id>/<int:is_in_bin>/', move_2_bin, name='move_2_bin'),

    path('test24', views.test24, name='test24'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
