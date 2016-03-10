'''
Created on 2016-03-08

@author: Tomy
'''

'''
Test de jugement de similarite
'''

from psychopy import core, visual, event
from random import randint

win = visual.Window(fullscr = True, color="white")

def write_instruction(sentence):
    written_instruction = str(sentence)
    instruction = visual.TextStim(win, text=written_instruction, pos=(0.0, 0.2))
    instruction.color = "black"
    instruction.draw()
    continuer = visual.TextStim(win, text="Appuyer sur une touche pour continuer", pos=(0.0, -0.6), height = 0.07)
    continuer.color = "black"
    continuer.draw()
    win.flip()
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            thisResp = 1
            

""" 
Fait apparaitre un texte de grosseur moyenne en noir dans l'ecran et attend que l'utilisateur soit pret a passer a l'etape suivante.
"""



def decompte(explication, temps):
    secondes = temps
    text_explication = str(explication)
    while secondes > 0 :
        explication_decompte = visual.TextStim(win, text=text_explication, pos=(0.0, 0.2))
        explication_decompte.color = "black"
        explication_decompte.draw()
        temps_decompte = visual.TextStim(win, text=str(secondes), pos=(0.0, -0.1), height = 0.5)
        temps_decompte.color = "black"
        temps_decompte.draw()
        secondes -= 1
        win.flip()
        core.wait(1)
""" Donne une explication en lien avec le decompte, et fait un decompte en seconde"""
        
debut_path = "C:\Exp\TextureTest\Texture"
fin_path = ".bmp"
path_stimuli = ""
lettre_categorie = ""
liste_utilise = []

def jugement_sim(type, categorie, numero1, numero2):
    if categorie == 1 :
        lettre_categorie = "A"
    elif categorie == 2 :
        lettre_categorie = "B"
    if type == 1 :
        path_stimuli = debut_path + str(lettre_categorie) + str(numero1) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        win.flip()
        core.wait(0.5)
        path_stimuli = debut_path + str(lettre_categorie) + str(numero2) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        
        written_indication = "Veuillez appuyer sur une touche de 0 a 9"
        indication = visual.TextStim(win, text=written_indication, pos=(0.0, 0.0))
        indication.color = "black"
        indication.draw()
        win.flip()
        
    elif type == 2 :
        path_stimuli = debut_path + str(lettre_categorie) + str(numero1) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        win.flip()
        core.wait(0.5)
        
        if lettre_categorie == "A" :
            lettre_categorie = "B"
        elif lettre_categorie == "B" :
            lettre_categorie = "A"
        
        path_stimuli = debut_path + str(lettre_categorie) + str(numero2) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        
        written_indication = "Veuillez appuyer sur une touche de 0 a 9"
        indication = visual.TextStim(win, text=written_indication, pos=(0.0, 0.0))
        indication.color = "black"
        indication.draw()
        win.flip()
    
    elif type == 3 :
        path_stimuli = debut_path + str(lettre_categorie) + str(numero1) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        win.flip()
        core.wait(0.5)
        path_stimuli = debut_path + str(lettre_categorie) + str(numero1) + fin_path
        stim = visual.ImageStim(win, image=path_stimuli)
        stim.draw()
        win.flip()
        core.wait(2)
        
        written_indication = "Veuillez appuyer sur une touche de 0 a 9"
        indication = visual.TextStim(win, text=written_indication, pos=(0.0, 0.0))
        indication.color = "black"
        indication.draw()
        win.flip()
        
        
        
        
        
    
        
    thisResp=None
    
    while thisResp==None:
        allKeys=event.waitKeys(maxWait=float(2),timeStamped=True)
        if allKeys[0] == 'num_0' :
            allKeys[0] = 0
        elif allKeys[0] == 'num_1' :
            allKeys[0] = 1
        elif allKeys[0] == 'num_2' :
            allKeys[0] = 2
        elif allKeys[0] == 'num_3' :
            allKeys[0] = 3
        elif allKeys[0] == 'num_4' :
            allKeys[0] = 4
        elif allKeys[0] == 'num_5' :
            allKeys[0] = 5
        elif allKeys[0] == 'num_6' :
            allKeys[0] = 6
        elif allKeys[0] == 'num_7' :
            allKeys[0] = 7
        elif allKeys[0] == 'num_8' :
            allKeys[0] = 8
        elif allKeys[0] == 'num_9' :
            allKeys[0] = 9
        elif allKeys[0] == 'q':
            core.quit() 
            event.clearEvents()
        elif allKeys == None :
            allKeys = "Attente trop longue!"
        else :
            allKeys = "Mauvaise touche!"
            
        thisResp = allKeys
        
            
    return thisResp

