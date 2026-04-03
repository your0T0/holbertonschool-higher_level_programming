#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""

def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendees.

    Args:
        template (str): Invitation template string
        attendees (list): List of dictionaries containing attendee data
    """

    # Check input types
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Handle empty inputs
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        if name is None:
            name = "N/A"
        if event_title is None:
            event_title = "N/A"
        if event_date is None:
            event_date = "N/A"
        if event_location is None:
            event_location = "N/A"

        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(event_title))
        output = output.replace("{event_date}", str(event_date))
        output = output.replace("{event_location}", str(event_location))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
