import os
from datetime import datetime


print(os.getcwd())
# print(dir(os))
os.mkdir("OS-DEMO-2")
print(os.listdir())

os.rmdir("OS-DEMO-2")
# os.makedirs() makedir is good for deep creating subdirs
print(os.listdir())
# os.mkdir("OS-DEMO-3")
print(os.listdir())

# os.rename("osmamodule.py", "osmanmodule.py")
# os.rmdir("osmamodule.py")


print(os.stat("osmanmodule.py").st_size)
time = os.stat("osmanmodule.py").st_mtime
print(datetime.fromtimestamp(time))
