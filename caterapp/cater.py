## importing modules
from shareBox import server as sender
from shareBox import client as receiver
from random import randint

######################


## banner printer
def printBanner():
    ## defining the banner
    banner='''     888                                                    
                  888                                                    
                  888                                                    
 .d8888b  8888b.  888888 .d88b.  888d888       8888b.  88888b.  88888b.  
d88P"        "88b 888   d8P  Y8b 888P"            "88b 888 "88b 888 "88b 
888      .d888888 888   88888888 888          .d888888 888  888 888  888 
Y88b.    888  888 Y88b. Y8b.     888          888  888 888 d88P 888 d88P 
 "Y8888P "Y888888  "Y888 "Y8888  888          "Y888888 88888P"  88888P"  
                                                       888      888      
______________________________________________________ 888 ____ 888 _____
                                                       888      888      
  Using v1.1                                           888      888      '''
    
    ## printing greeting
    print("\n  welcome to:",end="")
    
    ## choosing a color banner
    colorCode = 31 +  randint(1,100) % 7
    BANNERCOLOR = '\033[' + str(colorCode) + 'm' # 31 to 37
    
    ## printting the banner
    print(BANNERCOLOR + banner)
    
    ## resetting the colors
    BANNERCOLOR = '\033[m'
    print(BANNERCOLOR + "")
    
    return


######################################


class cater():
    def __init__(self, menuOption=""):
        ## greeting
        printBanner()
        ## menu
        self.__mainMenu = "\n Menu\n"+"-"*6+"\n\n1. Send Files! \n2. Receive Files!"+menuOption
        self.choice = self.__menu__()
    
    ## main menu
    def __menu__(self):
        print(self.__mainMenu)
        ch = input("\nEnter your choice: ")    
        return ch

    ## mainApp
    def cater(self):
        ## making host to share files
        if self.choice == '1':
            Sender = sender.server()
            print("\n"+"-"*20+"\n")
            Sender.server()
            return True
        ## making client to get files
        elif self.choice == '2':
            Receiver = receiver.client()
            print("\n"+"-"*20+"\n")
            Receiver.client()
            return True
        ## invalid input
        else:
            print("\n"+"-"*20+"\n")
            return False
        
        ## if ran at least once
        flag = False

######################
def app():
    flag = True
    firstRun = True
    addOnMenu = ''

    while flag:
        ## creating an instance
        caterApp = cater(addOnMenu)
        ## sharing the files
        flag = caterApp.cater()

        ## adding exit choice in menu
        if flag and firstRun:
            firstRun = False
        if firstRun is False:
            addOnMenu = "\n*  Any other key to exit!!"
        
        ## deleting current instence on Secreat Share App
        del(caterApp)
    
    ## exit prompt
    if firstRun:
        print("\nSomething went wrong!!\nApp terminated unexpectedly!!")
    else:
        print("\nThanks for using 'cater'!\n")


#############################################

if __name__ == '__main__':
    app()