# def display_current_datetime ():
from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculates and displays a future date based on user input."""
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    """Main function to execute the script."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
