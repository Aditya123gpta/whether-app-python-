import tkinter as tk
from tkinter import messagebox

# Sample dictionary to simulate room status (in a real application, this could come from a database)
room_status = {
    '101': {'status': 'available', 'guest': None},
    '102': {'status': 'available', 'guest': None},
    '103': {'status': 'occupied', 'guest': 'John Doe'},
    # Add more rooms as needed
}

# Function to handle room booking
def bookRoom():
    room_number = entry_room.get()
    guest_name = entry_name.get()
    checkin_date = entry_checkin.get()
    checkout_date = entry_checkout.get()
    
    # Check if the room is available
    if room_number in room_status and room_status[room_number]['status'] == 'available':
        # Update room status (in a real application, this would update a database)
        room_status[room_number]['status'] = 'occupied'
        room_status[room_number]['guest'] = guest_name
        
        # Show success message
        messagebox.showinfo("Room Booking", f"Room {room_number} booked for {guest_name} from {checkin_date} to {checkout_date}.")
        
        # Show booking details
        showBookingDetails(room_number, guest_name, checkin_date, checkout_date)
    else:
        messagebox.showerror("Booking Error", f"Room {room_number} is not available.")

# Function to display booking details
def showBookingDetails(room_number, guest_name, checkin_date, checkout_date):
    booking_details_window = tk.Toplevel(root)
    booking_details_window.title("Booking Details")
    booking_details_window.geometry("400x300")
    booking_details_window.configure(bg='light blue')
    
    label_room = tk.Label(booking_details_window, text=f"Room Number: {room_number}", font=('Arial', 18), bg='light blue')
    label_room.pack(pady=10)
    
    label_guest = tk.Label(booking_details_window, text=f"Guest Name: {guest_name}", font=('Arial', 18), bg='light blue')
    label_guest.pack(pady=10)
    
    label_checkin = tk.Label(booking_details_window, text=f"Check-in Date: {checkin_date}", font=('Arial', 18), bg='light blue')
    label_checkin.pack(pady=10)
    
    label_checkout = tk.Label(booking_details_window, text=f"Check-out Date: {checkout_date}", font=('Arial', 18), bg='light blue')
    label_checkout.pack(pady=10)

# Create main application window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("800x600")
root.configure(bg='green')

# Labels and Entry for Room Number
label_room = tk.Label(root, text="Room Number:", font=('Arial', 18), fg='blue', bg='orange')
label_room.grid(row=0, column=0, padx=10, pady=10)
entry_room = tk.Entry(root, font=('Arial', 18))
entry_room.grid(row=0, column=1, padx=10, pady=10)

# Labels and Entry for Guest Name
label_name = tk.Label(root, text="Guest Name:", font=('Arial', 18), fg='blue', bg='orange')
label_name.grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root, font=('Arial', 18))
entry_name.grid(row=1, column=1, padx=10, pady=10)

# Labels and Entry for Check-in Date
label_checkin = tk.Label(root, text="Check-in Date:", font=('Arial', 18), fg='blue', bg='orange')
label_checkin.grid(row=2, column=0, padx=10, pady=10)
entry_checkin = tk.Entry(root, font=('Arial', 18))
entry_checkin.grid(row=2, column=1, padx=10, pady=10)

# Labels and Entry for Check-out Date
label_checkout = tk.Label(root, text="Check-out Date:", font=('Arial', 18), fg='blue', bg='orange')
label_checkout.grid(row=3, column=0, padx=10, pady=10)
entry_checkout = tk.Entry(root, font=('Arial', 18))
entry_checkout.grid(row=3, column=1, padx=10, pady=10)

# Button for Booking Room
btn_book = tk.Button(root, text="Book Room", font=('Arial', 18), fg='blue', bg='orange', command=bookRoom)
btn_book.grid(row=4, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
