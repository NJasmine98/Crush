import pygame


class SoundManager:
    def __init__(self):
        # contient tout les effets sonore
        self.sounds = {
            "meduse_collistion" : pygame.mixer.Sound("assets/sounds/meduse_collistion.wav"),
            "game_over" : pygame.mixer.Sound("assets/sounds/game_over.wav")
        } 


# permet de jouer le son qui a le bon nom "dictionnaire = clé-valeur" ici name = clé

    def play(self, name):
        self.sounds[name].play()
