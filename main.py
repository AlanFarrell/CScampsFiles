#FIRST  SET OF IMPORTS
from sgp4.api import Satrec, jday
from datetime import datetime, timezone

from plot_groundtracks import plot_satellites
from ConvertCoordinates import coordinateCovert


def main():
    #==================================BLOCK 1 START
    with open("Starlink.tle") as tleFile:
        satellitesData = []
        for line in tleFile:
            if line.strip(): #CHECKS IF THERE IS CONTENT IN THAT LINE
                satellitesData.append(line.strip())
    #==================================BLOCK 1 END


    #==================================TEMP BLOCK, REMOVE AFTER USED
    #for sats in satellitesData:
        #print(sats)
    #==================================



    # ================================== BLOCK 2
    Organised_data = []  # DO THIS AFTER WHILE BLOCK
    i = 0
    while i < len(satellitesData):
        if satellitesData[i].startswith("1"):
            name = f"SAT-{i}"
            line1 = satellitesData[i]
            line2 = satellitesData[i+1]
            i += 2
        else:
            name = satellitesData[i]
            line1 = satellitesData[i+1]
            line2 = satellitesData[i+2]
            i += 3
        Organised_data.append([name, line1, line2])
    # ==================================BLOCK 2 END


    #==================================TEMP BLOCK, REMOVE AFTER USED
    for sats in Organised_data:
        print(sats)
    #==================
