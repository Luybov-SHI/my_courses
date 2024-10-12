def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    full_name_recipient = '@' in recipient and (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'))
    full_name_sender = '@' in sender and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))
    if full_name_recipient and full_name_sender:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для Urban', 'Luybov55@gmail.com')
send_email('Доброго всем  денечка!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, не торопитесь', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминание о встрече', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')