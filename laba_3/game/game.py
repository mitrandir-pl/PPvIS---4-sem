import pygame
import yaml
import json
import sys
import random
# menus
from game.menu import EndMenu, MainMenu, LeaderboardMenu, HelpMenu
# elements
from elements.paddle import Paddle
from elements.ball import Ball
from elements.blocks import Blocks
from elements.bonus_rect import BonusRect


class GamSettings:

    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    def __init__(self, settings_file: str, game):
        self.game = game
        self.settings = GamSettings.load_settings(settings_file)
        # main controls
        self.load_main_controls()
        # window
        self.laod_window(
            w=self.settings[0]["display_w"],
            h=self.settings[0]["display_h"],
            caption=self.settings[1]["caption"],
            icon=self.settings[1]["icon"],
            background=self.settings[1]["background"]
        )
        # game time
        self.load_game_time(fps=self.settings[0]["fps"])
        # menus
        self.load_menus()
        # fonts
        self.load_fonts()
        # elements
        self.load_elements(
            paddle_speed=self.settings[0]["paddle_speed"],
            ball_speed=self.settings[0]["ball_speed"],
        )
        # sounds
        self.load_sounds(
            self.settings[2]["bad_bonus_sound"],
            self.settings[2]["good_bonus_sound"],
            self.settings[2]["end_or_next_sound"],
            self.settings[2]["ball_block_sound"],
            self.settings[2]["paddle_sound"],
            self.settings[2]["gray_block_sound"]
        )
        # level
        self.load_level()

    @staticmethod
    def load_settings(sfile: str):
        try:
            with open(sfile, 'r') as f:
                settings = json.load(f)
        except Exception as e:
            print(e.__str__())
            print("Error to open file!")
        return settings

    def load_main_controls(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def laod_window(self, w, h, caption, icon, background):
        self.DISPLAY_W, self.DISPLAY_H = w, h
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.SCALED)
        self.caption = pygame.display.set_caption(caption)
        self.icon = pygame.display.set_icon(pygame.image.load(icon))
        self.background = pygame.image.load(background)

    def load_game_time(self, fps):
        self.clock = pygame.time.Clock()
        self.FPS = fps

    def load_level(self):
        try:
            self.level = int(sys.argv[1])
        except IndexError as ie:
            self.level = 1

    def load_menus(self):
        self.main_menu = MainMenu(self)
        self.leaderboard = LeaderboardMenu(self, max_leaders=10)
        self.help = HelpMenu(self)
        self.end = EndMenu(self)
        self.curr_menu = self.main_menu

    def load_elements(self, paddle_speed, ball_speed):
        self.paddle = Paddle(WIDTH=self.DISPLAY_W, HEIGHT=self.DISPLAY_H, paddle_speed=paddle_speed)
        self.ball = Ball(WIDTH=self.DISPLAY_W, HEIGHT=self.DISPLAY_H, ball_speed=ball_speed)
        self.blocks = None
        self.score = 0

    def load_fonts(self):
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.font_end = pygame.font.SysFont('Arial', 40, bold=True)
        self.font_score = pygame.font.SysFont('Arial', 20, bold=True)

    def load_sounds(self, *sounds):
        self.bad_bonus_sound = pygame.mixer.Sound(sounds[0])
        self.good_bonus_sound = pygame.mixer.Sound(sounds[1])
        self.end_or_next_sound = pygame.mixer.Sound(sounds[2])
        self.ball_block_sound = pygame.mixer.Sound(sounds[3])
        self.paddle_sound = pygame.mixer.Sound(sounds[4])
        self.gray_block_sound = pygame.mixer.Sound(sounds[5])


