set1 = {(1,2), (3,4), (5,6)}
set2 = {(5,6), (1,2), (3,4)}
print(set2 == set1)
list1 = list(set1)
list2 = list(set2)

def check(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True
print(check(set2, set1))