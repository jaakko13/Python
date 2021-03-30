from pyautogui import *
import pyautogui
import time
import keyboard

#pyautogui.displayMousePosition() #used to find location of thangs

#first city
#First (1077, 371)
#Second (829, 498)
#Third (832, 610)
#Fourth (1050, 743)
#Fifth (1318, 552)
#Sixth (1303, 481)

#second city
#First (1084, 319)
#Second (1249, 482)
#Third (1296, 552)
#Fourth (1200, 559)
#Fifth (1130, 584)
#Sixth (894, 551)

#Third City
#First (756, 529)
#Second (828, 452)
#Third(1329, 490)
#Fourth (1442, 535)
#Fifth (1344, 561)
#Sixth (1213, 651)

#Fourth
#First (759, 528)
#Second (822, 459)
#Third(1172, 380)
#Fourth (1261, 415)
#Fifth (1436, 547)
#Sixth (1207, 660)

#Fifth City
#First (772, 652)
#Second (752, 534)
#Third(820, 460)
#Fourth (1063, 389)
#Fifth (1172, 382)
#Sixth (1438, 542)

#ChangeCityRight (1056, 144)
#Center (148, 173)
#Close (1417, 254)
#Collect (644, 738)
#Swords (640, 744)
#Slingers (843, 744)
#Archers (1042, 744)
#Hops (1243, 744)




#Not needed with new way
#Dropdown (1033, 145)
#City 1 (947, 206)
#City 2 (984, 232)

where = ""
what = ""

print("Where would you like to collect? (all, first, second, third...)")
where = input()

print("What would you like to collect? (res, swords, slingers, archers, hops)")
what = input()


if where == "all" and what == "res":
    time.sleep(2)

    for x in range(1000):
        #collect all first island
        pyautogui.click(1077, 371)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(829, 498)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(832, 610)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1050, 743)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1318, 552)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1303, 481)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)


        #change island
        time.sleep(1)
        pyautogui.click(1056, 144)
        time.sleep(1)
        pyautogui.click(148, 173)
        time.sleep(1)


        #collect second island
        pyautogui.click(1084, 319)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1249, 482)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1296, 552)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1200, 559)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1130, 584)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(894, 551)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #change island
        time.sleep(1)
        pyautogui.click(1056, 144)
        time.sleep(1)
        pyautogui.click(148, 173)
        time.sleep(1)


        #Collect all third city
        pyautogui.click(756, 529)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(828, 452)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1329, 490)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1442, 535)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1344, 561)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1213, 651)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #Change island
        time.sleep(1)
        pyautogui.click(1056, 144)
        time.sleep(1)
        pyautogui.click(148, 173)
        time.sleep(1)

        #Collect fourth city
        #Fourth
#First (759, 528)
#Second (822, 459)
#Third(1172, 380)
#Fourth (1261, 415)
#Fifth (1436, 547)
#Sixth (1207, 660)
        pyautogui.click(759, 528)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(822, 459)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1172, 380)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1261, 415)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1436, 547)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1207, 660)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #Change island
        time.sleep(1)
        pyautogui.click(1056, 144)
        time.sleep(1)
        pyautogui.click(148, 173)
        time.sleep(1)

        #Collect all fifth city
        pyautogui.click(772, 652)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(752, 534)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(820, 460)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(6)
        pyautogui.click(1063, 389)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(6)
        pyautogui.click(1172, 382)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1438, 542)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #change island
        time.sleep(1)
        pyautogui.click(1056, 144)
        time.sleep(1)
        pyautogui.click(148, 173)
        time.sleep(1)


        #wait 10 min
        time.sleep(603)

elif where == "first" and what == "res":
    time.sleep(2)

    for x in range(1000):
        #collect all first island
        pyautogui.click(1077, 371)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(829, 498)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(832, 610)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1050, 743)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1318, 552)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1303, 481)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

            #wait 10 min
        time.sleep(603)

elif where == "second" and what == "res":

    time.sleep(2)

    for x in range(1000):
        #collect second island
        pyautogui.click(1084, 319)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1249, 482)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1296, 552)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1200, 559)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1130, 584)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(894, 551)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #wait 10 min
        time.sleep(603)

