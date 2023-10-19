from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

# Выбор изображения
images = ['Том пытается не спать.jpg', 'Том подбирает код.jpg', 'Кот в ресторане.png', 'Кот в очках.png', 'Джерри смеется.jpg']
print('Картинки для мема: ')
for i in range(len(images)):
    print(f'{i}: ', images[i])
selected_image = int(input('Выберите номер картинки: '))

# Ввод текста
text_type = int(input("Введите 1, если нужен только нижний текст, 2, если и верхний, и нижний, 3 если только верхний: "))
top_text = ''
bottom_text = ''
if text_type == 1:
    bottom_text = input()
elif text_type == 2:
    top_text = input()
    bottom_text = input()
elif text_type == 3:
    top_text = input()

# Основные расчеты с изображением
image = Image.open(f'{images[selected_image]}')
draw = ImageDraw.Draw(image)
width, height = image.size
font = ImageFont.truetype("arial.ttf", size=height*0.1)

# Вывод текста на изображение
ts = draw.textbbox((0, 0), top_text, font)
draw.text(((width - ts[2])/2, height//100 - ts[1]), top_text, font=font, fill="black")
ts = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - ts[2])/2, (height - ts[3]) - height//100), bottom_text, font=font, fill="black")

image.save("meme.png")