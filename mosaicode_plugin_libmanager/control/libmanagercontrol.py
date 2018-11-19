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
        Dialog().message_dialog("Exported all extensions as Python classes",
                    "Check " + System.get_user_dir() + "/extensions/",
                    self.main_window)

    # ----------------------------------------------------------------------
    def export_xml_dialog(self):
        self.export_xml()
        Dialog().message_dialog("Exported all extensions as XML",
                    "Check " + System.get_user_dir() + "/extensions/",
                    self.main_window)

    # ----------------------------------------------------------------------
    @classmethod
    def export_xml(cls):
        System()
        LibManagerControl.export_block("xml")
        LibManagerControl.export_port("xml")
        LibManagerControl.export_code_template("xml")

    # ----------------------------------------------------------------------
    @classmethod
    def export_block(cls, output):
        from mosaicode.system import System as System
        System()
        blocks = System.get_blocks()
        for block in blocks:
            path = System.get_user_dir() + "/extensions/"
            path = path + block.language + "/" + block.framework + "/"
            if output == "xml":
                BlockPersistence.save_xml(blocks[block], path)
            else:
                BlockPersistence.save_python(blocks[block], path)

    # ----------------------------------------------------------------------
    @classmethod
    def export_port(cls, output):
        from mosaicode.system import System as System
        System()
        ports = System.get_ports()
        for port in ports:
            path = System.get_user_dir() + "/extensions/"
            path = path + port.language + "/ports/"
            if output == "xml":
                PortPersistence.save_xml(ports[port], path)
            else:
                PortPersistence.save_python(ports[port])

    # ----------------------------------------------------------------------
    @classmethod
    def export_code_template(cls, output):
        from mosaicode.system import System as System
        System()
        code_templates = System.get_code_templates()
        for code_template in code_templates:
            path = System.get_user_dir() + "/extensions/"
            path = path + code_template.language + "/"
            if output == "xml":
                CodeTemplatePersistence.save_xml(code_templates[code_template])
            else:
                CodeTemplatePersistence.save_python(code_templates[code_template], path)

# ----------------------------------------------------------------------
