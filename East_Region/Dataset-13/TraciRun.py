import os
import sys
import traci
import traci.constants as tc
import math
import sumolib

#net = sumolib.net.readNet('./2023-06-15-20-27-12/osm.net.xml')
#net = sumolib.net.readNet('./2023-09-27-03-32-07/osm.net.xml')
#net = sumolib.net.readNet('./2023-04-04-16-16-26/osm.net.xml')
#net = sumolib.net.readNet('./2023-09-26-13-57-27/osm.net.xml')
net = sumolib.net.readNet('./osm.net.xml')


if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")


sumoBinary = "C:/Users/Ankita/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/East_Region/East_Region/Dataset-13/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0



#x,y = net.getNode('10189040386').getCoord()
#lon, lat = traci.simulation.convertGeo(x, y)
#print(lon)
#print(lat)

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['33263613','32792553','167610764'])

#Successful Route_2
#traci.vehicle.setRoute('veh0',['652412711','32792553','167610764','780407737'])

#Successful Route_3
#traci.vehicle.setRoute('veh0',['626072444','780407738','633182132','265150738','652412711'])

#Successful Route_4
#traci.vehicle.setRoute('veh0',['265150818','174402285'])





#f = open('Road_Trace_169195795#0_1.txt','w')
#f.write("169195795#0" + "\n")

#traci.vehicle.setRoute('veh0',['1126237668#0','340498982#0'])
#traci.vehicle.setRoute('veh0',['169195795#0','169195795#2','114667396#0'])
#traci.vehicle.setRoute('veh0',['169195795#0','169195795#2','114667396#0'])

#traci.vehicle.setRoute('veh0',['169195795#0'])
#traci.vehicle.setRoute('veh0',['340498982#0'])

#traci.vehicle.setRoute('veh0',['169195795#0'])

#f = open("ActualVehicleTrace.txt","w")

step = 0
while step < 250:
    traci.simulationStep()
    sampling_time = traci.simulation.getTime()
    print(sampling_time)

    vehicles = traci.vehicle.getIDList()  
    #if step <=100:
    for i in range(0, len(vehicles)):
        traci.vehicle.setSpeed(vehicles[i], 10) 
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
        #print(dist)
        #print(traci.simulation.getTime())
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + "\n")

    #if step == 80:
    #    traci.vehicle.moveToXY('veh0','169195795#0','169195795#0_0',224.18,43.25,angle=85,keepRoute=1,matchThreshold=100)
    
    step += 1


#f.close()

traci.close()
