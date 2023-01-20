import random
import pygame
from sound import SoundManager

#SELMA
class Bonus(pygame.sprite.Sprite):
    # CONSTRUCTEUR 
    def __init__(self, meduse_event): #on demande l'instance de meduse_event
        super().__init__()

        #arguments graphiques
        self.image = pygame.image.load("assets/meduse.png") 
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.soundmanager = SoundManager()

        #constructeurs de base 
        self.rect.x = 550
        self.rect.y = random.randint(0,325)
        self.vitesse = random.randint(7,9)
        self.meduse_event = meduse_event
        self.point = 30
        
    # METHODES
    #retirer meduse de la liste des meduses
    def remove(self):
        self.meduse_event.all_meduses.remove(self)

    #faire avancer les meduses
    def avancer(self):
        self.rect.x -= self.vitesse
        # s'il y a eu pas de collision et donc que meduse est arrivé au bout de l'axe x, je la supprime
        if self.rect.x == 0 : 
            self.remove()
           
        # s'il y a collision avec le joueur on rajoute 30 points
        if self.meduse_event.jeu.check_collision(self, self.meduse_event.jeu.all_players):
            self.meduse_event.jeu.add_score(self.point)
            self.soundmanager.play('meduse_collistion')
            #et ensuite je la retire
            self.remove()

