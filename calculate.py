''''
def calculate_fee(student_type, tuition_fee):
    if student_type == 'MSDS':  # Merit Seat Day Scholar
        return tuition_fee + bus_fee
    elif student_type == 'MSH':  # Merit Seat Hosteller
        return tuition_fee + hostel_fee
    elif student_type == 'MGSDS':  # Management Seat Day Scholar
        return 1.5 * tuition_fee + bus_fee
    elif student_type == 'MGSH':  # Management Seat Hosteller
        return 1.5 * tuition_fee + hostel_fee
    else:
        return None  # Invalid student type

# Constants for fees
tuition_fee = float(input("Enter the tuition fee amount: "))
bus_fee = 5000  # Example bus fee
hostel_fee = 10000  # Example hostel fee

def main():
    student_type = input("Enter the student type (MSDS, MSH, MGSDS, MGSH): ").strip().upper()

    # Calculate the fee based on student type
    fee = calculate_fee(student_type, tuition_fee)

    # Display the result
    if fee is not None:
        print(f"The total fee to be collected for {student_type} is: {fee:.2f}")
    else:
        print("Invalid student type entered.")

if __name__ == "__main__":
    main()
