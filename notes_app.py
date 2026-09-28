import json
import os

FILE_NAME = "notes.json"


# Load notes from JSON file
def load_notes():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    return []


# Save notes to JSON file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


# Add a new note
def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    note = {
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes(notes)

    print("Note added successfully!")


# View all notes
def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    print("\n===== ALL NOTES =====")

    for i, note in enumerate(notes, start=1):
        print(f"\nNote {i}")
        print("Title:", note["title"])
        print("Content:", note["content"])


# Search notes
def search_notes(notes):
    keyword = input("Enter keyword to search: ").lower()

    found = False

    for i, note in enumerate(notes, start=1):
        if (keyword in note["title"].lower()
                or keyword in note["content"].lower()):

            print(f"\nNote {i}")
            print("Title:", note["title"])
            print("Content:", note["content"])

            found = True

    if not found:
        print("No matching notes found.")


# Update a note
def update_note(notes):
    view_notes(notes)

    if not notes:
        return

    try:
        number = int(input("\nEnter note number to update: "))

        if number < 1 or number > len(notes):
            print("Invalid note number.")
            return

        new_title = input("Enter new title: ")
        new_content = input("Enter new content: ")

        notes[number - 1]["title"] = new_title
        notes[number - 1]["content"] = new_content

        save_notes(notes)

        print("Note updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Delete a note
def delete_note(notes):
    view_notes(notes)

    if not notes:
        return

    try:
        number = int(input("\nEnter note number to delete: "))

        if number < 1 or number > len(notes):
            print("Invalid note number.")
            return

        deleted_note = notes.pop(number - 1)

        save_notes(notes)

        print("Deleted:", deleted_note["title"])

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    notes = load_notes()

    while True:
        print("\n========================")
        print("       NOTES APP")
        print("========================")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            update_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("Thank you for using Notes App!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
