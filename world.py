import random
import enemies

r = random.random()
class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
                This adventure story game is loosely based on
                an excerpt from the Arabian tales of "The Thousand Nights and a Night"
                
                **********************************************************************
                
                In the times of the great Caliph Harrun ar-Rashid ibn Muhammad al Mahdi,
                lived a man in the city of Baghdad, and his name was Sinbad.
                
                One day Sinbad decided to explore the far lands beyond the realm,
                and upon the blessing of the Caliph, he joined a merchant ship.
                
                They sailed for a fortnight without land on sight,
                until they reached a barren yet magical island...
                
                Sinbad, excited by the place, had decided to set foot on it
                and looked at the palm trees and on the peculiar animals
                so he ventured for hours and hours...
                
                On his way back to the ship, he saw it is afar in sea
                "No! Come Back! Don't Leave Me Here!" He cried.
                
                As he gazed on the ship sailing away, 
                Sinbad understood he was alone on this island
                and that he must find a way to get out, but how?
               """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.4:
            self.enemy = enemies.Looter()
            self.alive_text = "A gold mugging looter is chasing you " \
                              "be prepared to attack!"
            self.dead_text = "The looter lies dead in his own blood"
        elif r < 0.7:
            self.enemy = enemies.Pirate()
            self.alive_text = "A bloodthirsty pirate " \
                              "ready to enslave you if you won't act fast!"
            self.dead_text = "Another low life found its end by your arms"
        elif r < 0.95:
            self.enemy = enemies.Ghoul()
            self.alive_text = "A Ghoul? Yes it is! " \
                              "Don't let Terror into your heart, Fight!"
            self.dead_text = "Allah be praised! the Ghoul withdrew back to Jahanam!"
        else:
            self.enemy = enemies.Jinn()
            self.alive_text = "A Jinn upon you! " \
                              "I seek refuge in Allah from the damned Devil!"
            self.dead_text = "The Jinn has been cast back to the Shadows! God is Great!"
        super().__init__(x,y)

    def intro_text(self):
        if self.enemy.is_alive():
            return self.alive_text
        else:
            return self.dead_text

        '''
        if self.enemy.is_alive():
            if r < 0.5:
                return "A {} awaits!".format(self.enemy.name)
            else:
                return "Out of nowhere A {} appeared. Be ready to fight!".format(self.enemy.name)
        else:
            return "Sinbad defeated the {}.".format(self.enemy.name)
        '''

    def modify_player(self, player):
        if self.enemy.is_alive:
            player.hp -= self.enemy.damage
            print("Enemy does {} damage. you have {} HP remaining.".format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        
                And the Roc grabbed Sinbad and flew far away into the skies...
                Alas, don't fear for our Sinbad! For this is not his end nor the end of his voyages,
                because Sharzhad still has many nights to recount the rest of his fabulous adventures...
        
        
        
                To Be Continued...
                
               """

world_map = [
             [None, VictoryTile(1,0), None],
             [None, EnemyTile(1,1), None],
             [EnemyTile(0,2), StartTile(1,2), EnemyTile(2,2)],
             [None,EnemyTile(1,3), None]
             ]

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None