import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import xml.etree.ElementTree as ET
from .models import Note
from .forms import NoteForm

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # перенаправление на страницу успеха или другую
    else:
        form = NoteForm()

    # return render(request, 'notesApp/add_note.html', {'form': form})
    return render(request, 'notesApp/add_note.html', {'form': form})


def note_list(request):
    notes = Note.objects.all()
    notesDesc = Note.objects.order_by('-created_at').filter(is_in_recycle=0)
    notesFavs = Note.objects.filter(is_favorite=1).order_by('-last_update').order_by('-created_at')
    notesTemp = Note.objects.exclude(action_dt='').order_by('-action_dt').filter(is_in_recycle=0)
    notesLast = Note.objects.filter(is_last=1).order_by('-last_update').order_by('-created_at')
    notesRec = Note.objects.filter(is_in_recycle=1).order_by('-last_update').order_by('-created_at')


   # results = Note.objects.filter(title__icontains=query)  # Поиск по полю 'title'
   # return render(request, 'search_results.html', {'results': results, 'query': query})

    return render(request, 'notesApp/note_list.html',
              {'notes': notes, 'notesDesc': notesDesc, 'notesFavs': notesFavs, 'notesTemp': notesTemp,
               'notesLast': notesLast, 'notesRec': notesRec})





def save_note(request):
    # return redirect('/succc111')  # Перенаправляем на страницу успеха

    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        action_dt = request.POST.get('action_dt')
        is_fav = int(request.POST.get('hid_fav'))

        mode = request.POST.get('mode')

        if (mode == 'create'):
            # Создаем новую запись в базе данных

            if request.FILES:
                file = request.FILES['pic']
                fs = FileSystemStorage()
                # сохраняем на файловой системе
                filename = fs.save(file.name, file)
                # получение адреса по которому лежит файл
                file_url = fs.url(filename)
            else:
                file_url = ''

            note = Note(title=title, content=content, action_dt=action_dt, is_favorite=is_fav, pic=file_url)

            note.save()

        elif (mode == 'update'):
            # Обновляем запись в базе данных
            note = Note.objects.get(id=note_id)
            note.title = title
            note.content = content
            note.action_dt = action_dt
            note.is_favorite = is_fav
            note.last_update = datetime.datetime.now()

            if request.FILES:
                file = request.FILES['pic']
                fs = FileSystemStorage()
                # сохраняем на файловой системе
                filename = fs.save(file.name, file)
                # получение адреса по которому лежит файл
                file_url = fs.url(filename)

                note.pic = file_url

            note.save()

        else:
            print('save_note: mode not defined!')

        return redirect('/')  # Перенаправляем на страницу успеха

    return render(request, 'note_list.html')  # Отображаем форму при GET запросе


def test_page(request):
    return HttpResponse("Hello")


def get_info(request, id):

    # Получаем объект по ID
    note_instance = get_object_or_404(Note, id=id)

    # Создаем XML-структуру
    root = ET.Element('Note')
    id1 = ET.SubElement(root, 'id')
    id1.text = str(note_instance.id)
    name = ET.SubElement(root, 'Title')
    name.text = note_instance.title
    description = ET.SubElement(root, 'Content')
    description.text = note_instance.content
    is_favorite = ET.SubElement(root, 'Is_favorite')
    is_favorite.text = str(note_instance.is_favorite)
    action_dt = ET.SubElement(root, 'Action_dt')
    action_dt.text = note_instance.action_dt

    is_in_recycle = ET.SubElement(root, 'Is_in_recycle')
    is_in_recycle.text = str(note_instance.is_in_recycle)

    pic_name = ET.SubElement(root, 'Img_name')
    try:
        pic_name.text = note_instance.pic.url
    except:
        pic_name.text  = ''


    # Преобразуем дерево в строку
    xml_str = ET.tostring(root, encoding='unicode')

    # Возвращаем ответ с правильным заголовком
    return HttpResponse(xml_str, content_type='application/xml')


def search(request):
    query = request.GET.get('q', '') # Получаем поисковый запрос
    if query:
        # ... ваш код поиска (например, с использованием Haystack или filter) ...
        results = Note.objects.filter(title__icontains=query).order_by('-last_update').order_by('-created_at')

        return render(request, 'search_results.html', {'results': results, 'query': query})


    else:
        return render(request, 'search_results.html') # Возвращаем пустой шаблон, если запроса нет


def move_2_bin(request, id, is_in_bin):
    note = get_object_or_404(Note, id=id)
    note.is_in_recycle = is_in_bin
    note.last_update = datetime.datetime.now()
    note.save()
    return render(request, 'notesApp/note_list.html')  # Отображаем форму при GET запросе
