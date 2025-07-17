for i in range(2,20,2):
    # if i ==17:
    # break
    print(i)
    
    
    l=["smartphone", "laptop", "tablet"]
    for i in l:
        if i == "smartphone":
            break
            print(i.center(20,"_"))
        else:
            print("end of the item")
            
            
            bullets=10
            while bullets>0:
                if bullets == 5:
                    print("bead")
                break
            print(f"{bullets} are left-you can shoot()")
            bullets -= 1
        else:
            print("gaame over")
            
            
            
            data = {
                1:{"product": "rice",  "price": 60},
                2:{"product:" "wheat", "price": 45},
                3:{"product:" "sugar", "price": 34},
                4:{"product:" "milk", "price": 60},
                5:{"product:" "egg", "price": 55},
                6:{"product:" "cooking", "price": 35},
                7:{"product:" "tea powder", "price": 40},
                8:{"product:" "salt", "price": 45},
                9:{"product:" "bread", "price": 70},
                10:{"product:" "soap", "price": 30},
            }
            
            print("data")
    for i in range(1,11):
        print(f'{i}.{data[i]["name"].ljust(20, " ")}:{data[i]["price"]}')
            