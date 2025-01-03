from django.shortcuts import render, redirect
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

    #return render(request, 'notesApp/add_note.html', {'form': form})
    return render(request, 'notesApp/add_note.html', {'form': form})



def note_list(request):
    notes = Note.objects.all()
    notesDesc = Note.objects.order_by('-created_at')
    notesFavs = Note.objects.filter(is_favorite=1)
    notesTemp = Note.objects.filter(is_temporary=1)
    notesLast = Note.objects.filter(is_last=1)
    notesRec = Note.objects.filter(is_in_recycle=1)
    return render(request, 'notesApp/note_list.html', {'notes':notes, 'notesDesc':notesDesc, 'notesFavs':notesFavs, 'notesTemp':notesTemp, 'notesLast':notesLast, 'notesRec':notesRec})



def save_note(request):
    #return redirect('/succc111')  # Перенаправляем на страницу успеха

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Создаем новую запись в базе данных
        note = Note(title=title, content=content)
        note.save()

        return redirect('/')  # Перенаправляем на страницу успеха

    return render(request, 'note_list.html')  # Отображаем форму при GET запросе