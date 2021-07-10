# pyqt5居中窗口

```Python
import sys

from PyQt5 import QtWidgets


class CentralWidget(QtWidgets.QWidget):
    """  窗口居中示例 """

    def __init__(self):
        super(CentralWidget, self).__init__()
        self.setFixedSize(500, 1000)  # 窗口足够大才会出现不居中的情况
        self.center()

    # def center(self):
    #     qr = self.frameGeometry()
    #     qr.moveCenter(QtWidgets.QDesktopWidget().availableGeometry().center())
    #     self.move(qr.topLeft())

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = CentralWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

```