class Game:

    __bonuses = {
        '2': ['up_score', 'up_paddle_size'],
        '3': ['up_ball_speed', 'down_paddle_size', 'make_blocks_line'],
    }

    def __init__(self, settings_file: str):
        self.settings = GamSettings(settings_file, self)

    def draw_game_style(self):
        self.settings.display.fill(self.settings.BLACK)
        self.settings.display.blit(self.settings.background, (0, 0))
        self.draw_level(path=str(self.settings.level)+'.yaml')
        pygame.draw.rect(self.settings.display, pygame.Color("blue"), self.settings.paddle.figure)
        pygame.draw.circle(self.settings.display, pygame.Color("white"), self.settings.ball.figure.center, self.settings.ball.radius)
        # show score
        render_score = self.settings.font_score.render(f'SCORE: {self.settings.score}', 1, pygame.Color('orange'))
        self.settings.display.blit(render_score, (5, 5))

    def win_or_game_over(self):
        if self.settings.ball.figure.bottom > self.settings.DISPLAY_H:
            self.close_game(score=self.settings.score, end_label='GAME OVER', end_color="red")
        elif not len(self.settings.blocks.block_list):
            self.settings.blocks = None
            if self.settings.level < 10:
                self.settings.level += 1
                self.draw_level(path=str(self.settings.level)+'.yaml')
                self.settings.paddle = Paddle(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
                self.settings.ball = Ball(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
            else:
                self.close_game(score=self.settings.score, end_label='YOU WIN!', end_color="green")

    def ball_moving(self):
        self.settings.ball.figure.x += self.settings.ball.speed * self.settings.ball.dx
        self.settings.ball.figure.y += self.settings.ball.speed * self.settings.ball.dy
        # collsion left right
        if self.settings.ball.figure.centerx < self.settings.ball.radius or self.settings.ball.figure.centerx > self.settings.DISPLAY_W - self.settings.ball.radius:
            self.settings.ball.dx = -self.settings.ball.dx
        # collision center
        if self.settings.ball.figure.centery < self.settings.ball.radius:
            self.settings.ball.dy = -self.settings.ball.dy
        # collision paddle
        if self.settings.ball.figure.colliderect(self.settings.paddle.figure) and self.settings.ball.dy > 0:
            self.settings.paddle_sound.play()
            self.settings.ball.dx, self.settings.ball.dy = Game.detect_collision(self.settings.ball.dx, self.settings.ball.dy, self.settings.ball.figure, self.settings.paddle.figure)

    def collision_blocks(self):
        for block in self.settings.blocks.block_list[:]:
            if block == 0:
                self.settings.blocks.block_list.remove(0)

        hit_index = self.settings.ball.figure.collidelist(self.settings.blocks.block_list)
        if hit_index != -1:
            bonus_index = self.settings.blocks.block_list[hit_index].bonus_index
            if bonus_index in ['2', '3']:
                if bonus_index == '2':
                    self.settings.good_bonus_sound.play()
                else:
                    self.settings.bad_bonus_sound.play()
                bonus = self.settings.blocks.block_list[hit_index].bonus_index
                self.apply_bonus(bonus_index=bonus)
            elif bonus_index != '4':
                self.settings.ball_block_sound.play()
            else:
                self.settings.gray_block_sound.play()
            hit_rect = self.settings.blocks.block_list.pop(hit_index)
            hit_color = self.settings.blocks.color_list.pop(hit_index)
            self.settings.ball.dx, self.settings.ball.dy = self.detect_collision(self.settings.ball.dx, self.settings.ball.dy, self.settings.ball.figure, hit_rect)
            # special effect
            hit_rect.inflate_ip(self.settings.ball.figure.width * 3, self.settings.ball.figure.height * 3)
            pygame.draw.rect(self.settings.display, hit_color, hit_rect)
            if bonus_index != '4':
                self.settings.score += 1
            self.settings.ball.speed += 0.1
            self.settings.paddle.speed += 0.1

    def see_controls(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.settings.paddle.figure.left > 0:
            self.settings.paddle.figure.left -= self.settings.paddle.speed
        if key[pygame.K_RIGHT] and self.settings.paddle.figure.right < self.settings.DISPLAY_W:
            self.settings.paddle.figure.right += self.settings.paddle.speed

        if self.settings.START_KEY:
            self.settings.playing = False

    def update_game_screen(self):
        self.settings.window.blit(self.settings.display, (0, 0))
        pygame.display.update()
        self.settings.clock.tick(self.settings.FPS)

    def game_loop(self):
        while self.settings.playing:
            self.check_events()
            self.draw_game_style()
            # win, game over
            self.win_or_game_over()
            # ball movement
            self.ball_moving()
            # collision blocks
            self.collision_blocks()
            # control
            self.see_controls()
            # update screen
            self.update_game_screen()
            self.reset_keys()

    def apply_bonus(self, bonus_index):
        bonus = random.choice(Game.__bonuses[bonus_index])
        print(bonus)
        if bonus == 'up_score':
            self.up_score(plus=10)
        elif bonus == 'up_ball_speed':
            self.up_ball_speed()
        elif bonus == 'down_paddle_size':
            self.down_paddle_size()
        elif bonus == 'up_paddle_size':
            self.up_paddle_size()
        elif bonus == 'make_blocks_line':
            self.make_blocks_line()

    def up_score(self, plus):
        self.settings.score += plus

    def up_ball_speed(self):
        self.settings.ball = Ball(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H, ball_radius=10-10//2, ball_xy=(self.settings.ball.figure.centerx, self.settings.ball.figure.centery))
        self.settings.ball.speed += self.settings.ball.speed//2

    def down_paddle_size(self):
        self.settings.paddle = Paddle(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H, paddle_w=140-140//2, paddle_h=16-16//2, paddle_xy=(self.settings.paddle.figure.centerx, self.settings.paddle.figure.centery))
        self.settings.paddle.speed += self.settings.paddle.speed//2

    def up_paddle_size(self):
        self.settings.paddle = Paddle(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H, paddle_w=140+140//2, paddle_xy=(self.settings.paddle.figure.centerx, self.settings.paddle.figure.centery))

    def make_blocks_line(self):
        for j in range(self.settings.blocks.blocks_in_line):
            block = BonusRect(15 + 52 * j, 50 + 22 * 10, int(self.settings.blocks.sizes[0]), int(self.settings.blocks.sizes[1]), bonus_index='4')
            # blocks_line.append(block)
            self.settings.blocks.block_list.append(block)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.running, self.settings.playing = False, False
                exit()

            if event.type == pygame.KEYDOWN:
                if not self.settings.playing:
                    if event.key == pygame.K_BACKSPACE:
                        self.settings.end.user_text = self.settings.end.user_text[:-1]
                    else:
                        self.settings.end.user_text += event.unicode
                    # new game
                    self.settings.paddle = Paddle(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
                    self.settings.ball = Ball(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
                    self.settings.score = 0
                    self.generate_level(path=f"{self.settings.level}.yaml")

                if event.key == pygame.K_RETURN:
                    self.settings.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.settings.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.settings.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.settings.UP_KEY = True

    def reset_keys(self):
        self.settings.UP_KEY, self.settings.DOWN_KEY, self.settings.START_KEY, self.settings.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, color, x, y, font='8bit_wonder/8-BIT WONDER.TTF'):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, pygame.Color(color))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.settings.display.blit(text_surface, text_rect)

    def draw_level(self, path: str):
        # drawing world
        if not self.settings.blocks:
            self.generate_level(path=path)
        draw_rects = []
        for color, block in enumerate(self.settings.blocks.block_list):
            if block != 0:
                if block.bonus_index == '1':  # neutral
                    bl = pygame.draw.rect(self.settings.display, self.settings.blocks.color_list[color], block)
                elif block.bonus_index == '2':  # good
                    bl = pygame.draw.rect(self.settings.display, (0, 255, 0), block)
                elif block.bonus_index == '3':  # bad
                    bl = pygame.draw.rect(self.settings.display, (255, 0, 0), block)
                elif block.bonus_index == '4':  # bonus
                    bl = pygame.draw.rect(self.settings.display, (80, 80, 80), block)
                draw_rects.append(bl)

    def generate_level(self, path: str):
        with open("levels/"+path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        sizes = data['size']
        data = data['blocks']
        for i in range(len(data)):
            data[i] = data[i].split()
        # print(data)
        self.settings.blocks = Blocks(data, sizes)

    @staticmethod
    def detect_collision(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    def close_game(self, score: int, end_label: str, end_color: str, score_label: str = "SCORE: ", score_color: str = "orange"):
        pygame.mouse.set_visible(True)
        self.settings.end_or_next_sound.play()
        self.settings.end = EndMenu(self.settings)
        self.settings.curr_menu = self.settings.end
        self.settings.playing = False
        self.settings.curr_menu.display_menu(score, end_label, end_color)
