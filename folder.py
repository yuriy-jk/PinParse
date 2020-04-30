parse_link = 'https://www.pinterest.ru/yuriyjk/1045/'
folder = parse_link[25:].replace('/', '_')
print(folder)

a = 'https://i.pinimg.com/564x/89/f0/92/89f092720e90844c71ff47d63998cc4d.jpg'
b = a.replace('564x', 'originals')
print(b)
