import random
import time
import math

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

team1 = input("Player one: What is your team name? ")
print("")
team2 = input("Player two: What is your team name? ")
ahd = 0
while ahd < 40:
    print("")
    ahd += 1
RaheemSterling = [1.6, 2.5, 7.6, "Raheem Sterling(A)", 0]
MarcusRashford = [8.8, 1.2, 3.2, "Marcus Rashford(A)", 0]
HarryKane = [9.3, 2.5, 3.1, "Harry Kane(A)", 0]

JackGrealish = [6.2, 3.0, 5.2, 5.4, "Jack Grealish(M)", 0]
KalvinPhilips = [9.5, 9.0, 5.2, 8.0, "Kalvin Philips(M)", 0]
BukayoSaka = [7.2, 6.1, 4.5, 5.9, "Bukayo Saka(M)", 0]
JudeBellingham = [6.1, 2.0, 5.7, 5.6, "Jude Bellingham(M)", 0]
PhilFoden = [6.4, 2.3, 5.1, 5.8, "Phil Foden(M)", 0]

JohnStones = [7.1, 8.5, 4.6, "John Stones(D)", 0]
KyleWalker = [7.6, 9.4, 5.1, "Kyle Walker(D)", 0]
BenChilwell = [6.2, 3.8, 4.4, "Ben Chilwell(D)", 0]
TrentAlexander = [6.4, 3.2, 4.5, "Trent Alexander-Arnold(D)", 0]
TyroneMings = [4.6, 0.5, 4.3, "Tryone Mings(D)", 0]

JordanPickford = [7.0, 6.5, 2.1, "Jordan Pickford(G)", 0]
SamJohnstone = [5.0, 9.7, 2.0, "Sam Johnstone(G)", 0]

RaheemSterling2 = [1.6, 2.5, 7.6, "Raheem Sterling(A2)", 0]
MarcusRashford2 = [8.8, 1.2, 3.2, "Marcus Rashford(A2)", 0]
HarryKane2 = [9.3, 2.5, 3.1, "Harry Kane(A2)", 0]

JackGrealish2 = [6.2, 3.0, 5.2, 5.4, "Jack Grealish(M2)", 0]
KalvinPhilips2 = [9.5, 9.0, 5.2, 8.0, "Kalvin Philips(M2)", 0]
BukayoSaka2 = [7.2, 6.1, 4.5, 5.9, "Bukayo Saka(M2)", 0]
JudeBellingham2 = [6.1, 2.0, 5.7, 5.6, "Jude Bellingham(M2)", 0]
PhilFoden2 = [6.4, 2.3, 5.1, 5.8, "Phil Foden(M2)", 0]

JohnStones2 = [7.1, 8.5, 4.6, "John Stones(D2)", 0]
KyleWalker2 = [7.6, 9.4, 5.1, "Kyle Walker(D2)", 0]
BenChilwell2 = [6.2, 3.8, 4.4, "Ben Chilwell(D2)", 0]
TrentAlexander2 = [6.4, 3.2, 4.5, "Trent Alexander-Arnold(D2)", 0]
TyroneMings2 = [4.6, 0.5, 4.3, "Tryone Mings(D2)", 0]

JordanPickford2 = [7.0, 2.5, 2.1, "Jordan Pickford(G2)", 0]
SamJohnstone2 = [2.0, 9.7, 2.0, "Sam Johnstone(G2)", 0]

JordanPickford2 = [7.0, 2.5, 2.1, "Jordan Pickford(G2)", 0]
SamJohnstone2 = [2.0, 9.7, 2.0, "Sam Johnstone(G2)", 0]
print("Attackers" + "        | " "Goal Scoring" + " | " "Risk of being carded" + " | " + "Penalty Skill")
print("Harry Kane" + "       |     " + str(HarryKane[0]) + "      |        " + str(HarryKane[1]) + "           |    " + str(HarryKane[2]))
print("Marcus Rashford" + "  |     " + str(MarcusRashford[0]) + "      |        " + str(MarcusRashford[1]) + "           |    " + str(MarcusRashford[2]))
print("Raheem Sterling" + "  |     " + str(RaheemSterling[0]) + "      |        " + str(RaheemSterling[1]) + "           |    " + str(RaheemSterling[2]))

print("")

T1A1 = list(input("Who is your first forward " + team1 + "? "))
if T1A1[0] == "H" or T1A1[0] == "h":
    T1A1 = HarryKane
elif T1A1[0] == "M" or T1A1[0] == "m":
    T1A1 = MarcusRashford
elif T1A1[0] == "R" or T1A1[0] == "r":
    T1A1 = RaheemSterling
print("")
T1A2 = list(input("Who is your second forward " + team1 + "? "))
if T1A2[0] == "H" or T1A2[0] == "h":
    T1A2 = HarryKane
elif T1A2[0] == "M" or T1A2[0] == "m":
    T1A2 = MarcusRashford
elif T1A2[0] == "R" or T1A2[0] == "r":
    T1A2 = RaheemSterling
print("")
print("")
print("")

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Midfielders" + "      | " + " Goal Scoring " + " | " + "Risk of being carded" + " | " + "Penalty Skill" + " | " + "Defending Skill")
print("Jack Grealish" + "    |     " + str(JackGrealish[0]) + "        |        " + str(JackGrealish[1]) + "           |     " + str(JackGrealish[2]) + "       |     " + str(JackGrealish[3]))
print("Kalvin Philips" + "   |     " + str(KalvinPhilips[0]) + "        |        " + str(KalvinPhilips[1]) + "           |     " + str(KalvinPhilips[2]) + "       |     " + str(KalvinPhilips[3]))
print("Bukayo Saka" + "      |     " + str(BukayoSaka[0]) + "        |        " + str(BukayoSaka[1]) + "           |     " + str(BukayoSaka[2]) + "       |     " + str(BukayoSaka[3]))
print("Jude Bellingham" + "  |     " + str(JudeBellingham[0]) + "        |        " + str(JudeBellingham[1]) + "           |     " + str(JudeBellingham[2]) + "       |     " + str(JudeBellingham[3]))
print("Phil Foden" + "       |     " + str(PhilFoden[0]) + "        |        " + str(PhilFoden[1]) + "           |     " + str(PhilFoden[2]) + "       |     " + str(PhilFoden[3]))

print("")
print("")
print("")

T1M1 = list(input("Who is your first midfielder? " + team1 + " "))
if T1M1[2] == "c":
    T1M1 = JackGrealish
elif T1M1[2] == "l":
    T1M1 = KalvinPhilips
elif T1M1[2] == "k":
    T1M1 = BukayoSaka
elif T1M1[2] == "d":
    T1M1 = JudeBellingham
elif T1M1[2] == "i":
    T1M1 = PhilFoden

print("")
T1M2 = list(input("Who is your second midfielder? " + team1 + " "))
if T1M2[2] == "c":
    T1M2 = JackGrealish
elif T1M2[2] == "l":
    T1M2 = KalvinPhilips
elif T1M2[2] == "k":
    T1M2 = BukayoSaka
elif T1M2[2] == "d":
    T1M2 = JudeBellingham
elif T1M2[2] == "i":
    T1M2 = PhilFoden
print("")
T1M3 = list(input("Who is your third midfielder? " + team1 + " "))
if T1M3[2] == "c":
    T1M3 = JackGrealish
elif T1M3[2] == "l":
    T1M3 = KalvinPhilips
elif T1M3[2] == "k":
    T1M3 = BukayoSaka
elif T1M3[2] == "d":
    T1M3 = JudeBellingham
elif T1M3[2] == "i":
    T1M3 = PhilFoden
ahd = 0
while ahd < 40:
    print("")
    ahd += 1

possession1 = 0
shot1 = 0
shot2 = 0
target1 = 0
target2 = 0

print("Defenders" + "        |    " + "Defending Skill" + " | " + "Risk of being carded" + " | " + "Penalty Skill")
print("John Stones" + "      |       " + str(JohnStones[0]) + "          |         " + str(JohnStones[1]) + "          |     " + str(JohnStones[2]))
print("Kyle Walker" + "      |       " + str(KyleWalker[0]) + "          |         " + str(KyleWalker[1]) + "          |     " + str(KyleWalker[2]))
print("Ben Chilwell" + "     |       " + str(BenChilwell[0]) + "          |         " + str(BenChilwell[1]) + "          |     " + str(BenChilwell[2]))
print("Trent Alexander" + "  |       " + str(TrentAlexander[0]) + "          |         " + str(TrentAlexander[1]) + "          |     " + str(TrentAlexander[2]))
print("Tyrone Mings" + "     |       " + str(TyroneMings[0]) + "          |         " + str(TyroneMings[1]) + "          |     " + str(TyroneMings[2]))

print("")
T1D1 = list(input("Who is your first defender " + team1 + "? "))
if T1D1[2] == "h":
    T1D1 = JohnStones
elif T1D1[2] == "l":
    T1D1 = KyleWalker
elif T1D1[2] == "n":
    T1D1 = BenChilwell
elif T1D1[2] == "e":
    T1D1 = TrentAlexander
elif T1D1[2] == "r":
    T1D1 = TyroneMings
print("")
T1D2 = list(input("Who is your second defender " + team1 + "? "))
if T1D2[2] == "h":
    T1D2 = JohnStones
elif T1D2[2] == "l":
    T1D2 = KyleWalker
elif T1D2[2] == "n":
    T1D2 = BenChilwell
elif T1D2[2] == "e":
    T1D2 = TrentAlexander
elif T1D2[2] == "r":
    T1D2 = TyroneMings
print("")
T1D3 = list(input("Who is your third defender " + team1 + "? "))
if T1D3[2] == "h":
    T1D3 = JohnStones
elif T1D3[2] == "l":
    T1D3 = KyleWalker
elif T1D3[2] == "n":
    T1D3 = BenChilwell
elif T1D3[2] == "e":
    T1D3 = TrentAlexander
elif T1D3[2] == "r":
    T1D3 = TyroneMings

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Goalkeepers" + "      | " + " Regular saving " + " | " + "Penalties saving" " | " + " Risk of being carded")
print("Jordan Pickford" + "  |        " + str(JordanPickford[0]) + "       |       " + str(JordanPickford[1]) + "        |         " + str(JordanPickford[2]))
print("Sam Johnstone" + "    |        " + str(SamJohnstone[0]) + "       |       " + str(SamJohnstone[1]) + "        |         " + str(SamJohnstone[2]))
print("")
T1K = input("Who is your goalie " + team1 + "? ")
if T1K[0] == "j" or T1K[0] == "J":
    T1K = JordanPickford
elif T1K[0] == "s" or T1K[0] == "S":
    T1K = SamJohnstone

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Attackers" + "        | " "Goal Scoring" + " | " "Risk of being carded" + " | " + "Penalty Skill")
print("Harry Kane" + "       |     " + str(HarryKane[0]) + "      |        " + str(HarryKane[1]) + "           |    " + str(HarryKane[2]))
print("Marcus Rashford" + "  |     " + str(MarcusRashford[0]) + "      |        " + str(MarcusRashford[1]) + "           |    " + str(MarcusRashford[2]))
print("Raheem Sterling" + "  |     " + str(RaheemSterling[0]) + "      |        " + str(RaheemSterling[1]) + "           |    " + str(RaheemSterling[2]))

print("")

T2A1 = list(input("Who is your first forward " + team2 + "? "))
if T2A1[0] == "H" or T2A1[0] == "h":
    T2A1 = HarryKane2
elif T2A1[0] == "M" or T2A1[0] == "m":
    T2A1 = MarcusRashford2
elif T2A1[0] == "R" or T2A1[0] == "r":
    T2A1 = RaheemSterling2
print("")
T2A2 = list(input("Who is your second forward " + team2 + "? "))
if T2A2[0] == "H" or T2A2[0] == "h":
    T2A2 = HarryKane2
elif T2A2[0] == "M" or T2A2[0] == "m":
    T2A2 = MarcusRashford2
elif T2A2[0] == "R" or T2A2[0] == "r":
    T2A2 = RaheemSterling2
ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Midfielders" + "      | " + " Goal Scoring " + " | " + "Risk of being carded" + " | " + "Penalty Skill" + " | " + "Defending Skill")
print("Jack Grealish" + "    |     " + str(JackGrealish[0]) + "        |        " + str(JackGrealish[1]) + "           |     " + str(JackGrealish[2]) + "       |     " + str(JackGrealish[3]))
print("Kalvin Philips" + "   |     " + str(KalvinPhilips[0]) + "        |        " + str(KalvinPhilips[1]) + "           |     " + str(KalvinPhilips[2]) + "       |     " + str(KalvinPhilips[3]))
print("Bukayo Saka" + "      |     " + str(BukayoSaka[0]) + "        |        " + str(BukayoSaka[1]) + "           |     " + str(BukayoSaka[2]) + "       |     " + str(BukayoSaka[3]))
print("Jude Bellingham" + "  |     " + str(JudeBellingham[0]) + "        |        " + str(JudeBellingham[1]) + "           |     " + str(JudeBellingham[2]) + "       |     " + str(JudeBellingham[3]))
print("Phil Foden" + "       |     " + str(PhilFoden[0]) + "        |        " + str(PhilFoden[1]) + "           |     " + str(PhilFoden[2]) + "       |     " + str(PhilFoden[3]))
print("")
T2M1 = list(input("Who is your first midfielder? " + team2 + " "))
if T2M1[2] == "c":
    T2M1 = JackGrealish2
