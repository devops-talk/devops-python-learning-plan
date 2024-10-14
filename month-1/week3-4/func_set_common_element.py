# Find Common Elements

# Description: Write a function common_elements(set1, set2) that returns the intersection of two sets set1 and set2.
# Example: common_elements({1, 2, 3}, {2, 3, 4}) should return {2, 3}.

def common_elements(set1, set2):
    common_items = set1.intersection(set2)
    return common_items





set_str1=input("eneter your ste value like {1,2,3,4,5}: ")
set_str2=input("eneter your ste value like {1,2,3,4,5}: ")

set1=eval(set_str1)
set2=eval(set_str2)


find_common=common_elements(set1,set2)

print(f"common element in both sets are {find_common}")