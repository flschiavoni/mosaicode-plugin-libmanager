#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the LibManagerMenu class.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from mosaicode.model.plugin import Plugin
from mosaicode_plugin_libmanager.control.libmanagercontrol import LibManagerControl
import gettext

_ = gettext.gettext

class LibManagerMenu(Gtk.Menu, Plugin):
    """
    This class contains methods related the LibManagerMenu
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        """Constructor."""
        Gtk.Menu.__init__(self)
        self.label = "Library Manager"
        self.control = None


    def load(self, main_window):
        self.control = LibManagerControl(main_window)
        main_window.menu.create_menu(_("Code Template Manager"), None,
                   self, self.control.code_template_manager)
        main_window.menu.create_menu(_("Block Manager"), None,
                   self, self.control.block_manager)
        main_window.menu.create_menu(_("Port Manager"), None,
                   self, self.control.port_manager)
        self.append(Gtk.SeparatorMenuItem())
        export_blocks = main_window.menu.create_menu(_("Export As..."), None, self, None)
        export_blocks_menu = Gtk.Menu()
        export_blocks.set_submenu(export_blocks_menu)
        main_window.menu.create_menu(_("Python"), None, export_blocks_menu, self.control.export_python_dialog)
        main_window.menu.create_menu(_("XML"), None, export_blocks_menu, self.control.export_xml_dialog)

        menu_item = Gtk.MenuItem("Edit Block")
        menu_item.connect("activate", self.control.edit_clicked)

        main_window.block_menu.append(menu_item)
