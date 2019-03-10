# Paradox IP150-MQTTv2
Python-based IP150 'middle-ware' that uses the IP module's software port for monitoring and control of the alarm via an MQTT Broker.

<b><i>NB: For a more updated project I suggest considering one of the forks that have been developed much further. E.g.: https://github.com/psyciknz</i></b>

The script was designed to be extendable to support more alarm types. See the ParadoxMap.py file for details. If you want to do some tcp dump of your alarm model to add into there, get Paradox's Winload software. Then within it's root folder find a file called COM.ini and change the 'IPEncrypted' setting to FALSE. You can then use WireShark (or equivalent) to trap whatever commands/replies you want to and either extend the ParadoxMap.py's existing dictionaries or add in a complete new Class for another alarm type.

Confirmed supported systems: See the [wiki](../../wiki) (please let me know if yours work, or not)

## Steps to use it:
1.  Tested with Python 2.7.10 & [Mosquitto MQTT Broker](http://mosquitto.org)
2.  Download the files in this repository and place it in some directory
3.  Copy the config-master.ini to config.ini file and edit to configure.
4.  Run the script: Python IP150-MQTTv2.py

NOTE: as at July-2017, there is not a configuration item for the location of the log directory.  See this in the config.


## What happens in the background:
The main script will connect to you IP module's software port (usually port 10000) and login with your password. It will then use two seperate classes (containing dictionaries) referenced in from the ParadoxMap.py file to extract different info from the alarm and translate events into meaningfull text. The dictionaries currently supports the MG5050 V4 firmware but could evolve over time if the community adds more alarm types to the dictionaries.

Once the info (mostly labels) has been extracted from the alarm, the MQTT broker is used as middleware between your application and the alarm panel.

Seeing as not all alarm variants are initially supported, you can use the config.ini file to switch off different portions of the script. You can also choose to only get events in their numeric form if you have the correct programming guide for your alarm detailing the event types. <b>I would prefer it though if you can do a PR to update the ParadoxMap.py file with new entries for supported alarms or altogether new class dictionaries for other alarm variants</b>.

## What to expect:
### Labels
If successfully connected to your IP150 and MQTT broker, the app will optionally start off by publishing (once-off) all the detected labels (zone, partition, output, etc. names) to your broker. Both the reading of label names and publishing thereof can be independantly controlled through the config.ini file. If you do read the labels, events such as "Zone open - Zone number 3" will translate to "Zone open - Garage door" or "Low battery on zone - Zone 1" to "Low battery on zone - Alley Beam" (assuming this is named/configured as such in your alarm).

Note: on a Spectre SP5500 these labels do not seem to read.  To this end, I've updated to pull the zone name from the event message and will publish an MQTT topic for the zone name.

* Zone Labels:
  * Topic: <b>Paradox/Labels/Zones</b>
  * Payload (example): <b>1:Front PIR;2:Back PIR;3:Garage Door;... </b>
* Output Labels:
  * Topic: <b>Paradox/Labels/Outputs</b>
  * Payload (example): <b>1:Status LED;2:ToggleGarage;3:UnlockFront;4:MakeCoffee;5:Output 05;6:Output 06;...</b>
* Partition Labels:
  * Topic: <b>Paradox/Labels/Partitions</b>
  * Payload (example): <b>1:Main Alarm;2:Front Beams</b>
* User Labels:
  * Topic: <b>Paradox/Labels/Users</b>
  * Payload (example): <b>1:System Master;2:Master 1;3:Master 2;4:Bob;5:Alice;6:User 06;...</b>
* Bus Module Labels:
  * Topic: <b>Paradox/Labels/BusModules</b>
  * Payload (example): <b>1:ZX8-1;2:Bus Module 02;3:Bus Module 03;4:Bus Module 04;5:Bus Module 05;...</b>
* Wireless Repeater Labels:
  * Topic: <b>Paradox/Labels/WirelessRepeaters</b>
  * Payload (example): <b>1:Front Rpt;2:Repeater 2</b>
* Wireless Keypad Labels:
  * Topic: <b>Paradox/Labels/WirelessKeypads</b>
  * Payload (example): <b>1:Main Keyp;2:Garage Keyp;3:Wireless Keyp 3;...</b>
* Wireless Siren Labels:
  * Topic: <b>Paradox/Labels/WirelessSirens</b>
  * Payload (example): <b>1:Wireless Siren 1;2:Wireless Siren 2;3:Wireless Siren 3;4:Wireless Siren 4</b>
* Site Name Labels:
  * Topic: <b>Paradox/Labels/SiteNames</b>
  * Payload (example): <b>1:Your Alarm Site</b>

### Events
Once the script has settled to listen for events, the following topics are available (and their names are also configurable in the config.ini file):
* Events:
  * Topic: <b>Paradox/Events</b>
    * Payload (example): <b>Event:Zone OK;SubEvent:Braaikamer PIR</b>
    * Payload (example): <b>Event:Zone open;SubEvent:Braaikamer PIR</b>
    * Payload (example): <b>Event:Partition status;SubEvent:Disarm partition</b>
    * Payload (example): <b>Event:Zone forced;SubEvent:Back Door</b>
    * Payload (example): <b>Event:Disarming with user;SubEvent:User 06</b>
    * Payload (example): <b>Event:Non-reportable event;SubEvent:Arm in sleep mode</b>
    * etc.....

  * Topic <b>Paradox/Zones/<i>zone label</i></b>
  Sets a status for on of off for each zone.  Allows Openhab to easily configure an item for each zone

  * Topic <b>Paradox/Partition</b>
  Shows the current partition status.  Can't be determines on startup though, only while running. 

### Controls
* Controlling the alarm or outputs
  * Publish the following topic to control the <b>alarm</b>:
    * <b>Paradox/C/P1/Disarm</b>
    * (C = Control; P = Partition, followed by number; Then the action = Disarm / Arm / Sleep / Stay)
    * The payload is not evaluated in this case. Note that alarm controls can take a few seconds as the script must first be re-authenticated
    * <b>Paradox/C/P1</b>, Payload: <b>Disarm</b>
    * In this case the payload is used to determine the command to send.
  * Publish the following topic to control (Force/Pulse) an <b>output</b> (PGM):
    * <b>Paradox/C/FO/4/Off</b>
    * (C = Control; <b>FO = Force output / PO = Pulse Output</b>, followed by the output number; Then the action (for pulse this will be the intermediate state, e.g. to pulse High then back to Low use "On" and vice versa).
    * The payload is not evaluated in this case. Note that output controls can take a few seconds as the script must first be re-authenticated 
    * Pulse outputs are configured for approx. 0.5sec.
    * <b>Paradox/C/PO/1</b>, Payload: <b>On</b>
    * In this case the payload is used to determine the command to send: Pulse Output 1, On->Off
* Controlling this application
  * Publish the following topics to enable/disable polling of the IP module:
    * <b>Paradox/C/Polling/Enable</b>
    * <b>Paradox/C/Polling/Disable</b>
    * The payload is not evaluated.
    * This command can be useful if the script was unable to correctly detect labels or you want it to re-scan them. Then simply disable and re-enable polling which will update the labels (if your config.ini file is configured for this).

<b>Note: If you modified the subscription topic for <b>controls</b> in the config.ini file ensure it ends with a '/'.</b>

### Script State
* The current state of the script is linked to a topic found in the config file. Examples:
 * Topic <b>Paradox/State</b>
  * Payload (example): State Machine 1, Connected to MQTT Broker
  * Payload (example): State Machine 2, Connecting to IP Module...
  * Payload (example): State Machine 2, Connected to IP Module, unlocking...
  * Payload (example): State Machine 2, Logged into IP Module successfully
  * Payload (example): State Machine 3, Reading labels from alarm
  * Payload (example): State Machine 4, Listening for events...
  * Payload (example): Output: Forcing PGM 1 to state: On

### 3rd Party Connections
This script will listen for 3rd party (Web-only, not software port) IP connections and if detected will disconnect for a period configured in the config.ini file. After the period has lapsed, the script will attempt to reconnect. This is useful if you still want to use web/smartphone apps (such as Alarmin). Note that it takes about 20 seconds to disconnect after which you can try to connect to the alarm again.

## Running as a service / daemon

If you want to run this as a daemon on Linux, 
 1. Copy the paradoxip.service file to /usr/lib/systemd/system (where mine is)
 2. Run: sudo systemctl daemon-reload
 3. Then you should be able to start the service with : sudo systemctl start paradoxip.service

