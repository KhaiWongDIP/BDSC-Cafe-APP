#BDSC Cafe App
from tkinter import*
import datetime
import random
import string
import pickle
import os

#Data
Users = [] #[Username,Password,ID Number]
CafeOrders = [] #[Users, Cafe Items]

#Blueprint for GUI
class Cafe():
    #This function runs as soon as the class is called
    def __init__(self, root):
        #----------------------------------------------------Log In Widgets-----------------------------------------------------
        self.LogOn = Frame(root)
        self.Title = Label(self.LogOn, text = "Botany Cafe", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))

        def CheckUser():
            User_Entry = self.UserEntry.get()
            Pass_Entry = self.PasswordEntry.get()
            User_Check = User_Entry in (item for sublist in Users for item in sublist)
            Pass_Check = Pass_Entry in (item for sublist in Users for item in sublist)
            print(str(User_Check), "\n", str(Pass_Check))
            find_in_nested_list(Users, User_Entry)
            if User_Check == True:
                 print(User_Entry, "is a User")
                 if Pass_Entry == User_Pass:
                      print("Correct Password")
                      self.Logged_Screen()
                 else:
                      print("Incorrect Password")
                      self.IncorrectInfo.config(text = "Incorrect Username or Password", fg = "red")
            else:
                 print("Not a User")
                 self.IncorrectInfo.config(text = "Incorrect Username or Password", fg = "red")

        def find_in_nested_list(mylist, char):
                 for sub_list in mylist:
                      if char in sub_list:
                           print("Position in List:", mylist.index(sub_list), sub_list.index(char))
                           Pass = int(sub_list.index(char))
                           Pass_find = Pass + 1
                           global User_Pass
                           User_Pass = sub_list[Pass_find]
                           print("User Pass:", User_Pass)
                           self.UserEntry.delete(0, END)
                           self.PasswordEntry.delete(0, END)
                           
        self.LogIn = Button(self.LogOn, text = "Log in", command = CheckUser)
        self.UserLabel = Label(self.LogOn, text = "Username", fg = "grey", font = ("Times", 20, "bold"))
        self.UserEntry = Entry(self.LogOn)
        self.PasswordLabel = Label(self.LogOn, text = "Password", fg = "grey", font = ("Times", 20, "bold"))
        self.PasswordEntry = Entry(self.LogOn)
        self.IncorrectInfo = Label(self.LogOn, text = "")
            #Sign Up Label and its Configurations
        def PageSendSUP(event = None):
            self.SignUp_Screen()
        def HighlightTextSUL(event = None):
            self.SignUpLabel.config(fg = "blue")
        def LowlightTextSUL(event = None):
            self.SignUpLabel.config(fg = "Navy")
        self.SignUpLabel = Label(self.LogOn, text = "Sign Up", cursor="hand2", fg = "Navy")
        self.SignUpLabel.bind("<Button-1>", PageSendSUP)
        self.SignUpLabel.bind("<Enter>", HighlightTextSUL)
        self.SignUpLabel.bind("<Leave>", LowlightTextSUL)

            #Forget Password Label and its Configurations
        def PageSendFP(event = None):
            self.ForgetPass_Screen()
        def HighlightTextFPL(event = None):
            self.ForgotPasswordLabel.config(fg = "blue")
        def LowlightTextFPL(event = None):
            self.ForgotPasswordLabel.config(fg = "Navy")
        self.ForgotPasswordLabel = Label(self.LogOn, text = "Forgot Password?", cursor="hand2", fg = "Navy")
        self.ForgotPasswordLabel.bind("<Button-1>", PageSendFP)
        self.ForgotPasswordLabel.bind("<Enter>", HighlightTextFPL)
        self.ForgotPasswordLabel.bind("<Leave>", LowlightTextFPL)

        #-----------------------------------------------------Sign Up Widgets------------------------------------------------
        self.SignUp = Frame(root)

        def AccountCreate():   
            RegisterUsername = self.RegisterUsernameEntry.get()
            print("Username Entry is {}".format(RegisterUsername))
            RegisterPassword = self.RegisterPasswordEntry.get()
            print("Password Entry is {}".format(RegisterPassword))
            if RegisterUsername != "":
                print("Username is valid")
                if RegisterUsername != "":
                    print("Password is valid")
                    Users.append([RegisterUsername, RegisterPassword])
                    print(Users)
                    print("Success!")
                    SaveData()
                    self.RegisterUsernameEntry.delete(0, END)
                    self.RegisterPasswordEntry.delete(0, END)
                else:
                    print("Password left blank")    
            else:
                print("Username left blank")
            
        self.SignUpTitle = Label(self.SignUp, text = "Registration", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))
        self.RegisterUsername = Label(self.SignUp, text = "Username:", fg = "grey", font = ("Times", 20, "bold"))
        self.RegisterUsernameEntry = Entry(self.SignUp)
        self.RegisterPassword = Label(self.SignUp, text = "Password:", fg = "grey", font = ("Times", 20, "bold"))
        self.RegisterPasswordEntry = Entry(self.SignUp)
        self.SignUpButton = Button(self.SignUp, text = "Sign Up", command = AccountCreate)
        self.GoBack1 = Button(self.SignUp, text = "Go Back", command = self.Log_Screen)

        
       #-------------------------------------------------Forgot Password Widgets--------------------------------------------
        self.ForgotPassPage = Frame(root)

        #Generates a random password.
        def ResetPass():
            def ChangePass():
                def randomString(stringLength):
                    #Creates a random string of letters
                    letters = string.ascii_letters
                    return ''.join(random.choice(letters) for i in range(stringLength))
                RandomPass = randomString(8)
                global Users
                find_in_nested_list(Users, FP_UE)
                self.ForgotPassInfo.config(text = "Password: {}".format(RandomPass))
                Users = [[x.replace(User_Pass,RandomPass) for x in l] for l in Users]
                SaveData()
                print(Users)


                
            FP_UE = self.ForgotPassUserEntry.get()
            FP_UE_Check = FP_UE in (item for sublist in Users for item in sublist)
            print(str(FP_UE_Check))
            if FP_UE_Check == True:
                self.ForgotPassUserEntry.delete(0, END)
                self.ForgotPassInfo.config(text = "Generating new password...")
                self.ForgotPassInfo.after(1000, ChangePass)
            else:
                self.ForgotPassInfo.config(text ="Please input a real Username")


        def ClearLabel():
            self.ForgotPassInfo.config(text = "")
            self.Log_Screen()
        
        self.ForgotPassTitle = Label(self.ForgotPassPage, text = "Forgot Password?", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))
        self.ForgotPassUser = Label(self.ForgotPassPage, text = "Username", fg = "grey", font = ("Times", 20, "bold"))
        self.ForgotPassUserEntry = Entry(self.ForgotPassPage)
        self.ForgotPassInfo = Label(self.ForgotPassPage, text = "")
        self.SendEmail = Button(self.ForgotPassPage, text = "Reset Password", command = ResetPass)
        self.GoBack2 = Button(self.ForgotPassPage, text = "Go Back", command = ClearLabel)

        #---------------------------------------------------Menu Widgets-------------------------------------------------
        self.MenuPage = Frame(root)
        self.MenuTitle = Label(self.MenuPage, text = "Menu", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))


        
        

        self.NumberOfItems = Label(self.MenuPage, text = "Number of Orders")
        self.PriceLabel = Label(self.MenuPage, text = "Price")
        self.MealLabel = Label(self.MenuPage, text = "Meals")
        
        #Meal of the Day
        self.MealofTheDay = Label(self.MenuPage, text = "Meal of the Day")
        
        self.DailyMeal = Label(self.MenuPage, text= "")
        self.DailyMealPrice = Label(self.MenuPage, text = "$")
        self.DailyMealNumber = Entry(self.MenuPage, width= 3)

        Date = datetime.datetime.today().weekday() #Monday = 0 to Sunday = 6
        print(Date)
        
        def MealOfTheDay():
            if Date == 0:
                self.DailyMeal.config(text = "Nachos")
                self.DailyMealPrice.config(text = "$4")
            elif Date == 1:
                self.DailyMeal.config(text = "Rolls")
                self.DailyMealPrice.config(text = "$3")
            elif Date ==2:
                self.DailyMeal.config(text = "Quinche")
                self.DailyMealPrice.config(text = "$3")
            elif Date ==3:
                self.DailyMeal.config(text = "Chicken Burger")
                self.DailyMealPrice.config(text = "$4")
            elif Date ==4:
                self.DailyMeal.config(text = "Sushi")
                self.DailyMealPrice.config(text = "$5")
            else:
                self.DailyMeal.config(text = "No Meals today", fg = "red")
                self.DailyMealPrice.config(text = "-----")
        MealOfTheDay()

        #Healthy Choices
        self.HealthyChoices = Label(self.MenuPage, text = "Healthy Choices")
        
        self.Fresh_Fruits = Label(self.MenuPage, text = "Fresh Fruits")
        self.Fresh_FruitsPrice = Label(self.MenuPage, text = "$1")
        self.Fresh_FruitsNumber = Entry(self.MenuPage, width= 3)
        
        self.Chicken_Sub = Label(self.MenuPage, text = "Chicken Sub")
        self.Chicken_SubPrice = Label(self.MenuPage, text = "$4")
        self.Chicken_SubNumber = Entry(self.MenuPage, width= 3)
        
        self.Wrap = Label(self.MenuPage, text = "Wraps")
        self.WrapPrice = Label(self.MenuPage, text = "$4.5")
        self.WrapNumber = Entry(self.MenuPage, width= 3)
        
        self.Pizza_Bread = Label(self.MenuPage, text = "Pizza Bread")
        self.Pizza_BreadPrice = Label(self.MenuPage, text = "$3")
        self.Pizza_BreadNumber = Entry(self.MenuPage, width= 3)
        
        #Snacks
        self.Snacks = Label(self.MenuPage, text = "Snacks")

        self.Potato_Chips = Label(self.MenuPage, text = "Potato Chips")
        self.Potato_ChipsPrice = Label(self.MenuPage, text = "$2")
        self.Potato_ChipsNumber = Entry(self.MenuPage, width= 3)
        
        self.Afghan_Cookie = Label(self.MenuPage, text = "Afghan Cookie")
        self.Afghan_CookiePrice = Label(self.MenuPage, text = "$1")
        self.Afghan_CookieNumber = Entry(self.MenuPage, width= 3)
        
        self.Popcorn  = Label(self.MenuPage, text = "Popcorn")
        self.PopcornPrice  = Label(self.MenuPage, text = "$2")
        self.PopcornNumber = Entry(self.MenuPage, width= 3)
        
        self.Other_Chips = Label(self.MenuPage, text = "Other Chips")
        self.Other_ChipsPrice = Label(self.MenuPage, text = "$2")
        self.Other_ChipsNumber = Entry(self.MenuPage, width= 3)

        #Hot Lunches
        self.Hot_Lunches = Label(self.MenuPage, text = "Hot Lunches")
        
        self.Spaghetti_Bun = Label(self.MenuPage, text = "Spaghetti Bun")
        self.Spaghetti_BunPrice = Label(self.MenuPage, text = "$1.5")
        self.Spaghetti_BunNumber = Entry(self.MenuPage, width= 3)
        
        self.Steam_Bun = Label(self.MenuPage, text = "Steam Bun")
        self.Steam_BunPrice = Label(self.MenuPage, text = "$3.5")
        self.Steam_BunNumber = Entry(self.MenuPage, width= 3)
        
        self.Sausage_Roll = Label(self.MenuPage, text = "Sausage Roll")
        self.Sausage_RollPrice = Label(self.MenuPage, text = "$2")
        self.Sausage_RollNumber = Entry(self.MenuPage, width= 3)
        
        self.Pizza = Label(self.MenuPage, text = "Pizza")
        self.PizzaPrice = Label(self.MenuPage, text = "$3")
        self.PizzaNumber = Entry(self.MenuPage, width= 3)

        #Drinks
        self.Drinks = Label(self.MenuPage, text = "Drinks")

        self.Hot_Chocolate = Label(self.MenuPage, text = "Hot Chocolate")
        self.Hot_ChocolatePrice = Label(self.MenuPage, text = "$2")
        self.Hot_ChocolateNumber = Entry(self.MenuPage, width= 3)
        
        self.Barrista_Bros = Label(self.MenuPage, text = "Barrista Bros")
        self.Barrista_BrosPrice = Label(self.MenuPage, text = "$4")
        self.Barrista_BrosNumber = Entry(self.MenuPage, width= 3)

        self.Incorrect_Order = Label(self.MenuPage, text = "")
        
        #Button to order/log out
        def Cart():
            HighOrder = 0
            
        #Meal of the Day
            DailyMealOrder = self.DailyMealNumber.get()
            DailyMealDigit = DailyMealOrder.isdigit()
            print(DailyMealDigit)
            if DailyMealDigit == True:
                DailyMealOrder = int(DailyMealOrder)
                if DailyMealOrder <= 3:
                    if Date == 0:
                        for _ in range(Fresh_FruitsOrder): 
                            CafeOrders.append(["Nachos",4])
                    elif Date == 1:
                        for _ in range(Fresh_FruitsOrder): 
                            CafeOrders.append(["Rolls",3])
                    elif Date == 2:
                        for _ in range(Fresh_FruitsOrder): 
                            CafeOrders.append(["Quinche",3])
                    elif Date == 3:
                        for _ in range(Fresh_FruitsOrder): 
                            CafeOrders.append(["Chicken Burger",4])
                    elif Date == 4:
                        for _ in range(Fresh_FruitsOrder): 
                            CafeOrders.append(["Sushi",5])
                    else:
                        print("No Daily Meal today")
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")

        #Healthy Choices
            Fresh_FruitsOrder = self.Fresh_FruitsNumber.get()
            Fresh_FruitsDigit = Fresh_FruitsOrder.isdigit()
            if Fresh_FruitsDigit == True:
                Fresh_FruitsOrder = int(Fresh_FruitsOrder)
                if Fresh_FruitsOrder <= 3:
                    for _ in range(Fresh_FruitsOrder): 
                        CafeOrders.append(["Fresh Fruits",1])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Chicken_SubOrder = self.Chicken_SubNumber.get()
            Chicken_SubDigit = Chicken_SubOrder.isdigit()
            if Chicken_SubDigit == True:
                Chicken_SubOrder = int(Chicken_SubOrder)
                if Chicken_SubOrder <= 3:
                    for _ in range(Chicken_SubOrder): 
                        CafeOrders.append(["Chicken Sub",4])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            WrapOrder = self.WrapNumber.get()
            WrapDigit = WrapOrder.isdigit()
            if WrapDigit == True:
                WrapOrder = int(WrapOrder)
                if WrapOrder <= 3:
                    for _ in range(WrapOrder): 
                        CafeOrders.append(["Wrap",4.5])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Pizza_BreadOrder = self.Pizza_BreadNumber.get()
            Pizza_BreadDigit = Pizza_BreadOrder.isdigit()
            if Pizza_BreadDigit == True:
                Pizza_BreadOrder = int(Pizza_BreadOrder)
                if Pizza_BreadOrder <= 3:
                    for _ in range(Pizza_BreadOrder): 
                        CafeOrders.append(["Pizza Bread",3])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
        
        #Snacks
            Potato_ChipsOrder = self.Potato_ChipsNumber.get()
            Potato_ChipsDigit = Potato_ChipsOrder.isdigit()
            if Potato_ChipsDigit == True:
                Potato_ChipsOrder = int(Potato_ChipsOrder)
                if Potato_ChipsOrder <= 3:
                    for _ in range(Potato_ChipsOrder): 
                        CafeOrders.append(["Potato Chips",2])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Afghan_CookieOrder = self.Afghan_CookieNumber.get()
            Afghan_CookieDigit = Afghan_CookieOrder.isdigit()
            if Afghan_CookieDigit == True:
                Afghan_CookieOrder = int(Afghan_CookieOrder)
                if Afghan_CookieOrder <= 3:
                    for _ in range(Afghan_CookieOrder): 
                        CafeOrders.append(["Afghan Cookie",1])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            PopcornOrder = self.PopcornNumber.get()
            PopcornDigit = PopcornOrder.isdigit()
            if PopcornDigit == True:
                PopcornOrder = int(PopcornOrder)
                if PopcornOrder <= 3:
                    for _ in range(PopcornOrder): 
                        CafeOrders.append(["Popcorn",2])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Other_ChipsOrder = self.Other_ChipsNumber.get()
            Other_ChipsDigit = Other_ChipsOrder.isdigit()
            if Other_ChipsDigit == True:
                Other_ChipsOrder = int(Other_ChipsOrder)
                if Other_ChipsOrder <= 3:
                    for _ in range(Other_ChipsOrder): 
                        CafeOrders.append(["Other Chips", 2])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")

        #Hot Lunches
            Spaghetti_BunOrder = self.Spaghetti_BunNumber.get()
            Spaghetti_BunDigit = Spaghetti_BunOrder.isdigit()
            if Spaghetti_BunDigit == True:
                Spaghetti_BunOrder = int(Spaghetti_BunOrder)
                if Spaghetti_BunOrder <= 3:
                    for _ in range(Spaghetti_BunOrder): 
                        CafeOrders.append(["Spaghetti Bun",1.5])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Steam_BunOrder = self.Steam_BunNumber.get()
            Steam_BunDigit = Steam_BunOrder.isdigit()
            if Steam_BunDigit == True:
                Steam_BunOrder = int(Steam_BunOrder)
                if Steam_BunOrder <= 3:
                    for _ in range(Steam_BunOrder): 
                        CafeOrders.append(["Steam Bun",3.5])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Sausage_RollOrder = self.Sausage_RollNumber.get()
            Sausage_RollDigit = Sausage_RollOrder.isdigit()
            if Sausage_RollDigit == True:
                Sausage_RollOrder = int(Sausage_RollOrder)
                if Sausage_RollOrder <= 3:
                    for _ in range(Sausage_RollOrder): 
                        CafeOrders.append(["Sausage Roll",2])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            PizzaOrder = self.PizzaNumber.get()
            PizzaDigit = PizzaOrder.isdigit()
            if PizzaDigit == True:
                PizzaOrder = int(PizzaOrder)
                if PizzaOrder <= 3:
                    for _ in range(PizzaOrder): 
                        CafeOrders.append(["Pizza",3])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")

        #Drinks
            Hot_ChocolateOrder = self.Hot_ChocolateNumber.get()
            Hot_ChocolateDigit = Hot_ChocolateOrder.isdigit()
            if Hot_ChocolateDigit == True:
                Hot_ChocolateOrder = int(Hot_ChocolateOrder)
                if Hot_ChocolateOrder <= 3:
                    for _ in range(Hot_ChocolateOrder): 
                        CafeOrders.append(["Hot Chocolate",2])
                else:
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")
                    #------------------------------------------------------------------------------
            Barrista_BrosOrder = self.Barrista_BrosNumber.get()
            Barrista_BrosDigit = Barrista_BrosOrder.isdigit()
            if Barrista_BrosDigit == True:
                Barrista_BrosOrder = int(Barrista_BrosOrder)
                if Barrista_BrosOrder <= 3:
                    for _ in range(Barrista_BrosOrder): 
                        CafeOrders.append(["Barrista Bros",4])
                else:
                    
                    print("Too high Order")
                    HighOrder = HighOrder + 1
            else:
                print("No Orders")

            if HighOrder >= 1:
                self.Incorrect_Order.config(text = "Max 3 per item", fg = "red")
            else:
                self.Incorrect_Order.config(text = "Added to Cart", fg = "green")
                

            def DeleteEntries():
                self.DailyMealNumber.delete(0,END)
                self.Fresh_FruitsNumber.delete(0, END)
                self.Chicken_SubNumber.delete(0, END)
                self.WrapNumber.delete(0, END)
                self.Pizza_BreadNumber.delete(0, END)
                self.Potato_ChipsNumber.delete(0, END)
                self.Afghan_CookieNumber.delete(0, END)
                self.Other_ChipsNumber.delete(0, END)
                self.PopcornNumber.delete(0, END)
                self.Spaghetti_BunNumber.delete(0, END)
                self.Steam_BunNumber.delete(0, END)
                self.Sausage_RollNumber.delete(0, END)
                self.PizzaNumber.delete(0, END)
                self.Hot_ChocolateNumber.delete(0, END)
                self.Barrista_BrosNumber.delete(0, END)
            DeleteEntries()
            print(CafeOrders)
            
        self.CartButton = Button(self.MenuPage, text = "Add to Cart", command = Cart)
        self.LogOutButton = Button(self.MenuPage, text = "Go Back", command = self.Logged_Screen)
        
        #-----------------------------------------------Orders Screen-----------------------------------------------
        def Orders():
            NumOfItems = len(CafeOrders)
            for x in range(NumOfItems):
                print(CafeOrders[x])
                
        #-----------------------------------------------Logged Screen Options-----------------------------------------------
        self.LoggedScreen = Frame(root)

        self.Logged_ScreenTitle = Label(self.LoggedScreen, text = "Options", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))
        self.ToMenuButton = Button(self.LoggedScreen, text = "Menu", command = self.Menu)
        self.ToAccountButton = Button(self.LoggedScreen, text = "Account")
        self.ToOrdersButton = Button(self.LoggedScreen, text = "Orders", command = Orders)
        self.LogOutOption = Button(self.LoggedScreen, text = "Log Out", command = self.Log_Screen)

        

        #------------------------------------------------------START------------------------------------------------------
        self.Log_Screen()

        def SaveData():
            with open('Users.List', 'wb') as Users_file:

                pickle.dump(Users, Users_file)
        
        
    #Calls tkinter widget to represent a GUI screen
    def Log_Screen(self):
        #Makes the widgets appear
        self.ForgotPassPage.grid_forget()
        self.SignUp.grid_forget()
        self.LoggedScreen.grid_forget()
        self.LogOn.grid()

        #Widgets being called
        self.Title.grid(columnspan = 2)
        self.UserLabel.grid(column = 0, columnspan = 2, pady = 5)
        self.UserEntry.grid(column = 0, columnspan = 2)
        self.PasswordLabel.grid(column = 0, columnspan = 2, pady = 5)
        self.PasswordEntry.grid(column = 0, columnspan = 2)
        self.IncorrectInfo.grid(column = 0, columnspan = 2)
        self.LogIn.grid(column = 0, columnspan = 2)
        self.ForgotPasswordLabel.grid(row = 6, column = 0, sticky = W, padx = 10)
        self.SignUpLabel.grid(row = 6, column = 1, sticky = E, padx = 10)
        
    def SignUp_Screen(self):
        self.LogOn.grid_forget()
        self.SignUp.grid()
        
        self.SignUpTitle.grid(columnspan = 2)
        self.RegisterUsername.grid(column = 0, row = 1)
        self.RegisterUsernameEntry.grid(column = 1, row = 1)
        self.RegisterPassword.grid(column = 0, row = 2)
        self.RegisterPasswordEntry.grid(column = 1, row = 2)
        self.SignUpButton.grid(column = 1, columnspan = 2, row = 3)
        self.GoBack1.grid(column = 0, row = 3, sticky = W)

    def ForgetPass_Screen(self):
        self.LogOn.grid_forget()
        self.ForgotPassPage.grid()
        
        self.ForgotPassTitle.grid(columnspan = 2)
        self.ForgotPassUser.grid(columnspan = 2)
        self.ForgotPassUserEntry.grid(columnspan = 2)
        self.ForgotPassInfo.grid(columnspan = 2)
        self.SendEmail.grid(columnspan = 2)
        self.GoBack2.grid(column = 0, sticky = W)

    def Logged_Screen(self):
        self.LogOn.grid_forget()
        self.MenuPage.grid_forget()
        self.LoggedScreen.grid()

        self.Logged_ScreenTitle.grid(columnspan = 3)
        self.ToMenuButton.grid(column = 0, row = 1)
        self.ToAccountButton.grid(column = 1, row = 1)
        self.ToOrdersButton.grid(column = 2, row = 1)
        self.LogOutOption.grid(column = 1, row = 2, sticky = S)
        
    def Menu(self):
        self.LoggedScreen.grid_forget()
        self.MenuPage.grid()

        self.MenuTitle.grid(columnspan = 3)
        self.NumberOfItems.grid(column = 2, row = 1)
        self.PriceLabel.grid(column = 1, row = 1)

    #Meal of the Day
        self.MealofTheDay.grid(column = 0, row = 1)
        
        self.DailyMeal.grid(column = 0, row = 2)
        self.DailyMealPrice.grid(column = 1, row = 2)
        self.DailyMealNumber.grid(column = 2, row = 2)

    #Healthy Choices
        self.HealthyChoices.grid(column = 0, row = 3)
        
        self.Fresh_Fruits.grid(column = 0, row = 4)
        self.Fresh_FruitsPrice.grid(column = 1, row = 4)
        self.Fresh_FruitsNumber.grid(column = 2, row = 4)
        
        self.Chicken_Sub.grid(column = 0, row = 5)
        self.Chicken_SubPrice.grid(column = 1, row = 5)
        self.Chicken_SubNumber.grid(column = 2, row = 5)
        
        self.Wrap.grid(column = 0, row = 6)
        self.WrapPrice.grid(column = 1, row = 6)
        self.WrapNumber.grid(column = 2, row = 6)
        
        self.Pizza_Bread.grid(column = 0, row = 7)
        self.Pizza_BreadPrice.grid(column = 1, row = 7)
        self.Pizza_BreadNumber.grid(column = 2, row = 7)

        #Snacks
        self.Snacks.grid(column = 0, row = 8)
        
        self.Potato_Chips.grid(column = 0, row = 9)
        self.Potato_ChipsPrice.grid(column = 1, row = 9)
        self.Potato_ChipsNumber.grid(column = 2, row = 9 )
        
        self.Afghan_Cookie.grid(column = 0, row = 10)
        self.Afghan_CookiePrice.grid(column = 1, row = 10)
        self.Afghan_CookieNumber.grid(column = 2, row = 10)
        
        self.Popcorn.grid(column = 0, row = 11)
        self.PopcornPrice.grid(column = 1, row = 11)
        self.PopcornNumber.grid(column = 2, row = 11)
        
        self.Other_Chips.grid(column = 0, row = 12)
        self.Other_ChipsPrice.grid(column = 1, row = 12)
        self.Other_ChipsNumber.grid(column = 2, row = 12)

        #Hot Lunches
        self.Hot_Lunches.grid(column = 0, row = 13)

        self.Spaghetti_Bun.grid(column = 0, row = 14)
        self.Spaghetti_BunPrice.grid(column = 1, row = 14)
        self.Spaghetti_BunNumber.grid(column = 2, row = 14)
        
        self.Steam_Bun.grid(column = 0, row = 15)
        self.Steam_BunPrice.grid(column = 1, row = 15)
        self.Steam_BunNumber.grid(column = 2, row = 15)
        
        self.Sausage_Roll.grid(column = 0, row = 16)
        self.Sausage_RollPrice.grid(column = 1, row = 16)
        self.Sausage_RollNumber.grid(column = 2, row = 16)
        
        self.Pizza.grid(column = 0, row = 17)
        self.PizzaPrice.grid(column = 1, row = 17)
        self.PizzaNumber.grid(column = 2, row = 17)

        #Drinks
        self.Drinks.grid(column = 0, row = 18)
        
        self.Hot_Chocolate.grid(column = 0, row = 19)
        self.Hot_ChocolatePrice.grid(column = 1, row = 19)
        self.Hot_ChocolateNumber.grid(column = 2, row = 19)
        
        self.Barrista_Bros.grid(column = 0, row = 20)
        self.Barrista_BrosPrice.grid(column = 1, row = 20)
        self.Barrista_BrosNumber.grid(column = 2, row = 20)

        #Others
        self.Incorrect_Order.grid(row = 21, columnspan = 3)
        self.CartButton.grid(column = 2, sticky = E, row = 22)
        self.LogOutButton.grid(column = 0, sticky = W, row = 22)
        

#Function to Start Up the program
def main():
    root = Tk()
    root.title("BDSC Cafe")
    root.geometry("367x420+420+160")
    root['background'] = '#F8F8F8'
    def LoadData():
        global Users_file
        global Users
        Users_file = 'Users.List'
        if os.path.exists(Users_file):
            with open(Users_file, 'rb') as Users_file:
                Users = pickle.load(Users_file)

            print(Users)
            App = Cafe(root)
        else:
            print("No User List")
            App = Cafe(root)
    LoadData()

#Automatically runs if the name of the program = the name of the program
if __name__ == "__main__":
    main()


