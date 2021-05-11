import pandas as pd
ui_data = pd.read_excel('test.xlsx')
ui_data['result_id'] = ""
id_dict = {}
count = 2
row = 0

# Creating a Dictionary for unique values as key and a number as value
for cell in ui_data['Detail']:
    if id_dict.get(cell):
        pass
    else:
        id_dict[cell] = count 
        count = count + 1
# Assigning the values from Dictionary to New Column
for index, row in ui_data.iterrows():
    if row['Detail'] in id_dict:
        ui_data.loc[index, 'result_id'] = id_dict[row['Detail']]

#views the head for Detail
ui_data['Detail'].head

#prints the created dictionary
print (id_dict)
