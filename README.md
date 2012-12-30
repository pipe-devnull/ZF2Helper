ZF2Helper
=========
           _                      _                        _ _ 
     _ __ (_)_ __   ___        __| | _____   ___ __  _   _| | |
    | '_ \| | '_ \ / _ \_____ / _` |/ _ \ \ / / '_ \| | | | | |
    | |_) | | |_) |  __/_____| (_| |  __/\ V /| | | | |_| | | |
    | .__/|_| .__/ \___|      \__,_|\___| \_/ |_| |_|\__,_|_|_|
    |_|     |_|   


Introduction
=============

Sublime Text 2 Plugin:  Zend Framework 2 (ZF2) Helper

The ZF2 Helper provides some useful functions to speed up the development of ZF2 applications.  It adds options to both the side bar menu and the edit are context menu.  

Current Features:

* Create a new ZF2 module which will include:
** Module directory structure
** Module config
** Module Bootstrap
** Standard template Controller
** Standard template view file
* Create a new ZF2 Controller action

Installation
===============


1. Using git

clone this project directly into the SublimeText 2 packages directory.  On Linux systems this can usually be found in "~/.config/sublime-text-2/Packages"


How to use 
============

_Create a new ZF2 Module_:

Create an entirely new ZF2 module with 1 click rather than copying, pasting, renaming all files individually. Much quicker:)

- In the side bar, right click in the modules folder and select "ZF2 Helper" -> "New ZF2 Module"
- Input the name of the new module
- Add the name of the module into the main ZF2 Application configuration file

_Create a new ZF2 Controller Action:

Adds sample MVC action code into the controller file and created a new view file in the view directory.

- Open up a ZF2 MVC controller file
- Right click in the file where you want to add a new action.
- Select "ZF2 - New Controller Action"
- Enter the name of the action in the prompt


