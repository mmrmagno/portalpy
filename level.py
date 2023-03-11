import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from player import Player
from portals import Blue_Portal, Orange_Portal

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.blue_portal = pygame.sprite.GroupSingle()
        self.orange_portal = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
          for col_index,cell in enumerate(row):
            x = col_index * tile_size
            y = row_index * tile_size

            if cell == "X":
                tile = Tile((x,y), tile_size)
                self.tiles.add(tile)
            if cell == "P":
                player_sprite = Player((x,y))
                self.player.add(player_sprite)
            if cell == "B":
                blue_portal_sprite = Blue_Portal((x,y))
                self.blue_portal.add(blue_portal_sprite)
            if cell == "O":
                orange_portal_sprite = Orange_Portal((x,y))
                self.orange_portal.add(orange_portal_sprite)

    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        if player.direction.y > player.max_speed:
            player.direction.y = player.max_speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def portal_collision(self):
        player = self.player.sprite
        orange_portal = self.orange_portal.sprite
        blue_portal = self.blue_portal.sprite
        
        if blue_portal.rect.colliderect(player.rect):
            # if player.direction.x > 0:    
            player.rect.x = orange_portal.rect.x 
            player.rect.y = orange_portal.rect.y + 8
            # elif player.direction.x < 0:
            #     player.rect.x = orange_portal.rect.x 
            #     player.rect.y = orange_portal.rect.y
            
            # if player.direction.y < 0:
            #     player.rect.x = orange_portal.rect.x
            #     player.rect.y = orange_portal.rect.y
            
            # elif player.direction.y > 0:
            #     player.rect.x = orange_portal.rect.x
            #     player.rect.y = orange_portal.rect.y + 25

        if orange_portal.rect.colliderect(player.rect):
            # if player.direction.x > 0:
            player.rect.x = blue_portal.rect.x
            player.rect.y = blue_portal.rect.y + 8

            # elif player.direction.x < 0:
            #     player.rect.x = blue_portal.rect.x - 30
            #     player.rect.y = blue_portal.rect.y
            
            # if player.direction.y < 0:
            #     player.rect.x = blue_portal.rect.x
            #     player.rect.y = blue_portal.rect.y

            # elif player.direction.y < 0:
            #     player.rect.x = blue_portal.rect.x
            #     player.rect.y = blue_portal.rect.y + 30

    def get_input_map(self):
        keys = pygame.key.get_pressed()
        blue_portal = self.blue_portal.sprite
        orange_portal = self.orange_portal.sprite

        if keys[pygame.K_o]:
            blue_portal.image = pygame.transform.rotate(blue_portal.image, 90)
            orange_portal.image = pygame.transform.rotate(orange_portal.image, 90)

            # blue_portal.image = pygame.image.load("assets/portals/h_blue_portal.png").convert()
            # orange_portal.image = pygame.image.load("assets/portals/h_orange_portal.png").convert()
            
                
                    

    def run(self):

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.blue_portal.update(self.world_shift)
        self.blue_portal.draw(self.display_surface)

        self.orange_portal.update(self.world_shift)
        self.orange_portal.draw(self.display_surface)

        self.scroll_x()
        self.get_input_map()

        self.portal_collision()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)