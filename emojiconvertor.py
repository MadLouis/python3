message =input(">")
words = message.split(' ')
emojis = {
    ':)': '😀',
    ':(': '😂'
}
output = ''
for word in words:
    output += emojis.get(word,word) + ' ' #加空格' ' 
print(output)

