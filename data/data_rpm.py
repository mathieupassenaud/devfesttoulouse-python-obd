import obd

connection = obd.OBD()
try:
    while True:
        response = connection.query(obd.commands.RPM)
        print(response.value)
except KeyboardInterrupt:   
    connection.close()
connection.close()