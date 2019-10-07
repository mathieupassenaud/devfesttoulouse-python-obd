import obd
connection = obd.OBD()

response = connection.query(obd.commands.GET_DTC)
print(response)

connection.close()