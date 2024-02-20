PHONE_REGEX = r"(\d{3}[-\s]?\d{3}[-\s]?\d{4})"  

with open("file.txt", "r") as file:
    for line in file:
      matches = re.findall(PHONE_REGEX, line)
        for match in matches:
            # Validate the number (optional)
            if len(match) == 10:  # Check for 10 digits (without country code)
                print("Found phone number:", match)

                # Format the number (optional)
                formatted_number = f"{match[:3]}-{match[3:6]}-{match[6:]}"
                print("Formatted number:", formatted_number)