elif where == "third" and what == "res":

    time.sleep(2)
    for x in range(1000):
        #Collect all third city
        pyautogui.click(756, 529)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(828, 452)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1329, 490)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1442, 535)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1344, 561)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1213, 651)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #wait 10 min
        time.sleep(603)

elif where == "fourth" and what == "res":
    time.sleep(2)

    for x in range(1000):
        #Collect fourth city
        #Fourth
#First (759, 528)
#Second (822, 459)
#Third(1172, 380)
#Fourth (1261, 415)
#Fifth (1436, 547)
#Sixth (1207, 660)
        pyautogui.click(759, 528)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(822, 459)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(1172, 380)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1261, 415)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1436, 547)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1207, 660)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #wait 10 min
        time.sleep(603)

elif where == "fifth" and what == "res":
    time.sleep(2)

    for x in range(1000):
        #Collect all fifth city
        pyautogui.click(772, 652)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(752, 534)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        pyautogui.click(820, 460)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(5)
        pyautogui.click(1063, 389)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1172, 382)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        time.sleep(1)
        pyautogui.click(1438, 542)
        time.sleep(1)
        pyautogui.click(644, 738)
        time.sleep(1)
        pyautogui.click(1417, 254)

        #wait 10 min
        time.sleep(603)

elif where == "first" and what == "swords":
    #Switch to troops (933, 572)
    #Swords (640, 744)
    #Slingers (843, 744)
    #Archers (1042, 744)
    #Hops (1243, 744)
    time.sleep(2)

    #collect all first island
    pyautogui.click(1077, 371)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(829, 498)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(832, 610)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1050, 743)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1318, 552)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1303, 481)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "first" and what == "slingers":
    #Switch to troops (933, 572)
    time.sleep(2)

    #collect all first island
    pyautogui.click(1077, 371)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(829, 498)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(832, 610)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1050, 743)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1318, 552)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1303, 481)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "first" and what == "archers":
    #Switch to troops (933, 572)
    time.sleep(2)

    #collect all first island
    pyautogui.click(1077, 371)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(829, 498)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(832, 610)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1050, 743)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1318, 552)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1303, 481)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "first" and what == "hops":
    #Switch to troops (933, 572)
    time.sleep(2)
    
    #collect all first island
    pyautogui.click(1077, 371)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(829, 498)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(832, 610)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1050, 743)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1318, 552)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(1303, 481)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)




elif where == "fifth" and what == "swords":
    #Switch to troops (933, 572)
    #Swords (640, 744)
    #Slingers (843, 744)
    #Archers (1042, 744)
    #Hops (1243, 744)

    #fifth City
    #First (772, 652)
    #Second (752, 534)
    #Third(820, 460)
    #Fourth (1063, 389)
    #Fifth (1172, 382)
    #Sixth (1438, 542)
    time.sleep(2)

    #collect all fifth island
    pyautogui.click(772, 652)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(752, 534)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(820, 460)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(6)
    pyautogui.click(1063, 389)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1172, 382)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1438, 542)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(644, 738)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "fifth" and what == "slingers":
    #Switch to troops (933, 572)
    time.sleep(2)

    #collect all first island
    pyautogui.click(772, 652)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(752, 534)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(820, 460)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1063, 389)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(5)
    pyautogui.click(1172, 382)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1438, 542)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(843, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "fifth" and what == "archers":
    #Switch to troops (933, 572)
    time.sleep(2)

    #collect all first island
    pyautogui.click(772, 652)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(752, 534)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(820, 460)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(6)
    pyautogui.click(1063, 389)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1172, 382)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1438, 542)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1042, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

elif where == "fifth" and what == "hops":
    #Switch to troops (933, 572)
    time.sleep(2)
    
    #collect all fifth island
    pyautogui.click(772, 652)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(752, 534)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    pyautogui.click(820, 460)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(6)
    pyautogui.click(1063, 389)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1172, 382)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

    time.sleep(1)
    pyautogui.click(1438, 542)
    time.sleep(1)
    pyautogui.click(933, 572)
    time.sleep(1)
    pyautogui.click(1243, 744)
    time.sleep(1)
    pyautogui.click(1417, 254)

















