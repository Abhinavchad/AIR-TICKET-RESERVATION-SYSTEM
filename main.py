from tkinter import *
from tkinter import messagebox
import mysql.connector
def goToHome():
  home = Tk() 
  home.geometry (500x500)
  home.title("Home")
  objectHome=Home(home) 
  Home.homePage(objectHome)

def trigger Home (window):
  window.destroy() 
  goToHome()

mydb= mysql.connector.connect(

  host="localhost", users="root",
  
  password="12345678",
  
  database="AirlineReservation"
)


class Login:

  def __init__(self,master) -> None:
    self.top master



def login(self, usernameField, passwordField):
  if len(usernameField.get()) 0 or len(passwordfield.get()) == 0: 
    messagebox. showerror("Empty Username or Password", "Username or Password Can Not Be Blank")
  else:
    sql= "SELECT PASSBORD FROM LOGIN WHERE USER_ID =%s"
    myCursor mydb.cursor()
    tup=(usernameField.get().strip(),)
    myCursor.execute(sql, tup)
    result=myCursor.fetchone() 
    if result is None:
      messagebox.showerror("Incorrect UserID", "Enter the Correct User ID or Register for New User ID")
      usernameField.set("") 
      passwordField.set("")
    elif result[0]= passwordField.get().strip():
      self.top.destroy() 
      goToHome()
    else:
      messagebox.showerror ("Incorrect Password", "Enter the Correct Password")
      usernameField.set("")
      passwordField.set("")
    myCursor.close()
def register(self):
  self.top.destroy()
  registerPage=Tk()
  registerPage.geometry("500x500")
  registerPage.title("Register New User")
  objectRegister=Register(registerPage)
  Register.registerPage(objectRegister)

def loginPage(self):
  Label (self.top, text="WELCOME TO HOLIDAY TRAVELS 11", font=("ARIAL", 25), bd='5').pack()
  Label(self.top, text="UserID", font=("ARIAL", 16)). place (x=48, y=100)
  Label(self.top, text="Password", font ("ARIAL", 16)).place(x=48, y=150)
  var_name StringVar()
  var_passwd StringVar()
  Entry(self.top, width=30, textvariable-var_name).place(x=158, y=108)
  Entry(self.top, shows"e", width=30, textvariable-var_passwd). place (x=150, y=150)
  Button(self.top, text="Login", font=("ARIAL", 16), pady 10, width-20, bd='5', command=lambda: self.login(var_name, var_passwd)).place(x=40, y=200)
  Button(self.top, text="New User? Register", font=("ARIAL", 16), pady=10, width=28, bd='5', command=self.register). place (x=260, y=200)
