# usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan

print('\033[1;32m This program will help you debug a hardstop due to an object that is too close to LiDAR (shroud) \n or far away (hanging lights)]') 


while True:
    inp=raw_input('\033[1;37m Are you debugging the case of shroud (a) or hanging lights (b), enter a or b: \n')
    if inp=='a':
        i=0.1
        break
    if inp=='b':
        i=0.28
        break     
    else:
        print('Incorrect input, try again')
        continue

def callback(msg):

    dist_list=list(msg.ranges)
    # print(len(msg.ranges))
    for j in range(1,len(dist_list)-25,5):
        if dist_list[j]<i and dist_list[j]>0:

            # print(i)
            if j<313:
                angle= -104.33+ 0.33*j
                print('Object at angle:',angle)
            elif j>=313:
                k=j-313
                angle= 0.33*k
                print('Object at angle:', angle)
           
    print('------------')

rospy.init_node('scan_dist')
subs=rospy.Subscriber('/sensors/lidar/scan',LaserScan,callback)
rospy.spin()
