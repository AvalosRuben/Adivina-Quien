from character import Character
import pygame
import characters_images
class Game:
    def __init__(self):
        self.characters= []
        self.create_characters()

    def create_characters(self):
        alex_attributes = {
        "glasses":"no",
        "skin_tone": "light",
        "hair_color": "black",
        "eye_color":"brown",
        "sex":"male",
        "facial_hair": "no",
        "hat":"no"
        }
        alex = Character("alex", alex_attributes)
        self.characters.append(alex)

        alfred_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "orange",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "moustache",
        "hat": "no"
        }
        alfred = Character("Alfred", alfred_attributes)
        self.characters.append(alfred)

        anita_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "female",
        "facial_hair": "no",
        "hat": "no"
        }
        anita = Character("Anita", anita_attributes)
        self.characters.append(anita)

        anne_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "blonde",
        "eye_color": "blue",
        "sex": "female",
        "facial_hair": "no",
        "hat": "no"
        }
        anne = Character("Anne", anne_attributes)
        self.characters.append(anne)

        bernard_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "moustache",
        "hat": "no"
        }
        bernard = Character("Bernard", bernard_attributes)
        self.characters.append(bernard)

        bill_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "orange",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "beard and moustache",
        "hat": "no"
        }
        bill = Character("Bill", bill_attributes)
        self.characters.append(bill)

        charles_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        charles = Character("Charles", charles_attributes)
        self.characters.append(charles)
        
        claire_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "orange",
        "eye_color": "brown",
        "sex": "female",
        "facial_hair": "no",
        "hat": "no"
        }
        claire = Character("Claire", claire_attributes)
        self.characters.append(claire)

        david_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "blonde",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }   
        david = Character("David", david_attributes)
        self.characters.append(david)

        eric_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "blonde",
        "eye_color": "blue",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        eric = Character("Eric", eric_attributes)
        self.characters.append(eric)

        frans_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "red",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "moustache",
        "hat": "no"
        }
        frans = Character("Frans", frans_attributes)
        self.characters.append(frans)

        george_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "white",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "beard and moustache",
        "hat": "no"
        }
        george = Character("George", george_attributes)
        self.characters.append(george)

        herman_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "no hair",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        herman = Character("Herman", herman_attributes)
        self.characters.append(herman)

        joe_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "no hair",
        "eye_color": "blue",
        "sex": "male",
        "facial_hair": "beard and moustache",
        "hat": "no"
        }
        joe = Character("Joe", joe_attributes)
        self.characters.append(joe)

        maria_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "female",
        "facial_hair": "no",
        "hat": "no"
        }
        maria = Character("Maria", maria_attributes)
        self.characters.append(maria)

        max_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "black",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        max = Character("Max", max_attributes)
        self.characters.append(max)

        paul_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "no hair",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        paul = Character("Paul", paul_attributes)
        self.characters.append(paul)

        peter_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "white",
        "eye_color": "blue",
        "sex": "male",
        "facial_hair": "moustache",
        "hat": "no"
        }
        peter = Character("Peter", peter_attributes)
        self.characters.append(peter)

        philip_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "red",
        "eye_color": "blue",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        philip = Character("Philip", philip_attributes)
        self.characters.append(philip)

        richard_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        richard = Character("Richard", richard_attributes)
        self.characters.append(richard)

        robert_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "brown",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "beard and moustache",
        "hat": "no"
        }
        robert = Character("Robert", robert_attributes)
        self.characters.append(robert)

        sam_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "blonde",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "no",
        "hat": "no"
        }
        sam = Character("Sam", sam_attributes)
        self.characters.append(sam)

        susan_attributes = {
        "glasses": "yes",
        "skin_tone": "light",
        "hair_color": "blonde",
        "eye_color": "blue",
        "sex": "female",
        "facial_hair": "no",
        "hat": "no"
        }
        susan = Character("Susan", susan_attributes)
        self.characters.append(susan)

        tom_attributes = {
        "glasses": "no",
        "skin_tone": "light",
        "hair_color": "black",
        "eye_color": "brown",
        "sex": "male",
        "facial_hair": "moustache",
        "hat": "no"
        }
        tom = Character("Tom", tom_attributes)
        self.characters.append(tom)
    
    def draw_board(self,screen):
        screen.fill((131,204,205))
        alex_image = pygame.image.load("characters_images/alex_image.png")
        screen.blit(alex_image,(100,200))
