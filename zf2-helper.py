'''
Sublime Text 2 Zend Framework Helper Plugin

Copyright (c) 2012 Adrian Bruce <ade@pipe-devnull.com>

'''

import sublime
import sublime_plugin
import os
import json
import re


## Create a Zend Framework 2 module structure
class CreatemoduleCommand(sublime_plugin.WindowCommand):

    # Every ST2 plugin must have a run method, we pass the current path to it
    def run(self, paths):
        self.base_path = paths[0]
        self.window.show_input_panel("Module Name:", "", self.on_done, None, None)

    # Handle input (module name)
    def on_done(self, text):
        try:
            # todo: validate name with zf2 conventions
            self.modulename = text
            self.create_zf2_module_structure()

        except ValueError:
            pass

    # Create ZF2 Module
    def create_zf2_module_structure(self):
        x = open(sublime.packages_path() + "/PHP Zend Framework 2 Helper/zf2-helper/files.json").read()
        x = x.replace('_MODULENAME_', self.modulename)
        x = x.replace('_ROUTENAME_', self.modulename.lower())

        zf2_files = json.loads(x)

        for dirpath in zf2_files['directories']:
            self.create_directory(self.base_path + dirpath)

        # Create some module files to start things off
        self.create_files_from_helper_config()

        sublime.message_dialog("Module '" + self.modulename + "' has been created.  Don't foget to add it to the application config")

    # Create directory
    def create_directory(self, fullpath):
        os.mkdir(fullpath)

    # Mapping of template to module files stored json file
    def create_files_from_helper_config(self):
        x = open(sublime.packages_path() + "/PHP Zend Framework 2 Helper/zf2-helper/files.json").read()
        x = x.replace('_MODULENAME_', self.modulename)
        x = x.replace('_ROUTENAME_', self.modulename.lower())

        zf2_files = json.loads(x)

        for template in zf2_files['files']:
            zf = utility_methods.get_helper_file_contents_as_string(sublime.packages_path(), template, self.modulename)

            f = open(self.base_path + zf2_files['files'][template], 'w+')
            f.write(zf)
            f.close()


# Command to create a new action on ZF2 MVC controller
# Assumes the standard ZF2 project layout
class CreatecontrolleractionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.edit = edit
        # Extract the module name, base path and view file for later use
        # TODO make a generic version in a helper class
        self.viewfile = self.view.file_name()
        self.module_name = os.path.split(self.viewfile)[0].split('/')[-2]
        self.module_base_path = '/'.join(os.path.split(self.viewfile)[0].split('/')[0:-3])

        if (re.match('.*Controller.php$', self.view.file_name())):

            # Get Snippet & inject into a new file
            # sublime.message_dialog(str(self.view.file_name()))
            self.view.window().show_input_panel("Action Name:", "", self.create_action, None, None)

        else:
            sublime.message_dialog("not a controller")

    # Create the action controller view file and controller method
    def create_action(self, action_name):
        # Figure out the view file path
        view_file = self.module_base_path + "/view/" + self.module_name.lower() + "/" + self.module_name.lower() + "/" + action_name + ".phtml"

        zf = open(sublime.packages_path() + "/PHP Zend Framework 2 Helper" + "/zf2-helper/view.phtml.template").read()

        sel = self.view.sel()[0]
        f = open(view_file, 'w+')
        f.write(zf)
        f.close()

        action_code = utility_methods.get_helper_file_contents_as_string(sublime.packages_path(), "/zf2-helper/controller.action.template", self.module_name)
        action_code = action_code.replace('_ACTIONNAME_', action_name)

        # Insert the template action
        self.view.insert(self.edit, sel.end(), action_code)

        # Open the newly created view file
        self.view.window().open_file(view_file)



# Static utility methods for use in all commands
class utility_methods():

    @staticmethod
    def get_helper_file_contents_as_string(sublime_base_path, path, module_name):
        zf = open(sublime_base_path + "/PHP Zend Framework 2 Helper" + path).read()
        zf = zf.replace('_MODULENAME_', module_name)
        zf = zf.replace('_ROUTENAME_', utility_methods.get_routename_from_moduleName(module_name))
        return zf

    # Generate route name from the module name supplied
    @staticmethod
    def get_routename_from_moduleName(module_name):
        # TODO take into account multiple capitals in the module name
        return module_name.lower()
