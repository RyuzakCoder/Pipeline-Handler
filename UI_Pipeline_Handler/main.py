import sys

from PyQt5.QtWidgets import QApplication

from Pipeline_Handler import *


def main():

	app = QApplication(sys.argv)

	pipeline_handler = Pipeline_Handler()

	pipeline_handler.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()