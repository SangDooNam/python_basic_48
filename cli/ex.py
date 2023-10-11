from datetime import datetime as dt, timedelta as td
from data import stock
# date = '2021-07-18 02:35:27'

# datetime_ob = dt.strptime(date, "%Y-%m-%d %H:%M:%S")

# print(date)

# differenz = dt.today() - datetime_ob

# print((dt.today() - datetime_ob).days)


# empty = []
# for dct in stock:
    
#     empty.append(dct['date_of_stock'])
    
# print(empty)

# total = 0
# empty = []
# for i in stock:
    
#     if 'category' in i:
        
#         empty.append(i['category'])
        
# print(list(set(empty)))
        
# count = 0
# for i in stock:
    
#     for key, value in i.items():
        
#         if key == 'category' and value =='Headphones':
            
#             count += 1
#             print(f'{value} ({count})')
# print(count)


product_counter = {}
product_dct = {}
for dct in stock:
    
    product = dct['category']
    
    if product in product_counter:
        product_counter[product] += 1
        
    else:
        product_counter[product] = 1
        
counter = 1
    
for key_counter, value in product_counter.items():
    
    product_dct[counter] = key_counter + ' ' + (str(value))
    counter += 1

print(product_dct)