

"""
MG5050: This class maps all MG5050 V4.xx register to labels or output actions
"""

class ParadoxMG5050Registers():

    zoneLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                  1: {"Send": "\x50\x00\x00\x10", "Receive": {"Start": 20, "Finish": 36}},   # I.e. get data from register \x50000010, extract text from posisiton 20 to 36
                  2: {"Send": "\x50\x00\x00\x10", "Receive": {"Start": 36, "Finish": 52}},
                  3: {"Send": "\x50\x00\x00\x30", "Receive": {"Start": 20, "Finish": 36}},
                  4: {"Send": "\x50\x00\x00\x30", "Receive": {"Start": 36, "Finish": 52}},
                  5: {"Send": "\x50\x00\x00\x50", "Receive": {"Start": 20, "Finish": 36}},
                  6: {"Send": "\x50\x00\x00\x50", "Receive": {"Start": 36, "Finish": 52}},
                  7: {"Send": "\x50\x00\x00\x70", "Receive": {"Start": 20, "Finish": 36}},
                  8: {"Send": "\x50\x00\x00\x70", "Receive": {"Start": 36, "Finish": 52}},
                  9: {"Send": "\x50\x00\x00\x90", "Receive": {"Start": 20, "Finish": 36}},
                  10: {"Send": "\x50\x00\x00\x90", "Receive": {"Start": 36, "Finish": 52}},
                  11: {"Send": "\x50\x00\x00\xb0", "Receive": {"Start": 20, "Finish": 36}},
                  12: {"Send": "\x50\x00\x00\xb0", "Receive": {"Start": 36, "Finish": 52}},
                  13: {"Send": "\x50\x00\x00\xd0", "Receive": {"Start": 20, "Finish": 36}},
                  14: {"Send": "\x50\x00\x00\xd0", "Receive": {"Start": 36, "Finish": 52}},
                  15: {"Send": "\x50\x00\x00\xf0", "Receive": {"Start": 20, "Finish": 36}},
                  16: {"Send": "\x50\x00\x00\xf0", "Receive": {"Start": 36, "Finish": 52}},
                  17: {"Send": "\x50\x00\x01\x10", "Receive": {"Start": 20, "Finish": 36}},
                  18: {"Send": "\x50\x00\x01\x10", "Receive": {"Start": 36, "Finish": 52}},
                  19: {"Send": "\x50\x00\x01\x30", "Receive": {"Start": 20, "Finish": 36}},
                  20: {"Send": "\x50\x00\x01\x30", "Receive": {"Start": 36, "Finish": 52}},
                  21: {"Send": "\x50\x00\x01\x50", "Receive": {"Start": 20, "Finish": 36}},
                  22: {"Send": "\x50\x00\x01\x50", "Receive": {"Start": 36, "Finish": 52}},
                  23: {"Send": "\x50\x00\x01\x70", "Receive": {"Start": 20, "Finish": 36}},
                  24: {"Send": "\x50\x00\x01\x70", "Receive": {"Start": 36, "Finish": 52}},
                  25: {"Send": "\x50\x00\x01\x90", "Receive": {"Start": 20, "Finish": 36}},
                  26: {"Send": "\x50\x00\x01\x90", "Receive": {"Start": 36, "Finish": 52}},
                  27: {"Send": "\x50\x00\x01\xb0", "Receive": {"Start": 20, "Finish": 36}},
                  28: {"Send": "\x50\x00\x01\xb0", "Receive": {"Start": 36, "Finish": 52}},
                  29: {"Send": "\x50\x00\x01\xd0", "Receive": {"Start": 20, "Finish": 36}},
                  30: {"Send": "\x50\x00\x01\xd0", "Receive": {"Start": 36, "Finish": 52}},
                  31: {"Send": "\x50\x00\x01\xf0", "Receive": {"Start": 20, "Finish": 36}},
                  32: {"Send": "\x50\x00\x01\xf0", "Receive": {"Start": 36, "Finish": 52}},
                  }

    outputLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                    1: {"Send": "\x50\x00\x02\x10", "Receive": {"Start": 20, "Finish": 36}},
                    2: {"Send": "\x50\x00\x02\x10", "Receive": {"Start": 36, "Finish": 52}},
                    3: {"Send": "\x50\x00\x02\x30", "Receive": {"Start": 20, "Finish": 36}},
                    4: {"Send": "\x50\x00\x02\x30", "Receive": {"Start": 36, "Finish": 52}},
                    5: {"Send": "\x50\x00\x02\x50", "Receive": {"Start": 20, "Finish": 36}},
                    6: {"Send": "\x50\x00\x02\x50", "Receive": {"Start": 36, "Finish": 52}},
                    7: {"Send": "\x50\x00\x02\x70", "Receive": {"Start": 20, "Finish": 36}},
                    8: {"Send": "\x50\x00\x02\x70", "Receive": {"Start": 36, "Finish": 52}},
                    9: {"Send": "\x50\x00\x02\x90", "Receive": {"Start": 20, "Finish": 36}},
                    10: {"Send": "\x50\x00\x02\x90", "Receive": {"Start": 36, "Finish": 52}},
                    11: {"Send": "\x50\x00\x02\xb0", "Receive": {"Start": 20, "Finish": 36}},
                    12: {"Send": "\x50\x00\x02\xb0", "Receive": {"Start": 36, "Finish": 52}},
                    13: {"Send": "\x50\x00\x02\xd0", "Receive": {"Start": 20, "Finish": 36}},
                    14: {"Send": "\x50\x00\x02\xd0", "Receive": {"Start": 36, "Finish": 52}},
                    15: {"Send": "\x50\x00\x02\xf0", "Receive": {"Start": 20, "Finish": 36}},
                    16: {"Send": "\x50\x00\x02\xf0", "Receive": {"Start": 36, "Finish": 52}}
                    }

    partitionLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                       1: {"Send": "\x50\x00\x03\x10", "Receive": {"Start": 20, "Finish": 36}},
                       2: {"Send": "\x50\x00\x03\x10", "Receive": {"Start": 36, "Finish": 52}}
                       }


    userLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                  1: {"Send": "\x50\x00\x03\x30", "Receive": {"Start": 20, "Finish": 36}},
                  2: {"Send": "\x50\x00\x03\x30", "Receive": {"Start": 36, "Finish": 52}},
                  3: {"Send": "\x50\x00\x03\x50", "Receive": {"Start": 20, "Finish": 36}},
                  4: {"Send": "\x50\x00\x03\x50", "Receive": {"Start": 36, "Finish": 52}},
                  5: {"Send": "\x50\x00\x03\x70", "Receive": {"Start": 20, "Finish": 36}},
                  6: {"Send": "\x50\x00\x03\x70", "Receive": {"Start": 36, "Finish": 52}},
                  7: {"Send": "\x50\x00\x03\x90", "Receive": {"Start": 20, "Finish": 36}},
                  8: {"Send": "\x50\x00\x03\x90", "Receive": {"Start": 36, "Finish": 52}},
                  9: {"Send": "\x50\x00\x03\xb0", "Receive": {"Start": 20, "Finish": 36}},
                  10: {"Send": "\x50\x00\x03\xb0", "Receive": {"Start": 36, "Finish": 52}},
                  11: {"Send": "\x50\x00\x03\xd0", "Receive": {"Start": 20, "Finish": 36}},
                  12: {"Send": "\x50\x00\x03\xd0", "Receive": {"Start": 36, "Finish": 52}},
                  13: {"Send": "\x50\x00\x03\xf0", "Receive": {"Start": 20, "Finish": 36}},
                  14: {"Send": "\x50\x00\x03\xf0", "Receive": {"Start": 36, "Finish": 52}},
                  15: {"Send": "\x50\x00\x04\x10", "Receive": {"Start": 20, "Finish": 36}},
                  16: {"Send": "\x50\x00\x04\x10", "Receive": {"Start": 36, "Finish": 52}},
                  17: {"Send": "\x50\x00\x04\x30", "Receive": {"Start": 20, "Finish": 36}},
                  18: {"Send": "\x50\x00\x04\x30", "Receive": {"Start": 36, "Finish": 52}},
                  19: {"Send": "\x50\x00\x04\x50", "Receive": {"Start": 20, "Finish": 36}},
                  20: {"Send": "\x50\x00\x04\x50", "Receive": {"Start": 36, "Finish": 52}},
                  21: {"Send": "\x50\x00\x04\x70", "Receive": {"Start": 20, "Finish": 36}},
                  22: {"Send": "\x50\x00\x04\x70", "Receive": {"Start": 36, "Finish": 52}},
                  23: {"Send": "\x50\x00\x04\x90", "Receive": {"Start": 20, "Finish": 36}},
                  24: {"Send": "\x50\x00\x04\x90", "Receive": {"Start": 36, "Finish": 52}},
                  25: {"Send": "\x50\x00\x04\xb0", "Receive": {"Start": 20, "Finish": 36}},
                  26: {"Send": "\x50\x00\x04\xb0", "Receive": {"Start": 36, "Finish": 52}},
                  27: {"Send": "\x50\x00\x04\xd0", "Receive": {"Start": 20, "Finish": 36}},
                  28: {"Send": "\x50\x00\x04\xd0", "Receive": {"Start": 36, "Finish": 52}},
                  29: {"Send": "\x50\x00\x04\xf0", "Receive": {"Start": 20, "Finish": 36}},
                  30: {"Send": "\x50\x00\x04\xf0", "Receive": {"Start": 36, "Finish": 52}},
                  31: {"Send": "\x50\x00\x05\x10", "Receive": {"Start": 20, "Finish": 36}},
                  32: {"Send": "\x50\x00\x05\x10", "Receive": {"Start": 36, "Finish": 52}},
                  }

    busModuleLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                       1: {"Send": "\x50\x00\x05\x30", "Receive": {"Start": 20, "Finish": 36}},
                       2: {"Send": "\x50\x00\x05\x30", "Receive": {"Start": 36, "Finish": 52}},
                       3: {"Send": "\x50\x00\x05\x50", "Receive": {"Start": 20, "Finish": 36}},
                       4: {"Send": "\x50\x00\x05\x50", "Receive": {"Start": 36, "Finish": 52}},
                       5: {"Send": "\x50\x00\x05\x70", "Receive": {"Start": 20, "Finish": 36}},
                       6: {"Send": "\x50\x00\x05\x70", "Receive": {"Start": 36, "Finish": 52}},
                       7: {"Send": "\x50\x00\x05\x90", "Receive": {"Start": 20, "Finish": 36}},
                       8: {"Send": "\x50\x00\x05\x90", "Receive": {"Start": 36, "Finish": 52}},
                       9: {"Send": "\x50\x00\x05\xb0", "Receive": {"Start": 20, "Finish": 36}},
                       10: {"Send": "\x50\x00\x05\xb0", "Receive": {"Start": 36, "Finish": 52}},
                       11: {"Send": "\x50\x00\x05\xd0", "Receive": {"Start": 20, "Finish": 36}},
                       12: {"Send": "\x50\x00\x05\xd0", "Receive": {"Start": 36, "Finish": 52}},
                       13: {"Send": "\x50\x00\x05\xf0", "Receive": {"Start": 20, "Finish": 36}},
                       14: {"Send": "\x50\x00\x05\xf0", "Receive": {"Start": 36, "Finish": 52}},
                       15: {"Send": "\x50\x00\x06\x10", "Receive": {"Start": 20, "Finish": 36}},
                       }

    wirelessRepeaterLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                              1: {"Send": "\x50\x00\x06\x10", "Receive": {"Start": 36, "Finish": 52}},
                              2: {"Send": "\x50\x00\x06\x30", "Receive": {"Start": 20, "Finish": 36}}
                              }

    wirelessKeypadLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                            1: {"Send": "\x50\x00\x06\x30", "Receive": {"Start": 36, "Finish": 52}},
                            2: {"Send": "\x50\x00\x06\x50", "Receive": {"Start": 20, "Finish": 36}},
                            3: {"Send": "\x50\x00\x06\x50", "Receive": {"Start": 36, "Finish": 52}},
                            4: {"Send": "\x50\x00\x06\x70", "Receive": {"Start": 20, "Finish": 36}},
                            5: {"Send": "\x50\x00\x06\x70", "Receive": {"Start": 36, "Finish": 52}},
                            6: {"Send": "\x50\x00\x06\x90", "Receive": {"Start": 20, "Finish": 36}},
                            7: {"Send": "\x50\x00\x06\x90", "Receive": {"Start": 36, "Finish": 52}},
                            8: {"Send": "\x50\x00\x06\xb0", "Receive": {"Start": 20, "Finish": 36}}
                            }

    siteName = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                1: {"Send": "\x50\x00\x06\xb0", "Receive": {"Start": 36, "Finish": 52}}
                }

    wirelessSirenLabels = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                           1: {"Send": "\x50\x00\x06\xd0", "Receive": {"Start": 20, "Finish": 36}},
                           2: {"Send": "\x50\x00\x06\xd0", "Receive": {"Start": 36, "Finish": 52}},
                           3: {"Send": "\x50\x00\x06\xf0", "Receive": {"Start": 20, "Finish": 36}},
                           4: {"Send": "\x50\x00\x06\xf0", "Receive": {"Start": 36, "Finish": 52}}
                           }

    controlOutputs = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                      1: {"ON": "\x40\x00\x30\x00", "OFF": "\x40\x00\x31\x00"},
                      2: {"ON": "\x40\x00\x30\x01", "OFF": "\x40\x00\x31\x01"},
                      3: {"ON": "\x40\x00\x30\x02", "OFF": "\x40\x00\x31\x02"},
                      4: {"ON": "\x40\x00\x30\x03", "OFF": "\x40\x00\x31\x03"},
                      5: {"ON": "\x40\x00\x30\x04", "OFF": "\x40\x00\x31\x04"},
                      6: {"ON": "\x40\x00\x30\x05", "OFF": "\x40\x00\x31\x05"},
                      7: {"ON": "\x40\x00\x30\x06", "OFF": "\x40\x00\x31\x06"},
                      8: {"ON": "\x40\x00\x30\x07", "OFF": "\x40\x00\x31\x07"},
                      9: {"ON": "\x40\x00\x30\x08", "OFF": "\x40\x00\x31\x08"},
                      10: {"ON": "\x40\x00\x30\x09", "OFF": "\x40\x00\x31\x09"},
                      11: {"ON": "\x40\x00\x30\x0a", "OFF": "\x40\x00\x31\x0a"},
                      12: {"ON": "\x40\x00\x30\x0b", "OFF": "\x40\x00\x31\x0b"},
                      13: {"ON": "\x40\x00\x30\x0c", "OFF": "\x40\x00\x31\x0c"},
                      14: {"ON": "\x40\x00\x30\x0d", "OFF": "\x40\x00\x31\x0d"},
                      15: {"ON": "\x40\x00\x30\x0e", "OFF": "\x40\x00\x31\x0e"},
                      16: {"ON": "\x40\x00\x30\x0f", "OFF": "\x40\x00\x31\x0f"},
                      }

    controlAlarm = {"Header": "\xaa\x25\x00\x04\x08\x00\x00\x14\xee\xee\xee\xee\xee\xee\xee\xee",
                    1: {"ARM": "\x40\x00\x04\x00", "DISARM": "\x40\x00\x05\x00", "SLEEP": "\x40\x00\x03\x00", "STAY": "\x40\x00\x01\x00"},
                    2: {"ARM": "\x40\x00\x04\x01", "DISARM": "\x40\x00\x05\x01", "SLEEP": "\x40\x00\x03\x01", "STAY": "\x40\x00\x01\x01"}}


    @staticmethod
    def getZoneLabelRegisters():
        return ParadoxMG5050Registers.zoneLabels

    @staticmethod
    def getPartitionLabelRegisters():
        return ParadoxMG5050Registers.partitionLabels

    @staticmethod
    def getUserLabelRegisters():
        return ParadoxMG5050Registers.userLabels

    @staticmethod
    def getBusModuleLabelRegisters():
        return ParadoxMG5050Registers.busModuleLabels

    @staticmethod
    def getWirelessRepeaterLabelRegisters():
        return ParadoxMG5050Registers.wirelessRepeaterLabels

    @staticmethod
    def getWirelessKeypadLabelRegisters():
        return ParadoxMG5050Registers.wirelessKeypadLabels

    @staticmethod
    def getSiteNameRegisters():
        return ParadoxMG5050Registers.siteName

    @staticmethod
    def getWirelessSirenLabelRegisters():
        return ParadoxMG5050Registers.wirelessSirenLabels

    @staticmethod
    def getOutputLabelRegisters():
        # try:
        return ParadoxMG5050Registers.outputLabels
    
    @staticmethod
    def getControlOutputRegisters():
        # try:
        return ParadoxMG5050Registers.controlOutputs


    @staticmethod
    def getAlarmRegisters():
        # try:
        return ParadoxMG5050Registers.controlAlarm
