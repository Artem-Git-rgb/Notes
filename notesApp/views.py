from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import xml.etree.ElementTree as ET
from .models import Note, Image
from .forms import NoteForm



"""
from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
from PIL import Image
import os
"""

"""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/' # Директория для хранения изображений
app.secret_key = "46324gf36r623rt" # Замените на ваш секретный ключ

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Опционально: изменение размера изображения с помощью Pillow
            try:
                img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                img.thumbnail((128, 128)) # Изменяем размер на 128x128 пикселей, сохраняя пропорции
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            except IOError as e:
                print(f"Ошибка обработки изображения: {e}")

            return redirect('/success')
    return render_template('upload.html')


@app.route('/success')
def success():
    return "Файл успешно загружен!"

if __name__ == '__main__':
    app.run(debug=True)

"""

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
    notesDesc = Note.objects.order_by('-created_at')
    notesFavs = Note.objects.filter(is_favorite=1).order_by('-last_update').order_by('-created_at')
    notesTemp = Note.objects.exclude(action_dt='').order_by('-action_dt') #111
    notesLast = Note.objects.filter(is_last=1).order_by('-last_update').order_by('-created_at')
    notesRec = Note.objects.filter(is_in_recycle=1)
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
        is_fav = request.POST.get('hid_fav')

        mode = request.POST.get('mode')

        if (mode == 'create'):
            # Создаем новую запись в базе данных
            note = Note(title=title, content=content, action_dt=action_dt, is_favorite=is_fav)
            note.save()
        elif (mode == 'update'):
            # Обновляем запись в базе данных
            note = Note.objects.get(id=note_id)
            note.title = title
            note.content = content
            note.action_dt = action_dt
            note.is_favorite = int(is_fav)
            note.save()
        else:
            print('save_note: mode not defined!')

        # Сохраняем картинку
        #if count(request.FILES) > 0:

















        return redirect('/')  # Перенаправляем на страницу успеха

    return render(request, 'note_list.html')  # Отображаем форму при GET запросе


def test_page(request):
    return HttpResponse("Hello")


def get_info(request, id):

    # Получаем объект по ID
    note_instance = get_object_or_404(Note, id=id)

    try:
        image_instance = Image.objects.get(note_id=id)  #111
    except Image.DoesNotExist:
        image_instance = None


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

    if image_instance != None:
        img_name = ET.SubElement(root, 'Img_name')
        img_name.text = str(image_instance.file_name)


    """
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=0)
    action_dt = models.TextField()
    is_last = models.BooleanField(default=False)
    is_in_recycle = models.BooleanField(default=False)
    last_update = models.TextField()
    """

    # Преобразуем дерево в строку
    xml_str = ET.tostring(root, encoding='unicode')

    # Возвращаем ответ с правильным заголовком
    return HttpResponse(xml_str, content_type='application/xml')
