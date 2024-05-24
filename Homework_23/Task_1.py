import json
import os


def calculate_avg_salary(data):
    avg_salaries = {}
    for dept, salaries in data.items():
        try:
            avg_salaries[dept] = sum(salaries) / len(salaries)
        except ZeroDivisionError:
            print(f"Warning: Department '{dept}' has no employees.")
            avg_salaries[dept] = 0
        except TypeError:
            print(f"Error: Invalid data format for department '{dept}'.")
            avg_salaries[dept] = None
    return avg_salaries


def main():
    input_file = "employee_salaries.json"
    output_file = "avg_salary.json"

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    # Read data from JSON file
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{input_file}'.")
        return

    # Calculate average salaries
    avg_salaries = calculate_avg_salary(data)

    # Print average salaries
    print("Average salaries for each department:")
    for dept, avg_salary in avg_salaries.items():
        print(f"{dept}: {avg_salary}")

    # Write average salaries to JSON file
    with open(output_file, 'w') as file:
        json.dump(avg_salaries, file, indent=4)

    print(f"Average salaries saved to '{output_file}'.")


if __name__ == "__main__":
    main()
