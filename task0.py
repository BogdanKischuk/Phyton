from random import randint 
 
 
def rand_arr(): 
    RArr = [] 
    for i in range(0, 30): 
        RArr.append(randint(-100, 100)) 
    return RArr 
 
 
def max_in_arr(arr): 
 
    arr_i = list(enumerate(arr, 0)) 
    max_i = max(arr_i, key=lambda i: i[1]) 
 
    return max_i[1], max_i[0] 
 
 
def unpaired_arr(arr): 
    un_p_arr = [] 
    for i in arr: 
        if i % 2 != 0: 
            un_p_arr.append(i) 
    if len(un_p_arr) == 0: 
        return "no unpaired numbers" 
    else: 
        return un_p_arr 
 
 
arr = rand_arr() 
print("initial random list :\n", arr) 
print("max num > ", max_in_arr(arr)[0], "\nposition of max num > ", max_in_arr(arr)[1]+1) 
 
# isinstance() проверяет принадлежность объекта к определенному типу данных isinstance(объект,тип данных) 
if isinstance(unpaired_arr(arr), list): 
    print("List of unpaired numbers sorted from highest to lowest :\n", 
          sorted(unpaired_arr(arr), reverse=True)) 
else: 
    print(unpaired_arr(arr))