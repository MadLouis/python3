"""
f  = lambda x: x*2
print(f(6))
"""

#def get_popu(country):
    #return country[2]   # can be replaced by lambda method 

countries = []
file = open("countries_zh.csv","r")
for line in file:
    line = line.strip()  # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    arr = line.split(",")
    name = arr[1]
    capt = arr[3]
    popu = int(arr[4])
    countries.append((name, capt, popu))

# countries.sort()  # 按首字母排序
countries.sort(key = lambda country: country[2], reverse = True)

for country in countries:
    print(country)