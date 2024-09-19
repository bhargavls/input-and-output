''''
def get_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    elif mark >= 40:
        return 'E'
    else:
        return 'F'

def main():
    try:
        # Input from user
        mark = float(input("Enter the mark (0-100): "))
        
        # Validate input
        if mark < 0 or mark > 100:
            print("Please enter a mark between 0 and 100.")
            return
        
        # Get the grade
        grade = get_grade(mark)
        
        # Display the grade
        print(f"The corresponding grade for the mark {mark} is: {grade}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()

