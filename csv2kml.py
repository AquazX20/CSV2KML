import csv
import simplekml

def description(*argv):
    """Creates a description block with the arguments of the function"""

    block = ''
    check = 0
    for arg in argv:
        if arg == argv[0] and check == 0:
            block = block + arg
            check = 1
        else:
            block = block + '<BR>' + arg
        
    return block

# Open the CSV file and read its contents
with open(r'D:\aleja\Downloads\cosa\Sample CSV format.csv', 'r', enconding='UTF-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    
    # Create a KML document
    kml = simplekml.Kml()
    
    # Iterate over the rows in the CSV file
    for row in reader:
        # Extract the data for each field in the row
        name = row[1]
        pressure = "Sensor de presion: " + row[2] + "    "  + row[3]
        starter = "Arrancador: " + row[4] + "    "  + row[5]
        flow = "Caudalimetro: " + row[6] + "    "  + row[7]
        power = "Analizador de potencia: " + row[8] + "    "  + row[9]
        switch = "Interruptor de presion: " + row[10] + "    " + row[11]
        rtu = "RTU: " + row[12] + "    "  + row[13]
        modem = "Modem: " + row[14] + "    "  + row[15]
        ID = "ID: " + row[18]
        level = "Sensor de nivel: " + row[19] + "    " + row[20]

        latitude = float(row[16])
        longitude = float(row[17])

        
        # Added function, arguments are data to be placed in description box
        datos = description(name, ID, pressure, starter, flow, power, switch, rtu, modem, level)

        # Add a new point to the KML document
        point = kml.newpoint(name=name, description=datos, coords=[(longitude, latitude)])
        point.style.labelstyle.scale = 1
        point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/water.png'

        
    # Write the KML data to a file
    print(kml.kml())
    kml.save(r'D:\aleja\Downloads\cosa\Output.kml')