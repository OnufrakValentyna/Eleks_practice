from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'  # потрібно для використання флеш-повідомлень


def create_table():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                category_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories (id)
                )''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    create_table()
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM categories")
    categories = c.fetchall()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', categories=categories, notes=notes)


@app.route('/add_category', methods=['POST'])
def add_category():
    category_name = request.form['category_name']
    if not category_name:
        flash('Category name cannot be empty!', 'error')
    else:
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        c.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
        conn.commit()
        conn.close()
        flash('Category added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/add_note', methods=['POST'])
def add_note():
    content = request.form['note_content']
    category_id = request.form.get('category_id')
    if not content:
        flash('Note content cannot be empty!', 'error')
    elif not category_id:
        flash('Please select a category for the note!', 'error')
    else:
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        c.execute("INSERT INTO notes (category_id, content) VALUES (?, ?)", (category_id, content))
        conn.commit()
        conn.close()
        flash('Note added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    flash('Note deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if request.method == 'POST':
        content = request.form['note_content']
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        c.execute("UPDATE notes SET content=? WHERE id=?", (content, note_id))
        conn.commit()
        conn.close()
        flash('Note edited successfully!', 'success')
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM notes WHERE id=?", (note_id,))
        note = c.fetchone()
        conn.close()
        return render_template('edit_note.html', note=note)


if __name__ == '__main__':
    app.run(debug=True)
