import obd
connection = obd.OBD()
print(connection.status())
print(connection.protocol_name())

# ID	Name
# "1"	SAE J1850 PWM
# "2"	SAE J1850 VPW
# "3"	AUTO, ISO 9141-2
# "4"	ISO 14230-4 (KWP 5BAUD)
# "5"	ISO 14230-4 (KWP FAST)
# "6"	ISO 15765-4 (CAN 11/500)
# "7"	ISO 15765-4 (CAN 29/500)
# "8"	ISO 15765-4 (CAN 11/250)
# "9"	ISO 15765-4 (CAN 29/250)
# "A"	SAE J1939 (CAN 29/250)