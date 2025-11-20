number_of_runners=int(input('Enter the Total runners: '))
scores=list(map(int,(input('Enter The Runners Details:').split())))

unique_runners=list(set(scores))
unique_runners.sort(reverse=True)

print(unique_runners[1])
