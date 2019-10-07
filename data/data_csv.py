import obd
import csv

connection = obd.OBD()
fieldnames = []
try:
    with open('data.csv', 'w') as csvfile:
        for cmd in obd.commands[1]:
            fieldnames.append(cmd.name)
        for cmd in obd.commands[2]:
            fieldnames.append(cmd.name)
        for cmd in obd.commands[3]:
            fieldnames.append(cmd.name)
        writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)
        row = {}
        writer.writeheader()
        while True:
            for n in range(0x01, 0x5F):
                response = connection.query(obd.commands[1][n])
                row[fieldnames[n]] = response.value
                print(response.value)
            writer.writerow(row)
except KeyboardInterrupt:   
    connection.close()
connection.close()