elif T2M1[2] == "l":
    T2M1 = KalvinPhilips2
elif T2M1[2] == "k":
    T2M1 = BukayoSaka2
elif T2M1[2] == "d":
    T2M1 = JudeBellingham2
elif T2M1[2] == "i":
    T2M1 = PhilFoden2
print("")
T2M2 = list(input("Who is your second midfielder? " + team2 + " "))
if T2M2[2] == "c":
    T2M2 = JackGrealish2
elif T2M2[2] == "l":
    T2M2 = KalvinPhilips2
elif T2M2[2] == "k":
    T2M2 = BukayoSaka2
elif T2M2[2] == "d":
    T2M2 = JudeBellingham2
elif T2M2[2] == "i":
    T2M2 = PhilFoden2
print("")
T2M3 = list(input("Who is your third midfielder? " + team2 + " "))
if T2M3[2] == "c":
    T2M3 = JackGrealish2
elif T2M3[2] == "l":
    T2M3 = KalvinPhilips2
elif T2M3[2] == "k":
    T2M3 = BukayoSaka2
elif T2M3[2] == "d":
    T2M3 = JudeBellingham2
elif T2M3[2] == "i":
    T2M3 = PhilFoden2

print("")
print("")
print("")

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Defenders" + "        |    " + "Defending Skill" + " | " + "Risk of being carded" + " | " + "Penalty Skill")
print("John Stones" + "      |       " + str(JohnStones[0]) + "          |         " + str(JohnStones[1]) + "          |     " + str(JohnStones[2]))
print("Kyle Walker" + "      |       " + str(KyleWalker[0]) + "          |         " + str(KyleWalker[1]) + "          |     " + str(KyleWalker[2]))
print("Ben Chilwell" + "     |       " + str(BenChilwell[0]) + "          |         " + str(BenChilwell[1]) + "          |     " + str(BenChilwell[2]))
print("Trent Alexander" + "  |       " + str(TrentAlexander[0]) + "          |         " + str(TrentAlexander[1]) + "          |     " + str(TrentAlexander[2]))
print("Tyrone Mings" + "     |       " + str(TyroneMings[0]) + "          |         " + str(TyroneMings[1]) + "          |     " + str(TyroneMings[2]))
print("")

T2D1 = list(input("Who is your first defender " + team2 + "? "))
if T2D1[2] == "h":
    T2D1 = JohnStones2
elif T2D1[2] == "l":
    T2D1 = KyleWalker2
elif T2D1[2] == "n":
    T2D1 = BenChilwell2
elif T2D1[2] == "e":
    T2D1 = TrentAlexander2
elif T2D1[2] == "r":
    T2D1 = TyroneMings2
print("")
T2D2 = list(input("Who is your second defender " + team2 + "? "))
if T2D2[2] == "h":
    T2D2 = JohnStones2
elif T2D2[2] == "l":
    T2D2 = KyleWalker2
elif T2D2[2] == "n":
    T2D2 = BenChilwell2
elif T2D2[2] == "e":
    T2D2 = TrentAlexander2
elif T2D2[2] == "r":
    T2D2 = TyroneMings2
print("")
T2D3 = list(input("Who is your third defender " + team2 + "? "))
if T2D3[2] == "h":
    T2D3 = JohnStones2
elif T2D3[2] == "l":
    T2D3 = KyleWalker2
elif T2D3[2] == "n":
    T2D3 = BenChilwell2
elif T2D3[2] == "e":
    T2D3 = TrentAlexander2
elif T2D3[2] == "r":
    T2D3 = TyroneMings2

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

print("Goalkeepers" + "      | " + " Regular saving " + " | " + "Penalties saving" " | " + " Risk of being carded")
print("Jordan Pickford" + "  |        " + str(JordanPickford[0]) + "       |       " + str(JordanPickford[1]) + "        |         " + str(JordanPickford[2]))
print("Sam Johnstone" + "    |        " + str(SamJohnstone[0]) + "       |       " + str(SamJohnstone[1]) + "        |         " + str(SamJohnstone[2]))
print("")
T2K = input("Who is your goalie " + team2 + "? ")
if T2K[0] == "j" or T2K[0] == "J":
    T2K = JordanPickford2
elif T2K[0] == "s" or T2K[0] == "S":
    T2K = SamJohnstone2

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

ahd = 0
while ahd < 40:
    print("")
    ahd += 1

team1attack = T1A1[0] + T1A2[0]
team1midfielda = T1M1[0] + T1M2[0] + T1M3[0]
team1midfieldd = T1M1[3] + T1M2[3] + T1M3[3]
team1defense = T1D1[0] + T1D2[0] + T1D3[0]

team2midfielda = T2M1[0] + T2M2[0] + T2M3[0]
team2midfieldd = T2M1[3] + T2M2[3] + T2M3[3]
team2defense = T2D1[0] + T2D2[0] + T2D3[0]
team2attack = T2A1[0] + T2A2[0]

team1players = [T1A1, T1A2, T1M1, T1M2, T1M3, T1D1, T1D2, T1D3]
team1playersa = [T1A1, T1A2]
team1playersm = [T1M1, T1M2, T1M3]
team1playersd = [T1D1, T1D2, T1D3]

team2players = [T2A1, T2A2, T2M1, T2M2, T2M3, T2D1, T2D2, T2D3]
team2playersa = [T2A1, T2A2]
team2playersm = [T2M1, T2M2, T2M3]
team2playersd = [T2D1, T2D2, T2D3]

dkd = 0
while dkd < 40:
    print("")
    dkd += 1

adlk = [-1, 1]
ball = random.choice(adlk)
startplacement = ball
us = 0

team1score = 0

team2score = 0

half = 46
full = 90

