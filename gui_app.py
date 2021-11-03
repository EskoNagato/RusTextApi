import sys

from api_rus import RusTxtApi
from PyQt5 import QtWidgets
from design import Ui_MainWindow
from qt_material import apply_stylesheet

class RusTxtGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(RusTxtGui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.api = RusTxtApi()

    def init_UI(self):
        self.setWindowTitle('МОЯ ПРОГРАММА')
        self.ui.pb_change.clicked.connect(self.get_syn_txt)
        self.ui.pb_generate.clicked.connect(self.nick_generate)
        self.ui.pb_clear_list.clicked.connect(self.ui.lw_nick.clear)
        self.ui.pb_generate_words.clicked.connect(self.anogram)

    def get_syn_txt(self):
        text = self.ui.te_working_place.toPlainText()
        res = self.api.get_syn_txt(text)
        self.ui.te_working_place.setText(res)
        self.ui.lb_percent_of_unique.setText(self.api.percent_unique)
        self.ui.lb_count_of_replace.setText(str(self.api.count_replace))
        self.ui.lb_count_of_symb.setText(str(self.api.count_symbol))
        self.ui.lb_time.setText(str(self.api.time))

    def nick_generate(self):
        min_count = self.ui.sb_min.value()
        max_count = self.ui.sb_max.value()
        count_nick = self.ui.sb_count_nick.value()
        if min_count >= 3 and max_count > 0 and count_nick > 0:
            res = self.api.get_nickname(count_nick, min_count, max_count)
            self.ui.lw_nick.addItems(res)

    def anogram(self):
        words = self.api.anagram(self.ui.le_letters.text())
        print(words)
        for key in words:
            self.ui.lw_all_words.addItems(words[key])
        self.ui.lw_all_words.sortItems()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    rus_gui = RusTxtGui()
    rus_gui.show()
    apply_stylesheet(app, theme='dark_teal.xml')
    sys.exit(app.exec())
