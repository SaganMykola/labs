"""Довідник студента. База даних – розклад занять, містить п’ять записів з наступними полями: 1-ша пара, 2-га пара, 3-тя
 пара, 4-та пара, секція. Організувати вибір за довільним запитом. Дані зберігаються в масиві записів,
 який створюється динамічно."""
def input_one_subject():
    subject={}
    subject['предмет']=input('Предмет: ')
    subject["пара"] = int(input("Пара: "))
    return subject
def input_one_section():
     section = {}
     section["секція"] = input('Секція: ')
     section["пара"] = int(input("Пара: "))
     return section
def input_subjects():
    return [input_one_subject() for i in range(4)]
def input_section():
    return [input_one_section() for j in range(1)]
def search_subject(subjects_list, subject_name):
    return list(filter(lambda subject: subject['предмет'] == subject_name, subjects_list))
def search_section(section_list, subject_name):
    return list(filter(lambda section: section['секція'] ==  subject_name, section_list))
subjects_list = input_subjects()
section_list = input_section()
while True:
    ans = input('Do you want to search {y/n}?')
    if ans =='n':
        break
    subject_name = input('Предмет для пошуку: ')
    subjects_res = search_subject(subjects_list, subject_name) or search_section(section_list, subject_name)
    if len(subjects_res) > 0:
        print(subjects_res)
    else:
        print('No subject')