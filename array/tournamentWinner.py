def tournamentWinner(competitions, results):
    # Write your code here.
    points = dict()
    i = 0
    while i < len(results):
        match_win = results[i]
        match_participant = competitions[i]  # [homeTeam, awayTeam]

        if match_win == 1:  # homeTeam wins
            if match_participant[0] in points:
                points[match_participant[0]] += 3
            else:
                points[match_participant[0]] = 3
        else:  # awayTeam wins
            if match_participant[1] in points:
                points[match_participant[1]] += 3
            else:
                points[match_participant[1]] = 3

        i += 1

    return max(points, key=points.get)


competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]
results = [0, 1, 1]

print(tournamentWinner(competitions, results))
