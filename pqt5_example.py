import sys
#sistemdeki çalışmalar aktif hale geldi

from PyQt5.QtWidgets import QApplication, QWidget
#pyqt 5 kütüphanesi ve ek paketleri
app = QApplication(sys.argv)
# #sistem içerisindeki tüm argümanlar geldi!
pencere = QWidget()
pencere.resize(500, 500)
pencere.move(700, 100)
pencere.setWindowTitle("Pencere Başlık Kısmı")
pencere.show