while us < full:
    if ball > 1:
        possession1 += 1
    if us != 0 and us != 45:
        time.sleep(5.5)
    print("")
    if us % 10 == 0 and us != 0:
        print(str(us) + "'")
        print("")
        time.sleep(0.5)
    if us == half + 2:
        ball = -startplacement
    us += 2
    if ball == 1:
        player = random.choice(team1playersa)
        player2 = random.choice(team1playersm)
        print(team1 + " start with the ball.")
        time.sleep(2)
        print("")
        x = random.randint(1, 2)
        if x == 1:
            print(player[3] + " starts off by passing to " + player2[4])
        if x == 2:
            print("The game commences with " + player[3] + " passing to " + player2[4])
        ball = 2
    elif ball == 2:
        mk = 0
        entered = 0
        x = random.randint(1, 100)
        if x < 60 * (player[0]) / (team2midfieldd):
            ball = -2
            entered = 1
            x = random.randint(1, 4)
            player = random.choice(team2playersm)
            if x == 1:
                print(player[4] + " steals the ball from " + player2[4])
            if x == 2:
                print("A bad pass from " + player2[4] + " leads to " + player[4] + " getting the ball for " + team2)
            if x == 3:
                print(player[4] + " cuts out " + player2[4] + "'s pass")
            if x == 4:
                print("A poor piece of play by " + player2[4] + " leads to an interception by " + player[4])
        else:
            for player in team2playersm:
                x = random.randint(1, 100)
                if x < (player[0] * 1.5) and entered == 0:
                    entered = 1
                    ha = random.randint(1, 20)
                    ball = -7
                    if ha == 1 and player[5] != 1:
                        player[5] += 2
                        ak = random.randint(1, 2)
                        if ak == 1:
                            print(player[4] + " slides into " + player2[4] + " out of nowhere, entirely missing the ball, and is given a RED CARD!")
                        if ak == 2:
                            print("A simply horrible challenge by " + player[4] + " on " + player2[4] + " gets him sent off")
                        team2playersm.remove(player)
                        team2midfieldd -= player[3]
                        team2midfielda -= player[0]
                    elif ha < 5:
                        player[5] += 1
                        if player[5] == 1:
                            ei = random.randint(1, 3)
                            if ei == 1:
                                print("A bad challenge by " + player[4] + " leads to a yellow card.")
                            if ei == 2:
                                print("The ref gives a yellow card to " + player[4] + " after they catch more of " + player2[4] + " than the ball.")
                            if ei == 3:
                                print("A sliding tackle by " + player[4] + " into the leg of " + player2[4] + " gives him a yellow card.")
                        if player[5] == 2:
                            ei = random.randint(1, 2)
                            if ei == 1:
                                print("A HORRIBLE CHALLENGE BY " + player[4] + "! He slides into the leg of " + player2[4] + " getting a second yellow card. He is sent off!")
                                team2playersm.remove(a)
                                team2midfieldd -= player[3]
                                team2midfielda -= player[0]
                    else:
                        aj = random.randint(1, 6)
                        if aj == 1:
                            print(player[4] + " fouls " + player2[4] + ". " + team1 + " gets a freekick from the middle, but no card is given.")
                        if aj == 2:
                            print("Freekick from the middle after a foul by " + player[4] + ".")
                        if aj == 3:
                            print("Challenge is poorly timed by " + player[4] + " and " + team1 + " gets a freekick")
                        if aj == 4:
                            print(player[4] + " caught more of the man than the ball and gives away a freekick")
                        if aj == 5:
                            print("Despite protests from many players on the team, the ref gives a freekick away after a challenge by " + player[4] + ".")
                        if aj == 6:
                            print(player[4] + "'s foot bounces off the ball onto the leg of " + player2[4] + ", showing studs and giving away a freekick.")
        if entered == 0:
            z = random.randint(1, 100)
            if z < 15:
                ball = 4
                x = random.randint(1, 4)
                player = random.choice(team1playersa)
                if x == 1:
                    print("A beautiful ball by " + player2[4] + " arrives right at the feet of " + player[3] + " in the box.")
                if x == 2:
                    print(player2[4] + " sees an opportunity and seizes it, passing the ball into the box at the feet of " + player[3] + ".")
                if x == 3:
                    print(player2[4] + " sails the ball over the heads of the midfield of " + team2 + " right to the feet of " + player[3] + ".")
                if x == 4:
                    print("What a spectacular through ball by " + player2[4] + " to give a ball right at the feet of " + player[3] + " in the box!")
            elif z < 70:
                ball = 3
                x = random.randint(1, 4)
                player = random.choice(team1playersa)
                if x == 1:
                    print(player2[4] + " plays a dangerous through ball to " + player[3] + " at the edge of the box.")
                if x == 2:
                    print(player[3] + " recieves a smart ball from " + player2[4] + " and is in open space near the box.")
                if x == 3:
                    print(player2[4] + " advances with the ball and plays it off to " + player[3] + " who is in a dangerous position.")
                if x == 4:
                    print(player2[4] + " plays a quick pass to " + player[3] + " who uses it well and starts advancing near the box.")
            else:
                ball = 2
                player = random.choice(team1playersm)
                while player == player2:
                    player = random.choice(team1playersm)
                fh = random.randint(1, 3)
                if fh == 1:
                    print(team1 + " are currently content to keep posession, and " + player2[4] + " passes it laterally to " + player[4])
                if fh == 2:
                    print(player2[4] + " passes the ball to " + player[4] + ".")
                if fh == 3:
                    print("The ball remains in the middle, as " + player2[4] + " gives the ball to " + player[4] + ".")
        player2 = player
    elif ball == 3:
        entered = 0
        for x in team2playersd:
            ks = random.randint(1, 100)
            if ks < 5 * (x[1]) and entered == 0:
                entered = 1
                ball = 6
                b = random.randint(1, 3)
                if b == 1:
                    print(x[3] + " tries to stop the threat with a challenge, but gives away a freekick.")
                if b == 2:
                    print(player2[3] + " goes down, and gets a freekick")
                if b == 3:
                    print(x[3] + " gets more of " + player2[3] + "'s leg than the ball and gives away a freekick.")
                b = random.randint(1, 3)
                if b == 1:
                    time.sleep(3)
                    print("")
                    x[4] += 1
                    if x[4] == 2:
                        print("The ref gives a second yellow card to " + x[3] + ", and he is sent off.")
                        team2playersm.remove(a)
                        team2midfieldd -= x[3]
                        team2midfielda -= x[0]
                    else:
                        y = random.randint(1, 3)
                        if y == 1:
                            print("The ref gives a yellow card to " + x[3])
                        if y == 2:
                            print(x[3] + " gets a yellow card for this challenge.")
                        if y == 3:
                            print("On top of the freekick given away, " + x[3] + " gets a yellow card.")
                pass
        if entered == 0:
            x = random.randint(1, 100)
            if x < 14 * (team2defense) / (player2[0]):
                ball = -9
                en = random.randint(1, 4)
                player = random.choice(team2playersd)
                if en == 1:
                    print(player2[3] + " gets the ball stripped off him by " + player[3] + ".")
                if en == 2:
                    print(player2[3] + " pulls his foot back for a shot, but " + player[3] + " steals the ball with an excellent sliding tackle.")
                if en == 3:
                    print(player2[3] + " dribbles around one player, but makes a mistake and " + player[3] + " gets the ball.")
                if en == 4:
                    print(player2[3] + " shoots, but it is blocked by the defense, and " + player[3] + " gets the rebound")
            elif x < 65:
                ball = 4
                player = random.choice(team1playersa)
                while player == player2:
                    player = random.choice(team1playersa)
                lkd = random.randint(1, 3)
                if lkd == 1:
                    print(player2[3] + " plays a through ball into the box straight to the feet of " + player[3] + ".")
                if lkd == 2:
                    print(player[3] + " recieves a brilliant ball from " + player2[3] + " in a dangerous position in the box")
                if lkd == 3:
                    print("Danger for " + team2 + " as a ball comes from " + player2[3] + " to " + player[3] + " in the box.")
            else:
                x = random.randint(1, 100)
                kda = random.randint(1, 3)
                if kda == 1:
                    print(player[3] + " takes a shot at goal.")
                if kda == 2:
                    print(player[3] + " puts his foot behind the ball and hits a powerful shot.")
                if kda == 3:
                    print(player[3] + " is the fortunate reciever of bad marking, and manages to get into space for a clear shot.")
                time.sleep(4)
                print("")
                shot1 += 1
                if x < 40 * (player[0] / T2K[0]):
                    ksj = random.randint(1, 4)
                    ball = 11
                    if ksj == 1:
                        print(player[3] + " sails the ball into the top right corner and scores!")
                    if ksj == 2:
                        print(player[3] + "'s shot takes a deflection, and goes past the goalkeeper into the bottom right corner!")
                    if ksj == 3:
                        print(player[3] + " hits a brilliant shot that curves into the top left corner past the goalkeeper's outstretched arms.")
                    if ksj == 4:
                        print(player[3] + "'s ball travels through the legs of defenders, making it difficult for the keeper to follow, and goes into the goal!")
                    target1 += 1
                else:
                    ksk = random.randint(1, 150)
                    if ksk < 8 * T2K[0]:
                        ball = -10
                        dkd = random.randint(1, 3)
                        if dkd == 1:
                            print(T2K[3] + "makes a great save and regains control of the ball.")
                        if dkd == 2:
                            print("A goal looked certain for a moment, but in the end, " + T2K[3] + " was able to barely grab the ball.")
                        if dkd == 3:
                            print("The save was fairly simple for " + T2K[3] + " as the shot failed to find the top corner of the goal.")
                        target1 += 1
                    else:
                        ball = 5
                        jfd = random.randint(1, 150)
                        if jfd < 10 * player[0]:
                            kds = random.randint(1, 3)
                            if kds == 1:
                                print(T2K[3] + " palms the ball wide, and it goes out for a corner.")
                            if kds == 2:
                                print(T2K[3] + " barely gets to the ball, but in the end, is able to nudge the ball out for a corner.")
                            if kds == 3:
                                print(T2K[3] + "'s fingertips just reach the ball, and it goes out for a corner.")
                            target1 += 1
                        else:
                            ball = -10
                            kd = random.randint(1, 3)
                            if kd == 1:
                                print(player[3] + "'s shot had some power behind it, but was unaccurate and went over the bar for a goalkick.")
                            if kd == 2:
                                print(player[3] + "'s shot barely goes wide, nearly bringing a brilliant goal.")
                            if kd == 3:
                                print(player[3] + "'s shot had just a bit too much curve, and went wide for a goalkick.")
        player2 = player
    elif ball == 4:
        entered = 0
        for a in team2playersd:
            x = random.randint(1, 25)
            if x < a[1] and entered == 0:
                entered = 1
                ball = 8
                h = random.randint(1, 3)
                if h == 1:
                    print(a[3] + " slides into " + player2[3] + "'s legs, completely missing the ball. PENALTY!")
                if h == 2:
                    print(a[3] + " tries and fails to get the ball from " + player2[3] + " but gets a lot of the player. The ref says PENALTY")
                if h == 3:
                    print(a[3] + " tries to pull " + player2[3] + " back, and in the end succeeds, but the ref gives a PENALTY for the poor challenge.")
                x = random.randint(1, 3)
                if x == 1:
                    print("")
                    a[4] += 1
                    if a[4] == 2:
                        print("The ref gives a second yellow card to " + a[3] + ", and he is sent off.")
                        team2playersm.remove(a)
                        team2midfieldd -= a[3]
                        team2midfielda -= a[0]
                    else:
                        time.sleep(3)
                        print("")
                        y = random.randint(1, 3)
                        if y == 1:
                            print("The ref gives a yellow card to " + a[3])
                        if y == 2:
                            print(a[3] + " gets a yellow card for this challenge.")
                        if y == 3:
                            print("On top of the penalty given away, " + a[3] + " gets a yellow card.")
                player2 = player
        x = random.randint(1, 100)
        if entered == 0:
            shot1 += 1
            if x < 40 * (player2[0] / T2K[0]):
                target1 += 1
                ball = 11
                h = random.randint(1, 3)
                if h == 1:
                    print(T2K[3] + " rushes out to tackle " + player2[3] + " but he slides the ball through the goalkeepers legs. GOAL!")
                elif h == 2:
                    print(player2[3] + " weaves round defenders and shoots the ball into the corner of the goal.")
                elif h == 3:
                    print("Poor defending leaves " + player2[3] + " in empty space, and he seizes the opportunity, putting the ball in the bottom left corner of the goal.")
            elif x < 70 * (player2[0] / T2K[0]):
                target1 += 1
                ball = 5
                kds = random.randint(1, 3)
                if kds == 1:
                    print(T2K[3] + " palms the ball wide, and it goes out for a corner.")
                if kds == 2:
                    print(T2K[3] + " barely gets to the ball, but in the end, is able to nudge the ball out for a corner.")
                if kds == 3:
                    print(T2K[3] + "'s fingertips just reach the ball, and it goes out for a corner.")
            else:
                ball = -10
                x = random.randint(1, 2)
                if x == 1:
                    kd = random.randint(1, 3)
                    if kd == 1:
                        print(player2[3] + "'s shot had some power behind it, but was unaccurate and went over the bar for a goalkick.")
                    if kd == 2:
                        print(player2[3] + "'s shot barely goes wide, nearly bringing a brilliant goal.")
                    if kd == 3:
                        print(player2[3] + "'s shot had just a bit too much curve, and went wide for a goalkick.")
                if x == 2:
                    target1 += 1
                    dkd = random.randint(1, 3)
                    if dkd == 1:
                        print(T2K[3] + "makes a great save and regains control of the ball.")
                    if dkd == 2:
                        print("A goal looked certain for a moment, but in the end, " + T2K[3] + " was able to barely grab the ball.")
                    if dkd == 3:
                        print("The save was fairly simple for " + T2K[3] + " as the shot failed to find the top corner of the goal.")
    elif ball == 5:
        y = random.randint(1, 2)
        if y == 1:
            player = random.choice(team1playersa)
            print(player[3] + " will take the corner.")
        if y == 2:
            player = random.choice(team1playersm)
            print(player[4] + " decides to take the corner.")
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        arrived = 0
        if x > player[0] * 9:
            ball = -10
            y = random.randint(1, 3)
            if y == 1:
                print("The ball goes straight towards " + T2K[3] + ".")
            if y == 2:
                print("The ball flies way long, and goes out for a goalkick.")
            if y == 3:
                print("No one is near the ball, leading it to go wide for a goalkick.")
        else:
            y = random.randint(1, 4)
            if y == 1:
                print("A promising ball flies into the box.")
            elif y == 2:
                print("The corner is good and curves towards the goal.")
            elif y == 3:
                print("The corner heads towards the middle of the box.")
            elif y == 4:
                print("It is well taken, and it curves into the middle of the box.")
            time.sleep(4)
            print("")
            x = random.randint(1, 100)
            if x < 4 * T2K[0]:
                y = random.randint(1, 3)
                ball = -10
                if y == 1:
                    print(T2K[3] + " comes out and grabs the ball.")
                elif y == 2:
                    print("The ball strays too close to the goal and " + T2K[3] + " is able to grab it.")
                elif y == 3:
                    print(T2K[3] + " takes a risk and comes out, but he is able to get the ball.")
            else:
                x = random.randint(1, 100)
                b = random.randint(1, 2)
                if b == 1:
                    player = random.choice(team1playersa)
                    k = 3
                else:
                    player = random.choice(team1playersm)
                    k = 4
                b = random.randint(1, 2)
                if b == 1:
                    player2 = random.choice(team2playersm)
                    n = 3
                    h = 4
                else:
                    player2 = random.choice(team2playersd)
                    n = 0
                    h = 3
                if x < 30 * (player2[n] / player[0]):
                    ball = -10
                    y = random.randint(1, 3)
                    if y == 1:
                        print(player2[h] + " is able to fend off " + player[k] + " and the ball goes out for a goalkick.")
                    elif y == 2:
                        print(player2[h] + " and " + player[k] + " compete for the ball, and in the end, neither of them get it, and it goes out for a goalkick")
                    elif y == 3:
                        print(player2[h] + " successfully defends " + player[k] + " and the ball flies long for a goalkick.")
                elif x < 50 * (player2[n] / player[0]):
                    ball = 5
                    y = random.randint(1, 3)
                    if y == 1:
                        print(player2[h] + " is able to prevent " + player[k] + " from getting the ball, and heads it out for another corner.")
                    elif y == 2:
                        print(player2[h] + " gets to the ball first, but can only head it back over the goal for another corner.")
                    elif y == 3:
                        print(player[k] + " looked dangerous for a second, but " + player2[h] + " heads the ball long for another corner.")
                else:
                    y = random.randint(1, 4)
                    shot1 += 1
                    target1 += 1
                    if y == 1:
                        print(player2[h] + " is not able to fend off " + player[k] + " who heads the ball at the goal.")
                    elif y == 2:
                        print(player[k] + " beats " + player2[h] + " and heads the ball towards the bottom corner.")
                    elif y == 3:
                        print(player[k] + " jumps high in the air and heads it towards the goal.")
                    else:
                        print(player[k] + " and " + player2[h] + " both jump for the ball, but in the end " + player[k] + " wins it and heads it towards the goal.")
                    print("")
                    time.sleep(5)
                    x = random.randint(1, 100)
                    if x < 7 * T2K[0]:
                        ball = -10
                        y = random.randint(1, 3)
                        if y == 1:
                            print(T2K[3] + " makes a brilliant save, and is able to hold onto the ball.")
                        elif y == 2:
                            print(T2K[3] + " leaps and is just able to grab the ball with his outstretched arms.")
                        elif y == 3:
                            print(T2K[3] + " reacts quickly and is able to hug the ball to his chest.")
                    else:
                        ball = 11
                        y = random.randint(1, 3)
                        if y == 1:
                            print(T2K[3] + " lungs for the ball, but he is too slow and it goes into the back of the net.")
                        elif y == 2:
                            print(T2K[3] + " dives towards the ball, but is too slow, and the ball flies into the back of net.")
                        elif y == 3:
                            print("The shot is accurate, and " + T2K[3] + " barely misses the chance to push it wide with his fingertips.")
    elif ball == 6:
        x = str(input("Who do you want to take the freekick? "))
        print("")
        playerchosen = 0
        for a in team1playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                print(a[3] + " will take the freekick.")
        for a in team1playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                print(a[4] + " will take the freekick.")
        print("")
        time.sleep(3)
        while playerchosen == 0:
            print("")
            print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
            time.sleep(1)
            x = str(input("Who do you want to take the freekick? "))
            print("")
            playerchosen = 0
            time.sleep(2)
            for a in team1playersa:
                if x == a[3]:
                    player = a
                    playerchosen = 1
                    print(a[3] + " will take the freekick.")
                    time.sleep(3)
                    print("")
            for a in team1playersm:
                if x == a[4]:
                    player = a
                    playerchosen = 1
                    print(a[4] + " will take the freekick.")
                    time.sleep(3)
                    print("")
        shot1 += 1
        x = random.randint(1, 100)
        if x > 9 * player[0]:
            b = random.randint(1, 3)
            if b == 1:
                print("The kick is poor and the ball sails over the goal.")
            elif b == 2:
                print("The freekick had some power to it, but the aim was off, and the ball is sent into the stands.")
            elif b == 3:
                print("The ball has some curl on it, but not enough, and goes past the goal for a goalkick.")
            ball = -10
        else:
            target1 += 1
            x = random.randint(1, 100)
            if x < 6 * T2K[1]:
                ball = -10
                b = random.randint(1, 3)
                if b == 1:
                    print("It was a decent shot, but a comfortable save for " + T2K[3] + " nonetheless.")
                if b == 2:
                    print("The ball curls towards the top left corner, but a fantastic save by " + T2K[3] + " ends up with the ball in his hands.")
                if b == 3:
                    print("The ball has some power on it, but " + T2K[3] + " is able to grab the ball.")
            elif x < 8 * T2K[0]:
                b = random.randint(1, 2)
                ball = 5
                if b == 1:
                    print("The ball has spin and power, but " + T2K[3] + " is able to knock it wide for a corner.")
                if b == 2:
                    print("The ball curves towards the top corner, but " + T2K[3] + " just gets a hand to it and knocks it wide for a corner.")
            else:
                ball = 11
                b = random.randint(1, 3)
                if b == 1:
                    print("GOAL! The ball flies into the corner, and there was nothing " + T2K[3] + " could do to stop it.")
                if b == 2:
                    print("He really got his foot behind it. The ball flies past " + T2K[3] + "'s fingertips into the goal.")
                if b == 3:
                    print("An unfortunate deflection for " + team2 + " ends up with the ball in the back of the net.")
        player2 = player
    elif ball == 7:
        player2 = random.choice(team1playersm)
        x = random.randint(1, 4)
        if x == 1:
            print(player2[4] + " takes the freekick from the middle quickly.")
        elif x == 2:
            print(team1 + " decide to move with speed, and " + player2[4] + " is quick to take the freekick.")
        elif x == 3:
            print("The freekick has little menace, but " + team1 + " are happy for the possession. " + player2[4] + " will take the freekick.")
        elif x == 4:
            print("The freekick is much to far away for a shot, and will be taken as a pass. It will be taken by " + player2[4])
        time.sleep(3.4)
        print("")
        x = random.randint(1, 100)
        if x < 30 / player[0]:
            ball = -2
            b = random.randint(1, 2)
            x = random.randint(1, 100)
            if x < 100 * (T2M1[0] / team2midfieldd):
                player = T2M1
            elif x < 100 * ((T2M1[0] + T2M2[0]) / team2midfieldd):
                player = T2M2
            else:
                player = T2M3
            if b == 1:
                print("The pass by " + player2[4] + " is horrible and is intercepted by " + player[4] + ".")
            if b == 2:
                print(player2[4] + "'s pass was weak and unnacurate, and it was intercepted by " + player[4] + ".")
        else:
            x = random.randint(1, 100)
            if x < 15:
                x = random.randint(1, 100)
                if x < 6 * player2[0]:
                    x = random.randint(1, 100)
                    if x < 100 * (T2M1[0] / team2midfieldd):
                        player = T2M1
                    elif x < 100 * ((T2M1[0] + T2M2[0]) / team2midfieldd):
                        player = T2M2
                    else:
                        player = T2M3
                    ball = -2
                    b = random.randint(1, 2)
                    if b == 1:
                        print(player2[4] + " attempts a long pass to right outside the box, but it is intercepted by " + player[4] + ".")
                    if b == 2:
                        print(player2[4] + " sees an opportunity for a long pass to right outside the box, but " + player[4] + " cuts it out.")
                else:
                    x = random.randint(1, 100)
                    ball = 3
                    if x < 100 * (T1A1[0] / team1attack):
                        player = T1A1
                    elif x < 100 * ((T1A1[0] + T1A2[0]) / team1attack):
                        player = T1A2
                    else:
                        player = T1A2
                    while player2 == player:
                        x = random.randint(1, 100)
                        if x < 100 * (T1A1[0] / team1attack):
                            player = T1A1
                        elif x < 100 * ((T1A1[0] + T1A2[0]) / team1attack):
                            player = T1A2
                        else:
                            player = T1A3

                    b = random.randint(1, 2)
                    if b == 1:
                        print(player2[4] + " sees an opportunity, and curves a ball up to " + player[3] + " who is right outside the box.")
                    elif b == 2:
                        print(player2[4] + " passes it over the heads of the opponent midfielders straight to the feet of " + player[3] + " who is standing right outside the box.")
            else:
                player = random.choice(team1playersm)
                while player2 == player:
                    player = random.choice(team1playersm)
                x = random.randint(1, 3)
                ball = 2
                if x == 1:
                    print(player2[4] + " plays a simple ball to " + player[4] + ".")
                if x == 2:
                    print(player2[4] + " plays a short pass to " + player[4] + ".")
                elif x == 3:
                    print("The game resumes with " + player2[4] + " passing to " + player[4] + ".")
        player2 = player
    elif ball == 8:
        x = str(input("Who do you want to take the penalty? "))
        print("")
        playerchosen = 0
        for a in team1playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                n = 3
                time.sleep(3)
                print(a[3] + " will take the penalty.")
                print("")
        for a in team1playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                print(a[4] + " will take the penalty.")
                n = 4
                time.sleep(3)
                print("")
        shot1 += 1
        while playerchosen == 0:
            time.sleep(3)
            print("")
            print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
            time.sleep(1)
            x = str(input("Who do you want to take the penalty? "))
            print("")
            playerchosen = 0
            time.sleep(2)
            for a in team1playersa:
                if x == a[3]:
                    player = a
                    playerchosen = 1
                    n = 3
                    print(a[3] + " will take the penalty.")
                    print("")
            for a in team1playersm:
                if x == a[4]:
                    player = a
                    playerchosen = 1
                    n = 4
                    print(a[4] + " will take the penalty.")
                    print("")
        time.sleep(3)
        x = random.randint(1, 2)
        if x == 1:
            print(T2K[3] + " dives right.")
            dive = 1
        elif x == 2:
            print(T2K[3] + " dives left.")
            dive = 2
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 45:
            print(player[n] + " shoots left.")
            shoot = 2
        elif x > 55:
            print(player[n] + " shoots right.")
            shoot = 1
        else:
            print(player[n] + " goes down the middle.")
            shoot = 6
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 50 / a[2]:
            x = random.randint(1, 3)
            if x == 1:
                print("The ball richochets off the post!")
            if x == 2:
                print("The shot has little aim, and the ball is sent long.")
            if x == 3:
                print("He went for the perfect shot, but ended up completely missing the goal.")
            ball = -10
        if ball != 10:
            if shoot == dive:
                x = random.randint(1, 100)
                if x < (40 * a[2] / T2K[1]):
                    ball = 11
                    b = random.randint(1, 3)
                    if b == 1:
                        print(player[n] + " just sails the ball past the goalkeepers outstretched arms.")
                    if b == 2:
                        print(T2K[3] + "'s fingers are mere inches away from the ball, but it sails into the net.")
                    if b == 3:
                        print("The ball flies into the top corner, and the goalkeeper cannot save it.")
                    target1 += 1
                elif (60 * a[2] / T2K[1]):
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T2K[3] + " is able to just get his palms to it, and the ball rebounds back out into the attacking players.")
                    elif x == 2:
                        print(T2K[3] + " is near the ball, but isn't able to grab the ball, and it rebounds off back into the fray of players.")
                    elif x == 3:
                        print("The ball doesn't go wide enough to make past the keeper, but " + T2K[3] + " isn't able to grab it, and it bounces off his palms.")
                    target1 += 1
                    x = random.randint(1, 100)
                    time.sleep(3)
                    print("")
                    if x < 15 * (team1attack + team1midfielda + 7 * player[0]) / (team2defense):
                        x = random.randint(1, 100)
                        if x < (800 * player[0]) / (team1attack + team1midfielda + 7 * player[0]):
                            player = player
                            n = 3
                        elif x < (team1attack - player[0]) / (team1attack + team1midfielda + 7 * player[0]):
                            player2 = random.choice(team1playersa)
                            while player2 == player:
                                player2 = random.choice(team1playersa)
                            player = player2
                            n = 3
                        else:
                            player2 = random.choice(team1playersm)
                            while player2 == player:
                                player2 = random.choice(team1playersm)
                            player = player2
                            n = 4
                        x = random.randint(1, 100)
                        if x < 70 * player[0] / T2K[1]:
                            ball = 11
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + " gets the ball on the rebound, and is able to put it past " + T2K[3] + " for his team.")
                            if b == 2:
                                print(player[n] + " lunges to get ther rebound and kicks it in the net.")
                            target1 += 1
                            shot1 += 1
                        else:
                            ball = -10
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + "gets the rebound and shoots, but " + T2K[3] + " is able to barely get back and grab hold of the ball.")
                            if b == 2:
                                print(player[n] + " lunges and shoots on the rebound, but " + T2K[3] + " is just able to get back and grabs the ball.")
                            shot1 += 1
                            target1 += 1
                    else:
                        ball = -9
                        x = random.randint(1, 100)
                        if x < (100 * T2D1[0]) / (Team2Defense):
                            player = T2D1
                        elif x < (100 * T2D2[0]) / (Team2Defense):
                            player = T2D2
                        else:
                            player = T2D3
                        b = random.randint(1, 3)
                        if b == 1:
                            print(player[3] + " is able to get to the ball first.")
                        if b == 2:
                            print(player[3] + " reaches the ball and is in a position to clear it.")
                        if b == 3:
                            print(player[3] + " lunges for the ball and gains possession.")

                else:
                    ball = -10
                    b = random.randint(1, 4)
                    if b == 1:
                        print(T2K[3] + " is able to grab onto the ball, negating the threat.")
                    elif b == 2:
                        print(player[n] + " hangs his head in his hands, as " + T2K[3] + "blocks his shot.")
                    elif b == 3:
                        print("The shot is weak, and " + T2K[3] + " is able to grab it")
                    else:
                        print("The ball flies into the bottom corner, but somehow, " + T2K[3] + "is able to grab it.")
            elif shoot - dive == 1 or shoot - dive == -1:
                ball = 11
                b = random.randint(1, 5)
                if b == 1:
                    print("The ball sails into the bottom corner uncontested.")
                elif b == 2:
                    print("The shot was mediocre, but it goes in nonetheless.")
                elif b == 3:
                    print("All " + T2K[3] + " can do is watch as the ball rolls into the bottom corner.")
                elif b == 4:
                    print("The shot likely wouldn't have been blocked anyway, but the goalkeeper diving the wrong way soldifies the goal.")
                else:
                    print("The shot is perfect, flying into the top corner.")
                target1 += 1
            else:
                x = random.randint(1, 100)
                target1 += 1
                if x < (60 * a[2] / T2K[1]):
                    ball = 11
                    b = random.randint(1, 3)
                    if b == 1:
                        print(a[n] + " just sails the ball past the goalkeepers outstretched legs, with nothing he can do to stop it.")
                    if b == 2:
                        print(T2K[3] + "'s feet are mere inches away from the ball, but it sails into the net, as his forward momentum prevents him from blocking it.")
                    if b == 3:
                        print("The ball flies into the goal behind him, and the goalkeeper cannot save it.")
                elif (70 * a[2] / T2K[1]):
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T2K[3] + " is able to just get his feet to it, and the ball rebounds back out into the attacking players.")
                    elif x == 2:
                        print(T2K[3] + "'s feet are near the ball, and it rebounds off back into the fray of players.")
                    elif x == 3:
                        print("The ball doesn't go high enough to make it in, but " + T2K[3] + " isn't able to knock it far with his feat, and it bounces off into the fray of players.")
                    x = random.randint(1, 100)
                    print("")
                    time.sleep(3)
                    if x < 15 * (team1attack + team1midfielda + 7 * player[0]) / (team2defense):
                        x = random.randint(1, 100)
                        if x < (800 * player[0]) / (team1attack + team1midfielda + 7 * player[0]):
                            player = player
                            n = 3
                        elif x < (team1attack - player[0]) / (team1attack + team1midfielda + 7 * player[0]):
                            player2 = random.choice(team1playersa)
                            while player2 == player:
                                player2 = random.choice(team1playersa)
                            player = player2
                            n = 3
                        else:
                            player2 = random.choice(team1playersm)
                            while player2 == player:
                                player2 = random.choice(team1playersm)
                            player = player2
                            n = 4
                        x = random.randint(1, 100)
                        shot1 += 1
                        target1 += 1
                        if x < 70 * player[0] / T2K[1]:
                            ball = 11
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + " gets the ball on the rebound, and is able to put it past " + T2K[3] + " for his team.")
                            if b == 2:
                                print(player[n] + " lunges to get ther rebound and kicks it in the net.")
                        else:
                            ball = -10
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + "gets the rebound and shoots, but " + T2K[3] + " is able to barely get back and grab hold of the ball.")
                            if b == 2:
                                print(player[n] + " lunges and shoots on the rebound, but " + T2K[3] + " is just able to get back and grabs the ball.")
                    else:
                        ball = -9
                        x = randint(1, 100)
                        if x < (100 * T2D1[0]) / (Team2Defense):
                            player = T2D1
                        elif x < (100 * T2D2[0]) / (Team2Defense):
                            player = T2D2
                        else:
                            player = T2D3
                        b = random.randint(1, 3)
                        if b == 1:
                            print(player[3] + " is able to get to the ball first.")
                        if b == 2:
                            print(player[3] + " reaches the ball and is in a position to clear it.")
                        if b == 3:
                            print(player[3] + " lunges for the ball and gains possession.")

                else:
                    ball = -10
                    b = random.randint(1, 4)
                    if b == 1:
                        print(T2K[3] + " is able to grab onto the ball, negating the threat.")
                    elif b == 2:
                        print(player[n] + " hangs his head in his hands, as " + T2K[3] + "blocks his shot.")
                    elif b == 3:
                        print("The shot is weak, and " + T2K[3] + " is able to grab it")
                    else:
                        print("The ball flies into the bottom corner, but somehow, " + T2K[3] + "is able to grab it.")

        player2 = player
    elif ball == 9:
        x = random.randint(1, 100)
        if x < 8 * (team2midfieldd) / (player2[0]):
            ball = -2
            player = random.choice(team2playersm)
            b = random.randint(1, 3)
            if b == 1:
                print(player2[3] + " tried to pass to midfield but " + player[4] + " intercepts the pass.")
            elif b == 2:
                print(player[4] + " cuts out the pass towards midfield of " + player2[3] + ".")
            else:
                print(player2[3] + "'s pass is poor, and it gets cut out by " + player[4] + ".")
        else:
            player = random.choice(team1playersm)
            b = random.randint(1, 4)
            ball = 2
            if b == 1:
                print(player2[3] + " passes to " + player[4])
            elif b == 2:
                print(player2[3] + " passes into midfield, where " + player[4] + " waits.")
            elif b == 3:
                print(player2[3] + " hits the ball towards " + player[4])
            else:
                print(player2[3] + " surveys his options and decides to pass to " + player[4] + ".")
        player2 = player
    elif ball == 10:
        x = random.randint(1, 100)
        if x < (8 * team2attack / T1K[0]):
            b = random.randint(1, 3)
            ball = -3
            player = random.choice(team2playersa)
            if b == 1:
                print(T1K[3] + " completely messes up the pass to his back line and passes to " + player[3] + " right outside the box.")
            if b == 2:
                print(T1K[3] + " doesn't see " + player[3] + " who cuts out the pass.")
            if b == 3:
                print(player[3] + "sees the intended pass and is able to get to it quickly")
        elif x < 18 * (team2attack / T1K[0]):
            ball = -2
            player = random.choice(team2playersm)
            b = random.randint(1, 3)
            if b == 1:
                print(T1K[3] + " kicks it to the middle, and " + player[4] + " intercepts the pass.")
            elif b == 2:
                print("The pass to the middle by " + T1K[3] + " is cut out by " + player[4])
            elif b == 3:
                print(player[4] + " sees the pass to the middle by the keeper and cuts it out.")
        elif x < 40 * (team2attack / T1K[0]):
            ball = 9
            b = random.randint(1, 3)
            player = random.choice(team1playersd)
            if b == 1:
                print(T1K[3] + " passes to " + player[3])
            elif b == 2:
                print(player[3] + " receives the ball from " + T1K[3])
            elif b == 3:
                print(T1K[3] + " plays the ball short to " + player[3])
        else:
            ball = 2
            b = random.randint(1, 3)
            player = random.choice(team1playersm)
            if b == 1:
                print(T1K[3] + " lobs it into the middle to " + player[4])
            elif b == 2:
                print(player[4] + " receives a long pass from " + T1K[3])
            elif b == 3:
                print(T1K[3] + " kicks it to " + player[4])
        player2 = player



    elif ball == -1:
        player = random.choice(team2playersa)
        player2 = random.choice(team2playersm)
        x = random.randint(1, 2)
        print(team2 + " start with the ball.")
        time.sleep(2)
        print("")
        if x == 1:
            print(player[3] + " starts off by passing to " + player2[4])
        if x == 2:
            print("The game commences with " + player[3] + " passing to " + player2[4])
        ball = -2
        player = player2
    elif ball == -2:
        mk = 0
        entered = 0
        x = random.randint(1, 100)
        if x < 60 * player[0] / team1midfieldd:
            entered = 1
            ball = 2
            x = random.randint(1, 4)
            player = random.choice(team1playersm)
            if x == 1:
                print(player[4] + " steals the ball from " + player2[4])
            if x == 2:
                print("A bad pass from " + player2[4] + " leads to " + player[4] + " getting the ball for " + team1)
            if x == 3:
                print(player[4] + " cuts out " + player2[4] + "'s pass")
            if x == 4:
                print("A poor piece of play by " + player2[4] + " leads to an interception by " + player[4])
        else:
            for a in team1playersm:
                rk = random.randint(1, 100)
                if rk < (a[1] * 1.5) and entered == 0:
                    entered = 1
                    ball = 7
                    ha = random.randint(1, 20)
                    if ha == 1 and a[5] != 1:
                        a[5] += 2
                        ak = random.randint(1, 2)
                        if ak == 1:
                            print(a[4] + " slides into " + player2[4] + " out of nowhere, entirely missing the ball, and is given a RED CARD!")
                        if ak == 2:
                            print("A simply horrible challenge by " + a[4] + " on " + player2[4] + " gets him sent off with a red card.")
                        team1playersm.remove(a)
                        team1midfieldd -= a[3]
                        team1midfielda -= a[0]
                    elif ha < 5:
                        a[5] += 1
                        if a[5] == 1:
                            ei = random.randint(1, 3)
                            if ei == 1:
                                print("A bad challenge by " + a[4] + " leads to a yellow card.")
                            if ei == 2:
                                print("The ref gives a yellow card to " + a[4] + " after they catch more of " + player2[4] + " than the ball.")
                            if ei == 3:
                                print("A sliding tackle by " + a[4] + " into the leg of " + player2[4] + " gives him a yellow card.")
                        if a[5] == 2:
                            ei = random.randint(1, 2)
                            if ei == 1:
                                print("A HORRIBLE CHALLENGE BY " + a[4] + "! He slides into the leg of " + player2[4] + " getting a second yellow card. He is sent off!")
                                team1playersm.remove(a)
                                team1midfieldd -= a[3]
                                team1midfielda -= a[0]
                    else:
                        aj = random.randint(1, 6)
                        if aj == 1:
                            print(a[4] + " fouls " + player2[4] + ". " + team2 + " gets a freekick from the middle, but no card is given.")
                        if aj == 2:
                            print("Freekick from the middle after a foul by " + a[4] + ".")
                        if aj == 3:
                            print("Challenge is poorly timed by " + a[4] + " and " + team2 + " gets a freekick")
                        if aj == 4:
                            print(a[4] + " caught more of the man than the ball and gives away a freekick")
                        if aj == 5:
                            print("Despite protests from many players on the team, the ref gives a freekick away after a challenge by " + a[4] + ".")
                        if aj == 6:
                            print(a[4] + "'s foot bounces off the ball onto the leg of " + player2[4] + ", showing studs and giving away a freekick.")
        if entered == 0:
            z = random.randint(1, 100)
            if z < 15:
                ball = -4
                x = random.randint(1, 4)
                player = random.choice(team2playersa)
                if x == 1:
                    print("A beautiful ball by " + player2[4] + " arrives right at the feet of " + player[3] + " in the box.")
                if x == 2:
                    print(player2[4] + " sees an opportunity and seizes it, passing the ball into the box at the feet of " + player[3] + ".")
                if x == 3:
                    print(player2[4] + " sails the ball over the heads of the midfield of " + team1 + " right to the feet of " + player[3] + ".")
                if x == 4:
                    print("What a spectacular through ball by " + player2[4] + " to give a ball right at the feet of " + player[3] + " in the box!")
            elif z < 70:
                ball = -3
                x = random.randint(1, 4)
                player = random.choice(team2playersa)
                if x == 1:
                    print(player2[4] + " plays a dangerous through ball to " + player[3] + " at the edge of the box.")
                if x == 2:
                    print(player[3] + " recieves a smart ball from " + player2[4] + " and is in open space near the box.")
                if x == 3:
                    print(player2[4] + " advances with the ball and plays it off to " + player[3] + " who is in a dangerous position.")
                if x == 4:
                    print(player2[4] + " plays a quick pass to " + player[3] + " who uses it well and starts advancing near the box.")
            else:
                ball = -2
                player = random.choice(team2playersm)
                while player == player2:
                    player = random.choice(team2playersm)
                fh = random.randint(1, 3)
                if fh == 1:
                    print(team2 + " are currently content to keep posession, and " + player2[4] + " passes it laterally to " + player[4])
                if fh == 2:
                    print(player2[4] + " passes the ball to " + player[4] + ".")
                if fh == 3:
                    print("The ball remains in the middle, as " + player2[4] + " gives the ball to " + player[4] + ".")
        player2 = player
    elif ball == -3:
        entered = 0
        for x in team1playersd:
            ks = random.randint(1, 100)
            if ks < 5 * (x[1]) and entered == 0:
                entered = 1
                ball = -6
                b = random.randint(1, 3)
                if b == 1:
                    print(x[3] + " tries to stop the threat with a challenge, but gives away a freekick.")
                if b == 2:
                    print(player2[3] + " goes down and gets a freekick")
                if b == 3:
                    print(x[3] + " gets more of " + player2[3] + "'s leg than the ball and gives away a freekick.")
                b = random.randint(1, 3)
                if b == 1:
                    time.sleep(3)
                    print("")
                    x[4] += 1
                    if x[4] == 2:
                        print("The ref gives a second yellow card to " + x[3] + ", and he is sent off.")
                        team1playersm.remove(a)
                        team1midfieldd -= x[3]
                        team1midfielda -= x[0]
                    else:
                        y = random.randint(1, 3)
                        if y == 1:
                            print("The ref gives a yellow card to " + x[3])
                        if y == 2:
                            print(x[3] + " gets a yellow card for this challenge.")
                        if y == 3:
                            print("On top of the freekick given away, " + x[3] + " gets a yellow card.")
                pass
        if entered == 0:
            x = random.randint(1, 100)
            if x < 14 * (team1defense) / (player2[0]):
                ball = 9
                en = random.randint(1, 4)
                player = random.choice(team1playersd)
                if en == 1:
                    print(player2[3] + " gets the ball stripped off him by " + player[3] + ".")
                if en == 2:
                    print(player2[3] + " pulls his foot back for a shot, but " + player[3] + " steals the ball with an excellent sliding tackle.")
                if en == 3:
                    print(player2[3] + " dribbles around one player, but makes a mistake and " + player[3] + " gets the ball.")
                if en == 4:
                    print(player2[3] + " shoots, but it is blocked by the defense, and " + player[3] + " gets the rebound")
            elif x < 65:
                ball = -4
                player = random.choice(team2playersa)
                while player == player2:
                    player = random.choice(team2playersa)
                lkd = random.randint(1, 3)
                if lkd == 1:
                    print(player2[3] + " plays a through ball into the box straight to the feet of " + player[3] + ".")
                if lkd == 2:
                    print(player[3] + " recieves a brilliant ball from " + player2[3] + " in a dangerous position in the box")
                if lkd == 3:
                    print("Danger for " + team1 + " as a ball comes from " + player2[3] + " to " + player[3] + " in the box.")
            else:
                x = random.randint(1, 100)
                kda = random.randint(1, 3)
                shot2 += 1
                if kda == 1:
                    print(player[3] + " takes a shot at goal.")
                if kda == 2:
                    print(player[3] + " puts his foot behind the ball and hits a powerful shot.")
                if kda == 3:
                    print(player[3] + " is the fortunate reciever of bad marking, and manages to get into space for a clear shot.")
                time.sleep(4)
                print("")
                if x < 40 * (player[0] / T1K[0]):
                    target2 += 1
                    ksj = random.randint(1, 4)
                    ball = -11
                    if ksj == 1:
                        print(player[3] + " sails the ball into the top right corner and scores!")
                    if ksj == 2:
                        print(player[3] + "'s shot takes a deflection, and goes past the goalkeeper into the bottom right corner!")
                    if ksj == 3:
                        print(player[3] + " hits a brilliant shot that curves into the top left corner past the goalkeeper's outstretched arms.")
                    if ksj == 4:
                        print(player[3] + "'s ball travels through the legs of defenders, making it difficult for the keeper to follow, and goes into the goal!")
                else:
                    ksk = random.randint(1, 150)
                    if ksk < 8 * T1K[0]:
                        ball = 10
                        dkd = random.randint(1, 3)
                        if dkd == 1:
                            print(T1K[3] + "makes a great save and regains control of the ball.")
                        if dkd == 2:
                            print("A goal looked certain for a moment, but in the end, " + T1K[3] + " was able to barely grab the ball.")
                        if dkd == 3:
                            print("The save was fairly simple for " + T1K[3] + " as the shot failed to find the top corner of the goal.")
                        target2 += 1

                    else:
                        ball = -5
                        jfd = random.randint(1, 150)
                        if jfd < 10 * player[0]:
                            kds = random.randint(1, 3)
                            if kds == 1:
                                print(T1K[3] + " palms the ball wide, and it goes out for a corner.")
                            if kds == 2:
                                print(T1K[3] + " barely gets to the ball, but in the end, is able to nudge the ball out for a corner.")
                            if kds == 3:
                                print(T1K[3] + "'s fingertips just reach the ball, and it goes out for a corner.")
                            target2 += 1
                        else:
                            ball = 10
                            kd = random.randint(1, 3)
                            if kd == 1:
                                print(player[3] + "'s shot had some power behind it, but was unaccurate and went over the bar for a goalkick.")
                            if kd == 2:
                                print(player[3] + "'s shot barely goes wide, nearly bringing a brilliant goal.")
                            if kd == 3:
                                print(player[3] + "'s shot had just a bit too much curve, and went wide for a goalkick.")
        player2 = player
    elif ball == -4:
        entered = 0
        for a in team1playersd:
            x = random.randint(1, 25)
            if x < a[1]:
                entered = 1
                ball = -8
                h = random.randint(1, 3)
                if h == 1:
                    print(a[3] + " slides into " + player[3] + "'s legs, completely missing the ball. PENALTY!")
                if h == 2:
                    print(a[3] + " tries and fails to get the ball from " + player[3] + " but gets a lot of the player. The ref says PENALTY")
                if h == 3:
                    print(a[3] + " tries to pull " + player[3] + " back, and in the end succeeds, but the ref gives a PENALTY for the poor challenge.")
                x = random.randint(1, 3)
                if x == 1:
                    a[4] += 1
                    if a[4] == 2:
                        print("The ref gives a second yellow card to " + a[3] + ", and he is sent off.")
                        team1playersm.remove(a)
                        team1midfieldd -= a[3]
                        team1midfielda -= a[0]
                    else:
                        time.sleep(3)
                        print("")
                        y = random.randint(1, 3)
                        if y == 1:
                            print("The ref gives a yellow card to " + a[3])
                        if y == 2:
                            print(a[3] + " gets a yellow card for this challenge.")
                        if y == 3:
                            print("On top of the penalty given away, " + a[3] + " gets a yellow card.")
                pass
        x = random.randint(1, 100)
        if entered == 0:
            shot2 += 1
            if x < 40 * (player[0] / T1K[0]):
                ball = -11
                h = random.randint(1, 3)
                target2 += 1
                if x == 1:
                    print(T1K[3] + " rushes out to tackle " + player2[3] + " but he slides the ball through the goalkeepers legs. GOAL!")
                if x == 2:
                    print(player2[3] + " weaves round defenders and shoots the ball into the corner of the goal.")
                if x == 3:
                    print("Poor defending leaves " + player2[3] + " in empty space, and he seizes the opportunity, putting the ball in the bottom left corner of the goal.")
            elif x < 70 * (player[0] / T1K[0]):
                ball = -5
                kds = random.randint(1, 3)
                target2 += 1
                if kds == 1:
                    print(T1K[3] + " palms the ball wide, and it goes out for a corner.")
                if kds == 2:
                    print(T1K[3] + " barely gets to the ball, but in the end, is able to nudge the ball out for a corner.")
                if kds == 3:
                    print(T1K[3] + "'s fingertips just reach the ball, and it goes out for a corner.")
            else:
                ball = 10
                x = random.randint(1, 2)
                if x == 1:
                    kd = random.randint(1, 3)
                    if kd == 1:
                        print(player2[3] + "'s shot had some power behind it, but was unaccurate and went over the bar for a goalkick.")
                    if kd == 2:
                        print(player2[3] + "'s shot barely goes wide, nearly bringing a brilliant goal.")
                    if kd == 3:
                        print(player2[3] + "'s shot had just a bit too much curve, and went wide for a goalkick.")
                if x == 2:
                    dkd = random.randint(1, 3)
                    if dkd == 1:
                        print(T1K[3] + "makes a great save and regains control of the ball.")
                    if dkd == 2:
                        print("A goal looked certain for a moment, but in the end, " + T1K[3] + " was able to barely grab the ball.")
                    if dkd == 3:
                        print("The save was fairly simple for " + T1K[3] + " as the shot failed to find the top corner of the goal.")
        player2 = player
    elif ball == -5:
        y = random.randint(1, 2)
        if y == 1:
            player = random.choice(team2playersa)
            print(player[3] + " will take the corner.")
        if y == 2:
            player = random.choice(team2playersm)
            print(player[4] + " decides to take the corner.")
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        arrived = 0
        if x > player[0] * 9:
            ball = -10
            y = random.randint(1, 3)
            if y == 1:
                print("The ball goes straight towards " + T2K[3] + ".")
            if y == 2:
                print("The ball flies way long, and goes out for a goalkick.")
            if y == 3:
                print("No one is near the ball, leading it to go wide for a goalkick.")
        else:
            y = random.randint(1, 4)
            if y == 1:
                print("A promising ball flies into the box.")
            elif y == 2:
                print("The corner is good and curves towards the goal.")
            elif y == 3:
                print("The corner heads towards the middle of the box.")
            elif y == 4:
                print("It is well taken, and it curves into the middle of the box.")
            time.sleep(4)
            print("")
            x = random.randint(1, 100)
            if x < 4 * T1K[0]:
                y = random.randint(1, 3)
                ball = -10
                if y == 1:
                    print(T1K[3] + " comes out and grabs the ball.")
                elif y == 2:
                    print("The ball strays too close to the goal and " + T1K[3] + " is able to grab it.")
                elif y == 3:
                    print(T1K[3] + " takes a risk and comes out, but he is able to get the ball.")
            else:
                x = random.randint(1, 100)
                b = random.randint(1, 2)
                if b == 1:
                    player = random.choice(team2playersa)
                    k = 3
                else:
                    player = random.choice(team2playersm)
                    k = 4
                b = random.randint(1, 2)
                if b == 1:
                    player2 = random.choice(team1playersm)
                    n = 3
                    h = 4
                else:
                    player2 = random.choice(team1playersd)
                    n = 0
                    h = 3
                if x < 30 * (player2[n] / player[0]):
                    ball = -10
                    y = random.randint(1, 3)
                    if y == 1:
                        print(player2[h] + " is able to fend off " + player[k] + " and the ball goes out for a goalkick.")
                    elif y == 2:
                        print(player2[h] + " and " + player[k] + " compete for the ball, and in the end, neither of them get it, and it goes out for a goalkick")
                    elif y == 3:
                        print(player2[h] + " successfully defends " + player[k] + " and the ball flies long for a goalkick.")
                elif x < 50 * (player2[n] / player[0]):
                    ball = 5
                    y = random.randint(1, 3)
                    if y == 1:
                        print(player2[h] + " is able to prevent " + player[k] + " from getting the ball, and heads it out for another corner.")
                    elif y == 2:
                        print(player2[h] + " gets to the ball first, but can only head it back over the goal for another corner.")
                    elif y == 3:
                        print(player[k] + " looked dangerous for a second, but " + player2[h] + " heads the ball long for another corner.")
                else:
                    y = random.randint(1, 4)
                    if y == 1:
                        print(player2[h] + " is not able to fend off " + player[k] + " who heads the ball at the goal.")
                    elif y == 2:
                        print(player[k] + " beats " + player2[h] + " and heads the ball towards the bottom corner.")
                    elif y == 3:
                        print(player[k] + " jumps high in the air and heads it towards the goal.")
                    else:
                        print(player[k] + " and " + player2[h] + " both jump for the ball, but in the end " + player[k] + " wins it and heads it towards the goal.")
                    print("")
                    time.sleep(5)
                    shot2 += 1
                    x = random.randint(1, 100)
                    if x < 7 * T1K[0]:
                        target2 += 1
                        ball = -10
                        y = random.randint(1, 3)
                        if y == 1:
                            print(T1K[3] + " makes a brilliant save, and is able to hold onto the ball.")
                        elif y == 2:
                            print(T1K[3] + " leaps and is just able to grab the ball with his outstretched arms.")
                        elif y == 3:
                            print(T1K[3] + " reacts quickly and is able to hug the ball to his chest.")
                    else:
                        target2 += 1
                        ball = 11
                        y = random.randint(1, 3)
                        if y == 1:
                            print(T1K[3] + " lungs for the ball, but he is too slow and it goes into the back of the net.")
                        elif y == 2:
                            print(T1K[3] + " dives towards the ball, but is too slow, and the ball flies into the back of net.")
                        elif y == 3:
                            print("The shot is accurate, and " + T1K[3] + " barely misses the chance to push it wide with his fingertips.")
    elif ball == -6:
        x = str(input("Who do you want to take the freekick? "))
        print("")
        playerchosen = 0
        for a in team2playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                print(a[3] + " will take the freekick.")
        for a in team2playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                print(a[4] + " will take the freekick.")
        time.sleep(3)
        print("")
        shot2 += 1
        while playerchosen == 0:
            print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
            time.sleep(1)
            print("")
            x = str(input("Who do you want to take the freekick? "))
            time.sleep(2)
            playerchosen = 0
            for a in team2playersa:
                if x == a[3]:
                    player = a
                    playerchosen = 1
                    print(a[3] + " will take the freekick.")
                    time.sleep(3)
                    print("")
            for a in team2playersm:
                if x == a[4]:
                    player = a
                    playerchosen = 1
                    print(a[4] + " will take the freekick.")
                    time.sleep(3)
                    print("")
        x = random.randint(1, 100)
        if x > 9 * player[0]:
            b = random.randint(1, 3)
            if b == 1:
                print("The kick is poor and the ball sails over the goal.")
            elif b == 2:
                print("The freekick had some power to it, but the aim was off, and the ball is sent into the stands.")
            elif b == 3:
                print("The ball has some curl on it, but not enough, and goes past the goal for a goalkick.")
            ball = 10
        else:
            x = random.randint(1, 100)
            if x < 6 * T1K[1]:
                target2 += 1
                ball = 10
                b = random.randint(1, 3)
                if b == 1:
                    print("It was a decent shot, but a comfortable save for " + T1K[3] + " nonetheless.")
                if b == 2:
                    print("The ball curls towards the top left corner, but a fantastic save by " + T1K[3] + " ends up with the ball in his hands.")
                if b == 3:
                    print("The ball has some power on it, but " + T1K[3] + " is able to grab the ball.")
            elif x < 8 * T1K[0]:
                b = random.randint(1, 2)
                target2 += 1
                ball = -5
                if b == 1:
                    print("The ball has spin and power, but " + T1K[3] + " is able to knock it wide for a corner.")
                if b == 2:
                    print("The ball curves towards the top corner, but " + T1K[3] + " just gets a hand to it and knocks it wide for a corner.")
            else:
                ball = -11
                target2 += 1
                b = random.randint(1, 3)
                if b == 1:
                    print("GOAL! The ball flies into the corner, and there was nothing " + T1K[3] + " could do to stop it.")
                if b == 2:
                    print("He really got his foot behind it. The ball flies past " + T1K[3] + "'s fingertips into the goal.")
                if b == 3:
                    print("An unfortunate deflection for " + team1 + " ends up with the ball in the back of the net.")
        player2 = player
    elif ball == -7:
        player2 = random.choice(team2playersm)
        x = random.randint(1, 4)
        if x == 1:
            print(player2[4] + " takes the freekick from the middle quickly.")
        elif x == 2:
            print(team2 + " decide to move with speed, and " + player2[4] + " is quick to take the freekick.")
        elif x == 3:
            print("The freekick has little menace, but " + team2 + " are happy for the possession. " + player2[4] + " will take the freekick.")
        elif x == 4:
            print("The freekick is much to far away for a shot, and will be taken as a pass. It will be taken by " + player2[4])
        x = random.randint(1, 100)
        time.sleep(3.4)
        print("")
        if x < 30 / player[0]:
            ball = 2
            b = random.randint(1, 2)
            x = random.randint(1, 100)
            if x < 100 * (T1M1[0] / team1midfieldd):
                player = T1M1
            elif x < 100 * ((T1M1[0] + T1M2[0]) / team1midfieldd):
                player = T1M2
            else:
                player = T1M3
            if b == 1:
                print("The pass by " + player2[4] + " is horrible and is intercepted by " + player[4] + ".")
            if b == 2:
                print(player2[4] + "'s pass was weak and unnacurate, and it was intercepted by " + player[4] + ".")
        else:
            x = random.randint(1, 100)
            if x < 11:
                x = random.randint(1, 100)
                if x < 6 * player2[0]:
                    x = random.randint(1, 100)
                    if x < 100 * (T1M1[0] / team1midfieldd):
                        player = T1M1
                    elif x < 100 * ((T1M1[0] + T1M2[0]) / team1midfieldd):
                        player = T1M2
                    else:
                        player = T1M3
                    ball = 2
                    b = random.randint(1, 2)
                    if b == 1:
                        print(player2[4] + " attempts a long pass to right outside the box, but it is intercepted by " + player[4] + ".")
                    if b == 2:
                        print(player2[4] + " sees an opportunity for a long pass to right outside the box, but " + player[4] + " cuts it out.")
                else:
                    x = random.randint(1, 100)
                    ball = -3
                    if x < 100 * (T2A1[0] / team2attack):
                        player = T2A1
                    elif x < 100 * ((T2A1[0] + T2A2[0]) / team2attack):
                        player = T2A2
                    else:
                        player = T2A3
                    while player2 == player:
                        x = random.randint(1, 100)
                        if x < 100 * (T2A1[0] / team2attack):
                            player = T2A1
                        elif x < 100 * ((T2A1[0] + T2A2[0]) / team2attack):
                            player = T2A2
                        else:
                            player = T2A3
                    b = random.randint(1, 2)
                    if b == 1:
                        print(player2[4] + " sees an opportunity, and curves a ball up to " + player[3] + " who is right outside the box.")
                    elif b == 2:
                        print(player2[4] + " passes it over the heads of the opponent midfielders straight to the feet of " + player[3] + " who is standing right outside the box.")
            else:
                player = random.choice(team2playersm)
                while player2 == player:
                    player = random.choice(team2playersm)
                x = random.randint(1, 3)
                ball = -2
                if x == 1:
                    print(player2[4] + " plays a simple ball to " + player[4] + ".")
                if x == 2:
                    print(player2[4] + " plays a short pass to " + player[4] + ".")
                elif x == 3:
                    print("The game resumes with " + player2[4] + " passing to " + player[4] + ".")
        player2 = player
    elif ball == -8:
        x = str(input("Who do you want to take the penalty? "))
        print("")
        playerchosen = 0
        for a in team2playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                n = 3
                print(a[3] + " will take the penalty.")
        for a in team2playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                print(a[4] + " will take the penalty.")
                n = 4
        print("")
        shot2 += 1
        time.sleep(3)
        while playerchosen == 0:
            print("")
            print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
            time.sleep(1)
            x = str(input("Who do you want to take the penalty? "))
            print("")
            playerchosen = 0
            time.sleep(2)
            for a in team2playersa:
                if x == a[3]:
                    player = a
                    playerchosen = 1
                    n = 3
                    print(a[3] + " will take the penalty.")
                    time.sleep(3)
                    print("")
            for a in team2playersm:
                if x == a[4]:
                    player = a
                    playerchosen = 1
                    n = 4
                    print(a[4] + " will take the penalty.")
                    time.sleep(3)
                    print("")
        x = random.randint(1, 2)
        if x == 1:
            print(T1K[3] + " dives right.")
            dive = 1
        elif x == 2:
            print(T1K[3] + " dives left.")
            dive = 2
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 45:
            print(player[n] + " shoots left.")
            shoot = 2
        elif x > 55:
            print(player[n] + " shoots right.")
            shoot = 1
        else:
            print(player[n] + " goes down the middle.")
            shoot = 6
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 50 / player[2]:
            x = random.randint(1, 3)
            if x == 1:
                print("The ball richochets off the post!")
            if x == 2:
                print("The shot has little aim, and the ball is sent long.")
            if x == 3:
                print("He went for the perfect shot, but ended up completely missing the goal.")
            ball = 10
        if ball != 10:
            target2 += 1
            if shoot == dive:
                x = random.randint(1, 100)
                if x < (40 * player[2] / T1K[1]):
                    ball = -12
                    b = random.randint(1, 3)
                    if b == 1:
                        print(player[n] + " just sails the ball past the goalkeepers outstretched arms.")
                    if b == 2:
                        print(T1K[3] + "'s fingers are mere inches away from the ball, but it sails into the net.")
                    if b == 3:
                        print("The ball flies into the top corner, and the goalkeeper cannot save it.")
                elif (60 * player[2] / T1K[1]):
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T1K[3] + " is able to just get his palms to it, and the ball rebounds back out into the attacking players.")
                    elif x == 2:
                        print(T1K[3] + " is near the ball, but isn't able to grab the ball, and it rebounds off back into the fray of players.")
                    elif x == 3:
                        print("The ball doesn't go wide enough to make it in, but " + T1K[3] + " isn't able to grab it, and it bounces off his palms.")
                    x = random.randint(1, 100)
                    print("")
                    time.sleep(3)
                    if x < 15 * (team2attack + team2midfielda + 7 * player[0]) / (team1defense):
                        x = random.randint(1, 100)
                        if x < (800 * player[0]) / (team2attack + team2midfielda + 7 * player[0]):
                            player = player
                            n = 3
                        elif x < (team2attack - player[0]) / (team2attack + team2midfielda + 7 * player[0]):
                            player2 = random.choice(team2playersa)
                            while player2 == player:
                                player2 = random.choice(team2playersa)
                            player = player2
                            n = 3
                        else:
                            player2 = random.choice(team2playersm)
                            while player2 == player:
                                player2 = random.choice(team2playersm)
                            player = player2
                            n = 4
                        x = random.randint(1, 100)
                        if x < 70 * player[0] / T1K[1]:
                            ball = -11
                            b = random.randint(1, 2)
                            shot2 += 1
                            target2 += 1
                            if b == 1:
                                print(player[n] + " gets the ball on the rebound, and is able to put it past " + T1K[3] + " for his team.")
                            if b == 2:
                                print(player[n] + " lunges to get ther rebound and kicks it in the net.")
                        else:
                            ball = 10
                            b = random.randint(1, 2)
                            shot2 += 1
                            target2 += 1
                            if b == 1:
                                print(player[n] + "gets the rebound and shoots, but " + T1K[3] + " is able to barely get back and grab hold of the ball.")
                            if b == 2:
                                print(player[n] + " lunges and shoots on the rebound, but " + T1K[3] + " is just able to get back and grabs the ball.")
                    else:
                        ball = 9
                        x = random.randint(1, 100)
                        if x < (100 * T1D1[0]) / (Team1Defense):
                            player = T1D1
                        elif x < (100 * T1D2[0]) / (Team1Defense):
                            player = T1D2
                        else:
                            player = T1D3
                        b = random.randint(1, 3)
                        if b == 1:
                            print(player[3] + " is able to get to the ball first.")
                        if b == 2:
                            print(player[3] + " reaches the ball and is in a position to clear it.")
                        if b == 3:
                            print(player[3] + " lunges for the ball and gains possession.")

                else:
                    ball = 10
                    b = random.randint(1, 4)
                    if b == 1:
                        print(T1K[3] + " is able to grab onto the ball, negating the threat.")
                    elif b == 2:
                        print(player[n] + " hangs his head in his hands, as " + T1K[3] + "blocks his shot.")
                    elif b == 3:
                        print("The shot is weak, and " + T1K[3] + " is able to grab it")
                    else:
                        print("The ball flies into the bottom corner, but somehow, " + T1K[3] + "is able to grab it.")
            elif shoot - dive == 1 or shoot - dive == -1:
                ball = -11
                b = random.randint(1, 5)
                if b == 1:
                    print("The ball sails into the bottom corner uncontested.")
                elif b == 2:
                    print("The shot was mediocre, but it goes in nonetheless.")
                elif b == 3:
                    print("All " + T1K[3] + " can do is watch as the ball rolls into the bottom corner.")
                elif b == 4:
                    print("The shot likely wouldn't have been blocked anyway, but the goalkeeper diving the wrong way soldifies the goal.")
                else:
                    print("The shot is perfect, flying into the top corner.")
            else:
                x = random.randint(1, 100)
                if x < (60 * player[2] / T1K[1]):
                    ball = -12
                    b = random.randint(1, 3)
                    if b == 1:
                        print(a[n] + " just sails the ball past the goalkeepers outstretched legs, with nothing he can do to stop it.")
                    if b == 2:
                        print(T1K[3] + "'s feet are mere inches away from the ball, but it sails into the net, as his forward momentum prevents him from blocking it.")
                    if b == 3:
                        print("The ball flies into the goal behind him, and the goalkeeper cannot save it.")
                elif (70 * player[2] / T1K[1]):
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T1K[3] + " is able to just get his feet to it, and the ball rebounds back out into the attacking players.")
                    elif x == 2:
                        print(T1K[3] + "'s feet are near the ball, and it rebounds off back into the fray of players.")
                    elif x == 3:
                        print("The ball doesn't go high enough to make it in, but " + T1K[3] + " isn't able to knock it far with his feat, and it bounces off into the fray of players.")
                    x = random.randint(1, 100)
                    print("")
                    time.sleep(3)
                    if x < 15 * (team2attack + team2midfielda + 7 * player[0]) / (team1defense):
                        x = random.randint(1, 100)
                        if x < (800 * player[0]) / (team2attack + team2midfielda + 7 * player[0]):
                            player = player
                            n = 3
                        elif x < (team2attack - player[0]) / (team2attack + team2midfielda + 7 * player[0]):
                            player2 = random.choice(team2playersa)
                            while player2 == player:
                                player2 = random.choice(team2playersa)
                            player = player2
                            n = 3
                        else:
                            player2 = random.choice(team2playersm)
                            while player2 == player:
                                player2 = random.choice(team2playersm)
                            player = player2
                            n = 4
                        x = random.randint(1, 100)
                        if x < 70 * player[0] / T1K[1]:
                            ball = -11
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + " gets the ball on the rebound, and is able to put it past " + T1K[3] + " for his team.")
                            if b == 2:
                                print(player[n] + " lunges to get ther rebound and kicks it in the net.")
                            shot2 += 1
                            target2 += 1
                        else:
                            ball = 10
                            b = random.randint(1, 2)
                            if b == 1:
                                print(player[n] + "gets the rebound and shoots, but " + T1K[3] + " is able to barely get back and grab hold of the ball.")
                            if b == 2:
                                print(player[n] + " lunges and shoots on the rebound, but " + T1K[3] + " is just able to get back and grabs the ball.")
                            shot2 += 1
                            target2 += 1
                    else:
                        ball = 9
                        x = randint(1, 100)
                        if x < (100 * T1D1[0]) / (Team1Defense):
                            player = T1D1
                        elif x < (100 * T1D2[0]) / (Team1Defense):
                            player = T1D2
                        else:
                            player = T1D3
                        b = random.randint(1, 3)
                        if b == 1:
                            print(player[3] + " is able to get to the ball first.")
                        if b == 2:
                            print(player[3] + " reaches the ball and is in a position to clear it.")
                        if b == 3:
                            print(player[3] + " lunges for the ball and gains possession.")

                else:
                    ball = 10
                    b = random.randint(1, 4)
                    if b == 1:
                        print(T1K[3] + " is able to grab onto the ball, negating the threat.")
                    elif b == 2:
                        print(player[n] + " hangs his head in his hands, as " + T1K[3] + "blocks his shot.")
                    elif b == 3:
                        print("The shot is weak, and " + T1K[3] + " is able to grab it")
                    else:
                        print("The ball flies into the bottom corner, but somehow, " + T1K[3] + "is able to grab it.")

        player2 = player
    elif ball == -9:
        x = random.randint(1, 100)
        if x < 8 * (team1midfieldd) / (player2[0]):
            ball = 2
            player = random.choice(team1playersm)
            b = random.randint(1, 3)
            if b == 1:
                print(player2[3] + " tried to pass to midfield but " + player[4] + " intercepts the pass.")
            elif b == 2:
                print(player[4] + " cuts out the pass towards midfield of " + player2[3] + ".")
            else:
                print(player2[3] + "'s pass is poor, and it gets cut out by " + player[4] + ".")
        else:
            player = random.choice(team2playersm)
            b = random.randint(1, 4)
            ball = -2
            if b == 1:
                print(player2[3] + " passes to " + player[4])
            elif b == 2:
                print(player2[3] + " passes into midfield, where " + player[4] + " waits.")
            elif b == 3:
                print(player2[3] + " hits the ball towards " + player[4])
            else:
                print(player2[3] + " surveys his options and decides to pass to " + player[4])
        player2 = player
    elif ball == - 10:
        x = random.randint(1, 100)
        if x < (8 * team1attack / T2K[0]):
            b = random.randint(1, 3)
            ball = 3
            player = random.choice(team1playersa)
            # add accurate chances of players intercepting, add different outcomes of messed up pas
            if b == 1:
                print(T2K[3] + " completely messes up the pass to his back line and passes to " + player[3] + " right outside the box.")
            if b == 2:
                print(T2K[3] + "'s pass is in accurate, and " + player[3] + " cuts it out right outside the box.")
            if b == 3:
                print(player[3] + "sees the intended pass and is able to get to it quickly, gaining possession of the ball right outside the box.")
        elif x < 18 * (team1attack / T2K[0]):
            ball = 2
            player = random.choice(team1playersm)
            b = random.randint(1, 3)
            if b == 1:
                print(T2K[3] + " kicks it to the middle, and " + player[4] + " intercepts the pass.")
            elif b == 2:
                print("The pass to the middle by " + T2K[3] + " is cut out by " + player[4])
            elif b == 3:
                print(player[4] + " sees the pass to the middle by the keeper and cuts it out.")
        elif x < 40 * (team1attack / T2K[0]):
            ball = -9
            b = random.randint(1, 3)
            player = random.choice(team2playersd)
            if b == 1:
                print(T2K[3] + " passes to " + player[3])
            elif b == 2:
                print(player[3] + " receives the ball from " + T2K[3])
            elif b == 3:
                print(T2K[3] + " plays the ball short to " + player[3])
        else:
            ball = - 2
            b = random.randint(1, 3)
            player = random.choice(team2playersm)
            if b == 1:
                print(T2K[3] + " lobs it into the middle to " + player[4])
            elif b == 2:
                print(player[4] + " receives a long pass from " + T2K[3])
            elif b == 3:
                print(T2K[3] + " kicks it to " + player[4])
        player2 = player
    if ball == -11:
        time.sleep(2.5)
        print("")
        print("GOALLLLLLLLLLLLLLLL!")
        time.sleep(1)
        print("")
        team2score += 1
        print(team1 + " - " + team2)
        print("")
        print("  " + str(team1score) + "    -    " + str(team2score) + "  ")
        ball = 1
    if ball == 11:
        time.sleep(2.5)
        print("")
        print("GOALLLLLLLLLLLLLLLL!")
        time.sleep(1)
        print("")
        team1score += 1
        print(team1 + " - " + team2)
        print("")
        print("  " + str(team1score) + "    -    " + str(team2score) + "  ")
        ball = -1
    if us == half:
        ball3 = abs(ball)
        done = 0
        if ball3 == 2 or ball3 == 7:
            done = 1
        elif ball3 == 9 or ball3 == 10:
            done = 1
        elif ball3 == 1:
            done = 1
        if done == 1:
            time.sleep(3)
            print("")
            print("Half Time")
            time.sleep(3)
            print("                  " + str(team1score) + "    -     " + str(team2score))
            time.sleep(3)
            print("")
            x = math.floor((100 / 45) * possession1)
            y = 100 - x
            print("Possession:       " + str(x) + "    -    " + str(y))
            print("Shots:             " + str(shot1) + "    -    " + str(shot2))
            print("Shots on target:   " + str(target1) + "    -    " + str(target2))

        else:
            half += 2
    if us == full:
        ball3 = abs(ball)
        done = 0
        if ball3 == 2 or ball3 == 7:
            done = 1
        elif ball3 == 9 or ball3 == 10:
            done = 1
        elif ball3 == 1:
            done = 1
        if done == 0:
            full += 2

