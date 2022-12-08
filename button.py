import pygame
import random

class Fontbtn():
    def __init__(self, x, y, image, scale):
        self.width = int(image.get_width() * scale)
        self.height = int(image.get_height() * scale)
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface, font, text):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        msg = font.render(text, True, (0, 0, 0))
        msg_rect = msg.get_rect(center = (int(self.rect.x + self.width/2), int(self.rect.y + self.height/2)))
        surface.blit(msg, msg_rect)

        return action

class Subbtn():
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width*scale), int(self.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface, font, text, sfont, stext, height):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        msg = font.render(text, True, (0, 0, 0))
        msg_rect = msg.get_rect(center = (int(self.rect.x + self.width/2), int(self.rect.y + self.height/2)))
        surface.blit(msg, msg_rect)

        smsg = sfont.render(stext, True, (0, 0, 0))
        smsg_rect = smsg.get_rect(center = (int(self.rect.x + self.width/2), int(self.rect.y + self.height/2 + height)))
        surface.blit(smsg, smsg_rect)

        return action

class Checkbtn():
    def __init__(self, x, y, image, scale, length):
        self.width = int(image.get_width() * scale)
        self.height = int(image.get_height() * scale)
        self.length = length
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x + 330 + 60 * (len(length) - 6), y -5)
        self.clicked = False

    def draw(self, surface, font, text):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        msg = font.render(text, True, (0, 0, 0))
        surface.blit(msg, (self.rect.x - (330 + 60 * (len(self.length) - 6)), self.rect.y + 5))

        return action

class Randbtn():
    def __init__(self, x, y, image):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface, font, text, sfont, stext, height):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        msg = font.render(text, True, (0, 0, 0))
        msg_rect = msg.get_rect(center = (int(self.rect.x + self.width/2), int(self.rect.y + self.height/2)))
        surface.blit(msg, msg_rect)

        smsg = sfont.render(stext, True, (0, 0, 0))
        smsg_rect = smsg.get_rect(center = (int(self.rect.x + self.width/2), int(self.rect.y + self.height/2 + height)))
        surface.blit(smsg, smsg_rect)

        return action