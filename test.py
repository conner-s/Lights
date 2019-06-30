import flux_led
from PySide2 import QtWidgets
from ui import ui

bulb_scanner = flux_led.BulbScanner()

class qtUI(ui.Ui_MainWindow, QtWidgets.QMainWindow):
        def __init__(self):
            super(qtUI, self).__init__()
            self.setupUi(self)

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
           bulb_scanner.scan()
           print(bulb_scanner.found_bulbs)

       elif int(userchoice) == 0:
           break

def gui_lights():
    app = QtWidgets.QApplication()
    lights_window = qtUI()
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
