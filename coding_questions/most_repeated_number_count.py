

def most_repeated_number_count(nums:list)->int:
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) +1
    return max(counter.values())

"""
max(counter.values()) - gives the count
max(counter, key= counter.get) - gives the number
"""

if __name__ =="__main__":
    nums1 = [1,3,4,1,2,2,2]
    print(most_repeated_number_count(nums1))



def most_repeated(numbers:list)-> int:
    counting = {}
    for n in numbers:
        counting[n] = counting.get(n, 0) +1
    return max(counting.values())


def most_repeating(numb):
    rep ={}
    for n in numb:
        rep[n] = rep.get(n, 0)+1
    return max(rep.values())