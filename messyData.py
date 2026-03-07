#arrange messy data
data = [
    "   Minhazur Rahman  ,  MINHAZXLUIS@GMAIL.COM ,  017-123-45678  ",
    "   Ali Hasan  ,  ALI@GMAIL.COM ,  018-987-65432  ",
    "   Sara Ahmed  ,  SARA@YAHOO.COM ,  019-111-22333  ",
]
cleaned_data = []
for entry in data:
    name, email, phone = entry.split(",")
    cleaned_entry = {
        "name": name.strip(),
        "email": email.strip().lower(),
        "phone": phone.strip().replace("-", "")
    }
    cleaned_data.append(cleaned_entry)
for contact in cleaned_data:
    print(f"Name: {contact['name']}\n Email: {contact['email']}\n Phone: {contact['phone']}\n")
