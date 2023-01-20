import random
import pygame
from sound import SoundManager

#JASMINE
class Obstacle(pygame.sprite.Sprite):
    # CONSTRUCTEUR
    def __init__(self, jeu):
        super().__init__()
        #arguments graphiques
        self.image = pygame.image.load("assets/plastique.png")
        self.rect = self.image.get_rect()
        self.soundmanager = SoundManager()
        #constructeurs de base 
        self.jeu = jeu
        self.rect.x = 550
        self.rect.y = random.randint(0,325)
        self.vitesse = random.randint(7,9)
        self.degat = 1
        

    # METHODES

    # faire avacer les obstacles
    def avancer(self):
        #le daplacement peut continuer à se faire que s'il n'y a pas de collision avec le joueur
        if not self.jeu.check_collision(self, self.jeu.all_players):
            self.rect.x -= self.vitesse #on met un - pr qu'il avance vers la gauche
            #si l'objet a passé 0 (et donc réussi à traverser sans collison)
            if self.rect.x <= 0:
                #on le replace au bout de l'axe des x pour qu"il recommence (et donc pour en créer à l'infini)
                self.rect.x = 550
                self.rect.y = random.randint(0,325)
                #et on ajoute un point au score
                self.jeu.add_score(1)

        else:
            # si collision, jeu terminé
            self.jeu.game_over()
            self.soundmanager.play('game_over')