"""
 Fonction prenant un type de test 1 = meme categorie, 2 = differente categorie, 3 = meme stimulus, 
 categorie indique la categorie du premier stimulus 1 pour A et 2 pour B,
 numero 1 et 2 indique le numero de reference de chaque stimuli.
 
 Chaque stimuli est presenter pendant 2 secondes avec 0.5 seconde de separation entre les deux.
 
 Le participant a 2 seconde pour decider de la similarite
 
 Si le participant manque de temps, la fonction retourne Attente trop longue!
 Si le participant appuie sur une mauvaise touche la fonction retourne Mauvaise touche!
 Si le participant appuie sur q, il quittera le programme
 Sinon, la fonction retournera un tuple ayant une valeur de 0 a 9 a l'indice [0]
 et un timestamp en float a l'indice [1]
 
"""
            
            
                
        
        
        
        
    







win.flip()
core.wait(2.0)

write_instruction("Vous vous appretter a faire une tache de jugement de similarite. Vous verrez deux stimuli un a la suite de l'autre.")
write_instruction("Vous devrez juger de leur similarite en utilisant une echelle de 0 a 9. 0 = Tres different 9 = Pareil")
write_instruction("Apres avoir vu chacun des stimulis vous aurez 2 secondes pour faire votre choix en appuyant sur une touche de 0 a 9 sur le numpad")

decompte("L'experimentation commencera dans :", 5)

nbr_essaie = 0
last_type = 0
last_categorie = 0
repetition = 0
repetition_categorie = 0
nbr_pareil = 0
nbr_dif = 0
pareil_1 = 0
pareil_2 = 0
this_trial_list = []
attention_check = False

while nbr_essaie < 11 :
    meme_categorie = randint(1,2)
    categorie = randint(1,2)
    numero_1 = randint(1,600)
    numero_2 = randint(1,600)
    
    already_use = True
    while already_use == True :
        used_item_value = 0
        for item in this_trial_list :
            if numero_1 == item :
                used_item_value += 1
        if used_item_value == 0 :
            already_use = False
        else : 
            numero_1 = randint(1,600)
    
    already_use = True
    while already_use == True :
        used_item_value = 0
        for item in this_trial_list :
            if numero_2 == item :
                used_item_value += 1
        if numero_2 == numero_1 :
            used_item_value +=1
        if used_item_value == 0 :
            already_use = False
        else : 
            numero_2 = randint(1,600)
                
    if nbr_dif == 5 :
        if attention_check == False :
            attention_check = True
            nbr_essaie += 1
            pass # event (2x meme stimuli)
        elif pareil_1 > pareil_2 :
            nbr_essaie += 1
            pareil_2 += 1
            nbr_pareil += 1 
            pass # event pareil categorie B
        else :
            nbr_essaie += 1
            pareil_1 += 1
            nbr_pareil += 1  
            pass # event pareil categorie A
    elif nbr_pareil == 5 :
        if attention_check == False :
            attention_check = True
            nbr_essaie += 1
            pass # event(2x meme stimuli)
        else :
            nbr_essaie += 1
            nbr_dif += 1 
            pass # event different
    
    else :
        if meme_categorie == 1 :
            if last_type == 1 :
                if repetition == 2 :
                    pass
                else :
                    if categorie == 1 :
                        if last_categorie == 1 :
                            if repetition_categorie == 2 :
                                pass
                            else :
                                pass  # event pareil categorie A
                        else :
                            pass # event pareil categorie A
                    else :
                        if last_categorie == 2 :
                            if repetition_categorie == 2 :
                                pass
                            else :
                                pass # event pareil categorie B
                        else :
                            pass # event pareil categorie B
                
                
        elif meme_categorie == 2 :
            if last_type == 2 :
                if repetition == 2 :
                    pass
            else : 
                pass # event pas pareil commencant par la categorie random

            
    
    
    
    
    
    
    
    
    
    




core.wait(2.0)
core.quit()










