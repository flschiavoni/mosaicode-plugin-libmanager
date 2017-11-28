#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the LibManagerControl class.
"""

from mosaicode.control.maincontrol import MainControl
from mosaicode.system import System as System
from mosaicode.control.portcontrol import PortControl
from mosaicode.control.blockcontrol import BlockControl
from mosaicode.control.codetemplatecontrol import CodeTemplateControl
from mosaicode.GUI.dialog import Dialog
from mosaicode_plugin_libmanager.GUI.blockcodeeditor import BlockCodeEditor
from mosaicode_plugin_libmanager.GUI.blockeditor import BlockEditor
from mosaicode_plugin_libmanager.GUI.blockmanager import BlockManager
from mosaicode_plugin_libmanager.GUI.codetemplateeditor import CodeTemplateEditor
from mosaicode_plugin_libmanager.GUI.codetemplatemanager import CodeTemplateManager
from mosaicode_plugin_libmanager.GUI.porteditor import PortEditor
from mosaicode_plugin_libmanager.GUI.portmanager import PortManager

import gettext
_ = gettext.gettext

class LibManagerControl(object):
    """
    This class contains methods related the LibManagerControl.
    """
    # ----------------------------------------------------------------------

    def __init__(self, main_window):
        """Constructor."""
        self.main_window = main_window

    # ----------------------------------------------------------------------
    def code_template_manager(self):
        """
        This add a new Code Template.
        """
        CodeTemplateManager(self.main_window)

    # ----------------------------------------------------------------------
    def block_manager(self):
        """
        This add a new Block.
        """
        BlockManager(self.main_window)

    # ----------------------------------------------------------------------
    def port_manager(self):
        """
        This add a new port.
        """
        PortManager(self.main_window)

    # ----------------------------------------------------------------------
    @classmethod
    def export_extensions(cls, extension):
        if extension == 'py':
            self.export_python()
        else:
            self.export_xml()

    # ----------------------------------------------------------------------
    @classmethod
    def export_python(cls):
        System()
        BlockControl.export_python()
        PortControl.export_python()
        CodeTemplateControl.export_python()

    # ----------------------------------------------------------------------
    def export_python_dialog(self):
        self.export_python()
        Dialog().message_dialog("Exporting as python", "Exported successfully!", self.main_window)

    # ----------------------------------------------------------------------
    @classmethod
    def export_xml(cls):
        System()
        BlockControl.export_xml()
        PortControl.export_xml()
        CodeTemplateControl.export_xml()

    # ----------------------------------------------------------------------
    def export_xml_dialog(self):
        self.export_xml()
        Dialog().message_dialog("Exporting as xml", "Exported successfully!", self.main_window)

    # ----------------------------------------------------------------------
    def edit_clicked(self, args):
        """
        This method monitors if the button delete was clicked.

            Parameters:
            * **args**

        """

        BlockEditor(self.main_window,
                System.blocks[self.main_window.main_control.get_selected_block().type])

# ----------------------------------------------------------------------
