import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == 'Addition (+)':
        return num1 + num2
    elif operation == 'Subtraction (-)':
        return num1 - num2
    elif operation == 'Multiplication (*)':
        return num1 * num2
    elif operation == 'Division (/)':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Streamlit UI
def main():
    st.title("Simple Calculator App")
    
    st.write("Select the operation and enter two numbers to calculate the result.")
    
    # Dropdown menu for selecting an operation
    operation = st.selectbox(
        "Choose an operation", 
        ['Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)']
    )
    
    # Inputs for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)
    
    # Button to perform the calculation
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        st.success(f"The result of {operation} is: {result}")
        
    st.write("This app was built using Streamlit.")

# Run the app
if __name__ == "__main__":
    main()
