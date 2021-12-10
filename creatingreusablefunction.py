def emoji_convertor(message):
    words = message.split(' ')
    emojis = {
        ':)': '😀',
        ':(': '😂'
    }
    output = ''
    for word in words:
        output += emojis.get(word,word) + ' ' #加空格' ' 
    return output


message =input(">")
print(emoji_convertor(message))
