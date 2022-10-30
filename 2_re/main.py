from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8',) as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

dict_names = {}
dict_dubl_names = {}

for x in contacts_list:
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
  if surname not in dict_names.keys():
    dict_names[surname] = x[1:]
  else:
    dict_dubl_names[surname] = x[1:]


for key, value in dict_names.items():
  for key_t, value_t in dict_dubl_names.items():
    if key == key_t:
      if len(value_t[0]) > len(value[0]):
        value[0] = value_t[0]
      if len(value_t[1]) > len(value[1]):
        value[1] = value_t[1]
      if len(value_t[2]) > len(value[2]):
        value[2] = value_t[2]
      if len(value_t[3]) > len(value[3]):
        value[3] = value_t[3]
      if len(value_t[4]) > len(value[4]):
        value[4] = value_t[4]
      if len(value_t[5]) > len(value[5]):
        value[5] = value_t[5]

done_list = []
list_first = []

for key, value in dict_names.items():
  list_first = []
  list_first.append(key)
  for values in value:
    list_first.append(values)
  done_list.append(list_first)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(done_list)




# информация для себя по данным
# value[0] - name
# value[1] - patr
# value[2] - organiz
# value[3] - position
# value[4] - phone
# value[5] - email
