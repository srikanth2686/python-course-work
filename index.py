data = {
                1:{"product": "rice",  "price": 60},
                2:{"product": "wheat", "price": 45},
                3:{"product": "sugar", "price": 34},
                4:{"product": "milk", "price": 60},
                5:{"product": "egg", "price": 55},
                6:{"product": "cooking", "price": 35},
                7:{"product": "tea powder", "price": 40},
                8:{"product": "salt", "price": 45},
                9:{"product": "bread", "price": 70},
                10:{"product": "soap", "price": 30},
            }
            
for i in range(1, 11):
        print(f'{i}.{(data[i]["name"]).ljust(20, " ")}:{data[i]["price"]}')
items=list(map(int,input("Enter the items indexes:").split()))
total=0
ids=set()
for i in items:
    if i not in ids:
                           co=items.count(i)
                           total += data[i]["price"] * co
                           print(f"{data[i]["product"].ljust(20, " ")}  {co} {data[i]['price']} {total}")
                           ids.add(i)
                           
            