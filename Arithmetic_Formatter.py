def arithmetic_arranger(problems, show_answers=False):

    # Check if the problems are within limit
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_numbers = []
    second_numbers = []
    separators = []
    results = []

    for problem in problems:
        parts = problem.split()
        first_num = parts[0]
        operator = parts[1]
        second_num = parts[2]
        
        # Check if operator is valid
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        # Check if numbers are digits
        if not first_num.isdigit() or not second_num.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if numbers are no more than four digits
        if len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the maximum length of each line (for formatting purposes)
        max_len = max(len(first_num),len(second_num)) +2
       # +2 for operator and space

        # Store formatted elements
        first_numbers.append(first_num.rjust(max_len))
        second_numbers.append(operator + " " + second_num.rjust(max_len - 2))
        
        # Separator line
        separators.append("-" * max_len)

        # Calculate the result if show_answers is True
        if show_answers:
            if operator == "+":
                results.append(str(int(first_num) + int(second_num)).rjust(max_len))
            else:
                results.append(str(int(first_num) - int(second_num)).rjust(max_len))

    # Join each line with four spaces separating the problems
   
    first_line = "    ".join(first_numbers)
    second_line = "    ".join(second_numbers)
    separator_line = "    ".join(separators)
    
    arrange_problems = f"{first_line}\n{second_line}\n{separator_line}"
   
    if show_answers:
        result_line = "    ".join(results)
        arrange_problems += f"\n{result_line}"

    return arrange_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
