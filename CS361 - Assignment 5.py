import random

def main():
    print("Welcome to OSU parking app. Please enter your personal information down below")
        
    f_name = input('First Name: ')
    l_name = input('Last Name: ')
    lc_plate = input('License Plate (no space): ')
    pm_type = input('Permit Type (A, B, C, or D): ')
    
    answer = 10
    while answer != 0:
        print("Press 1 to view your personal information")
        print("press 2 to view the entire campus map")
        print("press 3 to see available spots for your parking permit")
        print("press 0 to close the app")
        answer = int(input())
        
        if answer == 1:
            print(f_name)
            print(l_name)
            print(lc_plate)
            print(pm_type)
            answer_1 = int(input("Would you like to modify this information? Press 1 if yes, 0 if no."))
            if answer_1 == 1:
                while answer_1 != 0:
                    f_name = input('First Name: ')
                    l_name = input('Last Name: ')
                    lc_plate = input('License Plate (no space): ')
                    pm_type = input('Permit Type (A, B, C, or D): ')
                    print("")
                    print("Does the information displayed below seems correct to you? Press 1 if you want to modify, 0 if you want to save the information.")
                    print("")
                    print(f_name)
                    print(l_name)
                    print(lc_plate)
                    print(pm_type)
                    answer_1 = int(input())
                    
        if answer == 2:

            print("                   |" + "   " + "|")            
            print("        A          |" + "   " + "|          A")            
            print("                   |" + "   " + "|         FULL")
            print("___________________" + "     " + "____________________")
            print("     Campus Dr.                        ")
            print("___________________" + "     " + "____________________")
            print("                   |" + "   " + "|")            
            print("        C          |" + "   " + "|          B")            
            print("                   |" + "   " + "|         FULL")            
            print("")
            
        if answer == 3:
            print("Your permit type is " + pm_type)
            print("You can park at parking lots that corresbonds to the letter of your permit or below")
            
            if pm_type == 'A':
                print("                   |" + "   " + "|")            
                print("        A          |" + "   " + "|")            
                print("    Available      |" + "   " + "|")
                print("___________________" + "     " + "____________________")
                print("     Campus Dr.                        ")
                print("___________________" + "     " + "____________________")
                print("                   |" + "   " + "|")            
                print("        C          |" + "   " + "|          ")            
                print("    Available      |" + "   " + "|         ")            
                print("")
            
            if pm_type == 'B':
                print("                   |" + "   " + "|")            
                print("                   |" + "   " + "|          ")            
                print("                   |" + "   " + "|         ")
                print("___________________" + "     " + "____________________")
                print("     Campus Dr.                        ")
                print("___________________" + "     " + "____________________")
                print("                   |" + "   " + "|")            
                print("        C          |" + "   " + "|          ")            
                print("    Available      |" + "   " + "|         ")            
                print("")
                
            if pm_type == 'C':
                print("                   |" + "   " + "|")            
                print("                   |" + "   " + "|          ")            
                print("                   |" + "   " + "|         ")
                print("___________________" + "     " + "____________________")
                print("     Campus Dr.                        ")
                print("___________________" + "     " + "____________________")
                print("                   |" + "   " + "|")            
                print("        C          |" + "   " + "|          ")            
                print("    Available      |" + "   " + "|         ")            
                print("")
                
            if pm_type == 'D':
                print("                   |" + "   " + "|")            
                print("                   |" + "   " + "|          ")            
                print("                   |" + "   " + "|         ")
                print("___________________" + "     " + "____________________")
                print("     Campus Dr.                        ")
                print("___________________" + "     " + "____________________")
                print("                   |" + "   " + "|")            
                print("                   |" + "   " + "|          ")            
                print("                   |" + "   " + "|         ")            
                print("")
                print("No Spots currently availavle for your parking permit!")
    
    
main()