from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Шляхи до файлів JSON
NOTES_FILE = 'notes.json'

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    content = request.form['note_content']
    notes = load_notes()
    notes.append(content)
    save_notes(notes)
    return jsonify(notes)

@app.route('/edit_note', methods=['POST'])
def edit_note():
    note_id = int(request.form['note_id'])
    new_content = request.form['new_content']
    notes = load_notes()
    notes[note_id] = new_content
    save_notes(notes)
    return jsonify(notes)

@app.route('/delete_note', methods=['POST'])
def delete_note():
    note_id = int(request.form['note_id'])
    notes = load_notes()
    del notes[note_id]
    save_notes(notes)
    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True)
