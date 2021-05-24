nombre_parties = 0
if nombre_parties <= 10 : 
    scores = [].append(score_tot)
    scores.sort(reverse=True)
    fic = open("Meilleurs scores", "w")
    fic.write("Dix meilleurs scores :")
    for i in range len(scores) :
        fic.write(str(scores[i]))
elif nombre_parties > 10 :
    scores = [].append(score_tot)
    scores.sort(reverse=True)
    for i in range (1, len(scores)+1 ) : 
        if score_tot <= scores[-1] :
             pass
        elif score_tot > scores[-1] :
            del scores[-1]
            scores.append(score_tot)
            scores.sort(reverse=True)
    fic = open("Meilleurs scores", "w")
    fic.write("Dix meilleurs scores :")
    for i in range (len(scores)) :
        fic.write(str(scores[i]))
