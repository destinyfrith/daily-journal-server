import sqlite3
import json
from models import Entry, Mood


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./journal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.concept,
            e.mood_id,
            m.label label
        FROM Entry as e
        JOIN Mood as m
            ON m.id = e.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(row['id'], row['date'], row['entry'], row['concept'],
                          row['mood_id'])

            mood = Mood(
                row['id'], row['label'])

            # Add the dictionary representation of the location to the animal
            entry.mood = mood.__dict__

            # Add the dictionary representation of the animal to the list
            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.concept,
            e.mood_id
        FROM entry e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['date'], data['entry'],
                      data['concept'], data['mood_id'])

        return json.dumps(entry.__dict__)

# function that allows you to find animals by location
# use location_id as parameter
# make sure to add new if statement in do_GET function on request_handler
# import into init and requesthandler modules like always


def delete_entry(id):
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))


def search_entries(searchedTerm):
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM entry AS e
        WHERE e.entry LIKE ?
            OR e.concept LIKE ?
        """, ("%" + searchedTerm + "%", "%" + searchedTerm + "%"))

        # Initialize an empty list to hold an entries representations
        entries = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate the list of data returned from the database
        for row in dataset:
            entry = Entry(row['id'], row['date'], row['entry'], row['concept'],
                          row['mood_id'])
        # Add dictionary representation of the entry to the list
        entries.append(entry.__dict__)

    return json.dumps(entries)


def create_journal_entry(new_entry):
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            ( date, entry, concept, mood_id )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['date'], new_entry['entry'],
              new_entry['concept'], new_entry['moodId'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entry
            SET
                date = ?,
                entry = ?,
                concept = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['date'], new_entry['entry'],
              new_entry['concept'], new_entry['moodId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
