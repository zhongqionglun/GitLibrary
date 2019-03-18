# -*-coding:UTF-8-*
from PIL import Image

# 读取Image图片
img = Image.open('0000.JPG')

# 显示Image图片
img.show()

# 旋转Image图片
rotate1 = img.rotate(45)
rotate1.show()

# 旋转90，180或270度时可以使用transpose函数
rotate2 = img.transpose(Image.ROTATE_90)
rotate2.show()

# 翻转Image图片(左右)
flip1 = img.transpose(Image.FLIP_LEFT_RIGHT)
flip1.show()

# 翻转Image图片(上下)
flip2 = img.transpose(Image.FLIP_TOP_BOTTOM)
flip2.show()

# 转换Image图片(灰色)
grey = img.convert('L')
grey.show()

# 读取像素值
print img.getpixel((25, 25))

# 改变像素值
img.putpixel((25, 25), (0, 0, 0))
img.show()

# 裁剪Image图片
box = (20, 20, 100, 100)
region = img.crop(box)
region.show()

# 粘贴图片
img.paste(region, (50, 50))
img.show()

# 生成缩略图
img.thumbnail((100, 100))
img.show()

# 保存Image图片
img.save('thumbnail-0000.JPG', 'JPEG')

# 打印Image信息
print img.format, img.mode, img.size










