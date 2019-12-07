import numpy as np
import matplotlib.pyplot as plt
import random



##combinaison de point pour qui l'algo fonctionne bien

point_x = [2,0,4,6,7]
point_y = [0,4,4,0,2]

##


##Combinaison de point pour qui l'ago ne fonctionne pas (erreur de division par 0)

#point_x = [14, 7, 17, 18, 3, 20, 12, 1, 9]
#point_y = [12, 4, 2, 13, 6, 18, 5, 3, 11]

##

##à utiliser pour générer des points aléatoirement

# for i in range(10):
#     rand1 = random.randint(0,20)
#     rand2 = random.randint(0,20)
#     
#     if not(rand1 in point_x):
#         point_y += [rand2]
#         point_x += [rand1]
# 
# print(point_x)
# print(point_y)


def middle_point(point_x,point_y,t):
    
    if len(point_x) == 1:
        return point_x,point_y #Quand on a trouvé l'unique point d'où l'on peut tracer la courbe
    point_x_new = []
    point_y_new = []
    
    for i in range(len(point_x)-1): #on parcourt tous les points par paire pour pouvoir calculer la position du nouveau point entre les 2
        
        #calcul de la position x du point qui est à la distance (d = distance totale) égale à d*t entre les 2 points i et i+1
        point_x_new += [point_x[i]+(point_x[i+1]-point_x[i])*t] 
        
        #calcul de la position y du point qui est à la distance (d = distance totale) égale à d*t entre les 2 points i et i+1
        point_y_new += [(point_y[i+1]-point_y[i])/(point_x[i+1]-point_x[i])*(t*(point_x[i+1]-point_x[i]))+point_y[i]] 
    

    return middle_point(point_x_new,point_y_new,t) #appel récursif de la fonction pour calculer les points suivants en fonction des points calculés


x_list = []
y_list = []



for i in range(0,1000): #on calcule juste pour plein de points pour afficher sur le graphique et oui j'aurais pu utiliser le linspace de numpy (enfin je pense)
    x,y = middle_point(point_x,point_y,i/1000)
    x_list += [x]
    y_list += [y]



min_list = min([min(point_x),min(point_y)]) #on cherche le min et le max entre les 2 listes pour savoir quelle limite donner aux axes du graphique
max_list = max([max(point_x),max(point_y)])


plt.xlim(min_list,max_list)
plt.ylim(min_list,max_list)


plt.plot(x_list,y_list) #on affiche la belle courbe
plt.plot(point_x,point_y) #on affiche la courbe "brute" faite entre les points
plt.show() #on affiche le graphique

print("ok") #pour dire que tout va bien !
