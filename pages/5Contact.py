import streamlit as st
import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Your database host (for local, it's usually 'localhost')
            user="your_username",  # Your MySQL username
            password="your_password",  # Your MySQL password
            database="contact_form_db"  # Name of your database
        )
        return connection
    except Error as e:
        st.error(f"Error while connecting to MySQL: {e}")
        return None

# Function to insert form data into the database
def insert_contact_data(name, email, message):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
            values = (name, email, message)
            cursor.execute(query, values)
            connection.commit()
            st.success("Thank you for contacting us! Your message has been submitted.")
        except Error as e:
            st.error(f"Error while inserting data into database: {e}")
        finally:
            cursor.close()
            connection.close()

# Title
st.title(":mailbox: :blue[Get In Touch With Us!]")

# Create the form
with st.form(key='contact_form'):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message here")

    # Submit button
    submit_button = st.form_submit_button("Send")

    if submit_button:
        # Validate form fields
        if not name or not email or not message:
            st.error("Please fill in all fields before submitting.")
        else:
            # Insert data into the database
            insert_contact_data(name, email, message)
