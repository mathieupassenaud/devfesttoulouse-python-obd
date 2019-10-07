import obd

connection = obd.OBD()

response = connection.query(obd.commands.COOLANT_TEMP)
print(response.value) 
connection.close()