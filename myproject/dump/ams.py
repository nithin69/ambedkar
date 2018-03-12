import MySQLdb
import os
import datetime
import sys
import os, datetime

path = "D:/softwares/dbdunps/ams"

mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
target_dir = mydir
os.system ("mysqldump -P 3306 -h 103.44.220.147 -u rt8055 -pStarthere66% ambedkar > "+target_dir+"ams.sql")


