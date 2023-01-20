#CODE REALISE PAR SELMA, THOMAS ET JASMINE

from joueur import Joueur
from obstacle import Obstacle 
from bonus_event import BonusEvent
import pygame


class Jeu(): #JASMINE
    def __init__(self):

        self.is_playing = False # permet de verifier si le jeu est lancer ou pas.

        ### On génère le joueur
        self.tortue = Joueur(self) #on met self pour lui donner accès à l'instance de la classe Jeu 
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.tortue)
        self.pressed = {} #dictionnaire vide pour que quand touche appuyée, clé = True, et quand touche pas appuyée, clé = False
        self.score = 0
       
        ### On génère les obstacles (plastique)
        self.all_objets = pygame.sprite.Group()

        ### On génère les bonus (méduse)
        self.meduse_event = BonusEvent(self)

        
        

#THOMAS
# Au démarrage du jeu, on fait spawn les objets
    def start(self):
        self.is_playing = True
        self.spawn_objet()
        self.spawn_objet()

# Ajout de points 
    def add_score(self, point):
        self.score += point

#apparition des obstacles 
    def spawn_objet(self):
        plastique = Obstacle(self) #on lui passe aussi l'instance de Jeu 
        self.all_objets.add(plastique) #je viens ajouter mon objet à mon groupe d'obstacles

# Verification des colllisons
    def check_collision(self, joueur, objet): #check collision entre groupe de joueur et groupe d'oibstacle
        return pygame.sprite.spritecollide(joueur, objet, False, pygame.sprite.collide_mask)


#SELMA
#Fin du jeu
    def game_over(self):
        # remettre le jeu à neuf : 
        # retirer les obstacles de la liste
        self.all_objets = pygame.sprite.Group()
        # remettre la vie au joueur 
        self.tortue.vie = self.tortue.vie_max 
        # remettre le score à 0
        self.score = 0
        # remettre la jauge des bonus à 0
        self.meduse_event.reset_percent()
        # remettre le jeu au menu 
        self.is_playing = False


    def update(self, screen):
        
        # afficher le score sur l'écran
        font = pygame.font.SysFont("monospance", 25, bold=True) # la police de mon score
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0)) # permet d'afficher mon score toujours avec la même police et s'actuliser au fur et a mesure et le (000) == a la couleur black
        screen.blit(score_text, (20,20))
        screen.blit(self.tortue.image, self.tortue.rect)

        # actualiser la barre d'evenement du jeu : 
        self.meduse_event.update_bar(screen)


        #verifier si le joueur souhaite aller en haut ou en bas
        #si la touche préssée est flèche du haut et que la tortue ne se trouve déjà pas tout en haut
        if self.pressed.get(pygame.K_UP) and self.tortue.rect.y > 0 :
            self.tortue.monter() #on monte
        #si la touche préssée est flèche du bas et que la tortue ne se trouve déjà pas tout en bas
        elif self.pressed.get(pygame.K_DOWN) and self.tortue.rect.y < 325:
            self.tortue.descendre() #on descend

        #appliquer l'ensemble des images de mon groupe d'obstacles
        self.all_objets.draw(screen)
        
        #appliquer l'ensemble des images de mon groupe de meduse
        self.meduse_event.all_meduses.draw(screen)

        #récuperer les obstacles de notre jeu
        for plastique in self.all_objets:
            plastique.avancer() #pour que ca fasse le déplacement de l'ensemble des obstacles    

        for meduse in self.meduse_event.all_meduses:
            meduse.avancer()
