import os
import sys
import traci
import traci.constants as tc
import math
import sumolib

net = sumolib.net.readNet('./osm.net.xml')


if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")


sumoBinary = "C:/Users/Ankita/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/East_Region/East_Region/Dataset-15/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_153.txt","w")

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['304172621','85649521','223870425','223870421'])

#Successful Route_2
#traci.vehicle.setRoute('veh0',['660416278','660416279','471641535','471641531','223870426','74741535'])

#Successful Route_3
#traci.vehicle.setRoute('veh0',['85650318','649059863','728077853','223870423','223870418'])



step = 0
while step < 300:
    traci.simulationStep()
    sampling_time = traci.simulation.getTime()
    print(sampling_time)

    vehicles = traci.vehicle.getIDList()  
    if step%1 == 0:
        for i in range(0, len(vehicles)):
            traci.vehicle.setSpeed(vehicles[i],10) 
            print(traci.vehicle.getSpeed(vehicles[i]))
            speed = traci.vehicle.getSpeed(vehicles[i])
            print("Speed of the ", vehicles[i], "is : ", traci.vehicle.getSpeed(vehicles[i]))
            past_lat = lat
            past_long = lon
            #print("Position",traci.vehicle.getPosition(vehicles[i]))
            angle = traci.vehicle.getAngle(vehicles[i])
            print("Angle",angle)
            x, y = traci.vehicle.getPosition(vehicles[i])
            lon, lat = traci.simulation.convertGeo(x, y)
            print(lon,lat)
            dist = math.sqrt((past_lat-lat)*(past_lat-lat) + (past_long-lon)*(past_long-lon))
            f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        #print(dist)
        #print(traci.simulation.getTime())
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + "\n")

    #if step == 80:
    #    traci.vehicle.moveToXY('veh0','169195795#0','169195795#0_0',224.18,43.25,angle=85,keepRoute=1,matchThreshold=100)
    
    step += 1


f.close()

traci.close()
