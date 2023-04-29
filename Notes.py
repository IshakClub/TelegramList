class Notes:
    def __init__(self):
        self.list_notes = {}
        self.choosen_note = None

    def formate_note(self, note: dict):
        form = ''
        for i in range(1, len(note) + 1):
            form += f'  {i}. {note[str(i)]}\n'
        return form

    def add_note(self, name_of_note):
        self.list_notes[name_of_note] = {}
        self.choosen_note = name_of_note

    def remove_note(self, name_of_note):
        self.list_notes.pop(name_of_note)
        if name_of_note == self.choosen_note:
            self.choosen_note = None

    def return_notes(self):
        return '\n'.join(self.list_notes.keys())

    def choose_note(self, name_of_note):
        self.choosen_note = name_of_note
        return name_of_note, self.formate_note(self.list_notes[name_of_note])

    def exit_from_note(self):
        self.choosen_note = None
        return self.return_notes()

    def change_name(self, text):
        text = text.split(' *')
        if len(text) == 2:
            new_name_of_note, name_of_note = text
        else:
            new_name_of_note, name_of_note = text[0], ''
        if not name_of_note:
            if self.choosen_note is None:
                return
            name_of_note = self.choosen_note
        self.list_notes[new_name_of_note] = self.list_notes[name_of_note]
        self.list_notes.pop(name_of_note)

    def add_to_note(self, text):
        number = text.split('. ')[0]
        if number.isdigit():
            text = '. '.join(text.split('. ')[1:])
        text = text.split(' *')
        if len(text) == 2:
            text, name_of_note = text
        else:
            text, name_of_note = text[0], ''
        if not name_of_note:
            if self.choosen_note is None:
                return
            name_of_note = self.choosen_note
        if not number.isdigit():
            number = str(len(self.list_notes[name_of_note]) + 1)
        self.list_notes[name_of_note][number] = text

    def remove_from_note(self, text):
        text = text.split(' *')
        if len(text) == 2:
            numbers, name_of_note = text
        else:
            numbers, name_of_note = text[0], ''
        if not name_of_note:
            if self.choosen_note is None:
                return
            name_of_note = self.choosen_note
        if not numbers:
            numbers = str(len(self.list_notes[name_of_note]))
        for number in numbers.split():
            if not number.isdigit():
                continue
            self.list_notes[name_of_note].pop(number)

    def output_note(self, name_of_note):
        if not name_of_note:
            if self.choosen_note is None:
                return
            name_of_note = self.choosen_note
        return name_of_note, self.formate_note(self.list_notes[name_of_note])