'''
Created on 2016-02-17

@author: Tomy
'''
'''Programme de categorisation '''

from psychopy import core, visual, event
from random import randint

win = visual.Window(fullscr = True, color="white")
liste_reponses = {}
num_question = 0
Number_A = []
Number_B = []
numero = 0
categorie = 0
debut_path = "C:\Exp\TextureTest\Texture"
fin_path = ".bmp"
path_stimuli = ""
lettre_categorie = ""
text_feedback = ""
feedback = visual.TextStim(win, text=text_feedback, pos=(0.0, 0.0), height = 0.5)
win.flip()
core.wait(2.0)
while len(liste_reponses) < 10 :
    
    
    num_question += 1
    categorie = randint(1,2)
    numero = randint(1,600)
    if categorie == 1 :
        lettre_categorie = "A"
    elif categorie == 2 :
        lettre_categorie = "C"
    path_stimuli = debut_path + str(lettre_categorie) + str(numero) + fin_path
    stim = visual.ImageStim(win, image=path_stimuli)
    stim.draw()
    win.flip()
    core.wait(1)
    
    win.flip()
    
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            print thisKey
            if thisKey== 'num_1':
                if categorie == 1: 
                    liste_reponses[str(num_question)] =  True
                    thisResp = "Correcte"
                else: 
                    liste_reponses[str(num_question)] =  False
                    thisResp = "Incorrecte"
                    
            elif thisKey=='num_2':
                if categorie == 2: 
                    liste_reponses[str(num_question)] =  True
                    thisResp = "Correcte"
                else: 
                    liste_reponses[str(num_question)] =  False
                    thisResp = "Incorrecte"
            elif thisKey in ['q', 'return']:
                core.quit() 
                event.clearEvents()
            text_feedback= thisResp
            
    
    if text_feedback == "Incorrecte" :
        feedback.color = "red"
    elif text_feedback == "Correcte" :
        feedback.color = "green"

    feedback.text = text_feedback
    feedback.draw()
    win.flip()
    core.wait(2)

resultat = 0
pourcentage = 0
for item in liste_reponses :
    if liste_reponses[item] == True :
        resultat += 1

pourcentage = float(resultat*100/num_question)
print pourcentage




                
                
core.wait(2.0)
core.quit()