# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = [] #
    # TODO: Read teams into memory from file
    f = open(sys.argv[1], 'r')
    reader = csv.DictReader(f, fieldnames=["team", "rating"])

    for row in reader:
        #how to referance rating to make int from string
        row[rating] = int(row[rating]) #this is incorrect, how to referance???  NameError: name 'rating' is not defined
        teams.append(row)

    counts = {"team":"counts"}
    # TODO: Simulate N tournaments and keep track of win counts
    # seems that we have to populate the dictionary with countries
    # we can use our teams dictionary?
    # need to create keys and values in counts
    counts = teams #but only the names
    # simulate_tournament(teams):

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    # simulate round
    # take only the winning teams
    # so basically in a loop until len(list) > 1
    # rewriting the list with redeclaring
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams


if __name__ == "__main__":
    main()
