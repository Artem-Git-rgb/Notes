from .models import Note

new_entry = Note(title='TestNote', content='Text 2024.17.12')
new_entry.save()