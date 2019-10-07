import obd
connection = obd.OBD()

response = connection.query(obd.commands.CLEAR_DTC)

print(response)

connection.close()