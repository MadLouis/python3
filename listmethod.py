# num = [1,2,3,4,5,6]
# num.insert(2,20)
# print(num)
# num.pop() ----- to eliminate the first and last elements from the list
# num.index() ------ to show the first occurance of this item
# print(50 in num) ------ to obtain the boolean value which is False
# num.count()  ---------- to count how many the certain elements in the list
# num.sort() ----------- to sort your list with ascending order and wont return value into print function
# num.reverse() --------- to sort your list with descending order
# num.copy()  ---------- to copy another independent list with original list

# exercise --- write a program to remove the duplicates in a list
list1 = [1,2,3,4,5,6,7,8,9,2,4,5,2,3,5,6,7,8,2,2,0]
#uniques = []
#for num in list:
    #if num not in uniques:
        #uniques.append(num)
#print(uniques)
print(list(set(list1))) # set() 



