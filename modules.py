import math
import os
f = open("newfile.txt", "w")
f.write("Hello world")
print(os.getcwd())
os.mkdir("new folder")
print(os.listdir(os.getcwd()))
os.rmdir("new folder")
print(os.listdir(os.getcwd()))
print(os.getlogin())
os.system("dir")
f.close()
os.remove("newfile.txt")



x = -25.9
y = 25.9
print(f"The absolute value of {x + 29} is: " + str(math.fabs(x)))
print(math.fabs("hello"))
print(math.floor(x))
print(math.floor(math.fabs(x)))
print(math.floor(25.9))
print(25)
print(math.floor(y))