print("")
print("Game Over")
time.sleep(3)
print("                  " + str(team1score) + "    -     " + str(team2score))
time.sleep(3)
print("")
x = math.floor((100 / 45) * possession1)
y = 100 - x
print("Possession:       " + str(x) + "    -    " + str(y))
print("Shots:            " + str(shot1) + "    -    " + str(shot2))
print("Shots on target:  " + str(target1) + "    -    " + str(target2))

time.sleep(6)
print("")

if team1score - team2score > 2:
    destroyed1 = [team2 + " left in shambles after this defeat.", "Players on" + team2 + " return to the locker room with tears in their eyes after this performance ", "The stadium fills with mocking chants as " + team2 + " players leave the field",
                  " Grins are all that can be found on players of " + team1 + " as they return home.", " What a day for " + team2 + ". Simply nothing has gone their way today.",
                  "Players of " + team2 + " shocked, as they began the match favorites, but actually lost it " + str(team1score) + " - " + str(team2score)]
    print(random.choice(destroyed1))
elif team1score - team2score < -2:
    destroyed2 = [team1 + " left in shambles after this defeat.", "Players on" + team1 + " return to the locker room with tears in their eyes after this performance ", "The stadium fills with mocking chants as " + team1 + " players leave the field",
                  " Grins are all that can be found on players of " + team2 + " as they return home.", " What a day for " + team1 + ". Simply nothing has gone their way today.",
                  "Players of " + team1 + " shocked, as they began the match favorites, but actually lost it " + str(team1score) + " - " + str(team2score)]
    print(random.choice(destroyed2))