class Register:
  def __init__(self, master) -> None:
    self.top master
  def registerCustomer(self, usernameField, passwordField):
    if len(passwordField.get()) == 0:
      messagebox.showerror("Password Can Not be Blank", "Enter a Valid Password")
    else:
      sql="INSERT INTO LOGIN VALUES (X,X)"
      myCursor=mydb.cursor()
      tup=(int (usernameField.get().strip()), passwordField.get().strip(),)
      myCursor.execute(sal, tup)
      mydb.commit()
      myCursor.close()
      messagebox.showinfo("User Successfully Registered", "You have been registered successf
      self.top.destroy()
      top=Tk()
      top.geometry("500x500")
      top.title("Holiday Travels") 
      objectLogin=Login(top)
      Login.LoginPage(objectLogin)

def registerPage(self):

  Label(self.top, text="Enter the Details to Get Registered 11", font=("ARIAL", 25), bd='5').pack()
  Label(self, top, text="UserID", fante ("ARIAL", 16)).place(x=40, y=100)
  Label (self.top, texte "Enter Password", font=("ARIAL", 16)).place(x=40, y=150)
  var_name=Stringvar()
  var_passwd=StringVar()
  sql = "SELECT MAX(USER_ID) FROM LOGIN"
  myCursor=mydb.cursor()
  myCursor.execute(sql)
  result = myCursor.fetchone()
  userId=int(result[0])+1
  var_nene.set(str(userId))
  myCursor.close() 
  Entry(self.top, width=30, state='disabled',textvariable=var_name).place(x=200,y=100)
  Entry(self.top,show="*",width=30, textvariable=var_passwd).place(x=200,y=150)
  Button(self.top, text="Register", font=("ARIAL", 16), pady=10, width=20, bd='5', command=lambda: self.registerCustomer(var_name, var_passwd)).place(x=250,y=200)
class Home:
  def __init__(self, master) -> None:
    self.top=master
  def bookTicket(self): self.top.destroy()
    booking = Tk()
    booking.geometry("500x500")
    booking.title("Book Ticket")
    objectBook=BockTicket(booking)
    BookTicket.bookTicketPage(objectBook)
  def cancel Ticket(self):
    self.top.destroy()
    cancel TK()
    cancel.geometry("500x500")
    cancel.title("Cancel Ticket")
    objectCancel=Cancel(cancel)
    Cancel.cancelPage(objectCancel)

  def logoutButton(self):
    self.top.destroy()
    Logout=Tk()
    Logout.geometry("500x500")
    Logout.title("Log Out")
    objectLogout=Logout(logout)
    Logout.logoutPage(objectLogout)

  def homePage(self):
    Label(self.top, texts="How May We Help You ?", fonts ("ARIAL", 25), bd='5').pack() 
    Button(self.top, texts="Book Ticket", font ("ARIAL", 16), pady=10, width=15, bds='5', command=self.bookTicket).place(x-1,y=200)
    Button(self.top, texts="Cancel Ticket", font ("ARIAL", 16), pady=10, width=15, bds='5', command=self.cancelTicket).place(x=180,y=200)
    Button(self.top, texts="Logout", font ("ARIAL", 16), pady=10, width=15, bds='5', command=self.logoutButton).place(x-360,y=200)
  
  class BookTicket:

    def __init__(self, master)-> None:
        self.top = master

    def flightSearch(self, departure, arrival, date):
        if departure.get() == 'From' or arrival.get() == 'To' or len(date.get()) == 0:
            messagebox.showerror("Fields are empty", "Enter all the fields")
        elif departure.get() == arrival.get():
            messagebox.showerror("Departure and Arrival Are Same", "Departure and Arrival Must be different")
        else:
            self.top.destroy()
            details = Tk()
            details.geometry("500x500")
            details.title("Passenger Details")
            objectDetails = Detail(details, date, departure, arrival)
            Detail.detailsPage(objectDetails)

    def bookTicketPage(self):
        Label(self.top, text="Book Your Ticket", font=("ARIAL", 25)).pack()
        Label(self.top, text="Departure", font=("ARIAL", 16), width=15).place(x=100, y=100)
        Label(self.top, text="Arrival", font=("ARIAL", 16), width=15).place(x=100, y=150)
        Label(self.top, text="Travel Date", font=("Arial", 16), width=15).place(x=100, y=200)
        Label(self.top, text="(yyyy-mm-dd) format", font=("Arial", 9), width=15).place(x=120, y=220)

        options = [
            "Mumbai"
            "New Delhi",
            "Kolkata",
            "Chennai"
        ]
        departure = StringVar()
        arrival = StringVar()
        date = StringVar()

        departure.set("From")
        arrival.set("To")

        OptionMenu(self.top, departure, *options).place(x=300, y=100)
        OptionMenu(self.top, arrival, *options).place(x=300, y=150)
        Entry(self.top, textvariable=date,width=10).place(x=300,y=200)
        Button(self.top,text="Search Flights",font=("ARIAL",16),pady=10,width=15,bd='5',command=lambda:self.flightSearch(departure, arrival, date)).place(x=175,y=250)
        Button(self.top,text="Home",font=("ARIAL",16),pady=10,width=15,bd='5',command=lambda: triggerHome(self.top)).pack()
   
class Detail:
    def __init__(self, master, date, departure, arrival):
        self.top = master
        self.date = date
        self.departure = departure
        self.arrival = arrival

    def payment(self, ticketID, flightID, name, age, date):
        if flightID.get() == "Select Flight" or len(name.get()) == 0 or len(age.get()) == 0:
            messagebox.showerror("Fields are empty", "Enter all the Fields")
        else:
            self.top.destroy()
            pay = Tk()
            pay.geometry("500x500")
            pay.title("Payment")
            objectPayment = Payment(pay, ticketID, flightID, name, age, date)
            Payment.paymentPage(objectPayment)
    def detailsPage(self):
        Label(self.top, text="Enter Your Details", font=("ARIAL", 25)).pack()
        Label(self.top, text="Ticket ID", font=("ARIAL", 16)).place(x=100, y=100)
        Label(self.top, text="Flight ID", font=("ARIAL", 16)).place(x=100, y=150)
        Label(self.top, text="Name", font=("Arial", 16)).place(x=100, y=200)
        Label(self.top, text="Age", font=("Arial", 16)).place(x=100, y=250)
        options = []
        ticketID = StringVar()
        flightID = StringVar()
        name = StringVar()
        age = StringVar()

        sql = "SELECT MAX(TICKET_ID) FROM TICKETS"
        myCursor = mydb.cursor()
        myCursor.execute(sql)
        result = myCursor.fetchone()
        tId = int(result[0]) + 1
        ticketID.set(str(tId))
        flightID.set("Select Flight")

        sql = "SELECT FLIGHT_ID FROM FLIGHTS WHERE DEPARTURE = %s AND ARRIVAL = %s"
        tup = (self.departure.get().strip(), self.arrival.get().strip(),)  
        myCursor.execute(sql, val)
        result = myCursor.fetchall()

        for x in result:
            options.append(x[0])

        myCursor.close()

        Entry(self.top, width=18, state='disabled', textvariable=ticketID).place(x=300, y=100)
        OptionMenu(self.top, flightID, *options).place(x=300, y=158)
        Entry(self.top, textvariable=name, width=10).place(x=300, y=208)
        Entry(self.top, textvariable=age, width=10).place(x=300, y=250)

        Button(self.top, text="Make Payment", font=("ARIAL", 16), pady=10, width=15,
               command=lambda: self.payment(ticketID, flightID, name, age, self.date)).place(x=175, y=358)
        Button(self.top, text="Home", font=("ARIAL", 16), pady=10, width=15,
               command=lambda: triggerHome(self.top)).pack()
class Payment:
    def __init__(self, master, ticketID, flightID, name, age, date):
        self.top = master
        self.ticketID = ticketID
        self.flightID = flightID
        self.name = name
        self.age = age
        self.date = date

    def pay(self, cardNumber, cardName, expiry, cw):
        if len(cardNumber.get()) == 0 or len(cardName.get()) == 0 or len(expiry.get()) == 8 or len(cvv.get()) == 0:
            messagebox.showerror("Fields are empty", "Enter all the Fields")
        elif len(cardNumber.get()) != 16:
            messagebox.showerror("Incorrect Card Number", "Enter correct card number")
        elif len(cvv.get()) != 3:
            messagebox.showerror("Incorrect CVV", "Enter correct CVV")
        else:
            sql = "INSERT INTO TICKETS VALUES (%s, %s, %s, %s, %s)"
            tup = (self.ticketID.get().strip(), self.name.get().strip(), self.age.get().strip(),
                   self.date.get().strip(), self.flightID.get().strip(),)

            myCursor = mydb.cursor()
            myCursor.execute(sql, tup)
            mydb.commit()
            myCursor.close()

            messagebox.showinfo("Payment Successful", "Thank you for booking the ticket! \n\nREMEMBER TICKET ID FOR FUTURE REFERENCE: {}".format(self.ticketID.get()))

            self.top.destroy()    
            goToHome()
      def paymentPage(self):
        Label(self.top, text="Payment Details", font=("ARIAL", 25)).pack()
        Label(self.top, text="Card Number", font=("ARIAL", 16)).place(x=100, y=100)
        Label(self.top, text="Cardholder Name", font=("ARIAL", 16)).place(x=100, y=150)
        Label(self.top, text="Expiry Date", font=("Arial", 16)).place(x=100, y=200)
        Label(self.top, text="CVV", font=("Arial", 16)).place(x=100, y=250)

        cardNumber = StringVar()
        cardName = StringVar()
        expiry = StringVar()
        cvv = StringVar()
        Entry(self.top, textvariable=cardNumber, width=18).place(x=300, y=100)
        Entry(self.top, textvariable=cardName, width=10).place(x=300, y=150)
        Entry(self.top, textvariable=expiry, width=10).place(x=300, y=200)
        Entry(self.top, textvariable=cvv, width=10,show='*').place(x=300, y=250)
class Cancel:

    def __init__(self, master):
        self.top = master

    def cancelTicket(self, ticketID):
        result = messagebox.askquestion("Cancel Ticket", "Are you sure you want to cancel this ticket?", icon='warning')
        if result == 'yes':
            sql = "DELETE FROM TICKETS WHERE TICKET_ID = %s"
            tup = (ticketID.get(),)
            myCursor = mydb.cursor()
            myCursor.execute(sql, tup)
            mydb.commit()
            myCursor.close()
            messagebox.showinfo("Cancel Ticket", "Ticket Cancellation Successful")
            self.top.destroy()
            goToHome()
    def searchTicket(self, ticketID):
        name=StringVar()
        age=StringVar()
        flightID=StringVar()
        sql = "SELECT NAME, AGE, FLIGHT_ID FROM TICKETS WHERE TICKET_ID = %s"
        tup = (ticketID.get().strip(),)
        if ticketID.get().strip()=="1":
          messagebox.showerror("Incorrect Ticket ID","Enter the correct Ticket ID")
        else:
          myCursor = mydb.cursor()
          myCursor.execute(sql, tup)
          result = myCursor.fetchone()
          myCursor.close()
          if result is None:
              messagebox.showerror("Incorrect Ticket ID", "Enter the Correct Ticket ID")
          else:
              name.set(result[0])
              age.set(result[1])
              flightID.set(result[2])

    def cancelPage(self):
        tickets = StringVar()

        Label(self.top, text="Ticket Cancellation", font=("ARIAL", 25)).pack()
        Label(self.top, text="Ticket ID", font=("ARIAL", 16)).place(x=40, y=100)
        Entry(self.top, textvariable=ticketID, width=10).place(x=150, y=100)

        Button(self.top, text="Search Ticket", font=("ARIAL", 16), pady=10, width=15,bd='5',
               command=lambda: self.searchTicket(ticketID)).place(x=300, y=100)

        Button(self.top, text="Cancel Ticket", font=("ARIAL", 26), pady=10, width=15,bd='5'
               command=lambda: self.cancelTicket(ticketID)).place(x=175, y=350)

        Button(self.top, text="Home", font=("ARIAL", 16), pady=10, width=15,bd='5'
               command=lambda: triggerHome(self.top)).pack()

class Logout:

    def __init__(self, master):
        self.top = master

    def submit(self, feedbackBox):
        # Implementation for submitting feedback
        pass

    def LogoutPage(self):
        Label(self.top, text="Enter your valuable feedback", font=("ARIAL", 25)).pack()

        feedbackBox = Text(self.top, height=20, width=10, bd=10)
        feedbackBox.pack()

        Button(self.top, text="Submit", font=("ARIAL", 26), pady=10, width=15, bd="5801",
               command=lambda: self.submit(feedbackBox)).pack()
    
if __name__ == "__main__":
    top = Tk()
    top.geometry("500x500")
    top.title("Holiday Travels")

    objectLogin = Login(top)
    Login.LoginPage(objectLogin)

    top.mainloop()

    mydb.close()        
