# Indexing(positive & negative)

my_list =["python" , "java" , "c++"]
print(my_list[1])                        # output=java
print(my_list[0])                        # python
print(my_list[-1])                       # c++


# Slicing #
numbers = [10,20,30,40,50]  # OUTPUT
print(numbers[1:4])         #[20,30,40]
print(numbers[:3])          #[10,20,30] (FROM start)
print(numbers[2:])          #[30,40,50]  (to end)
print(numbers[-3:-1])       #[30,40]
print(numbers[::-1])        #[50,40,30,20,10] (rverse)


# 2.____________MODIFYING LIST_____________
# Changing element
numbers = [10,20,30,40]
numbers[2] = 100         # OUTPUT
print(numbers)           # [10,20,100,40]

# Adding elements
numbers.append(50)
numbers.insert(1 , 15)        # OUTPUT
numbers.extend([60,70,80])    # [10,15,20,100,40,50,60,70,80]
print(numbers)


# Remove elements
numbers.remove(100)
numbers.pop(2)
numbers.pop()
del numbers[1]
numbers.clear()

#__________LIST METHODS___________
# example
numbers =[1,2,3,4,5]
print(numbers.count(1))
print(numbers.index(4))         # OUTPUT
numbers.sort()                  # 1
print(numbers)                  # 3
numbers.reverse()               # [1,2,3,4,5]
print(numbers)                  # [5,4,3,2,1]


#________LOOP_________________
# For loop
fruits =["apple" , "mango" , "banana"]
for fruits in fruits:
    print(fruits)
    
    
    # while loop
    i = 0
    while i < len(fruits):
        print(fruits[i])
        i += 1
        
        # sorting and reversing
        numbers = [5,3,8,2]
        numbers.sort()
        numbers.sort(reverse=True)
        numbers.reverse()