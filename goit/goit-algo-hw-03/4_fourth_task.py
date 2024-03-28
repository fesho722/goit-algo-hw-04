from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday = birthday.replace(year=today.year)  

        if birthday < today: 
            birthday = birthday.replace(year=today.year + 1)  

        if (birthday - today).days <= 7:
            if birthday.weekday() in (5, 6):  
                birthday += timedelta(days=7 - birthday.weekday())
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday.strftime('%Y.%m.%d')})

    return upcoming_birthdays



        
   

    