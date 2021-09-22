import sys
import logging
import time
import json
import tempfile
import shutil
import os
import argparse
from typing import ContextManager

def logging_settings():
    logging.basicConfig( 
        format = '%(asctime)s %(levelname)-10s %(processName)s %(name)s %(message)s',
        datefmt =  "%Y-%m-%d-%H-%M-%S",
        filename = time.strftime("StrangFig-%Y-%m-%d.log"), 
        level=logging.DEBUG
        )

    # logging.debug("debug-test")
    # logging.info("info-test")
    # logging.warning("warning-test")
    # logging.error("error-test")
    # logging.critical("critical-test")

def wait_for_enter():
    print("\n")
    input("Press Enter to continue.")

class ExplainStep(object):
    def run(self, context):
        print('''
            **Adding Remote Access to Vive Hub**
            This is a "Do-nothing script" [0] to aid in the process of adding StrangFig to a New hub.
            [0] https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/?utm_source=pocket_mylist
            ''')
        wait_for_enter()

class GetHubDetails(object):
    def run(self, context):
        print("**Get Hub Details**")
        Hub_SN = input("!->Enter Hub SN: ")
        Hub_Ethernet_MAC = input("!->Enter Hub Ethernet MAC: ")
        Hub_Wifi_MAC = input("!->Enter Hub WiFi MAC: ")
        Hub_Wifi_Name = input("!->Enter exact name of the Hub Wi-Fi: ")
        Hub_Wifi_Password = input("!->Enter the hub WiFi Password: ")
        Hub_System_Password = input("!->Enter the Hub System Password (if set): ")

        new_data = ({
                    "HUB_SN":Hub_SN,
                    "HUB_Ethernet_MAC":Hub_Ethernet_MAC,
                    "HUB_Wifi_MAC":Hub_Wifi_MAC,
                    "HUB_Wifi_Name":Hub_Wifi_Name,
                    "HUB_Wifi_Password":Hub_Wifi_Password,
                    "HUB_System_Password":Hub_System_Password
             })

        # First load up the device class to firmware file data from the configuration file
        with open(args.config + "config.json",'r+') as config:
            # First we load existing data into a dict.
            config_data = json.load(config)

            # Join new_data with config_data inside HUBS  
            config_data["HUBS"].append(new_data)
          
            # Sets file's current position at offset.
            config.seek(0)

            # convert back to json.
            json.dump(config_data, config, indent = 4)

            #print(test)
        wait_for_enter()

def writeconfig(outputpath, update_files):
	# Make the data structures for our updates to serialize to json
	updatemap = {}

	# Process each device row and create the config for it
	for row in rows:
		# Determine which update to add it to
		if row[0] in update_files:
			if update_files[row[0]]["grouped"]:
				if row[0] in updatemap:
					updatemap[row[0]][0]["SerialNumbers"].append(row[1])
				else:
					updatemap[row[0]] = [{
						"SerialNumbers": [row[1]],
						"DeviceClass": row[0],
						"FirmwareFilePath": update_files[row[0]]["filepath"]
					}]
			else:
				if row[0] not in updatemap:
					updatemap[row[0]] = []
				updatemap[row[0]].append({
					"SerialNumbers": [row[1]],
					"DeviceClass": row[0],
					"FirmwareFilePath": update_files[row[0]]["filepath"]
				})

	# Generate a list of all the updates
	updates = []
	for key in updatemap:
		for update in updatemap[key]:
			updates.append(update)

	# Now serialize the updates to the config file
	with open(outputpath, 'w') as outfile:
		json.dump(updates, outfile, indent=4, separators=(',', ': '))
		outfile.write("\n")

	# Cleanup the connection after we are done
	conn.close()


if __name__ == "__main__":
    #Call Logging Settings
    logging_settings()
    
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Generate a StrangFig configuration file.')
    parser.add_argument('-u', '--user', type=str, default='NoUserEntered', help='Please Enter a User Name')
    parser.add_argument('-c', '--config', type=str, default='', help='Please Enter a User Name')
    parser.add_argument('-o', '--output', type=str, default='config.json', help='Output file path for the config file')
    args = parser.parse_args()
    
    #Upgrader is the person running the script
    logging.info("Upgrader is {0}".format(args.user))
    context = args.user
    procedure = [
        ExplainStep(),
        GetHubDetails()
    ]

    for step in procedure:
        step.run(context)
        logging.info("Class {0} completed".format(step.__class__.__name__))
    
    print("Done! Hopefully, you've added StrangFig to a Hub without breaking anything.")
