import pygame
import os
import math

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """
        #print(enemy.get_pos())
        x1, y1 = enemy.get_pos()
        x2,y2  = self.center
        dis    = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #print(x1,y1)
        if (dis <= self.radius)  :
            return True
        else:
            return False
        """
        Hint:
        x1, y1 = enemy.get_pos()
        ...
        """
        pass

    def draw_transparent(self, win):
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
       
        # create semi-transparent surface
        transparent_surface = pygame.Surface((1024, 600), pygame.SRCALPHA)
        transparency = 100  # define transparency: 0~255, 0 is fully transparent
        # draw the rectangle on the transparent surface
        pygame.draw.circle(transparent_surface, (128,128,128, transparency),(self.center),self.radius )

        win.blit(transparent_surface, (0,0))
        #pygame.display.update()
        


        pass


class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down (( self.cd_count
        :return: Bool
        """
        if self.cd_count < self.cd_max_count:
            self.cd_count +=1
            return False
        else :
            self.cd_count = 0
            return True
        """
        Hint:
        let counter be 0
        if the counter < max counter then
            set counter to counter + 1
            
        else 
            counter return to zero
        end if
        """
        pass

    def attack(self, enemy_group):
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """
        enemy_index = [] #create list for enemy
        for enemy in enemy_group.get(): #create enemy var in enemy_group.get()
            enemy_index.append(enemy)   # enemy_index add enemy
            #print(enemy)
            if self.is_cool_down():
                if self.range_circle.collide(enemy) and enemy_index[0] == enemy: # judge enemy in circle and enemy_index first equal enemy
                    enemy.get_hurt(self.damage)
        
            
        pass

    def is_clicked(self, x, y):
        """
        Bonus) Return whether the tower is clicked
        (1) If the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        #print(self.rect.top,self.rect.bottom,self.rect.right,self.rect.left,self.rect.topright[0],self.rect.bottomright[1])
        # if tower is  clicked by mouse  
        if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom: # if in rect range
            return True
        else:
            return False
        pass

    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower

