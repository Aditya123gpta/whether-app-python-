import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to SQLite database and create the tables
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aadhar_number TEXT NOT NULL UNIQUE,
        name TEXT,
        password TEXT NOT NULL,
        pincode TEXT,
        address TEXT,
        mobile_no TEXT,
        age INTEGER,
        father_name TEXT
    )
''')

# Create votes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        party_name TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

# Function to register a new user
def register_user():
    aadhar_number = entry_aadhar.get()
    name = entry_name.get()
    password = entry_password.get()
    pincode = entry_pincode.get()
    address = entry_address.get()
    mobile_no = entry_mobile.get()
    age = entry_age.get()
    father_name = entry_father.get()

    # Validate age
    try:
        age = int(age)
        if age < 18:
            messagebox.showerror("Error", "Age must be 18 or above.")
            return
    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")
        return

    # Connect to SQLite database and insert user
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (aadhar_number, name, password, pincode, address, mobile_no, age, father_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (aadhar_number, name, password, pincode, address, mobile_no, age, father_name))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Aadhar number already exists.")
    finally:
        conn.close()

# Function to log in a user
def login_user():
    login_aadhar = entry_login_aadhar.get()
    login_password = entry_login_password.get()

    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE aadhar_number=? AND password=?
    ''', (login_aadhar, login_password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Success", f"Welcome, {user[1]}!")
        open_home_page()
    else:
        messagebox.showerror("Error", "Invalid Aadhar number or password.")

# Function to open the home page with voting options
def open_home_page():
    global result_label
    home_page = tk.Toplevel(root)
    home_page.title("Voting Machine")
    home_page.configure(bg="light blue")
    
    label_instruction = tk.Label(home_page, text="Instruction:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
    label_instruction.grid(row=0, column=0, padx=10, pady=5)
    
    party_names = ["Party A", "Party B", "Party C", "Party D", "Party E"]
    buttons = []
    
    for i, party in enumerate(party_names):
        button = tk.Button(home_page, text=party, width=20, font=('monotype corsiva', 15, 'bold'), fg="red", command=lambda p=party: cast_vote(p))
        button.grid(row=i+1, column=0, padx=10, pady=5)
        buttons.append(button)
    
    label_winner = tk.Label(home_page, text="Winner:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
    label_winner.grid(row=len(party_names)+1, column=0, padx=10, pady=5)
    result_label = tk.Label(home_page, text="", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
    result_label.grid(row=len(party_names)+2, column=0, padx=10, pady=5)
    
    update_winner_label()  # Update the winner label when the home page is opened

    home_page.mainloop()

# Function to handle vote casting
def cast_vote(party):
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO votes (party_name) VALUES (?)
    ''', (party,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Vote Cast", f"You voted for {party}")
    update_winner_label()

# Function to calculate and display the winner
def update_winner_label():
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT party_name, COUNT(party_name) AS vote_count FROM votes GROUP BY party_name ORDER BY vote_count DESC LIMIT 1
    ''')
    winner = cursor.fetchone()
    conn.close()
    if winner:
        result_label.config(text=f"{winner[0]} with {winner[1]} votes")
    else:
        result_label.config(text="No votes yet")

# Create the main Tkinter window for registration and login
root = tk.Tk()
root.title("User Registration and Login")
root.configure(bg="light blue")

# Registration Section
label_aadhar = tk.Label(root, text="Aadhar Number:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_aadhar.grid(row=0, column=0, padx=10, pady=5)
entry_aadhar = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_aadhar.grid(row=0, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Name:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_name.grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_password.grid(row=2, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show='*', width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_password.grid(row=2, column=1, padx=10, pady=5)

label_pincode = tk.Label(root, text="Pincode:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_pincode.grid(row=3, column=0, padx=10, pady=5)
entry_pincode = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_pincode.grid(row=3, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_address.grid(row=4, column=0, padx=10, pady=5)
entry_address = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_address.grid(row=4, column=1, padx=10, pady=5)

label_mobile = tk.Label(root, text="Mobile No.:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_mobile.grid(row=5, column=0, padx=10, pady=5)
entry_mobile = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_mobile.grid(row=5, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_age.grid(row=6, column=0, padx=10, pady=5)
entry_age = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_age.grid(row=6, column=1, padx=10, pady=5)

label_father = tk.Label(root, text="Father's Name:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_father.grid(row=7, column=0, padx=10, pady=5)
entry_father = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_father.grid(row=7, column=1, padx=10, pady=5)

register_button = tk.Button(root, text="Register", width=20, font=('monotype corsiva', 15, 'bold'), fg="red", command=register_user)
register_button.grid(row=8, column=0, columnspan=2, pady=10)

# Login Section
label_login_aadhar = tk.Label(root, text="Aadhar Number:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_login_aadhar.grid(row=9, column=0, padx=10, pady=5)
entry_login_aadhar = tk.Entry(root, width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_login_aadhar.grid(row=9, column=1, padx=10, pady=5)

label_login_password = tk.Label(root, text="Password:", font=('Arial Black', 18, 'bold'), fg="blue", bg="light blue")
label_login_password.grid(row=10, column=0, padx=10, pady=5)
entry_login_password = tk.Entry(root, show='*', width=30, font=('monotype corsiva', 15, 'bold'), fg="red")
entry_login_password.grid(row=10, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", width=20, font=('monotype corsiva', 15, 'bold'), fg="red", command=login_user)
login_button.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
