# Read the number of participants (not used directly)
n = int(input('Enter the number:'))

# Read the list of scores, split into integers
scores = list(map(int, input("Enter the numbers:").split()))
print(scores)
# # Remove duplicates by converting to a set, then back to list
# unique_scores = list(set(scores))

# # Sort the unique scores in descending order
# unique_scores.sort(reverse=True)

# # The runner-up is the second highest score
# print(unique_scores[1])
