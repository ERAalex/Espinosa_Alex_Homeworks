from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8',) as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

dict_names = {}

for x in contacts_list:
  dict_dubl_names = {}
  full_name = x[0] + ' ' + x[1] + ' ' + x[2]
  full_name_split = full_name.split(' ')
  x[0] = full_name_split[0]  # x[0] - surname,  text_1[0] - surname
  x[1] = full_name_split[1]  # x[1] - name,  text_1[1] - name
  x[2] = full_name_split[2]  # x[2] - patr,  text_1[2] - patr

  text = x[5]
  pattern = "(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})\s?\(?(\доб.)?(\s+)?(\d+)?"
  result = re.sub(pattern, r"+7(\2)\3-\4-\5\7\6\8", text)


  x[5] = result
  surname = x[0]
  name = x[1]
  # Записываем как ключ и фамилию и имя, т.к. могут быть 1 фамильцы, а так точно исключим наличие родственников:
  keys = surname + ' ' + name

  if keys not in dict_names.keys():
    dict_names[keys] = x[2:]
  else:
    dict_dubl_names[keys] = x[2:]

    for key, value in dict_names.items():
      for key_t, value_t in dict_dubl_names.items():
        if key == key_t:
          if len(value_t[2]) > len(value[2]):
            value[2] = value_t[2]
          if len(value_t[3]) > len(value[3]):
            value[3] = value_t[3]
          if len(value_t[4]) > len(value[4]):
            value[4] = value_t[4]


done_list = []
list_first = []

for key, value in dict_names.items():
  list_first = []
  key_f = key.split(" ")
  list_first.append(key_f[0])
  list_first.append(key_f[1])
  for values in value:
    list_first.append(values)
  done_list.append(list_first)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(done_list)

