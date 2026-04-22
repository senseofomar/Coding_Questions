def distinct_unique_pairs(arr, target)->int:
    res = 0
    seen = {}
    for i in range(len(arr)):
        current = arr[i]
        complement = target - current
        if complement == current:
            if seen.get(complement, 0)==1:
                res+= 1
        elif seen.get(complement, 0) > 0 and seen.get(current
                , 0)== 0:
            res+=1
        seen[current] = seen.get(current, 0) +1
    return res

if __name__=="__main__":
    arr1 = [1,1,2,2,3,4,5,0]
    target1 = 5
    print(distinct_unique_pairs(arr1, target1))





"""
case 1 - when current == complement

if complement == current:
   if seen.get(complement, 0) ==1:
       res+=1
 for 3,3 if target is 6
 
case 2 - current is not equal complement

condition 1 - 
seen.get(compliment, 0) > 0 - have i already seen 
the numbers that pairs with current
condition 2 - seen.get(curent, 0) ==0 - 
is this the first time i am seeing current
      
elif seen.get(complement, 0) >0 and seen.get(current, 0) ==0
       res+= 1
       
seen[current] = seen.get(current, 0) +1
for preventing duplicates 4,1 and 1,4
"""


def uni_pairs(l:list, target:int)->int:

    result = 0
    seen = {}
    for i, num in enumerate(l):
        current = num[i]
        need = target - current
        if current == need:
            if seen.get(need, 0) ==1:
                result+=1
        elif seen.get(need, 0)> 0 and seen.get(current, 0) ==0:
            result+=1
        seen[current] = seen.get(current, 0 )+1
    return result
R = [1,2,3,4,5,6,7,8,9.10,0]
print(uni_pairs(R, 10))



