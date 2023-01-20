import pygame
from bonus import Bonus

#SELMA

#creation d'une classe barre/jauge d'evenement meduse (car les meduses n'apparaissent pas tout le temps)
class BonusEvent():
    ## CONSTRUCTEUR
     
    def __init__(self, jeu):
        self.jeu = jeu
        self.pourcentage = 0
        self.pourcentage_vitesse = 20

        # on doit definir un groupe pour verifier la colission et si jamais on veux faire apparaître plusieurs meduses en meme temps
        self.all_meduses = pygame.sprite.Group()

    ## METHODES
    
    # a chaque remplissage, une meduse spawn
    def add_percent(self):
        self.pourcentage += self.pourcentage_vitesse / 100

    def reset_percent(self):
        self.pourcentage = 0

    def bonus_spawn(self):
        self.all_meduses.add(Bonus(self))

    def is_full(self):
        return self.pourcentage >= 100 # si c'est plein alors return True

    def arrivee_meduse(self):
          if self.is_full():
            self.bonus_spawn()
            self.reset_percent()


    def update_bar(self, surface):

        self.arrivee_meduse()
        # ajouter du pourcentage
        self.add_percent()

        # barre noire (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe de X
            surface.get_height() -20 , # axe des y
            surface.get_width(), # longeur de la fenetre
            10 # epaisseur de la barre
        ])

        # barre rose (jauge d'evement)
        pygame.draw.rect(surface, (225, 102, 178), [0,surface.get_height() - 20,(surface.get_width() / 100) * self.pourcentage,10])
