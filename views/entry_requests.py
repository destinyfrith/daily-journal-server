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
            m.label
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
            entry.mood_id = mood.__dict__

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
