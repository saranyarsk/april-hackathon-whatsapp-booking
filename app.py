import datetime
import webbrowser
import stripe
import pymysql
 
# Services
services = {
    "Dog Grooming": ["Basic Grooming", "Premium Grooming", "Deluxe Grooming"],
    "Cat Grooming": ["Basic Grooming", "Premium Grooming", "Deluxe Grooming"],
    "Pet Spa": ["Relaxation Package", "Rejuvenation Package", "Deluxe Package"],
    "Pet Walking": ["30-minute Walk", "60-minute Walk", "Premium Walk"],
    "Pet Boarding": ["Standard Boarding", "Luxury Boarding", "Premium Boarding"]
}
 
# Slots for each service
slots = {
    "Basic Grooming": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "Premium Grooming": ["10:00 AM", "1:00 PM", "4:00 PM"],
    "Deluxe Grooming": ["8:00 AM", "12:00 PM", "3:00 PM"],
    "Relaxation Package": ["9:30 AM", "2:30 PM", "6:00 PM"],
    "Rejuvenation Package": ["10:00 AM", "3:00 PM", "7:00 PM"],
    "Deluxe Package": ["11:00 AM", "4:00 PM", "8:00 PM"],
    "30-minute Walk": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "60-minute Walk": ["10:00 AM", "1:00 PM", "4:00 PM"],
    "Premium Walk": ["11:00 AM", "3:00 PM", "6:00 PM"],
    "Standard Boarding": ["8:00 AM", "12:00 PM", "5:00 PM"],
    "Luxury Boarding": ["9:00 AM", "2:00 PM", "7:00 PM"],
    "Premium Boarding": ["10:00 AM", "4:00 PM", "8:00 PM"]
}
 
# Customers
customers = {
    "9487118768": {"name": "Sowmiya", "category": "Dog Owner", "pets": ["Buddy"]},
    "555-5678": {"name": "Sherin", "category": "Cat Owner", "pets": ["Whiskers"]},
    "555-9012": {"name": "Nebi", "category": "Dog and Cat Owner", "pets": ["Daisy", "Mittens"]},
    "555-3456": {"name": "Sarah Lee", "category": "Dog Owner", "pets": ["Rover"]},
    "555-7890": {"name": "Michael Brown", "category": "Cat Owner", "pets": ["Simba"]}
}
# try:
#     # Connect to the database
#     conn = pymysql.connect(
#         host="sql6.freesqldatabase.com",
#         user="sql6699776",
#         password="gzPizNrpya",
#         database="sql6699776",
#         port=3306,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("Connected to the database")
 
#     # Create a cursor object
#     cursor = conn.cursor()
 
#     # Define the query
#     query = "SELECT * FROM Customers"
 
#     # Execute the query
#     cursor.execute(query)
 
#     # Fetch all rows
#     customers = cursor.fetchall()
 
#     # Print the data
#     for customer in customers:
#         print(customer)
 
# except pymysql.Error as e:
#     print("Error connecting to the database:", e)
 
# finally:
#     # Close the cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if 'conn' in locals() and conn.open:
#         conn.close()
#         print("Connection closed")
 
 
def get_service_price(service, slot_type):
    if slot_type == "Basic Grooming":
        return 20
    elif slot_type == "Premium":
        return 50
    elif slot_type == "Deluxe":
        return 80
    else:
        return 0
 
def get_price_with_discount(service, slot_type, date):
    price = get_service_price(service, slot_type)
    if date.weekday() == 5:  # Saturday
        return price * 0.9  # 10% discount
    elif date.weekday() == 0:  # Monday
        return price * 1.2  # 20% premium
    else:
        return price
 
def handle_customer_interaction(phone_number):
    customer = customers[phone_number]
    print(f"Hello, {customer['name']}! Let's book a service for your pet(s).")
 
    # Display customer's pets
    print("Your pets:")
    for i, pet in enumerate(customer["pets"]):
        print(f"{i+1}. {pet}")
    pet_index = int(input("Please select your pet: ")) - 1
    pet = customer["pets"][pet_index]
 
    # Display service options
    print("Available services:")
    for service in services:
        print(f"- {service}")
    service = input("Please select a service: ")
 
    # Display available slots for the selected service
    print(f"Available slots for {service}:")
    for i, slot in enumerate(slots[services[service][0]]):
        print(f"{i+1}. {slot}")
    slot_index = int(input("Please select a slot: ")) - 1
    slot_type = services[service][0]
    slot_time = slots[slot_type][slot_index]
 
    # Calculate the price and send the message
    date_str = input("Please enter the date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    print(service, slot_type,"gggg")
    price = get_price_with_discount(service, slot_type, date)
    message = f"Hello, {customer['name']}!\nI have booked a {service} - {slot_type} for your pet {pet} on {date.strftime('%B %d, %Y')} at {slot_time}.\nThe total price is ${price:.2f}.\nPlease confirm the booking."
    print("Please open WhatsApp Web and send the following message:")
    print(message)
    stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    session = stripe.checkout.Session.create(  payment_method_types=['card'],  line_items=[{'price': 'price_1HKiSf2eZvKYlo2CxjF9qwbr','quantity': 1,}],  mode='subscription',  success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',  cancel_url='https://example.com/cancel',)
    webbrowser.open("https://saranyarsk.github.io/april-hackathon-whatsapp-booking/payment.html")
 
# Example usage
handle_customer_interaction("9487118768")