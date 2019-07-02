import flux_led
from PySide2 import QtWidgets
from ui import ui

bulb_scanner = flux_led.BulbScanner()


class QtUi(ui.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(QtUi, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("Python Lights")
		self.active_bulb = None

		# button function connection
		self.rgb_enter.clicked.connect(self.get_user_rgb)
		self.set_light.clicked.connect(self.connect_bulb)
		self.set_white_button.clicked.connect(self.set_white)
		self.set_red_button.clicked.connect(self.set_red)
		self.lights_on_button.clicked.connect(self.set_light_on)
		self.lights_off_button.clicked.connect(self.set_light_off)
		self.bright_lights_button.clicked.connect(self.brighten_light)
		self.dim_lights_button.clicked.connect(self.dim_light)


		found_bulbs = bulb_scanner.scan(3)
		if found_bulbs is not None:
			# Populates list with bulbs on the network
			for e in found_bulbs:
				item = QtWidgets.QListWidgetItem(self.light_list)
				bulb_ip = str(e)[12:25]
				item.setText(bulb_ip)

	# connects to selected bulb in list
	def connect_bulb(self):
		if self.light_list.selectedItems is not None:
			selected_item = self.light_list.selectedItems()
			bulb_ip = selected_item[0].text()
			self.active_bulb = flux_led.WifiLedBulb(bulb_ip)

	# execute when rgb_enter button is pressed
	def get_user_rgb(self):
		if self.active_bulb is not None:
			u_red = self.r_value.text()
			u_green = self.g_value.text()
			u_blue = self.b_value.text()
			if u_red is not None and u_green is not None and u_blue is not None:
				self.active_bulb.setRgb(int(u_red), int(u_green), int(u_blue))

	def set_white(self):
		if self.active_bulb is not None:
			self.active_bulb.setRgb(255, 255, 255)

	def set_red(self):
		if self.active_bulb is not None:
			self.active_bulb.setRgb(255, 0, 0)

	def set_light_on(self):
		if self.active_bulb is not None:
			self.active_bulb.turnOn()

	def set_light_off(self):
		if self.active_bulb is not None:
			self.active_bulb.turnOff()

	def brighten_light(self):
		if self.active_bulb is not None:
			rgbw = self.active_bulb.getRgbw()
			if rgbw[3]+5 < 255:
				self.active_bulb.setRgbw(rgbw[0], rgbw[1], rgbw[2], rgbw[3]+5)

	def dim_light(self):
		if self.active_bulb is not None:
			rgbw = self.active_bulb.getRgbw()
			if rgbw[3] - 5 > 0:
				self.active_bulb.setRgbw(rgbw[0], rgbw[1], rgbw[2], rgbw[3] - 5)


def cli_lights():
	bulb = []
	while True:
		print("================= \n"
			  "Lights App CLI Interface \n"
			  "\n"
			  "1: Lights On \n"
			  "2: Lights off \n"
			  "3: Lights to 5% \n"
			  "4: Lights to 100% \n"
			  "5: Set Lights IP \n"
			  "6: Scan Network Devices \n"
			  "0: Exit\n")
		userchoice = input("Please enter your choice: ")
		if userchoice == "":
			print("Please enter a selection... fucker")

		elif int(userchoice) == 1:
			active_bulb.turnOn()
			print("Lights On")

		elif int(userchoice) == 2:
			active_bulb.turnOff()
			print("Turning Off")

		elif int(userchoice) == 3:
			adjust_brightness(active_bulb, 5)

		elif int(userchoice) == 4:
			adjust_brightness(active_bulb, 100)

		elif int(userchoice) == 5:
			ip = input("Please enter the bulbs IP: ")
			active_bulb = flux_led.WifiLedBulb(ip)
			active_bulb.connect()

		elif int(userchoice) == 6:
			bulb_scanner.scan(3)
			print(bulb_scanner.found_bulbs)

		elif int(userchoice) == 0:
			break


def gui_lights():
	app = QtWidgets.QApplication()
	lights_window = QtUi()
	lights_window.show()
	app.exec_()


def adjust_brightness(bulb, brightness):
	rgb = bulb.getRgb()
	bulb.setRgbw(rgb[0], rgb[1], rgb[2], 255, True, brightness)


if __name__ == "__main__":
	print("1: CLI")
	print("2: GUI")
	ui_choice = input("Please enter the kind of UI you'd like")
	if int(ui_choice) == 1:
		cli_lights()
	elif int(ui_choice) == 2:
		gui_lights()