elif team1score - team2score > 0:
    won1 = ["It was generally strong show from " + team1 + " who at times looked unconfident, but pulled through in the end",
            "While it was a fairly even match for most of the game, it was " + team1 + " who took the opportunities they were given and converted them to goals.",
            " The scoreline of the game was relatively close, but it was " + team1 + " who had the advantage in techinique and persistance.",
            " Many fans concerned by the weakness shown by " + team1 + " at times, but mostly, they were fairly convinving"]
    print(random.choice(won1))
elif team1score - team2score < 0:
    won2 = ["It was generally strong show from " + team2 + " who at times looked unconfident, but pulled through in the end",
            "While it was a fairly even match for most of the game, it was " + team2 + " who took the opportunities they were given and converted them to goals.",
            " The scoreline of the game was relatively close, but it was " + team2 + " who had the advantage in techinique and persistance.",
            " Many fans concerned by the weakness shown by " + team2 + " at times, but mostly, they were fairly convinving"]
    print(random.choice(won2))
elif team1score == team2score:
    tie = ["While each side had chances, the game ultimately ended in a draw, with neither team pulling ahead", "To decide this match, the teams head to a penalty shootout.",
           "This was a important match for both sides, but neither team was able to get the win they wanted.", "Fans of both teams unconvinced after this showing by each side.", "Neither team is up. Time for penalties!",
           "The tension reaches a max as the players prepare for penalties.", "Anxious faces all around now, as the players await penalties."]
    print(random.choice(tie))
