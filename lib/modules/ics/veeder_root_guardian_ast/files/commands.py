#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from config import module_configuration


# todo: dynamic numbers
# todo add delay

def now(model="%b  %d, %Y %I:%M %p"):
    return datetime.datetime.now().strftime(model)


def I10100():
    return "".join(
        [
            '\x01\r\nI10100\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'SYSTEM STATUS REPORT',
            '\r\n\r\n',
            'D 8:ALARM CLEAR WARNING',
            '\r\n\r\n',
            '\x03'
        ]
    )


def I10200():
    return "".join(
        [
            '\x01\r\nI10200\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'SYSTEM CONFIGURATION',
            '\r\n\r\n',
            'SLOT  BOARD TYPE                    POWER ON RESET     CURRENT\r\n',
            '  1   PLLD SENSOR BD                     3882             3864\r\n',
            '  2   INTERSTITIAL BD                  202440           201698\r\n',
            '  3   8SMARTSENSOR BD                   39681            39594\r\n',
            '  4   4 PROBE / G.T.                   164489           164087\r\n',
            '  5   UNUSED                          9922452          9806112\r\n',
            '  6   UNUSED                          9895411          9794026\r\n',
            '  7   UNUSED                          9911016          9789239\r\n',
            '  8   UNUSED                          9892610          9806957\r\n',
            '  9   PLLD POWER BD                    100307           100205\r\n',
            ' 10   PLLD POWER BD                    100133            99984\r\n',
            ' 11   UNUSED                          9902247          9793640\r\n',
            ' 12   UNUSED                          9906330          9807243\r\n',
            ' 13   UNUSED                          9885509          9793619\r\n',
            ' 14   UNUSED                          9904257          9790045\r\n',
            ' 15   UNUSED                          9893889          9800940\r\n',
            ' 16   UNUSED                          9890811          9786016\r\n',
            '      COMM 1 ELEC DISP INT.            100852           100802\r\n',
            '      COMM 2 SERIAL SAT BD             481672           480551\r\n',
            '      COMM 3 UNUSED                   9906416          9803929\r\n',
            '      COMM 4 UNUSED                   9884056          9782746\r\n',
            '      COMM 5 UNUSED                   9898186          9806203\r\n',
            '      COMM 6 UNUSED                   9890469          9786623\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I11100():
    return "".join(
        [
            '\x01\r\nI11100\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'PRIORITY ALARM HISTORY\r\n',
            'ID  CATEGORY  DESCRIPTION          ALARM TYPE           STATE    DATE    TIME\r\n',
            'Q 4 OTHER     DIESEL               PERIODIC LINE FAIL   CLEAR   7-09-18  2:49PM\r\n',
            'Q 4 OTHER     DIESEL               PERIODIC LINE FAIL   ALARM   7-09-18  4:36AM\r\n',
            'Q 4 OTHER     DIESEL               PLLD SHUTDOWN ALARM  CLEAR   6-19-18  9:01AM\r\n',
            'Q 4 OTHER     DIESEL               GROSS LINE FAIL      CLEAR   6-19-18  9:01AM\r\n',
            'Q 4 OTHER     DIESEL               PLLD SHUTDOWN ALARM  ALARM   6-19-18  8:46AM\r\n',
            'Q 4 OTHER     DIESEL               GROSS LINE FAIL      ALARM   6-19-18  8:46AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   5-10-18 11:29AM\r\n',
            'Q 3 OTHER     SUPREME              GROSS LINE FAIL      CLEAR   5-10-18 11:29AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   5-10-18 11:24AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  ALARM   5-10-18 10:52AM\r\n',
            'Q 3 OTHER     SUPREME              GROSS LINE FAIL      ALARM   5-10-18 10:52AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        ALARM   5-10-18 10:43AM\r\n',
            'Q 4 OTHER     DIESEL               PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:34AM\r\n',
            'Q 4 OTHER     DIESEL               GROSS LINE FAIL      CLEAR   4-19-18 11:34AM\r\n',
            'Q 2 OTHER     PLUS                 PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:33AM\r\n',
            'Q 2 OTHER     PLUS                 GROSS LINE FAIL      CLEAR   4-19-18 11:33AM\r\n',
            'Q 1 OTHER     REGULAR              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:33AM\r\n',
            'Q 1 OTHER     REGULAR              GROSS LINE FAIL      CLEAR   4-19-18 11:33AM\r\n',
            'L 2 ANNULAR   PLUS ANNULAR         FUEL ALARM           CLEAR   4-19-18 11:09AM\r\n',
            'L 2 ANNULAR   PLUS ANNULAR         FUEL ALARM           ALARM   4-19-18 11:06AM\r\n',
            'L 1 ANNULAR   REGULAR ANNULAR      FUEL ALARM           CLEAR   4-19-18 11:01AM\r\n',
            'L 1 ANNULAR   REGULAR ANNULAR      FUEL ALARM           ALARM   4-19-18 11:00AM\r\n',
            'L 4 ANNULAR   DIESEL ANNULAR       FUEL ALARM           CLEAR   4-19-18 10:55AM\r\n',
            'L 4 ANNULAR   DIESEL ANNULAR       FUEL ALARM           ALARM   4-19-18 10:51AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   4-19-18 10:46AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        ALARM   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              WATER ALARM          CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              WATER ALARM          ALARM   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  ALARM   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              FUEL ALARM           CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              FUEL ALARM           ALARM   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  ALARM   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        ALARM   4-19-18 10:44AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:43AM\r\n',
            's 6 OTHER     3,4 PAN              WATER ALARM          CLEAR   4-19-18 10:43AM\r\n',
            's 6 OTHER     3,4 PAN              WATER ALARM          ALARM   4-19-18 10:42AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  ALARM   4-19-18 10:42AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:42AM\r\n',
            's 6 OTHER     3,4 PAN              FUEL ALARM           CLEAR   4-19-18 10:42AM\r\n',
            's 6 OTHER     3,4 PAN              FUEL ALARM           ALARM   4-19-18 10:42AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  ALARM   4-19-18 10:42AM\r\ns',
            ' 7 OTHER     5,6 PAN-DIESEL       WATER ALARM          CLEAR   4-19-18 10:41AM\r\n',
            's 7 OTHER     5,6 PAN-DIESEL       WATER ALARM          ALARM   4-19-18 10:41AM\r\n',
            's 7 OTHER     5,6 PAN-DIESEL       FUEL ALARM           CLEAR   4-19-18 10:41AM\r\n',
            's 7 OTHER     5,6 PAN-DIESEL       FUEL ALARM           ALARM   4-19-18 10:41AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:40AM\r\n',
            's 5 OTHER     1,2 PAN              WATER ALARM          CLEAR   4-19-18 10:40AM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I11200():
    return "".join(
        [
            '\x01\r\nI11200\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'NON-PRIORITY ALARM HISTORY\r\n',
            'ID  CATEGORY  DESCRIPTION          ALARM TYPE           STATE    DATE    TIME\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   8-02-18  5:36AM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      ALARM   8-02-18  5:09AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   7-24-18  4:17PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   7-24-18  1:36PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   6-29-18  5:40PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      ALARM   6-29-18  2:58AM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   6-20-18 12:15AM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   6-19-18  6:29PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   6-14-18  3:11PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   6-14-18  1:56PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   6-06-18  5:50PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   6-06-18  1:52PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   5-18-18  6:11AM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   5-18-18  6:11AM\r\n',
            '    SYSTEM                         PRINTER ERROR        ALARM   5-18-18  6:10AM\r\n',
            '    SYSTEM                         PAPER OUT            ALARM   5-18-18  6:10AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   5-15-18 10:03PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   5-15-18  9:58PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   5-15-18  6:56PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   5-15-18  6:49PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   5-11-18  3:08PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   5-11-18  3:07PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   5-11-18 12:07PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   5-10-18 10:52PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   5-08-18  1:08PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      ALARM   5-07-18  3:16PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-26-18 10:47PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   4-26-18 12:43PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-23-18  8:34PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   4-23-18  6:29PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   4-20-18  6:15PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   4-20-18  5:50PM\r\n',
            's 1 OTHER     REGULAR STP SUMP     WATER WARNING        CLEAR   4-19-18 10:31AM\r\n',
            's 1 OTHER     REGULAR STP SUMP     WATER WARNING        ALARM   4-19-18 10:31AM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-14-18 11:34PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   4-14-18  2:39PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-10-18  9:03PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      ALARM   4-10-18 11:01AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   4-04-18 12:33AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      ALARM   4-03-18 11:06PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        ALARM   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        ALARM   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PAPER OUT            ALARM   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        ALARM   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   3-30-18  9:58PM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I11300():
    return "".join(
        [
            '\x01\r\nI11300\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'ACTIVE ALARMS REPORT',
            '\r\n\r\n',
            'ID  CATEGORY  DESCRIPTION          ALARM TYPE             DATE    TIME\r\n',
            'D 8  OTHER    VEEDER ROOT (FMS)    ALARM CLEAR WARNING  \r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I11400():
    return "".join(
        [
            '\x01\r\nI11400\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'CLEARED ALARMS REPORT',
            '\r\n\r\n',
            'ID  CATEGORY  DESCRIPTION          ALARM TYPE           STATE    DATE    TIME\r\n',
            'Q 4 OTHER     DIESEL               PERIODIC LINE FAIL   CLEAR   7-09-18  2:49PM\r\n',
            'Q 4 OTHER     DIESEL               PLLD SHUTDOWN ALARM  CLEAR   6-19-18  9:01AM\r\n',
            'Q 4 OTHER     DIESEL               GROSS LINE FAIL      CLEAR   6-19-18  9:01AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   5-10-18 11:29AM\r\n',
            'Q 3 OTHER     SUPREME              GROSS LINE FAIL      CLEAR   5-10-18 11:29AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   5-10-18 11:24AM\r\n',
            'Q 4 OTHER     DIESEL               PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:34AM\r\n',
            'Q 4 OTHER     DIESEL               GROSS LINE FAIL      CLEAR   4-19-18 11:34AM\r\n',
            'Q 2 OTHER     PLUS                 PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:33AM\r\n',
            'Q 2 OTHER     PLUS                 GROSS LINE FAIL      CLEAR   4-19-18 11:33AM\r\n',
            'Q 1 OTHER     REGULAR              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 11:33AM\r\n',
            'Q 1 OTHER     REGULAR              GROSS LINE FAIL      CLEAR   4-19-18 11:33AM\r\n',
            'L 2 ANNULAR   PLUS ANNULAR         FUEL ALARM           CLEAR   4-19-18 11:09AM\r\n',
            'L 1 ANNULAR   REGULAR ANNULAR      FUEL ALARM           CLEAR   4-19-18 11:01AM\r\n',
            'L 4 ANNULAR   DIESEL ANNULAR       FUEL ALARM           CLEAR   4-19-18 10:55AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   4-19-18 10:46AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              WATER ALARM          CLEAR   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              FUEL ALARM           CLEAR   4-19-18 10:45AM\r\n',
            's 8 OTHER     7,8 PAN              INSTALL ALARM        CLEAR   4-19-18 10:45AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:43AM\r\n',
            's 6 OTHER     3,4 PAN              WATER ALARM          CLEAR   4-19-18 10:43AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:42AM\r\n',
            's 6 OTHER     3,4 PAN              FUEL ALARM           CLEAR   4-19-18 10:42AM\r\n',
            's 7 OTHER     5,6 PAN-DIESEL       WATER ALARM          CLEAR   4-19-18 10:41AM\r\n',
            's 7 OTHER     5,6 PAN-DIESEL       FUEL ALARM           CLEAR   4-19-18 10:41AM\r\n',
            'Q 3 OTHER     SUPREME              PLLD SHUTDOWN ALARM  CLEAR   4-19-18 10:40AM\r\n',
            's 5 OTHER     1,2 PAN              WATER ALARM          CLEAR   4-19-18 10:40AM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   8-02-18  5:36AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   7-24-18  4:17PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   6-29-18  5:40PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   6-20-18 12:15AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   6-14-18  3:11PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   6-06-18  5:50PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   5-18-18  6:11AM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   5-18-18  6:11AM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   5-15-18 10:03PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   5-15-18  9:58PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   5-11-18  3:08PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   5-11-18  3:07PM\r\n',
            'T 4 TANK      DIESEL               DELIVERY NEEDED      CLEAR   5-08-18  1:08PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-26-18 10:47PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-23-18  8:34PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   4-20-18  6:15PM\r\n',
            's 1 OTHER     REGULAR STP SUMP     WATER WARNING        CLEAR   4-19-18 10:31AM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-14-18 11:34PM\r\n',
            'T 3 TANK      SUPREME              DELIVERY NEEDED      CLEAR   4-10-18  9:03PM\r\n',
            'T 1 TANK      REGULAR              DELIVERY NEEDED      CLEAR   4-04-18 12:33AM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PRINTER ERROR        CLEAR   3-30-18  9:58PM\r\n',
            '    SYSTEM                         PAPER OUT            CLEAR   3-30-18  9:58PM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20100():
    return "".join(
        [
            "\x01\r\nI20100\r\n",
            now(),
            "\r\n\r\n",
            module_configuration()["company_name_address"],
            "\r\n\r\n",
            "IN-TANK INVENTORY       \r\n",
            "\r\n",
            "TANK PRODUCT             VOLUME TC VOLUME   ULLAGE   HEIGHT    WATER     TEMP\r\n",
            "  1  REGULAR               1693         0     9755    18.75     0.00    76.26\r\n",
            "  2  PLUS                  1788         0     6003    25.65     0.89    74.02\r\n",
            "  3  SUPREME               1748         0     7871    21.71     0.76    75.99\r\n",
            "  4  DIESEL                2147         0     7472    25.04     0.00    75.48\r\n",
            "\r\n",
            "\x03"
        ]
    )


def I20200():
    return "".join(
        [
            '\x01\r\nI20200\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'DELIVERY REPORT',
            '\r\n\r\n',
            'T 1:REGULAR\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  7, 2018  5:29 AM      9001       8908  0.00       74.67   65.05\r\n',
            '    START: AUG  7, 2018  4:55 AM      1693       1674  0.00       76.24   18.75\r\n',
            '   AMOUNT:                            7308       7234\r\n\r\n',
            '      END: AUG  4, 2018 10:03 AM      7816       7736  0.00       74.62   57.41\r\n',
            '    START: AUG  4, 2018  9:38 AM      2099       2076  0.00       75.67   21.76\r\n',
            '   AMOUNT:                            5717       5660\r\n\r\n',
            '      END: AUG  2, 2018  5:53 AM      7564       7488  0.00       74.18   55.85\r\n',
            '    START: AUG  2, 2018  5:35 AM      2517       2488  0.00       76.30   24.69\r\n',
            '   AMOUNT:                            5047       5000\r\n\r\n',
            '      END: AUG  1, 2018  1:23 AM      5147       5087  0.00       76.40   41.31\r\n',
            '    START: AUG  1, 2018  1:09 AM      2452       2419  0.00       78.47   24.24\r\n',
            '   AMOUNT:                            2695       2668\r\n\r\n',
            '      END: JUL 29, 2018  1:04 PM      8923       8809  0.00       78.22   64.53\r\n',
            '    START: JUL 29, 2018 12:32 PM      1214       1198  0.00       77.64   14.93\r\n',
            '   AMOUNT:                            7709       7611\r\n\r\n',
            '      END: JUL 25, 2018  2:22 PM      9923       9816  0.00       75.38   71.58\r\n',
            '    START: JUL 25, 2018  1:54 PM      2162       2138  0.00       75.73   22.21\r\n',
            '   AMOUNT:                            7761       7678\r\n\r\n',
            '      END: JUL 24, 2018  4:29 PM      4070       4024  0.00       75.96   34.75\r\n',
            '    START: JUL 24, 2018  4:16 PM       810        800  0.00       77.38   11.35\r\n',
            '   AMOUNT:                            3260       3224\r\n\r\n',
            '      END: JUL 21, 2018  9:05 PM      6562       6506  0.00       72.05   49.78\r\n',
            '    START: JUL 21, 2018  8:41 PM      1558       1537  0.00       78.74   17.71\r\n',
            '   AMOUNT:                            5004       4969\r\n\r\n',
            '      END: JUL 18, 2018  2:27 PM      9446       9324  0.00       78.47   68.11\r\n',
            '    START: JUL 18, 2018  2:00 PM      1662       1643  0.00       76.02   18.51\r\n',
            '   AMOUNT:                            7784       7681\r\n\r\n',
            '      END: JUL 17, 2018  2:35 AM      5632       5572  0.00       74.93   44.22\r\n',
            '    START: JUL 17, 2018  2:19 AM      1439       1423  0.00       75.78   16.77\r\n',
            '   AMOUNT:                            4193       4149\r\n\r\n',
            'T 2:PLUS\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  4, 2018  9:50 AM      2583       2554  0.89       75.49   33.18\r\n',
            '    START: AUG  4, 2018  9:38 AM      1387       1373  0.89       74.06   21.55\r\n',
            '   AMOUNT:                            1196       1181\r\n\r\n',
            '      END: AUG  1, 2018  1:21 AM      2510       2483  0.89       74.72   32.52\r\n',
            '    START: AUG  1, 2018  1:10 AM       821        812  0.90       74.48   15.10\r\n',
            '   AMOUNT:                            1689       1671\r\n\r\n',
            '      END: JUL 26, 2018  4:17 AM      2569       2544  0.90       73.61   33.06\r\n',
            '    START: JUL 26, 2018  4:05 AM       871        862  0.89       74.07   15.72\r\n',
            '   AMOUNT:                            1698       1682\r\n\r\n',
            '      END: JUL 21, 2018  9:01 PM      1903       1887  0.89       71.50   26.78\r\n',
            '    START: JUL 21, 2018  8:50 PM       902        893  0.84       73.68   16.09\r\n',
            '   AMOUNT:                            1001        994\r\n\r\n',
            '      END: JUL 14, 2018  7:02 AM      2966       2938  0.85       73.21   36.64\r\n',
            '    START: JUL 14, 2018  6:53 AM      1956       1939  0.88       71.84   27.30\r\n',
            '   AMOUNT:                            1010        999\r\n\r\n',
            '      END: JUL 11, 2018  1:46 AM      2893       2865  0.88       73.75   35.98\r\n',
            '    START: JUL 11, 2018  1:34 AM      1192       1182  0.90       71.36   19.42\r\n',
            '   AMOUNT:                            1701       1683\r\n\r\n',
            '      END: JUL  2, 2018  6:01 AM      3040       3013  0.89       72.37   37.29\r\n',
            '    START: JUL  2, 2018  5:51 AM      1344       1333  0.90       70.47   21.08\r\n',
            '   AMOUNT:                            1696       1680\r\n\r\n',
            '      END: JUN 27, 2018  4:50 AM      2709       2687  0.90       71.63   34.33\r\n',
            '    START: JUN 27, 2018  4:41 AM      1682       1668  0.92       71.49   24.60\r\n',
            '   AMOUNT:                            1027       1019\r\n\r\n',
            '      END: JUN 24, 2018  3:33 PM      2352       2328  0.88       74.07   31.06\r\n',
            '    START: JUN 24, 2018  3:24 PM      1352       1342  0.89       70.32   21.17\r\n',
            '   AMOUNT:                            1000        986\r\n\r\n',
            '      END: JUN 21, 2018 11:29 PM      2055       2037  0.88       71.97   28.26\r\n',
            '    START: JUN 21, 2018 11:18 PM      1061       1053  0.89       70.07   17.95\r\n',
            '   AMOUNT:                             994        984\r\n\r\n',
            'T 3:SUPREME\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  7, 2018  5:09 AM      2991       2955  0.76       76.83   31.61\r\n',
            '    START: AUG  7, 2018  5:01 AM      1748       1728  0.76       75.98   21.71\r\n',
            '   AMOUNT:                            1243       1227\r\n\r\n',
            '      END: AUG  4, 2018  9:55 AM      2911       2874  0.77       77.51   31.01\r\n',
            '    START: AUG  4, 2018  9:45 AM      1180       1167  0.76       76.00   16.59\r\n',
            '   AMOUNT:                            1731       1707\r\n\r\n',
            '      END: AUG  2, 2018  5:52 AM      1979       1956  0.77       76.39   23.66\r\n',
            '    START: AUG  2, 2018  5:45 AM       987        975  0.77       76.33   14.70\r\n',
            '   AMOUNT:                             992        981\r\n\r\n',
            '      END: JUL 29, 2018 12:45 PM      2330       2300  0.77       78.02   26.51\r\n',
            '    START: JUL 29, 2018 12:34 PM      1335       1319  0.76       76.17   18.04\r\n',
            '   AMOUNT:                             995        981\r\n\r\n',
            '      END: JUL 25, 2018  1:57 PM      2908       2871  0.77       77.83   30.99\r\n',
            '    START: JUL 25, 2018  1:51 PM      1913       1890  0.76       76.62   23.11\r\n',
            '   AMOUNT:                             995        981\r\n\r\n',
            '      END: JUL 24, 2018  4:33 PM      2103       2078  0.77       76.49   24.68\r\n',
            '    START: JUL 24, 2018  4:25 PM      1099       1086  0.77       75.86   15.81\r\n',
            '   AMOUNT:                            1004        992\r\n\r\n',
            '      END: JUL 18, 2018  2:03 PM      3212       3175  0.76       76.34   33.27\r\n',
            '    START: JUL 18, 2018  1:54 PM      2217       2196  0.76       73.43   25.61\r\n',
            '   AMOUNT:                             995        979\r\n\r\n',
            '      END: JUL 14, 2018  7:05 AM      3477       3440  0.76       75.05   35.22\r\n',
            '    START: JUL 14, 2018  6:52 AM      1789       1771  0.76       73.53   22.06\r\n',
            '   AMOUNT:                            1688       1669\r\n\r\n',
            '      END: JUL 11, 2018  1:49 AM      3150       3118  0.76       74.63   32.81\r\n',
            '    START: JUL 11, 2018  1:40 AM      1954       1936  0.76       72.58   23.45\r\n',
            '   AMOUNT:                            1196       1182\r\n\r\n',
            '      END: JUL  7, 2018  5:41 AM      3247       3216  0.76       73.58   33.53\r\n',
            '    START: JUL  7, 2018  5:30 AM      1312       1300  0.76       72.58   17.83\r\n',
            '   AMOUNT:                            1935       1916\r\n\r\n',
            'T 4:DIESEL\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  2, 2018  5:51 AM      3267       3240  0.00       77.40   33.67\r\n',
            '    START: AUG  2, 2018  5:36 AM       988        980  0.00       76.85   14.70\r\n',
            '   AMOUNT:                            2279       2260\r\n\r\n',
            '      END: JUL 21, 2018  8:54 PM      3399       3378  0.00       72.94   34.65\r\n',
            '    START: JUL 21, 2018  8:40 PM      1117       1108  0.00       76.97   15.98\r\n',
            '   AMOUNT:                            2282       2270\r\n\r\n',
            '      END: JUL  9, 2018  3:02 AM      3662       3639  0.00       73.90   36.57\r\n',
            '    START: JUL  9, 2018  2:39 AM      1376       1367  0.00       75.00   18.42\r\n',
            '   AMOUNT:                            2286       2272\r\n\r\n',
            '      END: JUN 29, 2018  5:52 PM      2979       2945  0.00       84.83   31.52\r\n',
            '    START: JUN 29, 2018  5:39 PM       697        692  0.00       74.63   11.62\r\n',
            '   AMOUNT:                            2282       2253\r\n\r\n',
            '      END: JUN 20, 2018 12:18 AM      3461       3437  0.00       75.22   35.10\r\n',
            '    START: JUN 20, 2018 12:04 AM      1176       1170  0.00       71.16   16.55\r\n',
            '   AMOUNT:                            2285       2267\r\n\r\n',
            '      END: JUN 12, 2018  4:22 AM      3785       3772  0.00       67.46   37.46\r\n',
            '    START: JUN 12, 2018  4:07 AM      1316       1309  0.00       70.96   17.86\r\n',
            '   AMOUNT:                            2469       2463\r\n\r\n',
            '      END: JUN  4, 2018  6:35 PM      3391       3364  0.00       77.20   34.59\r\n',
            '    START: JUN  4, 2018  6:22 PM      1108       1103  0.00       69.30   15.89\r\n',
            '   AMOUNT:                            2283       2261\r\n\r\n',
            '      END: MAY 23, 2018  9:06 AM      3667       3652  0.00       68.84   36.61\r\n',
            '    START: MAY 23, 2018  8:51 AM      1381       1376  0.00       67.20   18.46\r\n',
            '   AMOUNT:                            2286       2276\r\n\r\n',
            '      END: MAY 13, 2018  6:20 AM      3770       3756  0.00       67.62   37.35\r\n',
            '    START: MAY 13, 2018  6:07 AM      1485       1480  0.00       66.82   19.41\r\n',
            '   AMOUNT:                            2285       2276\r\n\r\n',
            '      END: MAY  8, 2018  1:19 PM      3133       3118  0.00       69.97   32.68\r\n',
            '    START: MAY  8, 2018  1:07 PM       857        855  0.00       64.64   13.36\r\n',
            '   AMOUNT:                            2276       2263\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20300():
    return "".join(
        [
            '\x01\r\nI20300\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'TANK 1    REGULAR                \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n',
            '\r\n\r\n',
            'TANK 2    PLUS                   \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n',
            '\r\n\r\n',
            'TANK 3    SUPREME                \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n',
            '\r\n\r\n',
            'TANK 4    DIESEL                 \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n',
            '\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20400():
    return "".join(
        [
            '\x01\r\nI20400\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            ' SHIFT REPORT \r\n\r\n',
            'SHIFT 1 TIME: 12:00 AM        \r\n\r\n',
            'TANK PRODUCT\r\n\r\n',
            '  1  REGULAR                VOLUME TC VOLUME  ULLAGE  HEIGHT  WATER   TEMP\r\n',
            'SHIFT  1 STARTING VALUES      4672      4621    6776   38.44   0.00  75.53\r\n',
            '         ENDING VALUES        1724      1704    9724   18.99   0.00  76.41\r\n',
            '         DELIVERY VALUE          0\r\n',
            '         TOTALS               2948\r\n\r\n',
            '  2  PLUS                   VOLUME TC VOLUME  ULLAGE  HEIGHT  WATER   TEMP\r\n',
            'SHIFT  1 STARTING VALUES      2133      2111    5658   29.00   0.89  74.16\r\n',
            '         ENDING VALUES        1788      1770    6003   25.66   0.89  74.18\r\n',
            '         DELIVERY VALUE          0\r\n',
            '         TOTALS                345\r\n\r\n',
            '  3  SUPREME                VOLUME TC VOLUME  ULLAGE  HEIGHT  WATER   TEMP\r\n',
            'SHIFT  1 STARTING VALUES      2204      2178    7415   25.50   0.76  76.20\r\n',
            '         ENDING VALUES        1765      1745    7854   21.86   0.76  76.13\r\n',
            '         DELIVERY VALUE          0\r\n',
            '         TOTALS                439\r\n\r\n',
            '  4  DIESEL                 VOLUME TC VOLUME  ULLAGE  HEIGHT  WATER   TEMP\r\n',
            'SHIFT  1 STARTING VALUES      2459      2442    7160   27.53   0.00  75.20\r\n',
            '         ENDING VALUES        2147      2132    7472   25.04   0.00  75.58\r\n',
            '         DELIVERY VALUE          0\r\n',
            '         TOTALS                312\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20500():
    return "".join(
        [
            '\x01\r\nI20500\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'TANK   PRODUCT                 STATUS\r\n\r\n',
            '  1    REGULAR                 NORMAL\r\n\r\n',
            '  2    PLUS                    NORMAL\r\n\r\n  3',
            '    SUPREME                 NORMAL\r\n\r\n',
            '  4    DIESEL                  NORMAL\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20600():
    return "".join(
        [
            '\x01\r\nI20600\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n\r\n',
            'TANK ALARM HISTORY\r\n\r\n',
            'TANK 1  REGULAR             \r\n\r\n',
            '     OVERFILL ALARM           FEB  8, 2018  5:29 AM\r\n\r\n',
            '     LOW PRODUCT ALARM        OCT 12, 2017  2:32 PM\r\n',
            '                              SEP 18, 2017  4:09 PM\r\n\r\n',
            '     SUDDEN LOSS ALARM        FEB 21, 2017  8:02 AM\r\n\r\n',
            '     PROBE OUT                FEB 21, 2017  8:02 AM\r\n\r\n',
            '     DELIVERY NEEDED          JUL 24, 2018  1:36 PM\r\n',
            '                              JUN 14, 2018  1:56 PM\r\n',
            '                              MAY 15, 2018  6:56 PM\r\n\r\n',
            'TANK 2  PLUS                \r\n\r\n',
            '     HIGH WATER ALARM         APR 20, 2017  2:10 PM\r\n\r\n',
            '     OVERFILL ALARM           APR 20, 2017  2:03 PM\r\n\r\n',
            '     LOW PRODUCT ALARM        APR 20, 2017  2:01 PM\r\n',
            '                              FEB 21, 2017  8:21 AM\r\n\r\n',
            '     HIGH PRODUCT ALARM       APR 20, 2017  2:04 PM\r\n\r\n',
            '     INVALID FUEL LEVEL       APR 20, 2017  2:01 PM\r\n\r\n',
            '     PROBE OUT                APR 20, 2017  2:33 PM\r\n',
            '                              APR 20, 2017  2:00 PM\r\n\r\n',
            '     HIGH WATER WARNING       APR 20, 2017  2:10 PM\r\n\r\n',
            '     DELIVERY NEEDED          OCT  7, 2017  7:12 PM\r\n',
            '                              SEP 18, 2017  5:44 PM\r\n',
            '                              JUN 26, 2017  5:31 PM\r\n\r\n',
            '     MAX PRODUCT ALARM        APR 20, 2017  2:04 PM\r\n\r\n',
            'TANK 3  SUPREME             \r\n\r\n',
            '     HIGH WATER ALARM         APR 20, 2017  2:11 PM\r\n\r\n',
            '     OVERFILL ALARM           APR 20, 2017  2:04 PM\r\n\r\n',
            '     LOW PRODUCT ALARM        MAY 20, 2017  4:38 PM\r\n',
            '                              APR 20, 2017  2:03 PM\r\n\r\n',
            '     SUDDEN LOSS ALARM        APR 20, 2017  2:02 PM\r\n\r\n',
            '     HIGH PRODUCT ALARM       APR 20, 2017  2:04 PM\r\n\r\n',
            '     INVALID FUEL LEVEL       APR 20, 2017  2:03 PM\r\n\r\n',
            '     PROBE OUT                APR 20, 2017  2:30 PM\r\n',
            '                              APR 20, 2017  2:02 PM\r\n\r\n',
            '     HIGH WATER WARNING       APR 20, 2017  2:11 PM\r\n\r\n',
            '     DELIVERY NEEDED          JUN 19, 2018  6:29 PM\r\n',
            '                              JUN  6, 2018  1:52 PM\r\n',
            '                              MAY 15, 2018  6:49 PM\r\n\r\n',
            '     MAX PRODUCT ALARM        APR 20, 2017  2:04 PM\r\n\r\n',
            'TANK 4  DIESEL              \r\n\r\n',
            '     LOW PRODUCT ALARM        AUG 11, 2017  9:40 AM\r\n',
            '                              AUG 11, 2017  9:02 AM\r\n',
            '                              AUG 11, 2017  8:55 AM\r\n\r\n',
            '     SUDDEN LOSS ALARM        AUG 11, 2017  8:55 AM\r\n\r\n',
            '     INVALID FUEL LEVEL       AUG 11, 2017  9:40 AM\r\n',
            '                              AUG 11, 2017  9:02 AM\r\n',
            '                              AUG 11, 2017  8:55 AM\r\n\r\n',
            '     PROBE OUT                AUG 11, 2017  8:56 AM\r\n\r\n',
            '     DELIVERY NEEDED          AUG  2, 2018  5:09 AM\r\n',
            '                              JUN 29, 2018  2:58 AM\r\n',
            '                              MAY  7, 2018  3:16 PM\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20700():
    return "".join(
        [
            '\x01\r\nI20700\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n\r\n',
            'TANK LEAK TEST HISTORY\r\n\r\n',
            'T 1:REGULAR\r\n\r\n',
            'LAST GROSS TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST ANNUAL TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'FULLEST ANNUAL TEST PASS\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST PERIODIC TEST PASS:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n\r\n',
            'FULLEST PERIODIC TEST\r\n',
            'PASSED EACH MONTH:\r\n\r\n',
            'TEST START TIME            HOURS    VOLUME   % VOLUME   TEST TYPE\r\n\r\n\r\n\r\n',
            'TANK LEAK TEST HISTORY\r\n\r\n',
            'T 2:PLUS\r\n\r\n',
            'LAST GROSS TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST ANNUAL TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'FULLEST ANNUAL TEST PASS\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST PERIODIC TEST PASS:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n\r\n',
            'FULLEST PERIODIC TEST\r\n',
            'PASSED EACH MONTH:\r\n\r\n',
            'TEST START TIME            HOURS    VOLUME   % VOLUME   TEST TYPE\r\n\r\n\r\n\r\n',
            'TANK LEAK TEST HISTORY\r\n\r\n',
            'T 3:SUPREME\r\n\r\n',
            'LAST GROSS TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST ANNUAL TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'FULLEST ANNUAL TEST PASS\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST PERIODIC TEST PASS:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n\r\n',
            'FULLEST PERIODIC TEST\r\n',
            'PASSED EACH MONTH:\r\n\r\n',
            'TEST START TIME            HOURS    VOLUME   % VOLUME   TEST TYPE\r\n\r\n\r\n\r\n',
            'TANK LEAK TEST HISTORY\r\n\r\n',
            'T 4:DIESEL\r\n\r\n',
            'LAST GROSS TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST ANNUAL TEST PASSED:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'FULLEST ANNUAL TEST PASS\r\n\r\n',
            'NO TEST PASSED\r\n\r\n',
            'LAST PERIODIC TEST PASS:\r\n\r\n',
            'NO TEST PASSED\r\n\r\n\r\n',
            'FULLEST PERIODIC TEST\r\n',
            'PASSED EACH MONTH:\r\n\r\n',
            'TEST START TIME            HOURS    VOLUME   % VOLUME   TEST TYPE\r\n\r\n\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20800():
    return "".join(
        [
            '\x01\r\nI20800\r\n',
            now(),
            '\r\n\r\n',
            'PREVIOUS IN TANK LEAK TEST RESULTS\r\n\r\n',
            'TANK 1    REGULAR                \r\n',
            'TEST TYPE  START TIME              RESULT     RATE  HOURS  VOLUME\r\n',
            ' ANNUAL    NO TEST DATA AVAILABLE\r\n',
            ' PERIODIC  NO TEST DATA AVAILABLE\r\n',
            ' GROSS     NO TEST DATA AVAILABLE\r\n\r\n',
            'TANK 2    PLUS                   \r\n',
            'TEST TYPE  START TIME              RESULT     RATE  HOURS  VOLUME\r\n',
            ' ANNUAL    NO TEST DATA AVAILABLE\r\n',
            ' PERIODIC  NO TEST DATA AVAILABLE\r\n',
            ' GROSS     NO TEST DATA AVAILABLE\r\n\r\n',
            'TANK 3    SUPREME                \r\n',
            'TEST TYPE  START TIME              RESULT     RATE  HOURS  VOLUME\r\n',
            ' ANNUAL    NO TEST DATA AVAILABLE\r\n',
            ' PERIODIC  NO TEST DATA AVAILABLE\r\n',
            ' GROSS     NO TEST DATA AVAILABLE\r\n\r\n',
            'TANK 4    DIESEL                 \r\n',
            'TEST TYPE  START TIME              RESULT     RATE  HOURS  VOLUME\r\n',
            ' ANNUAL    NO TEST DATA AVAILABLE\r\n',
            ' PERIODIC  NO TEST DATA AVAILABLE\r\n',
            ' GROSS     NO TEST DATA AVAILABLE\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20900():
    return "".join(
        [
            '\x01\r\nI20900\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'TANK 1    REGULAR                \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n\r\n\r\n',
            'TANK 2    PLUS                   \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n\r\n\r\n',
            'TANK 3    SUPREME                \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n\r\n\r\n',
            'TANK 4    DIESEL                 \r\n',
            '    TEST STATUS: OFF   \r\n',
            'LEAK DATA NOT AVAILABLE ON THIS TANK\r\n\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20C00():
    return "".join(
        [
            '\x01\r\nI20C00\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'LAST DELIVERY REPORT\r\n\r\n',
            'T 1:REGULAR\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  7, 2018  5:29 AM      9001       8908  0.00       74.67   65.05\r\n',
            '    START: AUG  7, 2018  4:55 AM      1693       1674  0.00       76.24   18.75\r\n',
            '   AMOUNT:                            7308       7234\r\n\r\n',
            'T 2:PLUS\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  4, 2018  9:50 AM      2583       2554  0.89       75.49   33.18\r\n',
            '    START: AUG  4, 2018  9:38 AM      1387       1373  0.89       74.06   21.55\r\n',
            '   AMOUNT:                            1196       1181\r\n\r\n',
            'T 3:SUPREME\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  7, 2018  5:09 AM      2991       2955  0.76       76.83   31.61\r\n',
            '    START: AUG  7, 2018  5:01 AM      1748       1728  0.76       75.98   21.71\r\n',
            '   AMOUNT:                            1243       1227\r\n\r\n',
            'T 4:DIESEL\r\n',
            'INCREASE   DATE / TIME             GALLONS TC GALLONS WATER  TEMP DEG F  HEIGHT\r\n\r\n',
            '      END: AUG  2, 2018  5:51 AM      3267       3240  0.00       77.40   33.67\r\n',
            '    START: AUG  2, 2018  5:36 AM       988        980  0.00       76.85   14.70\r\n',
            '   AMOUNT:                            2279       2260\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I20D00():
    return "".join(
        [
            '\x01\r\nI20D00\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I25100():
    return "".join(
        [
            '\x01\r\nI25100\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'CSLD TEST RESULTS\r\n',
            'TANK PRODUCT                RESULT\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I30100():
    return "".join(
        [
            '\x01\r\nI30100\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'LIQUID STATUS REPORT\r\n\r\n',
            'SENSOR  LOCATION               STATUS\r\n',
            '     1  REGULAR ANNULAR        SENSOR NORMAL\r\n',
            '     2  PLUS ANNULAR           SENSOR NORMAL\r\n',
            '     3  SUPER ANNULAR          SENSOR NORMAL\r\n',
            '     4  DIESEL ANNULAR         SENSOR NORMAL\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I30200():
    return "".join(
        [
            '\x01\r\nI30200\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'LIQUID ALARM HISTORY REPORT\r\n\r\n',
            'SENSOR  LOCATION\r\n',
            '     1  REGULAR ANNULAR      \r\n',
            '        APR 19, 2018 11:00 AM         FUEL ALARM\r\n',
            '        APR 20, 2017 12:49 PM         FUEL ALARM\r\n',
            '        JAN  5, 2017 10:15 AM         SETUP DATA WARNING \r\n',
            '     2  PLUS ANNULAR         \r\n',
            '        APR 19, 2018 11:06 AM         FUEL ALARM\r\n',
            '        APR 20, 2017 12:54 PM         FUEL ALARM\r\n',
            '        JAN  5, 2017 10:15 AM         SETUP DATA WARNING \r\n',
            '     3  SUPER ANNULAR        \r\n',
            '        APR 20, 2017  1:04 PM         FUEL ALARM\r\n',
            '        APR 20, 2017  1:03 PM         FUEL ALARM\r\n',
            '        APR 20, 2017  1:01 PM         FUEL ALARM\r\n',
            '     4  DIESEL ANNULAR       \r\n',
            '        APR 19, 2018 10:51 AM         FUEL ALARM\r\n',
            '        APR 20, 2017  1:13 PM         FUEL ALARM\r\n',
            '        JAN  5, 2017 10:15 AM         SETUP DATA WARNING \r\n',
            '\r\n',
            '\x03'
        ]
    )


def I50100():
    return "".join(
        [
            '\x01\r\nI50100\r\n',
            now(),
            '\r\n\r\n',
            'SYSTEM DATE AND TIME\r\n\r\n',
            '\r\n',
            '\x03',
        ]
    )


def I50A00():
    return "".join(
        [
            '\x01\r\nI50A00\r\n',
            now(),
            '\r\n\r\n',
            'ANNUAL TEST WARNING: DAYS = 355\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I50B00():
    return "".join(
        [
            '\x01\r\nI50B00\r\n',
            now(),
            '\r\n\r\n',
            'ANNUAL TEST ALARM: DAYS = 365\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I50C00():
    return "".join(
        [
            '\x01\r\nI50C00\r\n',
            now(),
            '\r\n\r\n',
            'REMOTE PRINTER\r\n',
            'DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I50E00():
    return "".join(
        [
            '\x01\r\nI50E00\r\n',
            now(),
            '\r\n\r\n',
            'TEMP COMPENSATION\r\n',
            'VALUE (DEG F ):   60.0\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I50F00():
    return "".join(
        [
            '\x01\r\nI50F00\r\n',
            now(),
            '\r\n\r\n',
            'MON DD YYYY HH:MM:SS xM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51400():
    return "".join(
        [
            '\x01\r\nI51400\r\n',
            now(),
            '\r\n\r\n',
            'H-PROTOCOL DATA FORMAT\r\n',
            'HEIGHT\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51700():
    return "".join(
        [
            '\x01\r\nI51700\r\n',
            now(),
            '\r\n\r\n',
            'SYSTEM TYPE AND LANGUAGE FLAG\r\n\r\n',
            'SYSTEM UNITS\r\n',
            ' U.S.\r\n',
            'SYSTEM LANGUAGE\r\n',
            ' ENGLISH\r\n',
            'SYSTEM DATE/TIME FORMAT\r\n',
            'MON DD YYYY HH:MM:SS xM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51A00():
    return "".join(
        [
            '\x01\r\nI51A00\r\n',
            now(),
            '\r\n\r\n',
            'DAYLIGHT SAVING TIME\r\n',
            'ENABLED ON\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51B00():
    return "".join(
        [
            '\x01\r\nI51B00\r\n',
            now(),
            '\r\n\r\n',
            'DAYLIGHT SAVING TIME\r\n\r\n',
            'START DATE    MAR   WEEK 2   SUN   2:00 AM\r\n\r\n',
            'END DATE      NOV   WEEK 1   SUN   2:00 AM\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51C00():
    return "".join(
        [
            '\x01\r\nI51C00\r\n',
            now(),
            '\r\n\r\n',
            'TICKETED DELIVERY\r\n',
            'DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I51F00():
    return "".join(
        [
            '\x01\r\nI51F00\r\n',
            now(),
            '\r\n\r\n',
            'EURO PROTOCOL PREFIX\r\n',
            'S\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I53100():
    return "".join(
        [
            '\x01\r\nI53100\r\n',
            now(),
            '\r\n\r\n',
            'RS-232 END OF MESSAGE\r\n',
            'DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I60100():
    return "".join(
        [
            '\x01\r\nI60100\r\n',
            now(),
            '\r\n\r\n',
            'TANK CONFIGURATION',
            '\r\n\r\n',
            'DEVICE  LABEL                  CONFIGURED\r\n',
            '     1  REGULAR                ON\r\n',
            '     2  PLUS                   ON\r\n',
            '     3  SUPREME                ON\r\n',
            '     4  DIESEL                 ON\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I60200():
    return "".join(
        [
            '\x01\r\nI60200\r\n',
            now(),
            '\r\n\r\n',
            'TANK PRODUCT LABEL',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            ' 1     REGULAR                   \r\n',
            ' 2     PLUS                      \r\n',
            ' 3     SUPREME                   \r\n',
            ' 4     DIESEL                    ',
            '\r\n',
            '\x03'
        ]
    )


def I60300():
    return "".join(
        [
            '\x01\r\nI60300\r\n',
            now(),
            '\r\n\r\n',
            'TANK PRODUCT CODE',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            ' 1     REGULAR                   1\r\n',
            ' 2     PLUS                      2\r\n',
            ' 3     SUPREME                   3\r\n',
            ' 4     DIESEL                    4',
            '\r\n',
            '\x03'
        ]
    )


def I60400():
    return "".join(
        [
            '\x01\r\nI60400\r\n',
            now(),
            '\r\n\r\n',
            'TANK FULL VOLUME',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                    11682\r\n',
            ' 2     PLUS                        7950\r\n',
            ' 3     SUPREME                     9816\r\n',
            ' 4     DIESEL                      9816',
            '\r\n',
            '\x03'
        ]
    )


def I60500():
    return "".join(
        [
            '\x01\r\nI60500\r\n',
            now(),
            '\r\n\r\n',
            'TANK 4 POINT VOLUMES',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL                         GALLONS\r\n',
            ' 1     REGULAR                      11682    9479    5856    2243\r\n',
            ' 2     PLUS                          7950    6473    3986    1505\r\n',
            ' 3     SUPREME                       9816    7976    4921    1874\r\n',
            ' 4     DIESEL                        9816    7976    4921    1874\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I60600():
    return "".join(
        [
            '\x01\r\nI60600\r\n',
            now(),
            '\r\n\r\n',
            'TANK 20 POINT VOLUMES',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL                         GALLONS\r\n',
            ' 1     REGULAR                      11682       0       0       0\r\n',
            '                                        0    9479       0       0\r\n',
            '                                        0       0    5856       0\r\n',
            '                                        0       0       0    2243\r\n',
            '                                        0       0       0       0\r\n',
            ' 2     PLUS                          7950       0       0       0\r\n',
            '                                        0    6473       0       0\r\n',
            '                                        0       0    3986       0\r\n',
            '                                        0       0       0    1505\r\n',
            '                                        0       0       0       0\r\n',
            ' 3     SUPREME                       9816       0       0       0\r\n',
            '                                        0    7976       0       0\r\n',
            '                                        0       0    4921       0\r\n',
            '                                        0       0       0    1874\r\n',
            '                                        0       0       0       0\r\n',
            ' 4     DIESEL                        9816       0       0       0\r\n',
            '                                        0    7976       0       0\r\n',
            '                                        0       0    4921       0\r\n',
            '                                        0       0       0    1874\r\n',
            '                                        0       0       0       0\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I60700():
    return "".join(
        [
            '\x01\r\nI60700\r\n',
            now(),
            '\r\n\r\n',
            'TANK DIAMETER',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             INCHES\r\n',
            ' 1     REGULAR                    91.13\r\n',
            ' 2     PLUS                       91.13\r\n',
            ' 3     SUPREME                    91.13\r\n',
            ' 4     DIESEL                     91.13',
            '\r\n',
            '\x03'
        ]
    )


def I60800():
    return "".join(
        [
            '\x01\r\nI60800\r\n',
            now(),
            '\r\n\r\n',
            'TANK TILT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             INCHES\r\n',
            ' 1     REGULAR                     0.00\r\n',
            ' 2     PLUS                        0.00\r\n',
            ' 3     SUPREME                     0.00\r\n',
            ' 4     DIESEL                      0.00',
            '\r\n',
            '\x03'
        ]
    )


def I60900():
    return "".join(
        [
            '\x01\r\nI60900\r\n',
            now(),
            '\r\n\r\n',
            'TANK THERMAL COEFFICIENT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            ' 1     REGULAR                   0.000700\r\n',
            ' 2     PLUS                      0.000700\r\n',
            ' 3     SUPREME                   0.000700\r\n',
            ' 4     DIESEL                    0.000450',
            '\r\n',
            '\x03'
        ]
    )


def I60A00():
    return "".join(
        [
            '\x01\r\nI60A00\r\n',
            now(),
            '\r\n\r\n'
            'TANK FULL VOLUME',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          TANK PROFILE   GALLONS\r\r\n',
            ' 1     REGULAR                     4 PTS      11682\r\r\n',
            ' 2     PLUS                        4 PTS       7950\r\r\n',
            ' 3     SUPREME                     4 PTS       9816\r\r\n',
            ' 4     DIESEL                      4 PTS       9816\r\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I60B00():
    return "".join(
        [

        ]
    )


def I60C00():
    return "".join(
        [
            '\x01\r\nI60B00\r\n',
            now(),
            '\r\n\r\n',
            'STICK HEIGHT OFFSET ENABLE STATUS\r\n',
            'DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61000():
    return "".join(
        [
            '\x01\r\nI61000\r\n',
            now(),
            '\r\n\r\n',
            'TANK DELIVERY DELAY',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            ' 1     REGULAR                   3\r\n',
            ' 2     PLUS                      3\r\n',
            ' 3     SUPREME                   3\r\n',
            ' 4     DIESEL                    3',
            '\r\n',
            '\x03'
        ]
    )


def I61100():
    return "".join(
        [
            '\x01\r\nI61100\r\n',
            now(),
            '\r\n\r\n',
            'LEAK TEST METHOD',
            '\r\n',
            '- - - - - -  - - - - - -\r\n',
            'TEST ON DATE : ALL TANK\r\n',
            'FEB  4, 2005\r\n',
            'START TIME : DISABLED\r\n',
            'TEST RATE  :0.20 GAL/HR\r\n',
            'DURATION   : 2  HOURS\r\n\r\n',
            'TST EARLY STOP:DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61200():
    return "".join(
        [
            '\x01\r\nI61200\r\n',
            now(),
            '\r\n\r\n',
            'TANK MANIFOLDED PARTNERS',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          SIPHON MANIFOLDED TANKS   LINE MANIFOLDED TANKS   \r\n',
            ' 1     REGULAR                   NONE                      NONE                \r\n',
            ' 2     PLUS                      NONE                      NONE                \r\n',
            ' 3     SUPREME                   NONE                      NONE                \r\n',
            ' 4     DIESEL                    NONE                      NONE                ',
            '\r\n',
            '\x03'
        ]
    )


def I61300():
    return "".join(
        [
            '\x01\r\nI61300\r\n',
            now(),
            '\r\n',
            'CSLD PROBABLITY OF DETECTION\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61400():
    return "".join(
        [
            '\x01\r\nI61400\r\n',
            now(),
            '\r\n',
            'CSLD CLIMATE FACTOR\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61500():
    return "".join(
        [
            '\x01\r\nI61500\r\n',
            now(),
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          METER DATA      \r\n',
            ' 1     REGULAR                   YES\r\n',
            ' 2     PLUS                      YES\r\n',
            ' 3     SUPREME                   YES\r\n',
            ' 4     DIESEL                    YES\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61600():
    return "".join(
        [
            '\x01\r\nI61600\r\n',
            now(),
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          CAL UPDATE\r\n',
            ' 1     REGULAR                   NEVER\r\n',
            ' 2     PLUS                      NEVER\r\n',
            ' 3     SUPREME                   NEVER\r\n',
            ' 4     DIESEL                    NEVER\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61700():
    return "".join(
        [
            '\x01\r\nI61700\r\n',
            now(),
            '\r\n',
            'CSLD CUSTOM PROBABLITY OF DETECTION\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61800():
    return "".join(
        [
            '\x01\r\nI61800\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61900():
    return "".join(
        [
            '\x01\r\nI61900\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61A00():
    return "".join(
        [
            '\x01\r\nI61A00\r\n',
            now(),
            '\r\n\r\n',
            'IN-TANK LEAK TEST EARLY STOP',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          TST EARLY STOP:\r\n',
            ' 1     REGULAR                   DISABLED\r\n',
            ' 2     PLUS                      DISABLED\r\n',
            ' 3     SUPREME                   DISABLED\r\n',
            ' 4     DIESEL                    DISABLED',
            '\r\n',
            '\x03'
        ]
    )


def I61B00():
    return "".join(
        [
            '\x01\r\nI61B00\r\n',
            now(),
            '\r\n\r\n',
            'IN-TANK LEAK GROSS TEST AUTO-CONFIRM\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61C00():
    return "".join(
        [
            '\x01\r\nI61C00\r\n',
            now(),
            '\r\n\r\n',
            'CSLD REPORT ONLY\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I61D00():
    return "".join(
        [
            '\x01\r\nI61D00\r\n',
            now(),
            '\r\n\r\n',
            'TANK MANIFOLDED PARTNERS',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          SIPHON MANIFOLDED TANKS   LINE MANIFOLDED TANKS   \r\n',
            ' 1     REGULAR                   NONE                      NONE                \r\n',
            ' 2     PLUS                      NONE                      NONE                \r\n',
            ' 3     SUPREME                   NONE                      NONE                \r\n',
            ' 4     DIESEL                    NONE                      NONE                ',
            '\r\n',
            '\x03'
        ]
    )


def I62100():
    return "".join(
        [
            '\x01\r\nI62100\r\n',
            now(),
            '\r\n\r\n',
            'TANK LOW PRODUCT LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                      600\r\n',
            ' 2     PLUS                         450\r\n',
            ' 3     SUPREME                      600\r\n',
            ' 4     DIESEL                       600',
            '\r\n',
            '\x03'
        ]
    )


def I62200():
    return "".join(
        [
            '\x01\r\nI62200\r\n',
            now(),
            '\r\n\r\n',
            'TANK HIGH PRODUCT LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                    11097\r\n',
            ' 2     PLUS                        7552\r\n',
            ' 3     SUPREME                     9325\r\n',
            ' 4     DIESEL                      9325',
            '\r\n',
            '\x03'
        ]
    )


def I62300():
    return "".join(
        [
            '\x01\r\nI62300\r\n',
            now(),
            '\r\n\r\n',
            'TANK OVERFILL LEVEL LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                    10513\r\n',
            ' 2     PLUS                        7155\r\n',
            ' 3     SUPREME                     8834\r\n',
            ' 4     DIESEL                      8834',
            '\r\n',
            '\x03'
        ]
    )


def I62400():
    return "".join(
        [
            '\x01\r\nI62400\r\n',
            now(),
            '\r\n\r\n',
            'TANK HIGH WATER LEVEL LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             INCHES\r\n',
            ' 1     REGULAR                    2.0\r\n',
            ' 2     PLUS                       2.0\r\n',
            ' 3     SUPREME                    2.0\r\n',
            ' 4     DIESEL                     2.0',
            '\r\n',
            '\x03'
        ]
    )


def I62500():
    return "".join(
        [
            '\x01\r\nI62500\r\n',
            now(),
            '\r\n\r\n',
            'TANK SUDDEN LOSS LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                       99\r\n',
            ' 2     PLUS                          99\r\n',
            ' 3     SUPREME                       99\r\n',
            ' 4     DIESEL                        99',
            '\r\n',
            '\x03'
        ]
    )


def I62600():
    return "".join(
        [
            '\x01\r\nI62600\r\n',
            now(),
            '\r\n\r\n',
            'TANK LEAK ALARM LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                       15\r\n',
            ' 2     PLUS                          15\r\n',
            ' 3     SUPREME                       15\r\n',
            ' 4     DIESEL                        15',
            '\r\n',
            '\x03'
        ]
    )


def I62700():
    return "".join(
        [
            '\x01\r\nI62700\r\n',
            now(),
            '\r\n\r\n',
            'TANK HIGH WATER WARNING LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             INCHES\r\n',
            ' 1     REGULAR                    1.5\r\n',
            ' 2     PLUS                       1.5\r\n'
            ' 3     SUPREME                    1.5\r\n',
            ' 4     DIESEL                     1.5',
            '\r\n',
            '\x03'
        ]
    )


def I62800():
    return "".join(
        [
            '\x01\r\nI62800\r\n',
            'AUG  7, 2018  6:08 AM',
            '\r\n\r\n',
            'TANK MAXIMUM VOLUME LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                    11448\r\n',
            ' 2     PLUS                        7791\r\n',
            ' 3     SUPREME                     9619\r\n',
            ' 4     DIESEL                      9619',
            '\r\n',
            '\x03'
        ]
    )


def I62900():
    return "".join(
        [
            '\x01\r\nI62900\r\n',
            now(),
            '\r\n\r\n',
            'TANK DELIVERY REQUIRED LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                     1141\r\n',
            ' 2     PLUS                         803\r\n',
            ' 3     SUPREME                      981\r\n',
            ' 4     DIESEL                       988',
            '\r\n',
            '\x03'
        ]
    )


def I62A00():
    return "".join(
        [
            '\x01\r\nI62A00\r\n',
            now(),
            '\r\n\r\n',
            'ANNUAL LEAK TEST MIN VOLUME',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                        0\r\n',
            ' 2     PLUS                           0\r\n',
            ' 3     SUPREME                        0\r\n',
            ' 4     DIESEL                         0',
            '\r\n',
            '\x03'
        ]
    )


def I62B00():
    return "".join(
        [
            '\x01\r\nI62B00\r\n',
            now(),
            '\r\n\r\n',
            'TANK LAST ANNUAL TEST',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             DATE \r\n',
            ' 1     REGULAR                   ???  0,    0\r\n',
            ' 2     PLUS                      ???  0,    0\r\n',
            ' 3     SUPREME                   ???  0,    0\r\n',
            ' 4     DIESEL                    ???  0,    0\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I62C00():
    return "".join(
        [
            '\x01\r\nI62C00\r\n',
            now(),
            '\r\n\r\n',
            'TANK PERIODIC TEST TYPE',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          PERIODIC TEST TYPE\r\n',
            ' 1     REGULAR                   STANDARD\r\n',
            ' 2     PLUS                      STANDARD\r\n',
            ' 3     SUPREME                   STANDARD\r\n',
            ' 4     DIESEL                    STANDARD\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I62D00():
    return "".join(
        [
            '\x01\r\nI62D00\r\n',
            now(),
            '\r\n\r\n',
            'TANK LEAK TEST FAIL ALARMS',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            ' 1     REGULAR                   GROSS TEST FAIL        ALARM ENABLED\r\n',
            '                                 PERIODIC TEST FAIL     ALARM DISABLED\r\n',
            '                                 ANNUAL TEST FAIL       ALARM DISABLED\r\n\r\n',
            ' 2     PLUS                      GROSS TEST FAIL        ALARM ENABLED\r\n',
            '                                 PERIODIC TEST FAIL     ALARM DISABLED\r\n',
            '                                 ANNUAL TEST FAIL       ALARM DISABLED\r\n\r\n',
            ' 3     SUPREME                   GROSS TEST FAIL        ALARM ENABLED\r\n',
            '                                 PERIODIC TEST FAIL     ALARM DISABLED\r\n',
            '                                 ANNUAL TEST FAIL       ALARM DISABLED\r\n\r\n',
            ' 4     DIESEL                    GROSS TEST FAIL        ALARM ENABLED\r\n',
            '                                 PERIODIC TEST FAIL     ALARM DISABLED\r\n',
            '                                 ANNUAL TEST FAIL       ALARM DISABLED\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I62E00():
    return "".join(
        [
            '\x01\r\nI62E00\r\n',
            now(),
            '\r\n\r\n',
            'CAP0 PROBE CONDUCTIVE BOOT FLAG',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          CAP0 CONDUCTIVE BOOT:\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I62F00():
    return "".join(
        [
            '\x01\r\nI62F00\r\n',
            now(),
            '\r\n\r\n',
            'MAG PROBE FLOAT SIZE',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL                FLOAT SIZE:\r\n',
            ' 1     REGULAR                      4.0 INCHES\r\n',
            ' 2     PLUS                         4.0 INCHES\r\n',
            ' 3     SUPREME                      4.0 INCHES\r\n',
            ' 4     DIESEL                       4.0 INCHES\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I63100():
    return "".join(
        [
            '\x01\r\nI63100\r\n',
            now(),
            '\r\n\r\n',
            'TANK LEAK TEST AVERAGING',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL           ANNUAL    PERIODIC\r\n',
            ' 1     REGULAR                   OFF        OFF\r\n',
            ' 2     PLUS                      OFF        OFF\r\n',
            ' 3     SUPREME                   OFF        OFF\r\n',
            ' 4     DIESEL                    OFF        OFF\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I63200():
    return "".join(
        [
            '\x01\r\nI63200\r\n',
            now(),
            '\r\n\r\n',
            'TANK TEST SIPHON BREAK',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL          SIPHON BREAK\r\n',
            ' 1     REGULAR                     OFF\r\n',
            ' 2     PLUS                        OFF\r\n',
            ' 3     SUPREME                     OFF\r\n',
            ' 4     DIESEL                      OFF\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I63300():
    return "".join(
        [
            '\x01\r\nI63300\r\n',
            now(),
            '\r\n\r\n',
            'LEAK TEST REPORT FORMAT: NORMAL\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I63400():
    return "".join(
        [
            '\x01\r\nI63400\r\n',
            now(),
            '\r\n\r\n',
            'RECONCILIATION WARNING LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                        0\r\n',
            ' 2     PLUS                           0\r\n',
            ' 3     SUPREME                        0\r\n',
            ' 4     DIESEL                         0',
            '\r\n',
            '\x03'
        ]
    )


def I63500():
    return "".join(
        [
            '\x01\r\nI63500\r\n',
            now(),
            '\r\n\r\n',
            'RECONCILIATION ALARM LIMIT',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                        1\r\n',
            ' 2     PLUS                           1\r\n',
            ' 3     SUPREME                        1\r\n',
            ' 4     DIESEL                         1',
            '\r\n',
            '\x03'
        ]
    )


def I63600():
    return "".join(
        [
            '\x01\r\nI63600\r\n',
            now(),
            '\r\n\r\n',
            'PERIODIC LEAK TEST MIN VOLUME',
            '\r\n\r\n',
            'TANK   PRODUCT LABEL             GALLONS\r\n',
            ' 1     REGULAR                        0\r\n',
            ' 2     PLUS                           0\r\n',
            ' 3     SUPREME                        0\r\n',
            ' 4     DIESEL                         0',
            '\r\n',
            '\x03'
        ]
    )


def I77100():
    return "".join(
        [
            '\x01\r\nI77100\r\n',
            now(),
            '\r\n\r\n',
            '\x03'
        ]
    )


def I85100():
    return "".join(
        [
            '\x01\r\nI85100\r\n',
            now(),
            '\r\n\r\n',
            'RESTORE SETUP DATA: DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I85200():
    return "".join(
        [
            '\x01\r\nI85200\r\n',
            'AUG  7, 2018  6:05 AM',
            '\r\n\r\n',
            'SAVE SETUP DATA: DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I85300():
    return "".join(
        [
            '\x01\r\nI85300\r\n',
            'AUG  7, 2018  6:02 AM',
            '\r\n\r\n',
            'CLEAR SETUP DATA: DISABLED\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I88100():
    return "".join(
        [
            '\x01\r\nI88100\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I88200():
    return "".join(
        [
            '\x01\r\nI88200\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I90100():
    return "".join(
        [
            '\x01\r\nI90100\r\n',
            now(),
            '\r\n\r\n',
            '                       I/O      RAM     PROM\r\n',
            'SYSTEM BOARD          PASS     PASS     PASS',
            '\r\n',
            '\x03'
        ]
    )


def I90200():
    return "".join(
        [
            '\x01\r\nI90200\r\n',
            now(),
            '\r\n',
            'SOFTWARE REVISION LEVEL\r\n',
            'VERSION 324.02\r\n',
            'SOFTWARE# 346324-100-C  \r\n',
            'CREATED - 05.02.04.13.57\r\n\r\n',
            'S-MODULE# 330160-160-A\r\n',
            'SYSTEM FEATURES:\r\n',
            '  PERIODIC IN-TANK TESTS\r\n',
            '  ANNUAL IN-TANK TESTS\r\n',
            '  BIR\r\n',
            'PLLD \r\n',
            '  0.10 AUTO\r\n',
            '  0.20 REPETITIV\r\n',
            'WPLLD \r\n',
            '  0.10 AUTO\r\n',
            '  0.20 REPETITIV\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I90300():
    return "".join(
        [
            '\x01\r\nI90300\r\n',
            now(),
            '\r\n',
            '   PC DIAGNOSTIC DATA   \r\n',
            '  PERIPHERAL CONTROLLER \r\n',
            '- - - - - -  - - - - - -\r\n\r\n',
            'PC SWARE# 330269-002-B  \r\n',
            'CREATED - 94.12.16.13.26\r\n',
            'PC ROM CHECKSUM = PASSED\r\n\r\n',
            'PC RESET COUNTS =     29\r\n',
            'PC COMM ERRORS  =     12\r\n',
            'MC CKSUM ERRS   =      1\r\n',
            'MC->PC COMMS = 456404704\r\n',
            'MC<-PC COMMS = 456410994',
            '\r\n',
            '\x03'
        ]
    )


def I90400():
    return "".join(
        [
            '\x01\r\nI90400\r\n',
            now(),
            '\r\n',
            ' WPLLD DIAGNOSTIC DATA  \r\n',
            '- - - - - -  - - - - - -\r\n',
            '#: \r\n\r\n',
            'PC COMM ERRORS  =      0\r\n\r\n\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def I90500():
    return "".join(
        [
            '\x01\r\nI90500\r\n',
            now(),
            '\r\n',
            'SOFTWARE REVISION LEVEL\r\n',
            'VERSION 324.02\r\n',
            'SOFTWARE# 346324-100-C  \r\n',
            'CREATED - 05.02.04.13.57\r\n\r\n',
            'S-MODULE# 330160-160-A\r\n',
            'SYSTEM FEATURES:\r\n',
            '  PERIODIC IN-TANK TESTS\r\n',
            '  ANNUAL IN-TANK TESTS\r\n',
            '  BIR\r\n',
            'PLLD \r\n',
            '  0.10 AUTO\r\n',
            '  0.20 REPETITIV\r\n',
            'WPLLD \r\n',
            '  0.10 AUTO\r\n',
            '  0.20 REPETITIV\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0100():
    return "".join(
        [
            '\x01\r\nIA0100\r\n',
            now(),
            '\r\n',
            '                               TYPE   CODE   LENGTH   SERIAL NO.  D/CODE\r\n',
            'TANK  1  REGULAR               MAG    C000    96.00     817402     2354\r\n',
            'TANK  2  PLUS                  MAG    C000    96.00     817403     2354\r\n',
            'TANK  3  SUPREME               MAG    C000    96.00     817404     2354\r\n',
            'TANK  4  DIESEL                MAG    C000    96.00     817401     2354\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0200():
    return "".join(
        [
            '\x01\r\nIA0200\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    GRADIENT =  350.9800\r\n',
            'TANK  2  PLUS                  MAG    GRADIENT =  350.7600\r\n',
            'TANK  3  SUPREME               MAG    GRADIENT =  350.4000\r\n',
            'TANK  4  DIESEL                MAG    GRADIENT =  350.9000\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0300():
    return "".join(
        [
            '\x01\r\nIA0300\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    GRADIENT =  350.9800\r\n',
            'TANK  2  PLUS                  MAG    GRADIENT =  350.7600\r\n',
            'TANK  3  SUPREME               MAG    GRADIENT =  350.4000\r\n',
            'TANK  4  DIESEL                MAG    GRADIENT =  350.9000\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0400():
    return "".join(
        [
            '\x01\r\nIA0400\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    \r\n',
            'TANK  2  PLUS                  MAG    \r\n',
            'TANK  3  SUPREME               MAG    \r\n',
            'TANK  4  DIESEL                MAG    \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0500():
    return "".join(
        [
            '\x01\r\nIA0500\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    \r\n',
            'TANK  2  PLUS                  MAG    \r\n',
            'TANK  3  SUPREME               MAG    \r\n',
            'TANK  4  DIESEL                MAG    \r\n',
            '\r\n',
            '\x03',
        ]
    )


def IA0600():
    return "".join(
        [
            '\x01\r\nIA0600\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    \r\n',
            'TANK  2  PLUS                  MAG    \r\n',
            'TANK  3  SUPREME               MAG    \r\n',
            'TANK  4  DIESEL                MAG    \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA0700():
    return "".join(
        [
            '\x01\r\nIA0700\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    \r\n',
            'ORIG REF DISTANCE  JAN  5, 2017      103.53\r\n',
            'CURR REF DISTANCE  AUG  6, 2018      103.57\r\n',
            'TANK  2  PLUS                  MAG    \r\n',
            'ORIG REF DISTANCE  JAN  5, 2017      103.64\r\n',
            'CURR REF DISTANCE  AUG  6, 2018      103.68\r\n',
            'TANK  3  SUPREME               MAG    \r\n',
            'ORIG REF DISTANCE  JAN  5, 2017      103.71\r\n',
            'CURR REF DISTANCE  AUG  6, 2018      103.74\r\n',
            'TANK  4  DIESEL                MAG    \r\n',
            'ORIG REF DISTANCE  JAN  5, 2017      103.68\r\n',
            'CURR REF DISTANCE  AUG  6, 2018      103.73\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA1000():
    return "".join(
        [
            '\x01\r\nIA1000\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    NUMBER OF SAMPLES = 21472\r\n',
            ' 1311.000 22713.000 22712.000 22712.000 22712.000 22712.000 22713.000 22712.000\r\n',
            '22712.000 22711.000 22712.000 44113.000 12960.000 15817.000 17370.000 17497.000\r\n',
            '17402.000 17389.000 44118.000 \r\n'
            'TANK  2  PLUS                  MAG    NUMBER OF SAMPLES = 35905\r\n',
            ' 1419.000  8868.000  8868.000  8868.000  8869.000  8869.000  8864.000  8864.000\r\n',
            ' 8865.000  8865.000  8866.000 44250.000 13937.000 14943.000 15675.000 16002.000\r\n',
            '16468.000 17777.000 44254.000 \r\n',
            'TANK  3  SUPREME               MAG    NUMBER OF SAMPLES = 33548\r\n',
            ' 1375.000 10990.000 10989.000 10990.000 10990.000 10990.000 10990.000 10990.000\r\n',
            '10990.000 10989.000 10990.000 44554.000 13429.000 14972.000 15683.000 16084.000\r\n',
            '17042.000 17368.000 44554.000 \r\n',
            'TANK  4  DIESEL                MAG    NUMBER OF SAMPLES = 14929\r\n',
            ' 1347.000  8691.000  8692.000  8692.000  8692.000  8692.000  8692.000  8692.000\r\n',
            ' 8692.000  8692.000  8692.000 43826.000 12441.000 14140.000 14504.000 14709.000\r\n',
            '15049.000 16946.000 43831.000 \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA1100():
    return "".join(
        [
            '\x01\r\nIA1100\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    NUMBER OF SAMPLES =     5\r\n',
            ' 1310.000 22715.199 22715.199 22714.801 22714.801 22714.801 22715.199 22715.199\r\n',
            '22715.000 22715.199 22715.400 44114.801 12961.200 15817.800 17372.000 17498.600\r\n',
            '17403.000 17390.400 44118.199 \r\n',
            'TANK  2  PLUS                  MAG    NUMBER OF SAMPLES =     5\r\n',
            ' 1419.000  8868.200  8868.200  8868.400  8868.200  8868.200  8872.200  8872.400\r\n',
            ' 8872.400  8872.000  8872.000 44249.398 13937.000 14943.600 15676.000 16003.000\r\n',
            '16466.000 17774.801 44252.801 \r\n',
            'TANK  3  SUPREME               MAG    NUMBER OF SAMPLES =     5\r\n',
            ' 1375.000 10989.800 10989.600 10989.800 10989.400 10989.000 10990.000 10989.800\r\n',
            '10990.000 10989.800 10989.800 44552.199 13431.000 14974.600 15684.000 16082.400\r\n',
            '17044.600 17366.400 44555.602 \r\n',
            'TANK  4  DIESEL                MAG    NUMBER OF SAMPLES =     5\r\n',
            ' 1346.000  8692.000  8692.000  8692.200  8692.000  8692.000  8692.000  8692.000\r\n',
            ' 8692.000  8692.000  8692.200 43827.398 12443.000 14139.000 14506.600 14710.199\r\n',
            '15049.400 16948.000 43830.398 \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA1200():
    return "".join(
        [
            '\x01\r\nIA1200\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    NUMBER OF SAMPLES =    20\r\n',
            ' 1310.050 22689.100 22689.100 22689.301 22689.500 22689.699 22689.400 22689.449\r\n',
            '22689.350 22689.250 22689.350 44115.250 12965.850 15803.250 17387.949 17499.900\r\n',
            '17402.150 17390.500 44119.102 \r\n',
            'TANK  2  PLUS                  MAG    NUMBER OF SAMPLES =    20',
            '\r\n',
            ' 1419.000  8868.000  8868.000  8868.000  8868.150  8868.200  8868.150  8868.050\r\n',
            ' 8868.000  8868.050  8868.450 44249.500 13939.350 14941.100 15671.350 16000.199\r\n',
            '16459.199 17764.699 44252.500 \r\n',
            'TANK  3  SUPREME               MAG    NUMBER OF SAMPLES =    20\r\n',
            ' 1375.000 10966.000 10966.150 10966.300 10966.000 10966.300 10968.300 10968.250\r\n',
            '10968.300 10968.100 10968.450 44552.949 13434.800 14971.900 15678.500 16077.300\r\n',
            '17038.801 17370.650 44556.250 \r\n',
            'TANK  4  DIESEL                MAG    NUMBER OF SAMPLES =    20\r\n',
            ' 1346.850  8569.400  8569.050  8569.550  8569.450  8569.350  8607.650  8607.500\r\n',
            ' 8607.450  8607.850  8607.700 43828.000 12394.300 14136.650 14506.800 14711.050\r\n',
            '15048.199 16941.000 43830.801 \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA1300():
    return "".join(
        [
            '\x01\r\nIA1300\r\n',
            now(),
            'TANK  1  REGULAR               MAG    NUMBER OF SAMPLES = 22000\r\n',
            ' 1309.544  8495.360  8495.391  8495.426  8495.444  8495.459  8141.306  8141.313\r\n',
            ' 8141.318  8141.329  8141.326 44130.418 12982.622 14662.228 15316.570 15745.305\r\n',
            '16043.447 16734.730 44134.391 \r\n',
            'TANK  2  PLUS                  MAG    NUMBER OF SAMPLES = 36406\r\n',
            ' 1419.385  8963.937  8963.943  8963.941  8963.942  8963.945  9702.666  9702.666\r\n',
            ' 9702.664  9702.662  9702.665 44249.879 14269.152 14997.830 15690.572 16061.698\r\n',
            '16677.355 17736.182 44253.391 \r\n',
            'TANK  3  SUPREME               MAG    NUMBER OF SAMPLES = 34028\r\n',
            ' 1374.816  7891.065  7891.068  7891.069  7891.076  7891.079  7752.301  7752.302\r\n',
            ' 7752.299  7752.303  7752.297 44553.336 13913.104 14784.168 15222.324 15357.686\r\n',
            '15891.219 16851.512 44556.688 \r\n',
            'TANK  4  DIESEL                MAG    NUMBER OF SAMPLES = 15394\r\n',
            ' 1346.628  8690.236  8690.261  8690.289  8690.277  8690.271  8710.821  8710.803\r\n',
            ' 8710.777  8710.807  8710.799 43987.930 12486.401 14191.391 14560.227 14764.843\r\n',
            '15104.500 17004.602 43990.926 \r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA1400():
    return "".join(
        [
            '\x01\r\nIA1400\r\n',
            now(),
            '\r\n\r\n',
            'MAG PROBE OPTIONS TABLE',
            '\r\n\r\n',
            'TNK   LOW\r\n',
            'NUM  TEMP\r\n\r\n',
            '   1   NO \r\n',
            '   2   NO \r\n',
            '   3   NO \r\n',
            '   4   NO ',
            '\r\n',
            '\x03'
        ]
    )


def IA1500():
    return "".join(
        [
            '\x01\r\nIA1500\r\n',
            now(),
            '\r\n',
            'IN-TANK DIAGNOSTIC      \r\n',
            '- - - - - -  - - - - - -\r\n',
            'PROBE DIAGNOSTICS\r\n',
            'T 1: PROBE TYPE MAG1\r\n',
            'SERIAL NUMBER    817402\r\n',
            'LENGTH            96.00\r\n',
            'DATE CODE = 9044\r\n',
            'ID CHAN = 0xC000\r\n',
            'GRADIENT =  350.9800\r\n',
            'PROBE INIT:\r\n',
            '  FEB 21,2017 11:26AM\r\n\r\n',
            'NUM SAMPLES =    20\r\n\r\n',
            'C00  1310.0  C01 22687.8\r\n',
            'C02 22687.7  C03 22687.8\r\n',
            'C04 22687.8  C05 22687.9\r\n',
            'C06 22697.3  C07 22697.2\r\n',
            'C08 22697.3  C09 22697.3\r\n',
            'C10 22697.4  C11 44115.0\r\n',
            'C12 12963.5  C13 15812.9\r\n',
            'C14 17375.7  C15 17497.8\r\n',
            'C16 17402.3  C17 17390.3\r\n',
            'C18 44118.0\r\n\r\n',
            'SAMPLES READ =39406095\r\n',
            'SAMPLES USED =39229006\r\n',
            'LAST ERROR   =39400891\r\n',
            'LAST SAMPLE ERROR TIME:\r\n',
            '  AUG  7,2018  4:09AM\r\n\r\n',
            'TEMP SENSOR DATA\r\n',
            'T6:    84.886 F\r\n',
            'T5:    78.259 F\r\n',
            'T4:    74.755 F\r\n',
            'T3:    74.484 F\r\n',
            'T2:    74.696 F\r\n',
            'T1:    74.723 F\r\n\r\n'
            'ORIG REF DISTANCE  \r\n',
            'JAN  5, 2017      103.53\r\n',
            'CURR REF DISTANCE  \r\n',
            'AUG  6, 2018      103.57\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n',
            'IN-TANK DIAGNOSTIC      \r\n',
            '- - - - - -  - - - - - -\r\n',
            'PROBE DIAGNOSTICS\r\n',
            'T 2: PROBE TYPE MAG1\r\n',
            'SERIAL NUMBER    817403\r\n',
            'LENGTH            96.00\r\n',
            'DATE CODE = 9044\r\n',
            'ID CHAN = 0xC000\r\n',
            'GRADIENT =  350.7600\r\n',
            'PROBE INIT:\r\n',
            '  APR 20,2017  2:33PM\r\n\r\n',
            'NUM SAMPLES =    20\r\n\r\n',
            'C00  1419.0  C01  8868.3\r\n',
            'C02  8868.0  C03  8868.0\r\n',
            'C04  8868.2  C05  8868.0\r\n',
            'C06  8868.8  C07  8869.3\r\n',
            'C08  8868.7  C09  8868.8\r\n',
            'C10  8868.7  C11 44249.1\r\n',
            'C12 13937.4  C13 14943.4\r\n',
            'C14 15675.3  C15 16003.3\r\n',
            'C16 16464.2  C17 17767.3\r\n',
            'C18 44252.4\r\n\r\n',
            'SAMPLES READ =38281632\r\n',
            'SAMPLES USED =38122605\r\n',
            'LAST ERROR   =38278301\r\n',
            'LAST SAMPLE ERROR TIME:\r\n',
            '  AUG  7,2018  4:45AM\r\n\r\n',
            'TEMP SENSOR DATA\r\n',
            'T6:    82.681 F\r\n',
            'T5:    80.349 F\r\n',
            'T4:    78.679 F\r\n',
            'T3:    77.937 F\r\n',
            'T2:    76.901 F\r\n',
            'T1:    74.008 F\r\n\r\n',
            'ORIG REF DISTANCE  \r\n',
            'JAN  5, 2017      103.64\r\n',
            'CURR REF DISTANCE  \r\n',
            'AUG  6, 2018      103.68\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n',
            'IN-TANK DIAGNOSTIC      \r\n',
            '- - - - - -  - - - - - -\r\n',
            'PROBE DIAGNOSTICS\r\n',
            'T 3: PROBE TYPE MAG1\r\n',
            'SERIAL NUMBER    817404\r\n',
            'LENGTH            96.00\r\n',
            'DATE CODE = 9044\r\n',
            'ID CHAN = 0xC000\r\n',
            'GRADIENT =  350.4000\r\n',
            'PROBE INIT:\r\n',
            '  APR 20,2017  2:31PM\r\n\r\n',
            'NUM SAMPLES =    20\r\n\r\n',
            'C00  1375.0  C01 10972.0\r\n',
            'C02 10972.0  C03 10972.0\r\n',
            'C04 10971.8  C05 10972.0\r\n',
            'C06 10987.1  C07 10987.3\r\n',
            'C08 10986.7  C09 10987.3\r\n',
            'C10 10987.1  C11 44552.3\r\n',
            'C12 13432.9  C13 14973.3\r\n',
            'C14 15682.0  C15 16082.4\r\n',
            'C16 17043.2  C17 17367.3\r\n',
            'C18 44555.9\r\n\r\n',
            'SAMPLES READ =37315717\r\n',
            'SAMPLES USED =37080015\r\n',
            'LAST ERROR   =37301681\r\n',
            'LAST SAMPLE ERROR TIME:\r\n',
            '  AUG  7,2018 12:55AM\r\n\r\n',
            'TEMP SENSOR DATA\r\n',
            'T6:    84.082 F\r\n',
            'T5:    80.515 F\r\n',
            'T4:    78.907 F\r\n',
            'T3:    78.006 F\r\n',
            'T2:    75.867 F\r\n',
            'T1:    75.152 F\r\n\r\n',
            'ORIG REF DISTANCE  \r\n',
            'JAN  5, 2017      103.71\r\n',
            'CURR REF DISTANCE  \r\n',
            'AUG  6, 2018      103.74',
            '\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n',
            'IN-TANK DIAGNOSTIC      \r\n',
            '- - - - - -  - - - - - -\r\n',
            'PROBE DIAGNOSTICS\r\n',
            'T 4: PROBE TYPE MAG1\r\n',
            'SERIAL NUMBER    817401\r\n',
            'LENGTH            96.00\r\n',
            'DATE CODE = 9044\r\n',
            'ID CHAN = 0xC000\r\n',
            'GRADIENT =  350.9000\r\n',
            'PROBE INIT:\r\n',
            '  AUG 11,2017  9:00AM\r\n\r\n',
            'NUM SAMPLES =    20\r\n\r\n',
            'C00  1347.0  C01  8641.9\r\n',
            'C02  8642.3  C03  8642.3\r\n',
            'C04  8642.0  C05  8642.2\r\n',
            'C06  8673.7  C07  8673.5\r\n',
            'C08  8673.7  C09  8673.4\r\n',
            'C10  8673.5  C11 43828.0\r\n',
            'C12 12438.9  C13 14138.4\r\n',
            'C14 14505.9  C15 14710.0\r\n',
            'C16 15050.5  C17 16948.8\r\n',
            'C18 43831.1\r\n\r\n',
            'SAMPLES READ =35758710\r\n',
            'SAMPLES USED =35301496\r\n',
            'LAST ERROR   =35756651\r\n',
            'LAST SAMPLE ERROR TIME:\r\n',
            '  AUG  7,2018  5:09AM\r\n\r\n',
            'TEMP SENSOR DATA\r\n',
            'T6:    85.950 F\r\n',
            'T5:    81.895 F\r\n',
            'T4:    81.036 F\r\n',
            'T3:    80.561 F\r\n',
            'T2:    79.773 F\r\n',
            'T1:    75.457 F\r\n\r\n',
            'ORIG REF DISTANCE  \r\n',
            'JAN  5, 2017      103.68\r\n',
            'CURR REF DISTANCE  \r\n',
            'AUG  6, 2018      103.73',
            '\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA2000():
    return "".join(
        [
            '\x01\r\nIA2000\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    PRESENT LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  2  PLUS                  MAG    PRESENT LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  3  SUPREME               MAG    PRESENT LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  4  DIESEL                MAG    PRESENT LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA2100():
    return "".join(
        [
            '\x01\r\nIA2100\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    STORED LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  2  PLUS                  MAG    STORED LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  3  SUPREME               MAG    STORED LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            'TANK  4  DIESEL                MAG    STORED LEAK TEST ANALYSIS REPORT\r\n',
            '   0.10 GAL/HR FLAGS:\r\n',
            '   0.20 GAL/HR FLAGS:\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA2200():
    return "".join(
        [
            '\x01\r\nIA2200\r\n',
            now(),
            '\r\n',
            'TANK  1  REGULAR               MAG    GROSS LEAK TEST ANALYSIS REPORT\r\n\r\n',
            '   GROSS LEAK TEST FLAGS:\r\n\r\n\r\n\r\n',
            'TANK  2  PLUS                  MAG    GROSS LEAK TEST ANALYSIS REPORT\r\n\r\n',
            '   GROSS LEAK TEST FLAGS:\r\n\r\n\r\n\r\n',
            'TANK  3  SUPREME               MAG    GROSS LEAK TEST ANALYSIS REPORT\r\n\r\n',
            '   GROSS LEAK TEST FLAGS:\r\n\r\n\r\n\r\n',
            'TANK  4  DIESEL                MAG    GROSS LEAK TEST ANALYSIS REPORT\r\n\r\n',
            '   GROSS LEAK TEST FLAGS:\r\n\r\n\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA5100():
    return "".join(
        [
            '\x01\r\nIA5100\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA5200():
    return "".join(
        [
            '\x01\r\nIA5200\r\n',
            now(),
            '\r\n\r\n\r\n',
            'CSLD DIAGNOSTICS: RATE TEST\r\n\r\n',
            'TK        DATE  LRATE INTVL ST  AVLRTE    VOL  C1  C3 FDBK ACPT THPUT  EVAP RJT\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA5300():
    return "".join(
        [
            '\x01\r\nIA5300\r\n',
            now(),
            '\r\n\r\n\r\n',
            'CSLD DIAGNOSTICS: VOLUME TABLE\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA5400():
    return "".join(
        [
            '\x01\r\nIA5400\r\n',
            now(),
            '\r\n\r\n\r\n',
            'CSLD DIAGNOSTICS: MOVING AVERAGE TABLE\r\n\r\n',
            'T 1:REGULAR             \r\n',
            '        TIME  SMPLS     TCVOL    HEIGHT   AVGTEMP   TOPTEMP    BDTEMP\r\n',
            '180807054001     24   8901.49    64.999     74.64     78.17     84.91 \r\n',
            '180807054031     27   8900.02    64.989     74.64     78.17     84.91 \r\n',
            '180807054101     22   8900.14    64.990     74.64     78.18     84.91 \r\n',
            '180807054131     23   8900.21    64.990     74.63     78.18     84.91 \r\n',
            '180807054201     26   8901.06    64.996     74.63     78.18     84.91 \r\n',
            '180807054231     22   8900.76    64.994     74.63     78.18     84.91 \r\n',
            '180807054301     22   8900.63    64.993     74.63     78.18     84.91 \r\n',
            '180807054331     20   8900.25    64.990     74.63     78.18     84.91 \r\n',
            '180807054401     26   8901.30    64.998     74.63     78.19     84.90 \r\n',
            '180807054431     26   8900.70    64.993     74.63     78.19     84.90 \r\n',
            '180807054501     24   8900.04    64.989     74.63     78.19     84.90 \r\n',
            '180807054531     26   8899.87    64.988     74.63     78.19     84.90 \r\n',
            '180807054601     24   8900.89    64.995     74.63     78.20     84.90 \r\n',
            '180807054631     25   8901.07    64.996     74.63     78.20     84.90 \r\n',
            '180807054701     24   8899.83    64.988     74.63     78.20     84.90 \r\n',
            '180807054731     24   8899.98    64.989     74.63     78.20     84.90 \r\n',
            '180807054801     23   8898.95    64.982     74.63     78.20     84.90 \r\n',
            '180807054831     24   8900.29    64.991     74.63     78.21     84.90 \r\n',
            '180807054901     23   8900.07    64.989     74.63     78.21     84.90 \r\n',
            '180807054931     28   8900.87    64.995     74.64     78.21     84.90 \r\n',
            '180807055001     25   8901.14    64.997     74.64     78.22     84.90 \r\n',
            '180807055031     23   8900.46    64.992     74.64     78.22     84.90 \r\n',
            '180807055101     24   8899.82    64.988     74.64     78.22     84.90 \r\n',
            '180807055131     24   8900.34    64.992     74.65     78.22     84.90 \r\n',
            '180807055201     24   8900.93    64.996     74.65     78.23     84.90 \r\n',
            '180807055231     23   8899.65    64.987     74.65     78.23     84.90 \r\n',
            '180807055301     20   8900.50    64.993     74.65     78.23     84.89 \r\n',
            '180807055331     22   8900.23    64.991     74.65     78.24     84.89 \r\n',
            '180807055401     23   8899.99    64.990     74.66     78.24     84.89 \r\n',
            '180807055431     22   8900.11    64.991     74.66     78.24     84.89 \r\n',
            '180807055501     24   8896.92    64.969     74.66     78.25     84.89 \r\n',
            '180807055531     19   8893.25    64.944     74.66     78.25     84.89 \r\n',
            '180807055601     24   8889.86    64.921     74.66     78.25     84.89 \r\n',
            '180807055631     21   8889.15    64.916     74.66     78.25     84.89 \r\n',
            '180807055701     23   8888.83    64.914     74.66     78.26     84.89 \r\n',
            '180807055731     23   8888.67    64.913     74.66     78.26     84.89 \r\n',
            '180807055801     20   8888.80    64.914     74.66     78.26     84.88 \r\n',
            '180807055831     24   8889.11    64.916     74.66     78.26     84.88 \r\n',
            '180807055901     25   8889.56    64.919     74.66     78.27     84.88 \r\n',
            '180807055931     24   8888.95    64.915     74.65     78.27     84.89 \r\n',
            '180807060010     17   8889.54    64.919     74.65     78.28     84.88 \r\n',
            '180807060040     23   8888.88    64.914     74.65     78.28     84.88 \r\n',
            '180807060110     24   8889.36    64.917     74.65     78.28     84.88 \r\n',
            '180807060140     15   8888.98    64.915     74.65     78.28     84.88 \r\n',
            '180807060210     17   8889.41    64.918     74.65     78.29     84.88 \r\n',
            '180807060240     13   8888.86    64.914     74.65     78.29     84.88 \r\n',
            'MOVING AVERAGE:      0.00\r\n\r\n',
            'DISPENSE STATE: ACTIVE *  411.329926\r\n\r\n',
            'T 2:PLUS                \r\n',
            '        TIME  SMPLS     TCVOL    HEIGHT   AVGTEMP   TOPTEMP    BDTEMP\r\n',
            '180807054001     23   1770.50    25.654     73.99     80.30     82.68 \r\n',
            '180807054031     25   1770.51    25.654     73.99     80.30     82.68 \r\n',
            '180807054101     22   1770.51    25.654     73.99     80.30     82.68 \r\n',
            '180807054131     21   1770.53    25.654     73.99     80.30     82.68 \r\n',
            '180807054201     24   1770.53    25.654     73.99     80.31     82.68 \r\n',
            '180807054231     22   1770.51    25.654     73.99     80.31     82.68 \r\n',
            '180807054301     22   1770.51    25.654     73.99     80.31     82.68 \r\n',
            '180807054331     20   1770.51    25.654     73.99     80.31     82.68 \r\n',
            '180807054401     23   1770.52    25.654     73.99     80.31     82.68 \r\n',
            '180807054431     27   1770.54    25.654     73.99     80.32     82.68 \r\n',
            '180807054501     23   1770.50    25.654     73.99     80.32     82.68 \r\n',
            '180807054531     24   1770.52    25.654     73.99     80.32     82.68 \r\n',
            '180807054601     24   1770.54    25.654     73.99     80.32     82.68 \r\n',
            '180807054631     25   1770.49    25.654     73.99     80.32     82.68 \r\n',
            '180807054701     24   1770.51    25.654     73.99     80.33     82.68 \r\n',
            '180807054731     25   1770.54    25.654     73.99     80.33     82.68 \r\n',
            '180807054801     22   1770.51    25.654     73.99     80.33     82.68 \r\n',
            '180807054831     23   1770.52    25.654     73.99     80.33     82.68 \r\n',
            '180807054901     24   1770.50    25.654     73.99     80.33     82.68 \r\n',
            '180807054931     27   1770.52    25.654     73.99     80.34     82.68 \r\n',
            '180807055001     24   1770.50    25.654     73.99     80.34     82.68 \r\n',
            '180807055031     23   1770.50    25.654     73.99     80.34     82.68 \r\n',
            '180807055101     23   1770.53    25.654     73.99     80.34     82.68 \r\n',
            '180807055131     22   1769.20    25.641     73.99     80.34     82.68 \r\n',
            '180807055201     23   1765.00    25.599     73.99     80.34     82.68 \r\n',
            '180807055231     23   1761.32    25.562     73.99     80.34     82.68 \r\n',
            '180807055301     20   1760.49    25.553     73.99     80.35     82.68 \r\n',
            '180807055331     22   1760.33    25.552     73.99     80.35     82.68 \r\n',
            '180807055401     21   1760.53    25.554     73.99     80.35     82.68 \r\n',
            '180807055431     21   1760.41    25.553     73.99     80.35     82.68 \r\n',
            '180807055501     22   1760.46    25.553     73.99     80.35     82.68 \r\n',
            '180807055531     21   1760.49    25.553     74.00     80.35     82.68 \r\n',
            '180807055601     22   1760.46    25.553     74.00     80.35     82.68 \r\n',
            '180807055631     20   1760.41    25.553     74.00     80.35     82.68 \r\n',
            '180807055701     22   1760.34    25.552     74.00     80.35     82.68 \r\n',
            '180807055731     21   1760.45    25.553     74.01     80.35     82.68 \r\n',
            '180807055801     20   1760.40    25.553     74.01     80.35     82.68 \r\n',
            '180807055831     22   1760.37    25.552     74.01     80.35     82.68 \r\n',
            '180807055901     22   1760.39    25.553     74.01     80.35     82.68 \r\n',
            '180807055931     22   1760.42    25.553     74.01     80.35     82.68 \r\n',
            '180807060010     17   1760.40    25.553     74.01     80.35     82.68 \r\n',
            '180807060040     23   1760.44    25.553     74.01     80.35     82.68 \r\n',
            '180807060110     23   1760.43    25.553     74.01     80.36     82.68 \r\n',
            '180807060140     14   1760.40    25.553     74.01     80.36     82.68 \r\n',
            '180807060210     17   1760.41    25.553     74.02     80.36     82.68 \r\n',
            '180807060240     13   1760.42    25.553     74.02     80.36     82.67 \r\n',
            'MOVING AVERAGE:      0.00\r\n\r\n',
            'DISPENSE STATE: ACTIVE *  0.046480\r\n\r\n',
            'T 3:SUPREME             \r\n',
            '        TIME  SMPLS     TCVOL    HEIGHT   AVGTEMP   TOPTEMP    BDTEMP\r\n',
            '180807054001     19   2960.48    31.632     75.54     80.47     84.09 \r\n',
            '180807054031     24   2960.51    31.632     75.54     80.47     84.08 \r\n',
            '180807054101     22   2960.53    31.633     75.54     80.47     84.08 \r\n',
            '180807054131     22   2960.54    31.633     75.54     80.47     84.08 \r\n',
            '180807054201     24   2960.48    31.632     75.54     80.47     84.08 \r\n',
            '180807054231     22   2960.55    31.633     75.54     80.47     84.08 \r\n',
            '180807054301     21   2960.50    31.632     75.54     80.48     84.08 \r\n',
            '180807054331     21   2960.46    31.632     75.54     80.48     84.08 \r\n',
            '180807054401     24   2960.51    31.632     75.54     80.48     84.08 \r\n',
            '180807054431     25   2960.49    31.632     75.54     80.48     84.08 \r\n',
            '180807054501     22   2960.39    31.632     75.55     80.48     84.08 \r\n',
            '180807054531     24   2960.42    31.632     75.55     80.48     84.08 \r\n',
            '180807054601     23   2960.56    31.633     75.55     80.49     84.08 \r\n',
            '180807054631     24   2960.49    31.632     75.55     80.49     84.08 \r\n',
            '180807054701     24   2960.44    31.632     75.55     80.49     84.08 \r\n',
            '180807054731     24   2960.44    31.632     75.55     80.49     84.09 \r\n',
            '180807054801     21   2960.55    31.633     75.55     80.49     84.09 \r\n',
            '180807054831     24   2960.59    31.633     75.55     80.49     84.09 \r\n',
            '180807054901     24   2960.43    31.632     75.55     80.50     84.09 \r\n',
            '180807054931     24   2960.48    31.632     75.55     80.50     84.09 \r\n',
            '180807055001     23   2960.47    31.632     75.55     80.50     84.09 \r\n',
            '180807055031     21   2960.50    31.632     75.55     80.50     84.09 \r\n',
            '180807055101     23   2960.48    31.632     75.55     80.50     84.09 \r\n',
            '180807055131     21   2960.44    31.632     75.55     80.51     84.09 \r\n',
            '180807055201     23   2960.49    31.632     75.55     80.51     84.09 \r\n',
            '180807055231     23   2960.52    31.633     75.55     80.51     84.09 \r\n',
            '180807055301     20   2960.56    31.633     75.55     80.51     84.09 \r\n',
            '180807055331     23   2960.53    31.633     75.55     80.51     84.09 \r\n',
            '180807055401     23   2960.54    31.633     75.55     80.51     84.09 \r\n',
            '180807055431     20   2960.52    31.633     75.55     80.51     84.09 \r\n',
            '180807055501     22   2960.49    31.632     75.55     80.51     84.09 \r\n',
            '180807055531     19   2960.50    31.632     75.55     80.51     84.09 \r\n',
            '180807055601     21   2960.46    31.632     75.55     80.51     84.08 \r\n',
            '180807055631     21   2959.22    31.623     75.55     80.51     84.08 \r\n',
            '180807055701     18   2956.04    31.598     75.55     80.51     84.08 \r\n',
            '180807055731     20   2953.59    31.580     75.55     80.52     84.08 \r\n',
            '180807055801     18   2951.81    31.566     75.55     80.52     84.08 \r\n',
            '180807055831     22   2951.83    31.566     75.55     80.52     84.08 \r\n',
            '180807055901     22   2951.78    31.566     75.55     80.52     84.08 \r\n',
            '180807055931     20   2951.86    31.567     75.55     80.52     84.08 \r\n',
            '180807060010     17   2951.76    31.566     75.55     80.52     84.08 \r\n',
            '180807060040     20   2951.79    31.566     75.55     80.52     84.08 \r\n',
            '180807060110     24   2951.74    31.566     75.55     80.52     84.08 \r\n',
            '180807060140     12   2951.85    31.567     75.55     80.52     84.08 \r\n',
            '180807060210     15   2951.85    31.567     75.55     80.52     84.08 \r\n',
            '180807060240     11   2951.85    31.567     75.55     80.52     84.08 \r\n',
            'MOVING AVERAGE:      0.00\r\n\r\n',
            'DISPENSE STATE: ACTIVE *  329.783142\r\n\r\n',
            'T 4:DIESEL              \r\n',
            '        TIME  SMPLS     TCVOL    HEIGHT   AVGTEMP   TOPTEMP    BDTEMP\r\n',
            '180807054001     21   2132.36    25.041     75.46     81.89     85.91 \r\n',
            '180807054031     23   2132.39    25.041     75.46     81.89     85.91 \r\n',
            '180807054101     21   2132.38    25.041     75.46     81.89     85.92 \r\n',
            '180807054131     21   2132.37    25.041     75.46     81.89     85.92 \r\n',
            '180807054201     23   2132.38    25.041     75.46     81.89     85.92 \r\n',
            '180807054231     19   2132.38    25.041     75.46     81.89     85.92 \r\n',
            '180807054301     22   2132.34    25.040     75.46     81.89     85.92 \r\n',
            '180807054331     20   2132.36    25.041     75.46     81.89     85.92 \r\n',
            '180807054401     23   2132.36    25.040     75.46     81.89     85.92 \r\n',
            '180807054431     21   2132.35    25.040     75.46     81.89     85.92 \r\n',
            '180807054501     21   2132.36    25.041     75.46     81.89     85.92 \r\n',
            '180807054531     23   2132.38    25.041     75.46     81.89     85.92 \r\n',
            '180807054601     21   2132.39    25.041     75.46     81.89     85.93 \r\n',
            '180807054631     24   2132.36    25.041     75.46     81.89     85.93 \r\n',
            '180807054701     20   2132.37    25.041     75.46     81.89     85.93 \r\n',
            '180807054731     23   2132.35    25.040     75.46     81.89     85.93 \r\n',
            '180807054801     20   2132.36    25.041     75.46     81.89     85.93 \r\n',
            '180807054831     26   2132.36    25.040     75.46     81.90     85.93 \r\n',
            '180807054901     21   2132.37    25.041     75.46     81.89     85.93 \r\n',
            '180807054931     21   2132.36    25.041     75.46     81.89     85.93 \r\n',
            '180807055001     21   2132.39    25.041     75.46     81.89     85.93 \r\n',
            '180807055031     22   2132.36    25.041     75.46     81.89     85.93 \r\n',
            '180807055101     22   2132.38    25.041     75.46     81.89     85.93 \r\n',
            '180807055131     19   2132.38    25.041     75.46     81.89     85.94 \r\n',
            '180807055201     22   2132.37    25.041     75.46     81.89     85.94 \r\n',
            '180807055231     22   2132.35    25.040     75.46     81.89     85.94 \r\n',
            '180807055301     20   2132.33    25.040     75.46     81.89     85.94 \r\n',
            '180807055331     20   2132.38    25.041     75.46     81.89     85.94 \r\n',
            '180807055401     23   2132.35    25.040     75.46     81.89     85.94 \r\n',
            '180807055431     20   2132.38    25.041     75.46     81.89     85.94 \r\n',
            '180807055501     21   2132.15    25.039     75.46     81.89     85.94 \r\n',
            '180807055531     21   2129.29    25.015     75.46     81.89     85.94 \r\n',
            '180807055601     19   2125.52    24.985     75.46     81.89     85.94 \r\n',
            '180807055631     18   2121.54    24.952     75.46     81.90     85.94 \r\n',
            '180807055701     18   2117.87    24.922     75.46     81.90     85.95 \r\n',
            '180807055731     21   2114.96    24.898     75.46     81.90     85.95 \r\n',
            '180807055801     18   2114.18    24.892     75.46     81.89     85.96 \r\n',
            '180807055831     21   2110.73    24.863     75.46     81.89     85.97 \r\n',
            '180807055901     22   2107.05    24.833     75.46     81.90     85.99 \r\n',
            '180807055931     20   2103.34    24.803     75.46     81.90     86.00 \r\n',
            '180807060010     16   2099.66    24.772     75.46     81.90     86.01 \r\n',
            '180807060040     20   2095.21    24.736     75.47     81.90     86.03 \r\n',
            '180807060140     11   2088.59    24.682     75.47     81.90     86.07 \r\n',
            '180807060210     15   2088.25    24.679     75.48     81.90     86.09 \r\n',
            '180807060240     11   2088.22    24.679     75.49     81.90     86.10 \r\n',
            '180807060310     15   2088.25    24.679     75.49     81.90     86.12 \r\n',
            'MOVING AVERAGE:      0.00\r\n\r\nDISPENSE STATE: ACTIVE *  5436.755859\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA5500():
    return "".join(
        [
            '\x01\r\nIA5500\r\n',
            now(),
            '\r\n\r\n\r\n',
            'CSLD DIAGNOSTICS: LEAK TEST STATUS',
            '\r\n\r\n',
            'TANK          TEST STATUS  DURATION\r\n',
            '\r\n',
            '\x03'
        ]
    )


def IA9100():
    return "".join(
        [
            '\x01\r\nIA9100\r\n',
            now(),
            '\r\n\r\n',
            module_configuration()["company_name_address"],
            '\r\n\r\n',
            'POWER OUTAGE REPORT\r\n\r\n',
            'T 1:REGULAR             \r\n',
            'INCREASE  DATE / TIME                  FUEL VOLUME    WATER VOLUME   TEMP DEG F\r\n\r\n',
            'POWER REMOVED:  MAY 18, 2017  8:53:15 AM     3960           0            70.3\r\n',
            'POWER RESTORED: MAY 18, 2017  9:36:15 AM     3960           0            70.2\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'POWER REMOVED:  JAN  1, 1970 12:00:00 AM        0           0             0.0\r\n',
            'POWER RESTORED: JAN  5, 2017  9:57:15 AM        0           0            52.0\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'T 2:PLUS                \r\n',
            'INCREASE  DATE / TIME                  FUEL VOLUME    WATER VOLUME   TEMP DEG F\r\n\r\n',
            'POWER REMOVED:  MAY 18, 2017  8:53:15 AM     2055           0            65.3\r\n',
            'POWER RESTORED: MAY 18, 2017  9:36:15 AM     2055           0            65.3\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'POWER REMOVED:  JAN  1, 1970 12:00:00 AM        0           0             0.0\r\n',
            'POWER RESTORED: JAN  5, 2017  9:57:15 AM        0           0            54.3\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'T 3:SUPREME             \r\n',
            'INCREASE  DATE / TIME                  FUEL VOLUME    WATER VOLUME   TEMP DEG F\r\n\r\n',
            'POWER REMOVED:  MAY 18, 2017  8:53:15 AM     1967          14            66.5\r\n',
            'POWER RESTORED: MAY 18, 2017  9:36:15 AM     1967          15            66.5\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'POWER REMOVED:  JAN  1, 1970 12:00:00 AM        0           0             0.0\r\n',
            'POWER RESTORED: JAN  5, 2017  9:57:15 AM        0           0            53.2\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'T 4:DIESEL              \r\n',
            'INCREASE  DATE / TIME                  FUEL VOLUME    WATER VOLUME   TEMP DEG F\r\n\r\n',
            'POWER REMOVED:  MAY 18, 2017  8:53:15 AM     3661           0            69.9\r\n',
            'POWER RESTORED: MAY 18, 2017  9:36:15 AM     3661           0            69.9\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            'POWER REMOVED:  JAN  1, 1970 12:00:00 AM        0           0             0.0\r\n',
            'POWER RESTORED: JAN  5, 2017  9:57:15 AM        0           0            55.0\r\n',
            'GROSS VOLUME CHANGE:                            0\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S00100():
    return "".join(
        [
            '\x01\r\nS00100\r\n',
            now(),
            '\r\n',
            '\x03'  # todo: must re-check \x03 not exist?
        ]
    )


def S00200():
    return "".join(
        [
            '\x01\r\nS00200\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S00300():
    return "".join(
        [
            '\x01\r\nS00300\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S01000():
    return "".join(
        [
            '\x01\r\nS01000\r\n',
            now(),
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S05100():
    return "".join(
        [
            '\x01\r\nS05100\r\n',
            now(),
            '\r\n\r\n',
            'DELIVERY REPORTS ERASED',
            '\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S05200():
    return "".join(
        [
            '\x01\r\nS05200\r\n',
            now(),
            '\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            '  1  REGULAR                LEAK TEST START\r\n',
            '                            TEST BY EXTERN INTERFACE\r\n\r\n',
            '  2  PLUS                   LEAK TEST START\r\n',
            '                            TEST BY EXTERN INTERFACE\r\n\r\n',
            '  3  SUPREME                LEAK TEST START\r\n',
            '                            TEST BY EXTERN INTERFACE\r\n\r\n',
            '  4  DIESEL                 LEAK TEST START\r\n',
            '                            TEST BY EXTERN INTERFACE\r\n\r\n',
            '\r\n',
            '\x03'
        ]
    )


def S05300():
    return "".join(
        [
            '\x01\r\nS05300\r\n',
            now(),
            '\r\n',
            'TANK   PRODUCT LABEL          \r\n',
            '  1  REGULAR                LEAK TEST WAS NOT IN PROGRESS\r\n',
            '  2  PLUS                   LEAK TEST WAS NOT IN PROGRESS\r\n',
            '  3  SUPREME                LEAK TEST WAS NOT IN PROGRESS\r\n'
            '  4  DIESEL                 LEAK TEST WAS NOT IN PROGRESS\r\n',
            '\r\n',
            '\x03'
        ]
    )
