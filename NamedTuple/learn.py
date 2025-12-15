from collections import namedtuple


# color = (55, 155, 255)
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(red=55, green=155, blue=255)
print(color[0])
print(color.red)
