"""
Enhanced Grade Calculator

This module contains functions to get a student's score and determine their grade.
It demonstrates function decomposition and modular design.
"""

def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates the input, and returns a numerical score.
    Returns:
        float: The valid numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score using standard grading scale.
    Args:
        score (float): The numerical score of the student.
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def main():
    """
    Main function to get user score, calculate grade, and display the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()

    