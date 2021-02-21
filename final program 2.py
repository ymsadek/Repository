class Atc: #Atc class
    flight=[] #Store flight number
    def __init__(self,flight):
        self.flight=list(flight.strip().split(',')) #Split the string and convert to list then assign it

    def add(self,sign):
        self.flight.append(sign) #Add flights

    def remove(self,sign):
        self.flight.remove(sign) #Remove flights


class Parking:
    flight=[] #Store waiting flights 
    def __init__(self,waiting):
        self.flight=list(waiting.strip().split(',')) #Split the string and convert to list then assign it

    def add(self,sign):
        self.flight.append(sign) #Add flights

    def remove(self,sign):
        self.flight.remove(sign) #Remove last in first out.

    def __str__(self): #Display the total number of planes in the waiting area
        return "There are "+str(len(self.flight))+" planes in waiting area"


def menu(): #The menu
    print("\n1. Land")
    print("2. Take Off")
    print("3. Start Waiting")
    print("4. Move From Waiting to Takeoff")
    print("5. Next")
    print("6. Quit")


def print_answer(land,takeoff,waiting): #Display result
    print("There are "+str(len(land.flight))+" planes waiting to land") #Print number of planes that are waiting to land
    print("There are "+str(len(takeoff.flight))+" planes waiting to takeoff") #Print the number of planes that are waiting to takeoff
    print(waiting) #Print the number of planes of in the waiting area

def main():
    land=Atc("AA1943") #Object for landing
    takeoff=Atc("DL312,UA45,SW23") #Object for takeoff
    waiting=Parking("US1231") #Object for parking

    print("Initial Flights in the Landing Line: ",end="") #Print plane sign of landing 
    print(','.join(land.flight))
    print("Initial Flights in the Take Off Line: ", end="") #Print plane sign of takeoff 
    print(','.join(takeoff.flight))
    print("Initial Flights in the Waiting Area: ", end="") #Print plane sign of waiting 
    print(','.join(waiting.flight))

    choice=1
    while(True): # Loop till you enter 6
        menu()
        choice=int(input("Choice: "))
        if(choice==1):
            k = input("Please enter a flight sign : ")  #Enter flight sign
            print("LAND "+str(k))
            print_answer(land,takeoff,waiting)
        elif(choice==2):
            if(len(takeoff.flight)!=0):
                    print("TAKEOFF "+takeoff.flight[0])
                    takeoff.remove(takeoff.flight[0])
            else:
                pass
            print_answer(land,takeoff,waiting)
        elif(choice==3):
            k=input("Please enter a flight sign: ") # Enter flight sign
            waiting.flight.append(k) #Append list of object class parking
            if (len(takeoff.flight) != 0):
                print("TAKEOFF " + takeoff.flight[0]) #Takeoff plan from takeoff list 
                takeoff.remove(takeoff.flight[0]) #Remove plan from the list
            else:
                pass
            print_answer(land,takeoff,waiting)
        elif(choice==4):
            if (len(takeoff.flight) != 0):
                print("TAKEOFF " + takeoff.flight[0]) #Takeoff plan from takeoff list 
                takeoff.remove(takeoff.flight[0]) #Remove plan from the list
            else:
                print("TAKEOFF " + waiting.flight[-1]) #If no planes are taking off
                waiting.remove(waiting.flight[-1]) #Remove from the waiting list
            print_answer(land,takeoff,waiting)
        elif(choice==5):
            if (len(land.flight) == 0):
                if (len(takeoff.flight) != 0):
                    print("TAKEOFF " + takeoff.flight[0]) #Takeoff plan from takeoff list
                    takeoff.remove(takeoff.flight[0]) # Remove plan from the list
                elif (len(waiting.flight) != 0):
                    takeoff.add(waiting.flight[-1])  #If no planes are taking off
                    waiting.remove(waiting.flight[-1]) # Remove from the waiting list
                else:
                    pass
            else:
                print("LAND " + land.flight[0])
                land.remove(land.flight[0]) #Remove plan from landing list
            print_answer(land,takeoff,waiting)
        elif(choice==6):
            break 
        else:
            print("Unknown choice! Try again...") #Message to put valid input
        

if __name__ == '__main__':
    main()

