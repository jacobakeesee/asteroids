import pygame

def show_score(x, y, score, font, screen):
    score_text = font.render("Score: " + str(score), True, "White")
    screen.blit(score_text, (x,y))
