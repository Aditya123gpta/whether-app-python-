import tkinter as t
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Function to handle registration
def submitButton():
    username = ename.get()
    password = epass.get()
    gender = m.get()
    usertype = ttype.get()

    if username and password and gender and usertype != '-Select User Type-':
        db = sqlite3.connect("prashansha.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS newuser(name TEXT, password TEXT, gender TEXT, usertype TEXT)")
        q = "INSERT INTO newuser(name, password, gender, usertype) VALUES (?, ?, ?, ?)"
        v = (username, password, gender, usertype)
        cur.execute(q, v)
        db.commit()
        messagebox.showinfo("Register", "Thanks for Registration")
    else:
        messagebox.showwarning("Register", "Please fill all the fields")

# Function to handle sign-in
def signInButton():
    signin_window = t.Toplevel(root)
    signin_window.title("Sign In")
    signin_window.geometry("800x600")
    signin_window.configure(bg='light blue')

    # Define Labels
    luser = t.Label(signin_window, text="User Name", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    luser.grid(row=0, column=0, padx=10, pady=10)
    lpass = t.Label(signin_window, text="Password", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    lpass.grid(row=1, column=0, padx=10, pady=10)

    # Entry box
    euser = t.Entry(signin_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
    euser.grid(row=0, column=1, padx=10, pady=10)
    epass = t.Entry(signin_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red", show="*")
    epass.grid(row=1, column=1, padx=10, pady=10)

    # Function to validate user credentials
    def validateCredentials():
        username = euser.get()
        password = epass.get()
        db = sqlite3.connect("prashansha.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM newuser WHERE name = ? AND password = ?", (username, password))
        result = cur.fetchone()
        if result:
            messagebox.showinfo("Sign In", "Welcome " + username)
            signin_window.destroy()
            openBookingSystem(username)
        else:
            messagebox.showerror("Sign In", "Invalid Credentials")

    # Button to submit sign-in
    submit = t.Button(signin_window, text="Sign In", font=('monotype corsiva', 20, 'bold'), fg="red", bg="pink", command=validateCredentials)
    submit.grid(row=2, column=1, padx=10, pady=10)

# Function to open Airline ticket booking system
def openBookingSystem(username):
    booking_window = t.Toplevel(root)
    booking_window.title("Airline Ticket Booking System")
    booking_window.geometry("800x600")
    booking_window.configure(bg='light blue')

    # Example elements in the booking system window
    lbook = t.Label(booking_window, text="Welcome to the Airline Ticket Booking System", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    lbook.pack(padx=10, pady=10)

    # Labels and entry widgets for flight details
    lsource = t.Label(booking_window, text="Source", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    lsource.pack(padx=10, pady=10)
    esource = t.Entry(booking_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
    esource.pack(padx=10, pady=10)

    ldest = t.Label(booking_window, text="Destination", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    ldest.pack(padx=10, pady=10)
    edest = t.Entry(booking_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
    edest.pack(padx=10, pady=10)

    ldate = t.Label(booking_window, text="Date", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    ldate.pack(padx=10, pady=10)
    edate = t.Entry(booking_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
    edate.pack(padx=10, pady=10)

    lclass = t.Label(booking_window, text="Class", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    lclass.pack(padx=10, pady=10)
    eclass = t.Entry(booking_window, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
    eclass.pack(padx=10, pady=10)

    # Function to handle booking
    def bookTicket():
        source = esource.get()
        destination = edest.get()
        date = edate.get()
        travel_class = eclass.get()

        if source and destination and date and travel_class:
            showTicket(username, source, destination, date, travel_class)
        else:
            messagebox.showwarning("Booking", "Please fill all the fields")

    # Button to book ticket
    book_button = t.Button(booking_window, text="Book Ticket", font=('monotype corsiva', 20, 'bold'), fg="red", bg="pink", command=bookTicket)
    book_button.pack(padx=10, pady=10)

# Function to show the booked ticket
def showTicket(username, source, destination, date, travel_class):
    ticket_window = t.Toplevel(root)
    ticket_window.title("Ticket Details")
    ticket_window.geometry("800x600")
    ticket_window.configure(bg='light blue')

    lticket = t.Label(ticket_window, text="Ticket Details", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    lticket.pack(padx=10, pady=10)

    details = f"Name: {username}\nSource: {source}\nDestination: {destination}\nDate: {date}\nClass: {travel_class}"
    ldetails = t.Label(ticket_window, text=details, font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
    ldetails.pack(padx=10, pady=10)

root = t.Tk()
root.title("Register")
root.geometry("800x600")
root.configure(bg='light blue')

# Define Labels
lname = t.Label(root, text="User Name", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
lname.grid(row=0, column=0, padx=10, pady=10)
lpass = t.Label(root, text="Password", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
lpass.grid(row=1, column=0, padx=10, pady=10)
lgen = t.Label(root, text="Gender", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
lgen.grid(row=2, column=0, padx=10, pady=10)
ltype = t.Label(root, text="User Type", font=('Arial Black', 18, 'bold'), fg="white", bg="pink")
ltype.grid(row=3, column=0, padx=10, pady=10)

# Entry box
ename = t.Entry(root, width=30, font=('monotype corsiva', 20, 'bold'), fg="red")
ename.grid(row=0, column=1, padx=10, pady=10)
epass = t.Entry(root, width=30, font=('monotype corsiva', 20, 'bold'), fg="red", show="*")
epass.grid(row=1, column=1, padx=10, pady=10)

# Define Radiobutton
m = t.StringVar()
radiomale = t.Radiobutton(root, text="Male", value="Male", variable=m, font=('monotype corsiva', 20, 'bold'))
radiomale.grid(row=2, column=1, padx=10, pady=10)
radiofemale = t.Radiobutton(root, text="Female", value="Female", variable=m, font=('monotype corsiva', 20, 'bold'))
radiofemale.grid(row=2, column=2, padx=10, pady=10)

# Define Combobox
ttype = ttk.Combobox(root, values=['-Select User Type-', 'Admin', 'Faculty', 'Student', 'Other'], font=('monotype corsiva', 20, 'bold'))
ttype.current(0)
ttype.grid(row=3, column=1, padx=10, pady=10)

# Registration Button
submit = t.Button(root, text="Sign Up", font=('monotype corsiva', 20, 'bold'), fg="white", bg="pink", command=submitButton)
submit.grid(row=6, column=1, padx=10, pady=10)

# Sign-In Button
signin = t.Button(root, text="Sign In", font=('monotype corsiva', 20, 'bold'), fg="white", bg="pink", command=signInButton)
signin.grid(row=6, column=2, padx=10, pady=10)
root.mainloop()
