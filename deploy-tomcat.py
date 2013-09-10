__author__ = 'shleger'

import os
import sys

import shutil

if sys.argv.__len__() == 1:
    print " WAR location does not defined"
    exit(0)

WEBAPPS_DIR = "C:/dev/apache-tomcat/webapps/"
WAR_LOCATION = sys.argv[1]

print "Start deploy: " + WAR_LOCATION
print "Stopping tomcat server"
os.system("net stop Tomcat6 ")
print "Done."

print "Clear webapps dir"

shutil.rmtree(WEBAPPS_DIR)
os.mkdir(WEBAPPS_DIR)

print "Rename war file to ROOT.war"

for root, dirs, files in os.walk(WAR_LOCATION):
    for file_ in files:
        if file_.endswith(".war"):
            shutil.move(os.path.join(root, file_), WAR_LOCATION + "ROOT.war")
            print "Copy war file"
            shutil.copy(WAR_LOCATION + "ROOT.war", WEBAPPS_DIR)
            print "Done."
            break

print "Start tomcat server"
os.system("net start Tomcat6 ")
print "Done."












