import sys
import flux_led


bulb_scanner = flux_led.BulbScanner()


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

       elif int(userchoice) == 5:
           ip = input("Please enter the bulbs IP: ")
           active_bulb = flux_led.WifiLedBulb(ip)
           active_bulb.connect()

       elif int(userchoice) == 6:

           bulb_scanner.scan()
           print(bulb_scanner.found_bulbs)

       elif int(userchoice) == 0:
           break








if __name__ == "__main__":
    cli_lights()
