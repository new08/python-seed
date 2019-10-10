##Filesystem structure of a Python project

### Do

+ name the directory something related to your project. For example, if your project is named "Twisted", name the top-level directory for its source files Twisted. When you do releases, you should include a version number suffix: Twisted-2.5.   
+ create a directory Twisted/bin and put your executables there, if you have any. Don't give them a .py extension, even if they are Python source files. Don't put any code in them except an import of and call to a main function defined somewhere else in your projects. (Slight wrinkle: since on Windows, the interpreter is selected by the file extension, your Windows users actually do want the .py extension. So, when you package for Windows, you may want to add it. Unfortunately there's no easy distutils trick that I know of to automate this process. Considering that on POSIX the .py extension is a only a wart, whereas on Windows the lack is an actual bug, if your userbase includes Windows users, you may want to opt to just have the .py extension everywhere.)   
+ If your project is expressable as a single Python source file, then put it into the directory and name it something related to your project. For example, Twisted/twisted.py. If you need multiple source files, create a package instead (Twisted/twisted/, with an empty Twisted/twisted/__init__.py) and place your source files in it. For example, Twisted/twisted/internet.py.   
+ put your unit tests in a sub-package of your package (note - this means that the single Python source file option above was a trick - you always need at least one other file for your unit tests). For example, Twisted/twisted/test/. Of course, make it a package with Twisted/twisted/test/__init__.py. Place tests in files like Twisted/twisted/test/test_internet.py.
+ dd Twisted/README and Twisted/setup.py to explain and install your software, respectively, if you're feeling nice.   





