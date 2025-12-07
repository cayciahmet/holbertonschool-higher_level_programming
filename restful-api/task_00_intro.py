import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            content = template
            keys_to_replace = ["name", "event_title", "event_date", "event_location"]
            
            for key in keys_to_replace:
                value = attendee.get(key)
                if value is None:
                    value = "N/A"
                
                placeholder = "{" + key + "}"
                content = content.replace(placeholder, str(value))

            output_filename = "output_{}.txt".format(index)
            
            if os.path.exists(output_filename):
                pass
                
            with open(output_filename, 'w') as f:
                f.write(content)
                
        except Exception as e:
            print("An error occurred while processing attendee {}: {}".format(index, e))
