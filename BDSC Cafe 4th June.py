#BDSC Cafe App
from tkinter import*
import datetime
import random
import string

#Data
Users = [["test","User"]] #[Username,Password,ID Number]
Cafe_Orders = [] #[Users, Cafe Items]

#Cafe Items (Food,Cost)
Drinks = [["Hot Chocolate", 2], ["Barista Bros", 4]]
Hot_Lunches = [["Spaghetti Bun", 1.5], ["Steam Bun", 3.5], ["Sausage Roll", 2], ["Pizza", 3]]
HealthyChoices = [["Fresh_Fruits", 1],["Chicken_Sub", 4],["Wrap", 4.50],["Pizza Bread", 3]]
Snacks = [["Potato Chips", 2],["Popcorn", 2],["Other Chips", 2],["Afghan Cookies", 1]]
MealOfTheDay = [ [["Nachos", 4],["Pies", 4.50],["Potato Puffs", 3]], ["Rolls", 3], ["Quinche", 3], [["Chicken Burger", 4], ["Board Special", 5]], ["Sushi", 5]]
               #Monday--------------------------------------------  Tuesday----   Wednesday-----  Thursday-------------------------------------  Friday------

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
                      self.Menu()
                 else:
                      print("Incorrect Password")
            else:
                 print("Not a User")

        def find_in_nested_list(mylist, char):
                 for sub_list in mylist:
                      if char in sub_list:
                           print("Position in List:", mylist.index(sub_list), sub_list.index(char))
                           Pass = int(sub_list.index(char))
                           Pass_find = Pass + 1
                           global User_Pass
                           User_Pass = sub_list[Pass_find]
                           print("User Pass:", User_Pass)
                           
        self.LogIn = Button(self.LogOn, text = "Log in", command = CheckUser )
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

        self.SignUpTitle = Label(self.SignUp, text = "Registration", bg = "#d3e0ec", fg = "orange", width = 15
                           , padx = 10, pady = 10, font = ("Helvetica", 30, "italic"))
        self.GoBack1 = Button(self.SignUp, text = "Go Back", command = self.Log_Screen)
        self.RegisterUsername = Label(self.SignUp, text = "Username:", fg = "grey", font = ("Times", 20, "bold"))
        self.RegisterUsernameEntry = Entry(self.SignUp)
        self.RegisterPassword = Label(self.SignUp, text = "Password:", fg = "grey", font = ("Times", 20, "bold"))
        self.RegisterPasswordEntry = Entry(self.SignUp)
        self.SignUpButton = Button(self.SignUp, text = "Sign Up")

        #-------------------------------------------------Forgot Password Widgets--------------------------------------------
        self.ForgotPassPage = Frame(root)
            
        def ResetPass():
            def ChangePass():
                def randomString(stringLength):
                    letters = string.ascii_letters
                    return ''.join(random.choice(letters) for i in range(stringLength))
                RandomPass = randomString(8)
                global Users
                find_in_nested_list(Users, FP_UE)
                self.ForgotPassInfo.config(text = "Password: {}".format(RandomPass))
                Users = [[x.replace(User_Pass,RandomPass) for x in l] for l in Users]
                print(Users)


                
            FP_UE = self.ForgotPassUserEntry.get()
            FP_UE_Check = FP_UE in (item for sublist in Users for item in sublist)
            print(str(FP_UE_Check))
            if FP_UE_Check == True:
                self.ForgotPassUserEntry.delete(0, END)
                self.ForgotPassInfo.config(text = "Generating new password...")
                self.ForgotPassInfo.after(100, ChangePass)
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
        def CheckMealOfTheDay():
            Date = datetime.datetime.today().weekday() #Monday = 0 to Sunday = 6
            print(Date)
            NumofMeals = len(MealOfTheDay[Date])
            print(NumofMeals)
            for NumofMeals in MealOfTheDay[Date]:
                print(NumofMeals)
            MealOfTheDay[Date][1]

        CheckMealOfTheDay()
        #Meal of the Day
        self.MealofTheDay = Label(self.MenuPage, text = "Meal of the Day")
        self.DailyMeal = Label(self.MenuPage, text = "")

        #Healthy Choices
        self.HealthyChoices = Label(self.MenuPage, text = "Healthy Choices")
        self.Fresh_Fruits = Label(self.MenuPage, text = "Fresh Fruits")
        self.Chicken_Sub = Label(self.MenuPage, text = "Chicken Sub")
        self.Wrap = Label(self.MenuPage, text = "Wraps")
        self.Pizza_Bread = Label(self.MenuPage, text = "Pizza Bread")

        #Snacks
        self.Snacks = Label(self.MenuPage, text = "Snacks")
        self.Potato_Chips = Label(self.MenuPage, text = "Potato Chips")
        self.Afghan_Cookie = Label(self.MenuPage, text = "Afghn Cookie")
        self.Popcorn  = Label(self.MenuPage, text = "Popcorn")
        self.Other_Chips = Label(self.MenuPage, text = "Other Chips")

        #Hot Lunches
        self.Hot_Lunches = Label(self.MenuPage, text = "Hot Lunches")
        self.Spaghetti_Bun = Label(self.MenuPage, text = "Spaghetti Bun")
        self.Steam_Bun = Label(self.MenuPage, text = "Steam Bun")
        self.Sausage_Roll = Label(self.MenuPage, text = "Sausage Roll")
        self.Pizza = Label(self.MenuPage, text = "Pizza")

        #Drinks
        self.Drinks = Label(self.MenuPage, text = "Drinks")
        self.Hot_Chocolate = Label(self.MenuPage, text = "Hot Chocolate")
        self.Barrista_Bros = Label(self.MenuPage, text = "Barrista Bros")
        
        
        #Start the first GUI
        self.Log_Screen()
        
        
    #Calls tkinter widget to represent a GUI screen
    def Log_Screen(self):
        #Makes the widgets appear
        self.ForgotPassPage.grid_forget()
        self.SignUp.grid_forget()
        self.LogOn.grid()

        #Widgets being called
        self.Title.grid(columnspan = 2)
        self.UserLabel.grid(column = 0, columnspan = 2, pady = 5)
        self.UserEntry.grid(column = 0, columnspan = 2)
        self.PasswordLabel.grid(column = 0, columnspan = 2, pady = 5)
        self.PasswordEntry.grid(column = 0, columnspan = 2)
        self.IncorrectInfo.grid()
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
   
    def Menu(self):
        self.LogOn.grid_forget()
        self.MenuPage.grid()
        
        self.MenuTitle.grid(columnspan = 3)

        self.MealofTheDay.grid(column = 0)
        self.DailyMeal.grid(column = 0)

        self.HealthyChoices.grid(column = 0)
        self.Fresh_Fruits.grid(column = 0)
        self.Chicken_Sub.grid(column = 0)
        self.Wrap.grid(column = 0)
        self.Pizza_Bread.grid(column = 0)

        self.Snacks.grid(column = 0)
        self.Potato_Chips.grid(column = 0)
        self.Afghan_Cookie.grid(column = 0)
        self.Popcorn.grid(column = 0)
        self.Other_Chips.grid(column = 0)

        self.Hot_Lunches.grid(column = 0)
        self.Spaghetti_Bun.grid(column = 0)
        self.Steam_Bun.grid(column = 0)
        self.Sausage_Roll.grid(column = 0)
        self.Pizza.grid(column = 0)

        self.Drinks.grid(column = 0)
        self.Hot_Chocolate.grid(column = 0)
        self.Barrista_Bros.grid(column = 0)
        
    def ForgetPass_Screen(self):
        self.LogOn.grid_forget()
        self.ForgotPassPage.grid()
        
        self.ForgotPassTitle.grid(columnspan = 2)
        self.ForgotPassUser.grid(columnspan = 2)
        self.ForgotPassUserEntry.grid(columnspan = 2)
        self.ForgotPassInfo.grid(columnspan = 2)
        self.SendEmail.grid(columnspan = 2)
        self.GoBack2.grid(column = 0, sticky = W)

#Program to "Start Up" the program
def main():
    root = Tk()
    root.title("BDSC Cafe")
    root.geometry("365x420+420+160")
    root['background'] = '#F8F8F8'
    App = Cafe(root)

#Automatically runs if the name of the program = the name of the program
if __name__ == "__main__":
    main()



https://www.geeksforgeeks.org/python-after-method-in-tkinter/
https://pynative.com/python-generate-random-string/
https://stackoverflow.com/questions/13781828/replace-a-string-in-list-of-lists
