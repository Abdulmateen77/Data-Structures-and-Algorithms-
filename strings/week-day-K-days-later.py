def solution(S, K):
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    current_day_index = days_of_week.index(S)
    new_day_index = (current_day_index + K) % 7
    return days_of_week[new_day_index]

# Example usage:
result1 = solution("Wed", 2)
result2 = solution("Sat", 23)

print(result1)  # Output: "Fri"
print(result2)  # Output: "Mon"
