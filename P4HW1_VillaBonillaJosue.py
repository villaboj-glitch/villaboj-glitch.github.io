# Josue VillaBonilla
# 16 APR 26
# P4HW1
# This program collects scores, validates input, drops the lowest score,
# calculates the average, and displays the letter grade.

# Pseudocode:
# Ask the user how many scores they want to enter
# Create an empty list to store valid scores
# Use a loop to collect each score
# If a score is less than 0 or greater than 100, keep asking again
# Add each valid score to the list
# Find the lowest score in the list
# Remove the lowest score from the list
# Calculate the average of the modified list
# Determine the letter grade based on the average
# Display the results

num_scores = int(input("How many scores do you want to enter? "))

score_list = []

for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    score_list.append(score)

lowest_score = min(score_list)
score_list.remove(lowest_score)

average_score = sum(score_list) / len(score_list)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("-------------------------------")