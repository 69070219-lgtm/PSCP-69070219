"""SurprisingVote"""
total = float(input())
Max_score = float(input())
minmum = (total - Max_score) - Max_score
if minmum < 0:
    minmum = 0

if minmum + 2 < Max_score:
    print("Surprising")
else:
    print("Not surprising")
