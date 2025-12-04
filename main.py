from logic import *
from television import *

def main():
    tv = Television()
    application = QApplication([])
    window = Logic(tv)
    window.show()
    application.exec()

if __name__ == "__main__":
    main()