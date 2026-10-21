# Travel Fare Calculator

## Description

This program calculates the total travel fare based on the distance traveled and the number of passengers. Each kilometer costs PHP 14.

## Version 1 - Original Code Without Input Validation

- **Input:** Passenger name, distance in kilometers, and number of passengers.
- **Process:** Multiplies the distance by the fare rate (PHP 14) and the number of passengers.
- **Output:** Displays the passenger's name and total fare in PHP.
- **Validation:** Does not include input validation.

## Version 2 - Updated Code With Input Validation

- **Input:** Passenger name, distance in kilometers, and number of passengers.
- **Process:** Multiplies the distance by the fare rate (PHP 14) and the number of passengers after validating the inputs.
- **Output:** Displays the passenger's name and total fare in PHP, rounded to two decimal places.
- **Validation:** Includes input validation to ensure that the passenger name is not empty, the distance is a number greater than zero, and the number of passengers is a positive whole number.

### Input Validation Rules

1. **Passenger Name:** Must not be empty. If the user enters an empty name or only spaces, the program displays an error message and asks the user to enter the name again.
2. **Distance:** Must be a numeric value greater than zero. If the user enters letters, an invalid number, zero, or a negative number, the program displays an error message and asks the user to re-enter the distance.
3. **Number of Passengers:** Must be a positive whole number. If the user enters letters, decimals, zero, or a negative number, the program displays an error message and asks the user to enter the number again.

### Explanation of the Added Code in Version 2

#### 1. Passenger Name Validation

The `.strip()` method removes leading and trailing spaces from the passenger name. The `while True` loop repeatedly asks the user to enter a name until a valid, non-empty name is provided. The `if name:` statement checks whether the name contains any characters after removing spaces. The `break` statement exits the loop when the input is valid.

#### 2. Distance Validation

The program uses `float()` to convert the distance input into a numeric value that can include decimals. A `try` and `except ValueError` structure handles inputs that cannot be converted into a number. The `if distance > 0:` condition ensures that the distance is greater than zero. If the input is invalid, the program displays an error message and asks the user to enter the distance again.

#### 3. Number of Passengers Validation

The `.isdigit()` string method checks whether the input contains only digit characters. If the input passes this check, `int()` converts it into a whole number. The program also checks that the number is greater than zero. If the input is invalid, the program displays an error message and asks the user to re-enter the number of passengers.

#### 4. Use of Loops and Selection Structures

The `while` loops allow the program to repeat an input request until valid data is entered. The `if` statements check whether the input meets the validation rules. The `break` statement stops the loop when the input is valid. These structures help prevent invalid data from being used in the fare calculation.

#### 5. Fare Calculation and Output

After all inputs pass validation, the program calculates the total fare using the following formula:

**Total Fare = Distance × Fare Rate × Number of Passengers**

The fare rate is PHP 14 per kilometer. The `round(total_fare, 2)` function rounds the calculated fare to two decimal places before displaying the result.

### Example Output

```text
Enter passenger name: Juan
Enter distance (km): 10
Enter number of passengers: 2

Passenger: Juan
Total Fare: PHP 280.0
```

### Example of Input Validation

```text
Enter passenger name:
Invalid name. Passenger name cannot be empty. Please try again.
Enter passenger name: Juan

Enter distance (km): abc
Invalid distance. Please enter a numeric value.
Enter distance (km): -5
Invalid distance. Enter a number greater than 0.
Enter distance (km): 10

Enter number of passengers: 2.5
Invalid number of passengers. Enter a positive whole number.
Enter number