"""
MG5050: This class is used for reporting events. The generic names for grouped items will be
updated if a correspondig register location is goven in the Registers class
See: http://www.imotionsecurite.com/pdf/paradox/MGSP-EP20.pdf
"""

import pickle

class ParadoxMG5050EventMap():

    def __init__(self):
        print 'init'


    '''mapping of event and subevent groups here'''
    eventGroupMap = {0: 'Zone OK',
                     1: 'Zone open',
                     2: 'Partition status',
                     3: 'Bell status (Partition 1)',
                     # 5: 'Non-Reportable Event',
                     6: 'Non-reportable event',
                     # 7: 'PGM Activation',
                     8: 'Button B pressed on remote',
                     9: 'Button C pressed on remote',
                     10: 'Button D pressed on remote',
                     11: 'Button E pressed on remote',
                     12: 'Cold start wireless zone',
                     13: 'Cold start wireless module (Partition 1)',
                     14: 'Bypass programming',
                     15: 'User code activated output (Partition 1)',
                     16: 'Wireless smoke maintenance signal',
                     17: 'Delay zone alarm transmission',
                     18: 'Zone signal strength weak 1 (Partition 1)',
                     19: 'Zone signal strength weak 2 (Partition 1)',
                     20: 'Zone signal strength weak 3 (Partition 1)',
                     21: 'Zone signal strength weak 4 (Partition 1)',
                     22: 'Button 5 pressed on remote',
                     23: 'Button 6 pressed on remote',
                     24: 'Fire delay started',
                     # 25: 'N/A',
                     26: 'Software access',
                     27: 'Bus module event',
                     28: 'StayD pass acknowledged',
                     29: 'Arming with user',
                     30: 'Special arming',
                     31: 'Disarming with user',
                     32: 'Disarming after alarm with user',
                     33: 'Alarm cancelled with user',
                     34: 'Special disarming',
                     35: 'Zone bypassed',
                     36: 'Zone in alarm',
                     37: 'Fire alarm',
                     38: 'Zone alarm restore',
                     39: 'Fire alarm restore',
                     40: 'Special alarm',
                     41: 'Zone shutdown',
                     42: 'Zone tampered',
                     43: 'Zone tamper restore',
                     44: 'New trouble (Partition 1, both for sub event 7',
                     45: 'Trouble restored ',
                     46: 'Bus / EBus / Wireless module new trouble (Partition 1)',
                     47: 'Bus / EBus / Wireless module trouble restored (Partition 1)',
                     48: 'Special (Partition 1)',
                     49: 'Low battery on zone',
                     50: 'Low battery on zone restore',
                     51: 'Zone supervision trouble',
                     52: 'Zone supervision restore',
                     53: 'Wireless module supervision trouble (Partition 1)',
                     54: 'Wireless module supervision restore (Partition 1)',
                     55: 'Wireless module tamper trouble (Partition 1)',
                     56: 'Wireless module tamper restore (Partition 1)',
                     57: 'Non-medical alarm (paramedic)',
                     58: 'Zone forced',
                     59: 'Zone included',
                     64: 'System Status'
                     }

    _zoneNumber = {1: 'Zone 1',
                   2: 'Zone 2',
                   3: 'Zone 3',
                   4: 'Zone 4',
                   5: 'Zone 5',
                   6: 'Zone 6',
                   7: 'Zone 7',
                   8: 'Zone 8',
                   9: 'Zone 9',
                   10: 'Zone 10',
                   11: 'Zone 11',
                   12: 'Zone 12',
                   13: 'Zone 13',
                   14: 'Zone 14',
                   15: 'Zone 15',
                   16: 'Zone 16',
                   17: 'Zone 17',
                   18: 'Zone 18',
                   19: 'Zone 19',
                   20: 'Zone 20',
                   21: 'Zone 21',
                   22: 'Zone 22',
                   23: 'Zone 23',
                   24: 'Zone 24',
                   25: 'Zone 25',
                   26: 'Zone 26',
                   27: 'Zone 27',
                   28: 'Zone 28',
                   29: 'Zone 29',
                   30: 'Zone 30',
                   31: 'Zone 31',
                   32: 'Zone 32',
                   99: 'Any zone'}

    _partitionStatus = {0: 'N/A',
                        1: 'N/A',
                        2: 'Silent alarm',
                        3: 'Buzzer alarm',
                        4: 'Steady alarm',
                        5: 'Pulse alarm',
                        6: 'Strobe',
                        7: 'Alarm stopped',
                        8: 'Squawk ON (Partition 1)',
                        9: 'Squawk OFF (Partition 1)',
                        10: 'Ground Start (Partition 1)',
                        11: 'Disarm partition',
                        12: 'Arm partition',
                        13: 'Entry delay started',
                        14: 'Exit delay started',
                        15: 'Pre-alarm delay',
                        16: 'Report confirmation',
                        99: 'Any partition status event'
                        }

    _bellStatus = {0: ' Bell OFF',
                   1: ' Bell ON',
                   2: ' Bell squawk arm',
                   3: ' Bell squawk disarm',
                   99: 'Any bell status event'}

    _nonReportableEvents = {0: 'Telephone line trouble',
                            1: '[ENTER]/[CLEAR]/[POWER] key was pressed (Partition 1 only)',
                            2: 'N/A',
                            3: 'Arm in stay mode',
                            4: 'Arm in sleep mode',
                            5: 'Arm in force mode',
                            6: 'Full arm when armed in stay mode',
                            7: 'PC fail to communicate (Partition 1)',
                            8: 'Utility Key 1 pressed (keys [1] and [2]) (Partition 1)',
                            9: 'Utility Key 2 pressed (keys [4] and [5]) (Partition 1)',
                            10: 'Utility Key 3 pressed (keys [7] and [8]) (Partition 1)',
                            11: 'Utility Key 4 pressed (keys [2] and [3]) (Partition 1)',
                            12: 'Utility Key 5 pressed (keys [5] and [6]) (Partition 1)',
                            13: 'Utility Key 6 pressed (keys [8] and [9]) (Partition 1)',
                            14: 'Tamper generated alarm',
                            15: 'Supervision loss generated alarm',
                            16: 'N/A',
                            17: 'N/Ad',
                            18: 'N/A',
                            19: 'N/A',
                            20: 'Full arm when armed in sleep mode',
                            21: 'Firmware upgrade -Partition 1 only (non-PGM event)',
                            22: 'N/A',
                            23: 'StayD mode activated',
                            24: 'StayD mode deactivated',
                            25: 'IP Registration status change',
                            26: 'GPRS Registration status change',
                            99: 'Any non-reportable event'}

    _userNumber = {1: 'User Number 1',
                   2: 'User Number 2',
                   3: 'User Number 3',
                   4: 'User Number 4',
                   5: 'User Number 5',
                   6: 'User Number 6',
                   7: 'User Number 7',
                   8: 'User Number 8',
                   9: 'User Number 9',
                   10: 'User Number 10',
                   11: 'User Number 11',
                   12: 'User Number 12',
                   13: 'User Number 13',
                   14: 'User Number 14',
                   15: 'User Number 15',
                   16: 'User Number 16',
                   17: 'User Number 17',
                   18: 'User Number 18',
                   19: 'User Number 19',
                   20: 'User Number 20',
                   21: 'User Number 21',
                   22: 'User Number 22',
                   23: 'User Number 23',
                   24: 'User Number 24',
                   25: 'User Number 25',
                   26: 'User Number 26',
                   27: 'User Number 27',
                   28: 'User Number 28',
                   29: 'User Number 29',
                   30: 'User Number 30',
                   31: 'User Number 31',
                   32: 'User Number 32'
                   }

    _remoteNumber = {1: 'Remote control number 1',
                     2: 'Remote control number 2',
                     3: 'Remote control number 3',
                     4: 'Remote control number 4',
                     5: 'Remote control number 5',
                     6: 'Remote control number 6',
                     7: 'Remote control number 7',
                     8: 'Remote control number 8',
                     9: 'Remote control number 9',
                     10: 'Remote control number 10',
                     11: 'Remote control number 11',
                     12: 'Remote control number 12',
                     13: 'Remote control number 13',
                     14: 'Remote control number 14',
                     15: 'Remote control number 15',
                     16: 'Remote control number 16',
                     17: 'Remote control number 17',
                     18: 'Remote control number 18',
                     19: 'Remote control number 19',
                     20: 'Remote control number 20',
                     21: 'Remote control number 21',
                     22: 'Remote control number 22',
                     23: 'Remote control number 23',
                     24: 'Remote control number 24',
                     25: 'Remote control number 25',
                     26: 'Remote control number 26',
                     27: 'Remote control number 27',
                     28: 'Remote control number 28',
                     29: 'Remote control number 29',
                     30: 'Remote control number 30',
                     31: 'Remote control number 31',
                     32: 'Remote control number 32',
                     99: 'Any remote control number'
                     }

    _specialArming = {0: 'Auto-arming (on time/no movement)',
                      1: 'Late to close',
                      2: 'No movement arming',
                      3: 'Partial arming',
                      4: 'Quick arming',
                      5: 'Arming through WinLoad',
                      6: 'Arming with keyswitch',
                      99: 'Any special arming'
                      }

    _specialDisarming = {0: 'Auto-arm cancelled (on time/no movement)',
                         1: 'Disarming through WinLoad',
                         2: 'Disarming through WinLoad after alarm',
                         3: 'Alarm cancelled through WinLoad',
                         4: 'Paramedical alarm cancelled',
                         5: 'Disarm with keyswitch',
                         6: 'Disarm with keyswitch after an alarm',
                         7: 'Alarm cancelled with keyswitch',
                         99: 'Any special disarming'
                         }

    _specialAlarm = {0: 'Panic non-medical emergency',
                     1: 'Panic medical',
                     2: 'Panic fire',
                     3: 'Recent closing',
                     4: 'Global shutdown',
                     5: 'Duress alarm',
                     6: 'Keypad lockout (Partition 1)',
                     99: 'Any special alarm event'
                     }

    _newTrouble = {0: 'N/A',
                   1: 'AC failure',
                   2: 'Battery failure',
                   3: 'Auxiliary current overload',
                   4: 'Bell current overload',
                   5: 'Bell disconnected',
                   6: 'Clock loss',
                   7: 'Fire loop trouble',
                   8: 'Fail to communicate to monitoring station telephone #1',
                   9:  'Fail to communicate to monitoring station telephone #2',
                   11: 'Fail to communicate to voice report',
                   12: 'RF jamming',
                   13: 'GSM RF jamming',
                   14: 'GSM no service',
                   15: 'GSM supervision lost',
                   16: 'Fail To Communicate IP Receiver 1 (GPRS)',
                   17: 'Fail To Communicate IP Receiver 2 (GPRS)',
                   18: 'IP Module No Service',
                   19: 'IP Module Supervision Loss',
                   20: 'Fail To Communicate IP Receiver 1 (IP)',
                   21: 'Fail To Communicate IP Receiver 2 (IP)',
                   99: 'Any new trouble event'
                   }

    _troubleRestored = {0: 'Telephone line restore',
                        1: 'AC failure restore',
                        2: 'Battery failure restore',
                        3: 'Auxiliary current overload restore',
                        4: 'Bell current overload restore',
                        5: 'Bell disconnected restore',
                        6: 'Clock loss restore',
                        7: 'Fire loop trouble restore',
                        8: 'Fail to communicate to monitoring station telephone #1 restore',
                        9: 'Fail to communicate to monitoring station telephone #2 restore',
                        11: 'Fail to communicate to voice report restore',
                        12: 'RF jamming restore',
                        13: 'GSM RF jamming restore',
                        14: 'GSM no service restore',
                        15: 'GSM supervision lost restore',
                        16: 'Fail To Communicate IP Receiver 1 (GPRS) restore',
                        17: 'Fail To Communicate IP Receiver 2 (GPRS) restore',
                        18: 'IP Module No Service restore',
                        19: 'IP Module Supervision Loss restore',
                        20: 'Fail To Communicate IP Receiver 1 (IP) restore',
                        21: 'Fail To Communicate IP Receiver 2 (IP) restore',
                        99: 'Any trouble event restore'
                        }

    _softwareAccess = {0: 'Non-valid source ID',
                       1: 'WinLoad direct',
                       2: 'WinLoad through IP module',
                       3: 'WinLoad through GSM module',
                       4: 'WinLoad through modem',
                       9: 'IP100 direct',
                       10: 'VDMP3 direct',
                       11: 'Voice through GSM module',
                       12: 'Remote access',
                       13: 'SMS through GSM module',
                       99: 'Any software access'
                       }

    _pgmNumber = {1: 'PGM Number 1',
                  2: 'PGM Number 2',
                  3: 'PGM Number 3',
                  4: 'PGM Number 4',
                  5: 'PGM Number 5',
                  6: 'PGM Number 6',
                  7: 'PGM Number 7',
                  8: 'PGM Number 8',
                  9: 'PGM Number 9',
                  10: 'PGM Number 10',
                  11: 'PGM Number 11',
                  12: 'PGM Number 12',
                  13: 'PGM Number 13',
                  14: 'PGM Number 14',
                  15: 'PGM Number 15',
                  16: 'PGM Number 16'
                  }

    _wirelessRepeater = {1: 'Wireless repeater 1',
                         2: 'Wireless repeater 2'}

    _wirelessKeypad = {1: 'Wireless keypad 1',
                       2: 'Wireless keypad 2',
                       3: 'Wireless keypad 3',
                       4: 'Wireless keypad 4',
                       5: 'Wireless keypad 5',
                       6: 'Wireless keypad 6',
                       7: 'Wireless keypad 7',
                       8: 'Wireless keypad 8'
                       }

    _wirelessSiren = {1: 'Wireless siren 1',
                      2: 'Wireless siren 2',
                      3: 'Wireless siren 3',
                      4: 'Wireless siren 4'}

    _busModuleEvent = {0: 'A bus module was added',
                       1: 'A bus module was removed',
                       2: '2-way RF Module Communication Failure',
                       3: '2-way RF Module Communication Restored'
                       }

    _moduleTrouble = {0: 'Bus / EBus / Wireless module communication fault',
                      1: 'Tamper trouble',
                      2: 'Power fail',
                      3: 'Battery failure',
                      99: 'Any bus module new trouble event'
                      }

    _moduleTroubleRestore = {0: 'Bus / EBus / Wireless module communication fault restore',
                             1: 'Tamper trouble restore',
                             2: 'Power fail restore',
                             3: 'Battery failure restore',
                             99: 'Any bus module trouble restored event'
                             }

    _special = {0: 'System power up',
                1: 'Reporting test',
                2: 'Software log on',
                3: 'Software log off',
                4: 'Installer in programming mode',
                5: 'Installer exited programming mode',
                6: 'Maintenance in programming mode',
                7: 'Maintenance exited programming mode',
                8: 'Closing delinquency delay elapsed',
                99: 'Any special event'
                }

    _systemStatus = {0: 'Follow Arm LED status',
                     1: 'PGM pulse fast in alarm',
                     2: 'PGM pulse fast in exit delay below 10 sec.',
                     3: 'PGM pulse slow in exit delay over 10 sec.',
                     4: 'PGM steady ON if armed',
                     5: 'PGM OFF if disarmed',
                     }

    _eventOpt1 = {1: _pgmNumber[1],
                  2: _pgmNumber[2],
                  3: _pgmNumber[3],
                  4: _pgmNumber[4],
                  5: _pgmNumber[5],
                  6: _pgmNumber[6],
                  7: _pgmNumber[7],
                  8: _pgmNumber[8],
                  9: _pgmNumber[9],
                  10: _pgmNumber[10],
                  11: _pgmNumber[11],
                  12: _pgmNumber[12],
                  13: _pgmNumber[13],
                  14: _pgmNumber[14],
                  15: _pgmNumber[15],
                  16: _pgmNumber[16],
                  17: _wirelessRepeater[1],
                  18: _wirelessRepeater[2],
                  19: _wirelessKeypad[1],
                  20: _wirelessKeypad[2],
                  21: _wirelessKeypad[3],
                  22: _wirelessKeypad[4],
                  27: _wirelessSiren[1],
                  28: _wirelessSiren[2],
                  29: _wirelessSiren[3],
                  30: _wirelessSiren[4],
                  99: 'Any output number'
                  }

    '''dictionary consisting of dictionary'''
    subEventGroupMap = {0: _zoneNumber,
                        1: _zoneNumber,
                        2: _partitionStatus,
                        3: _bellStatus,
                        6: _nonReportableEvents,
                        8: _remoteNumber,
                        9: _remoteNumber,
                        10: _remoteNumber,
                        11: _remoteNumber,
                        12: _zoneNumber,
                        13: _eventOpt1,
                        14: _zoneNumber,
                        15: _zoneNumber,
                        16: _zoneNumber,
                        17: _zoneNumber,
                        18: _zoneNumber,
                        19: _zoneNumber,
                        20: _zoneNumber,
                        21: _zoneNumber,
                        22: _remoteNumber,
                        23: _remoteNumber,
                        24: _zoneNumber,
                        # 25 :_zoneNumber,
                        26: _softwareAccess,
                        27: _busModuleEvent,
                        28: _zoneNumber,
                        29: _userNumber,
                        30: _specialArming,
                        31: _userNumber,
                        32: _userNumber,
                        33: _userNumber,
                        34: _specialDisarming,
                        35: _zoneNumber,
                        36: _zoneNumber,
                        37: _zoneNumber,
                        38: _zoneNumber,
                        39: _zoneNumber,
                        40: _specialAlarm,
                        41: _zoneNumber,
                        42: _zoneNumber,
                        43: _zoneNumber,
                        44: _newTrouble,
                        45: _troubleRestored,
                        46: _moduleTrouble,
                        47: _moduleTroubleRestore,
                        48: _special,
                        49: _zoneNumber,
                        50: _zoneNumber,
                        51: _zoneNumber,
                        52: _zoneNumber,
                        53: _eventOpt1,
                        54: _eventOpt1,
                        55: _eventOpt1,
                        56: _eventOpt1,
                        57: _userNumber,
                        58: _zoneNumber,
                        59: _zoneNumber,
                        64: _systemStatus
                        }

    _partitionLabels = {1: 'Partition 1',
                        2: 'Partition 2'
                        }

    _busModuleLabels = {1: 'Bus Module 1',
                        2: 'Bus Module 2',
                        3: 'Bus Module 3',
                        4: 'Bus Module 4',
                        5: 'Bus Module 5',
                        6: 'Bus Module 6',
                        7: 'Bus Module 7',
                        8: 'Bus Module 8',
                        9: 'Bus Module 9',
                        10: 'Bus Module 10',
                        11: 'Bus Module 11',
                        12: 'Bus Module 12',
                        13: 'Bus Module 13',
                        14: 'Bus Module 14',
                        15: 'Bus Module 15'
                        }

    _siteName = {1: 'Site Name'}

    '''mapping of Label Types'''
    labelTypeMap = {0: 'Zone Label',
                    1: 'User Label',
                    2: 'Partition Label',
                    3: 'PGM Label',
                    4: 'Bus Module Label',
                    5: 'Wireless Repeater Label',
                    6: 'Wireless Keypad Label'}

    @staticmethod
    def getEventGroupDescription(eg):
      try:
        return ParadoxMG5050EventMap.eventGroupMap[eg]
      except KeyError:
        print "No ParadoxMap for: eg=%d"%(eg)
        return "-"
        

    @staticmethod
    def getSubEventGroupDescription(eg, seg):
        try:
          return ParadoxMG5050EventMap.subEventGroupMap[eg][seg]
        except KeyError:
          print "No ParadoxMap for: eg=%d \t seg=%d"%(eg,seg)
          return "-"

    @staticmethod
    def getEventDescription(eg, seg):
        try:
            return ParadoxMG5050EventMap.eventGroupMap[eg], ParadoxMG5050EventMap.subEventGroupMap[eg][seg]
        except KeyError:
            print "No ParadoxMap for: eg=%d \t seg=%d" % (eg, seg)
            return "-"

    @staticmethod
    def getLabelTypeDescription(lt):
        return ParadoxMG5050EventMap.labelTypeMap[lt]

    @staticmethod
    def setZoneName(number, value):
        ParadoxMG5050EventMap._zoneNumber.update({number: value})
        return

    @staticmethod
    def getZoneName(number):
        value = ParadoxMG5050EventMap._zoneNumber[number]
        return value

    @staticmethod
    def getAllZoneNames():
        return ParadoxMG5050EventMap._zoneNumber

    @staticmethod
    def setUserLabel(number, value):
        ParadoxMG5050EventMap._userNumber.update({number: value})
        return

    @staticmethod
    def getAllUserLabels():
        return ParadoxMG5050EventMap._userNumber

    @staticmethod
    def setPartitionLabel(number, value):
        ParadoxMG5050EventMap._partitionLabels.update({number: value})
        return

    @staticmethod
    def getAllPartitionLabels():
        return ParadoxMG5050EventMap._partitionLabels

    @staticmethod
    def setBusModuleLabel(number, value):
        ParadoxMG5050EventMap._busModuleLabels.update({number: value})
        return

    @staticmethod
    def getBusModuleLabel(number):
        value = ParadoxMG5050EventMap._busModuleLabels[number]
        return value

    @staticmethod
    def getAllBusModuleLabels():
        return ParadoxMG5050EventMap._busModuleLabels

    @staticmethod
    def setWirelessRepeaterLabel(number, value):
        ParadoxMG5050EventMap._wirelessRepeater.update({number: value})
        return

    @staticmethod
    def getWirelessRepeaterLabel(number):
        value = ParadoxMG5050EventMap._wirelessRepeater[number]
        return value

    @staticmethod
    def getAllWirelessRepeaterLabels():
        return ParadoxMG5050EventMap._wirelessRepeater

    @staticmethod
    def setWirelessKeypadLabel(number, value):
        ParadoxMG5050EventMap._wirelessKeypad.update({number: value})
        return

    @staticmethod
    def getWirelessKeypadLabel(number):
        value = ParadoxMG5050EventMap._wirelessKeypad[number]
        return value

    @staticmethod
    def getAllWirelessKeypadLabels():
        return ParadoxMG5050EventMap._wirelessKeypad

    @staticmethod
    def setSiteName(number, value):
        ParadoxMG5050EventMap._siteName.update({number: value})
        return

    @staticmethod
    def getSiteName(number):
        value = ParadoxMG5050EventMap._siteName[number]
        return value

    @staticmethod
    def getAllSiteNames():
        return ParadoxMG5050EventMap._siteName

    @staticmethod
    def setWirelessSirenLabel(number, value):
        ParadoxMG5050EventMap._wirelessSiren.update({number: value})
        return

    @staticmethod
    def getWirelessSirenLabel(number):
        value = ParadoxMG5050EventMap._wirelessSiren[number]
        return value

    @staticmethod
    def getAllWirelessSirenLabels():
        return ParadoxMG5050EventMap._wirelessSiren

    @staticmethod
    def setOutputName(number, value):
        ParadoxMG5050EventMap._pgmNumber.update({number: value})
        return

    @staticmethod
    def getOutputName(number):
        value = ParadoxMG5050EventMap._pgmNumber[number]
        return value

    @staticmethod
    def getAllOutputNames():
        return ParadoxMG5050EventMap._pgmNumber

    @staticmethod
    def saveZoneLabels():
        with open('zonesLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._zoneNumber, handle)

    @staticmethod
    def saveUserLabels():
        with open('userLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._userNumber, handle)

    @staticmethod
    def saveRemoteControlLabels():
        with open('remoteControlLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._remoteNumber, handle)

    @staticmethod
    def saveOutputLabels():
        with open('outputLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._pgmNumber, handle)

    @staticmethod
    def savePartitionLabels():
        with open('partitionLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._partitionLabels, handle)

    @staticmethod
    def saveBusModuleLabels():
        with open('busModuleLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._busModuleLabels, handle)

    @staticmethod
    def saveWirelessKeypadLabels():
        with open('wirelessKeypadLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._wirelessKeypad, handle)

    @staticmethod
    def saveWirelessSirenLabels():
        with open('wirelessSirenLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._wirelessSiren, handle)

    @staticmethod
    def saveSiteName():
        with open('siteName.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._siteName, handle)

    @staticmethod
    def saveWirelessRepeaterLabels():
        with open('wirelessRepeaterLabels.pcl', 'wb') as handle:
            pickle.dump(ParadoxMG5050EventMap._wirelessRepeater, handle)

    '''-----------------------Loading of labels from files-------------------------'''

    @staticmethod
    def loadZoneLabels():
        try:
            with open('zonesLabels.pcl', 'rb') as handle:

                return 0, pickle.load(handle)
        except IOError:
            return 1


    @staticmethod
    def loadUserLabels():
        try:
            with open('userLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._userNumber = pickle.load(handle)
                return 0
        except IOError:
            return 1


    @staticmethod
    def loadRemoteControlLabels():
        try:
            with open('remoteControlLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._remoteNumber = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadOutputLabels():
        try:
            with open('outputLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._pgmNumber = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadPartitionLabels():
        try:
            with open('partitionLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._partitionLabels = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadBusModuleLabels():
        try:
            with open('busModuleLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._busModuleLabels = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadWirelessKeypadLabels():
        try:
            with open('wirelessKeypadLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._wirelessKeypad = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadWirelessSirenLabels():
        try:
            with open('wirelessSirenLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._wirelessSiren = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadSiteName():
        try:
            with open('siteName.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._siteName = pickle.load(handle)
                return 0
        except IOError:
            return 1

    @staticmethod
    def loadWirelessRepeaterLabels():
        try:
            with open('wirelessRepeaterLabels.pcl', 'rb') as handle:
                ParadoxMG5050EventMap._wirelessRepeater = pickle.load(handle)
                return 0
        except IOError:
            return 1





if __name__ == '__main__':
    print "Loaded Paradox Mapping"
    #print ParadoxEventMap.getEventGroupDescription(0)
    #print ParadoxEventMap.getSubEventGroupDescription(1,22)
    #print ParadoxEventMap.getEventDescription(34,2)
