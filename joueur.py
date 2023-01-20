import pygame

#THOMAS

class Joueur(pygame.sprite.Sprite):
    # CONSTRUCTEUR
    def __init__(self, jeu): #on demande l'instance de jeu 
        super().__init__()
        #arguments graphiques 
        self.image = pygame.image.load("assets/tortue.png")
        self.rect = self.image.get_rect() #rect est une forme à 4 cotés dont on souhaite récuperer les coordonnées et déplacer
        self.all_players = pygame.sprite.Group()
        #constructeurs de base
        self.jeu = jeu
        self.vie = 1
        self.vie_max = 1
        self.vitesse = 7
        self.rect.y = 325 #valeur en partant du haut de l'écran
        
    # METHODES

    #le joueur peut mourir
    def meurt(self, degat):
        self.vie -= degat
        return True
        
    #le joueur peut monter
    def monter(self):
        #si le joueur n'est pas en collision on peut se deplacer
        if not self.jeu.check_collision(self, self.jeu.all_objets): #on compare que le joueur entre en collision avec le groupe d'obstacles
            self.rect.y = self.rect.y - self.vitesse
        

    #le joueur peut desencdre
    def descendre(self):
        #si le joueur n'est pas en collision on peut se deplacer
        if not self.jeu.check_collision(self, self.jeu.all_objets): 
            self.rect.y = self.rect.y + self.vitesse
            

