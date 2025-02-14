import csv
import sys


def main():  #<- how to use command-line args in python? 2 arguments

    # TODO: Check for command-line usage
    if len(sys.argv) != 3: # here what?
        print('shit')
        return

    # TODO: Read database file into a variable
    people = [] # list of dicts?
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            people.append(row)
    str_types = tuple(people[0].keys())

    # TODO: Read DNA sequence file into a variable
    #but i need to open multiple files?
    with open(sys.argv[2], mode='r', encoding='utf-8') as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # this function does not work correctly
    unknown_profile ={}
    for i in str_types[1:]:
        unknown_profile[i] = str(longest_match(dna, i))

    # TODO: Check database for matching profiles
    for i in people:
        next_person = False

        for j in str_types[1:]:
            if i[j] != unknown_profile[j]:
                next_person = True
                break

        if next_person == True:
            continue
        print(i['name'])
        return
    
    print('No match')
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
