import os

def generate_invitations(template, attendees):
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Create a personalized content from the template
            content = template
            
            # List of keys we expect to replace
            keys_to_replace = ["name", "event_title", "event_date", "event_location"]
            
            for key in keys_to_replace:
                # Get the value, default to "N/A" if key is missing or value is None
                value = attendee.get(key)
                if value is None:
                    value = "N/A"
                
                # Replace the placeholder in the content
                placeholder = "{" + key + "}"
                content = content.replace(placeholder, str(value))

            # 4. Generate Output Files
            output_filename = "output_{}.txt".format(index)
            
            # Check if file exists (as per hints, though 'w' handles overwrite)
            if os.path.exists(output_filename):
                # Just a safety check or log if needed, but we proceed to write
                pass
                
            with open(output_filename, 'w') as f:
                f.write(content)
                
        except Exception as e:
            print("An error occurred while processing attendee {}: {}".format(index, e))

