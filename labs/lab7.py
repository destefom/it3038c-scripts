from PIL import Image, ImageChops, ImageFilter
image_philo = "C:\Users\Administrator\it3038c-scripts\labs"
p = Image.open(image_philo)

print('image size: ', x.size, ' color mode: ', x.mode)
print('image size: ', y.size, ' color mode: ', y.mode)

#change color scheme
greyscale = image_philo.convert('L')

pixel = image_philo.load()

#changing any pixels that are not white to black
for row in range(image_philo.size[0]):
    for column in range(image_philo[1]):
        if pixel[row, column] != (255,255,255):
            pixel[row, column] = (0,0,0)

#Inverting image
invert = image_philo.invert(greyscale)

#adding a blur
blur = greyscale.filter(ImageFilter.GaussianBlur(radius=1))