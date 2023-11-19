def solution(S, K):
    # List representing the days of the week
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Find the index of the given day in the list
    current_day_index = days_of_week.index(S)

    # Calculate the index of the new day after adding K days, using modulo to handle wrap-around
    new_day_index = (current_day_index + K) % 7

    # Return the day of the week corresponding to the new index
    return days_of_week[new_day_index]

# Example usage:
result1 = solution("Wed", 2)
result2 = solution("Sat", 23)

# Displaying the results
print(result1)  # Output: "Fri"
print(result2)  # Output: "Mon"
