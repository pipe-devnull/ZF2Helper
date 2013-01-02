
     __________ ____  _   _      _                 
    |__  /  ___|___ \| | | | ___| |_ __   ___ _ __ 
      / /| |_    __) | |_| |/ _ \ | '_ \ / _ \ '__|
     / /_|  _|  / __/|  _  |  __/ | |_) |  __/ |   
    /____|_|   |_____|_| |_|\___|_| .__/ \___|_|   
                                  |_|              


Introduction
=============

Sublime Text 2 Plugin:  Zend Framework 2 (ZF2) Helper

The ZF2 Helper provides some useful functions to speed up the development of ZF2 applications.  It adds options to both the side bar menu and the edit are context menu.  

Current Features:

* Create a new ZF2 module which will include:
    * Module directory structure
    * Module config
    * Module Bootstrap
    * Standard template Controller
    * Standard template view file
* Create a new ZF2 Controller action


Installation
===============


1. Using git

clone this project directly into the SublimeText 2 packages directory.  On Linux systems this can usually be found in "~/.config/sublime-text-2/Packages"


How to use 
============

__Create a new ZF2 Module__:

Create an entirely new ZF2 module with 1 click rather than copying, pasting, renaming all files individually. Much quicker:)

- In the side bar, right click in the modules folder and select "ZF2 Helper" -> "New ZF2 Module"
- Input the name of the new module
- Add the name of the module into the main ZF2 Application configuration file

__Create a new ZF2 Controller Action__:

Adds sample MVC action code into the controller file and created a new view file in the view directory.

- Open up a ZF2 MVC controller file
- Right click in the file where you want to add a new action.
- Select "ZF2 - New Controller Action"
- Enter the name of the action in the prompt


Snippets
============

Plugin includes additional snippets useful for ZF2 development:

* New Action - tab trigger 'action'

License
===============

ZF2Helper is released under the MIT license.

Copyright (c) 2012 Adrian Bruce <ade@pipe-devnull.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Version
===============

* 0.1 - Initial release



  [1]: http://www.sublimetext.com/2
  [2]: http://wbond.net/sublime_packages/package_control