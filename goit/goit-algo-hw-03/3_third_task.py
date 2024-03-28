import re

def normalize_phone(phone_number):
    pattern = r"[\d]"
    formatted_phone_list = re.findall(pattern, phone_number)
    formatted_phone = ''.join(formatted_phone_list)
    if len(formatted_phone) == 12:
        return f"+{formatted_phone}"
    elif len(formatted_phone) == 10:
        return f"+38{formatted_phone}"
    else:
        return ""
