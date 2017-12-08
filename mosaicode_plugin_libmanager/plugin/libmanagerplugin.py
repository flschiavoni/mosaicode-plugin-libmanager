#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the LibManagerMenu class.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from mosaicode.model.plugin import Plugin
from mosaicode_plugin_libmanager.GUI.libmanagermenu import LibManagerMenu
from mosaicode_plugin_libmanager.GUI.blockmenuitem import BlockMenuItem
import gettext

_ = gettext.gettext

class LibManagerPlugin(Plugin):
    """
    This class contains methods related the LibManagerMenu
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor."""
        self.label = "Library Manager"

    # ----------------------------------------------------------------------
    def load(self, main_window):
        menu = LibManagerMenu(main_window)
        main_window.menu.add_menu_category(self.label, menu)

        menu_item = BlockMenuItem(main_window)
        main_window.block_menu.append(menu_item)
