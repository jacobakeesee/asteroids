import pygame

def triangle_hitbox(vector1, vector2):
    t = (pygame.math.Vector2.dot(vector2, vector1)) / (pygame.math.Vector2.dot(vector1, vector1))
    t_clamped = max(0, min(1, t))
    if t_clamped < 0 or t_clamped > 1:
        return False
    else:
        return True
