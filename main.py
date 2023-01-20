#CODE REALISE PAR SELMA, THOMAS ET JASMINE

from jeu import Jeu
import pygame 

#JASMINE

# clock utilisé pour les FPS
clock = pygame.time.Clock()
FPS = 60 # en majuscule car variable constante (variable qui change pas)

pygame.init()

# création de la fenêtre de notre jeu. 
pygame.display.set_caption("Tortue Game") # titre de la fenêtre
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
screen = pygame.display.set_mode((600,400))  # Largeur et hauteur --> envoie une surface qu'on récupère

background = pygame.image.load("assets/bg.jpg")

# importer notre bannière 
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (200,200)) # permet redimensionner notre image
banner_rect = banner.get_rect() # on recupère le rectange de notre image
banner_rect.x = screen.get_width() / 3
banner_rect.y = 70

# importer notre boutton play ! 

button = pygame.image.load("assets/button.png")
button = pygame.transform.scale(button, (200,100))
button_rect = button.get_rect()
button_rect.x = screen.get_width() / 3
button_rect.y = 220

#THOMAS
jeu = Jeu()
actif = True
while actif : #tant que le jeu est actif, et tout mon code va se passer dans cette boucle
    #appliquer l'arrière plan du jeu (ma fenetre)
    screen.blit(background, (0,0)) #blit injecte l'image. #longueur, hauteur

    # verifier si le jeu a commencer ou non 

    if jeu.is_playing == True:
        # on va lancer notre jeu 
        jeu.update(screen)

    # verifier si le jeu n'a pas commence : 
    else: 
        # on va afficher notre menu dans ce cas
        screen.blit(banner, banner_rect)
        screen.blit(button, button_rect)


    #mettre à jour l'écran 
    pygame.display.flip()


    #SELMA
    #Boucle pour les évènements possibles 
    for event in pygame.event.get():
        #condition de sortie du jeu = évèneent joueur ferme fenetre
        if event.type == pygame.QUIT: #si l'évènement est quitter ou que je n'ai plus de point de vie
            actif = False #on n'est plus actif
            pygame.quit() #on quitte l'application jeu
            print("fermeture jeu")
        elif event.type == pygame.KEYDOWN: #si l'évènement en court est une touche du clavier
            jeu.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si le clique de la souris est en collision avec le bouton jouer
            if button_rect.collidepoint(event.pos) and jeu.is_playing == False: # Si cette condition est vrai ça veut dire qu'on a cliqué sur le rectangle de l'image du bouton play et donc qu'on veut jouer 
                # on lancer le jeu 
                jeu.start() # je lance mon jeu et je fais apparaître mes objets


    

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)
                
