import re

text =''
file = open('poem.txt')
for line in file:
    text = text +line
file.close()

#result = re.findall('a..',text)   # '.' represents any character in re
result = re.findall(' (a[a-z][a-z]) |(A[a-z][a-z]) ',text) # () select the specific part excluding the space

final_result = []
for pair in result:
    if pair[0] not in final_result:
        final_result.append(pair[0])
    if pair[1] not in final_result:
        final_result.append(pair[1])

final_result.remove('')
print(set(final_result))
