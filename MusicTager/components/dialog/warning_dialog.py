#!/usr/bin/python
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui.ui_source.WarningDialog import Ui_WarningDialog
from components.mask_widget import MaskWidget


class WarningDialog(QDialog, Ui_WarningDialog):
    def __init__(self, parent=None):
        super(WarningDialog, self).__init__(parent)
        self.setupUi(self)
        self.warning_label.setWordWrap(True)

    def set_text(self, msg):
        self.warning_label.setText(msg)
        self.adjustSize()

    def show(self) -> None:
        self._set_mask_visible(True)
        super(WarningDialog, self).show()

    def done(self, a0: int) -> None:
        self._set_mask_visible(False)
        super(WarningDialog, self).done(a0)

    def _set_mask_visible(self, flag: bool):
        if self.parent():
            if not hasattr(self.parent(), "mask_widget"):
                self.parent().mask_widget = MaskWidget(self.parent())
            if flag:
                self.parent().mask_widget.show()
            else:
                self.parent().mask_widget.hide()


if __name__ == "__main__":
    import sys
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = WarningDialog()
    myWin.show()
    sys.exit(app.exec_())


