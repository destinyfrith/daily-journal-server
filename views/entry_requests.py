import sqlite3
import json
from models import Entry


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

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
            e.moodId
        FROM Entry e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(row['id'], row['date'], row['entry'], row['concept'],
                          row['moodId'])

            # Add the dictionary representation of the animal to the list
            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)