# penalties


team1goals = 0
team2goals = 0
team1shots = 0
team2shots = 0
h = 0
time.sleep(3)
print("")
while (team2goals - team1goals) < (6 - team1shots) and (team1goals - team2goals) < (6 - team1shots):
    h += 1
    if h == 1:
        order = 'first'
    if h == 2:
        order = 'second'
    if h == 3:
        order = 'third'
    if h == 4:
        order = 'fourth'
    if h == 5:
        order = 'fifth'
    if h == 6:
        order = 'sixth'
    if h == 7:
        order = 'seventh'
    if h == 8:
        order = 'eight'
    if h == 9:
        order = 'ninth'
    if h == 10:
        order = 'tenth'
    if h == 11:
        order = 'eleventh'
    if h == 12:
        order = 'twelfth'
    team1shots += 1
    team2shots += 2

    x = str(input("Who do you want to take the " + str(order) + " penalty " + team1 + "? "))
    print("")
    playerchosen = 0
    for a in team1playersa:
        if x == a[3]:
            player = a
            playerchosen = 1
            n = 3
            time.sleep(3)
            print(a[3] + " will take the penalty.")
            print("")
    for a in team1playersm:
        if x == a[4]:
            player = a
            playerchosen = 1
            print(a[4] + " will take the penalty.")
            n = 4
            time.sleep(3)
            print("")
    shot1 += 1
    while playerchosen == 0:
        time.sleep(3)
        print("")
        print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
        time.sleep(1)
        x = str(input("Who do you want to take the penalty? "))
        print("")
        playerchosen = 0
        time.sleep(2)
        for a in team1playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                n = 3
                print(a[3] + " will take the penalty.")
                print("")
        for a in team1playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                n = 4
                print(a[4] + " will take the penalty.")
                print("")
    time.sleep(3)
    x = random.randint(1, 2)
    if x == 1:
        print(T2K[3] + " dives right.")
        dive = 1
    elif x == 2:
        print(T2K[3] + " dives left.")
        dive = 2
    time.sleep(3)
    print("")
    x = random.randint(1, 100)
    if x < 45:
        print(player[n] + " shoots left.")
        shoot = 2
    elif x > 55:
        print(player[n] + " shoots right.")
        shoot = 1
    else:
        print(player[n] + " goes down the middle.")
        shoot = 6
    time.sleep(3)
    print("")
    x = random.randint(1, 100)
    if x < 50 / a[2]:
        x = random.randint(1, 3)
        if x == 1:
            print("The ball richochets off the post!")
        if x == 2:
            print("The shot has little aim, and the ball is sent long.")
        if x == 3:
            print("He went for the perfect shot, but ended up completely missing the goal.")
        ball = -10
    else:
        if shoot == dive:
            x = random.randint(1, 100)
            if x < (40 * a[2] / T2K[1]):
                ball = 11
                b = random.randint(1, 3)
                if b == 1:
                    print(player[n] + " just sails the ball past the goalkeepers outstretched arms.")
                if b == 2:
                    print(T2K[3] + "'s fingers are mere inches away from the ball, but it sails into the net.")
                if b == 3:
                    print("The ball flies into the top corner, and the goalkeeper cannot save it.")
                team1goals += 1
                target1 += 1
            elif (60 * a[2] / T2K[1]):
                x = random.randint(1, 3)
                if x == 1:
                    print(T2K[3] + " is able to just get his palms to it, and the ball bounces away from the goal.")
                elif x == 2:
                    print(T2K[3] + " is near the ball and just isn't able to grab the ball, but in the end it doesn't matter, and the ball rolls away from the goal.")
                elif x == 3:
                    print("The ball doesn't go wide enough to make past the keeper, and while " + T2K[3] + " isn't able to grab it, and it bounces off his palms.")

            else:
                ball = -10
                b = random.randint(1, 4)
                if b == 1:
                    print(T2K[3] + " is able to grab onto the ball, negating the threat.")
                elif b == 2:
                    print(player[n] + " hangs his head in his hands, as " + T2K[3] + "blocks his shot.")
                elif b == 3:
                    print("The shot is weak, and " + T2K[3] + " is able to grab it")
                else:
                    print("The ball flies into the bottom corner, but somehow, " + T2K[3] + "is able to grab it.")
        elif shoot - dive == 1 or shoot - dive == -1:
            ball = 11
            b = random.randint(1, 5)
            if b == 1:
                print("The ball sails into the bottom corner uncontested.")
            elif b == 2:
                print("The shot was mediocre, but it goes in nonetheless.")
            elif b == 3:
                print("All " + T2K[3] + " can do is watch as the ball rolls into the bottom corner.")
            elif b == 4:
                print("The shot likely wouldn't have been blocked anyway, but the goalkeeper diving the wrong way soldifies the goal.")
            else:
                print("The shot is perfect, flying into the top corner.")
            team1goals += 1
        else:
            x = random.randint(1, 100)
            target1 += 1
            if x < (60 * a[2] / T2K[1]):
                ball = 11
                team1goals += 1
                b = random.randint(1, 3)
                if b == 1:
                    print(a[n] + " just sails the ball past the goalkeepers outstretched legs, with nothing he can do to stop it.")
                if b == 2:
                    print(T2K[3] + "'s feet are mere inches away from the ball, but it sails into the net, as his forward momentum prevents him from blocking it.")
                if b == 3:
                    print("The ball flies into the goal behind him, and the goalkeeper cannot save it.")
            elif (70 * a[2] / T2K[1]):
                x = random.randint(1, 3)
                if x == 1:
                    print(T2K[3] + " is able to just get his palms to it, and the ball bounces away from the goal.")
                elif x == 2:
                    print(T2K[3] + " is near the ball and just isn't able to grab the ball, but in the end it doesn't matter, and the ball rolls away from the goal.")
                elif x == 3:
                    print("The ball doesn't go wide enough to make past the keeper, and while " + T2K[3] + " isn't able to grab it, and it bounces off his palms.")

    if (team2goals - team1goals) < (6 - team1shots) and (team1goals - team2goals) < (6 - team1shots):
        time.sleep(3)
        print("")

        x = str(input("Who do you want to take the " + str(order) + " penalty " + team2 + "? "))
        print("")
        playerchosen = 0
        for a in team2playersa:
            if x == a[3]:
                player = a
                playerchosen = 1
                n = 3
                print(a[3] + " will take the penalty.")
        for a in team2playersm:
            if x == a[4]:
                player = a
                playerchosen = 1
                print(a[4] + " will take the penalty.")
                n = 4
        print("")
        shot2 += 1
        time.sleep(3)
        while playerchosen == 0:
            print("")
            print("Please give the player's full name, with caps and spaces. It also must be an attacker or midfielder. Please add (M) or (A) after their name. ")
            time.sleep(1)
            x = str(input("Who do you want to take the penalty? "))
            print("")
            playerchosen = 0
            time.sleep(2)
            for a in team2playersa:
                if x == a[3]:
                    player = a
                    playerchosen = 1
                    n = 3
                    print(a[3] + " will take the penalty.")
                    time.sleep(3)
                    print("")
            for a in team2playersm:
                if x == a[4]:
                    player = a
                    playerchosen = 1
                    n = 4
                    print(a[4] + " will take the penalty.")
                    time.sleep(3)
                    print("")
        x = random.randint(1, 2)
        if x == 1:
            print(T1K[3] + " dives right.")
            dive = 1
        elif x == 2:
            print(T1K[3] + " dives left.")
            dive = 2
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 45:
            print(player[n] + " shoots left.")
            shoot = 2
        elif x > 55:
            print(player[n] + " shoots right.")
            shoot = 1
        else:
            print(player[n] + " goes down the middle.")
            shoot = 6
        time.sleep(3)
        print("")
        x = random.randint(1, 100)
        if x < 50 / player[2]:
            x = random.randint(1, 3)
            if x == 1:
                print("The ball richochets off the post!")
            if x == 2:
                print("The shot has little aim, and the ball is sent long.")
            if x == 3:
                print("He went for the perfect shot, but ended up completely missing the goal.")
            ball = 10
        else:
            target2 += 1
            if shoot == dive:
                x = random.randint(1, 100)
                if x < (40 * player[2] / T1K[1]):
                    ball = -12
                    b = random.randint(1, 3)
                    if b == 1:
                        print(player[n] + " just sails the ball past the goalkeepers outstretched arms.")
                    if b == 2:
                        print(T1K[3] + "'s fingers are mere inches away from the ball, but it sails into the net.")
                    if b == 3:
                        print("The ball flies into the top corner, and the goalkeeper cannot save it.")
                    team2goals += 1
                elif (60 * player[2] / T1K[1]):
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T2K[3] + " is able to just get his palms to it, and the ball bounces away from the goal.")
                    elif x == 2:
                        print(T2K[3] + " is near the ball and just isn't able to grab the ball, but in the end it doesn't matter, and the ball rolls away from the goal.")
                    elif x == 3:
                        print("The ball doesn't go wide enough to make past the keeper, and while " + T2K[3] + " isn't able to grab it, and it bounces off his palms.")
                else:
                    ball = 10
                    b = random.randint(1, 4)
                    if b == 1:
                        print(T1K[3] + " is able to grab onto the ball, negating the threat.")
                    elif b == 2:
                        print(player[n] + " hangs his head in his hands, as " + T1K[3] + "blocks his shot.")
                    elif b == 3:
                        print("The shot is weak, and " + T1K[3] + " is able to grab it")
                    else:
                        print("The ball flies into the bottom corner, but somehow, " + T1K[3] + "is able to grab it.")
            elif shoot - dive == 1 or shoot - dive == -1:
                ball = -11
                b = random.randint(1, 5)
                if b == 1:
                    print("The ball sails into the bottom corner uncontested.")
                elif b == 2:
                    print("The shot was mediocre, but it goes in nonetheless.")
                elif b == 3:
                    print("All " + T1K[3] + " can do is watch as the ball rolls into the bottom corner.")
                elif b == 4:
                    print("The shot likely wouldn't have been blocked anyway, but the goalkeeper diving the wrong way soldifies the goal.")
                else:
                    print("The shot is perfect, flying into the top corner.")
                team2goals += 1
            else:
                x = random.randint(1, 100)
                if x < (60 * player[2] / T1K[1]):
                    ball = -12
                    b = random.randint(1, 3)
                    if b == 1:
                        print(a[n] + " just sails the ball past the goalkeepers outstretched legs, with nothing he can do to stop it.")
                    if b == 2:
                        print(T1K[3] + "'s feet are mere inches away from the ball, but it sails into the net, as his forward momentum prevents him from blocking it.")
                    if b == 3:
                        print("The ball flies into the goal behind him, and the goalkeeper cannot save it.")
                    team2goals += 1
                else:
                    x = random.randint(1, 3)
                    if x == 1:
                        print(T2K[3] + " is able to just get his palms to it, and the ball bounces away from the goal.")
                    elif x == 2:
                        print(T2K[3] + " is near the ball and just isn't able to grab the ball, but in the end it doesn't matter, and the ball rolls away from the goal.")
                    elif x == 3:
                        print("The ball doesn't go wide enough to make past the keeper, and while " + T2K[3] + " isn't able to grab it, and it bounces off his palms.")
    print("")
    time.sleep(3)

    print("Game Over")
    print(str(team1goals) + "  -  " + str(team2goals))
    print("")
    time.sleep(3)

