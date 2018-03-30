# -*-coding:UTF-8-*-

"""
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
Draws the string at the given position.
Parameters:
xy – Top left corner of the text.
text – Texta to be drawn. If it contains any newline characters, the text is passed on to mulitiline_text()
fill – Color to use for the text.
font – An ImageFont instnce.
1、坐标（0,0）表示左上角，img.size是一个二元组，分别为图片的宽和高
2、ImageFont的获取有很多方法，从truetype中获取的路径“/usr/share/font”
"""

from PIL import Image, ImageFont, ImageDraw


class DrawString(ImageDraw.ImageDraw):
	
	def drow_num(self, size):
		numfont = ImageFont.truetype('C:\WINDOWS\Fonts\Arial.ttf', size=30)
		fillcolor = "#ff0000"
		width, height = size
		self.text((width - 30, 5), '1', font=numfont, fill=fillcolor)
	
if __name__ == "__main__":
	image = Image.open('0000.jpg')
	drawnum = DrawString(image)
	drawnum.drow_num(image.size)
	image.save('result.jpg', 'JPEG')
	image.show()
