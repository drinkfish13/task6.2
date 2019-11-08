import re
email= input()
def check_email(adress):
    if re.match(r"[^@]+@[^@]+\.[^@]+", adress): # вполне себе пригодный вариант
    #if re.match(r"регулярное выражение отсюда http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html", email): - понять выражение не получилось по причине "шоб оно горело"
        return 'корректный'
    else:
        return 'некорректный'
print(check_email(email))

