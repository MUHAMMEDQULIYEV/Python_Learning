from collections import namedtuple


# color = (55, 155, 255)
Color = namedtuple("h", ["red", "green", "blue"])
color = Color(55, 155, 255)
print(color[0])
print(color.red)
