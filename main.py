import pygame as pg
import spritesheet
import random
import questions

pg.init()
screen_w, screen_h = 900, 600
screen = pg.display.set_mode((screen_w, screen_h))
pg.display.set_caption("Quiz")

pygame_icon = pg.image.load('./img/dauphin.png')
pg.display.set_icon(pygame_icon)

spr_dauphin = pg.image.load('./img/dauphin.png').convert_alpha()
spr_sand = pg.image.load('./img/sand.png').convert_alpha()
spr_rocks = pg.image.load('./img/rocks.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(spr_dauphin)
char_speed = 5

factor = 3
w, h = spr_dauphin.get_size()
image = pg.transform.scale(spr_dauphin, (w * factor, h * factor))
s_w, s_h = spr_sand.get_size()
sand = pg.transform.scale(spr_sand, (s_w * factor, s_h * factor))
r_w, r_h = spr_rocks.get_size()
rocks = pg.transform.scale(spr_rocks, (r_w * factor, r_h * factor))

color = (25, 171, 255)

menu_bg = pg.image.load("./img/menu_bg.png").convert()
mb_w, mb_h = menu_bg.get_size()
scale_factor = screen_h / mb_h
menu_bg = pg.transform.scale(menu_bg, (int(mb_w * scale_factor), screen_h))
menu_bg_w, menu_bg_h = menu_bg.get_size()

play_button = pg.image.load("./img/play_button.png").convert_alpha()
play_button_pressed = pg.image.load("./img/play_button_pressed.png").convert_alpha()
pb_w, pb_h = play_button.get_size()
play_button = pg.transform.scale(play_button, (pb_w * factor, pb_h * factor))
play_button_pressed = pg.transform.scale(play_button_pressed, (pb_w * factor, pb_h * factor))
button_rect = play_button.get_rect(center=(screen_w // 2, screen_h // 2))

answer_button = pg.image.load("./img/answer_button.png").convert_alpha()
answer_button_pressed = pg.image.load("./img/answer_button_pressed.png").convert_alpha()
ab_w, ab_h = answer_button.get_size()
answer_button = pg.transform.scale(answer_button, (ab_w * factor, ab_h * factor))
answer_button_pressed = pg.transform.scale(answer_button_pressed, (ab_w * factor, ab_h * factor))

frame_0 = sprite_sheet.get_image(0, 67, 34, 3)
frame_1 = sprite_sheet.get_image(1, 67, 34, 3)
frame_2 = sprite_sheet.get_image(2, 67, 34, 3)
left_frames = [frame_0, frame_1, frame_0, frame_2]
right_frames = [pg.transform.flip(f, True, False) for f in left_frames]

clock = pg.time.Clock()
FPS = 60

char_x = 100
char_y = screen_h // 2 - h // 2
scroll_offset = 0
frame_index = 0
frame_timer = 0
frame_delay = 10

rock_spacing = 600
rock_positions = []
last_x = 0
for _ in range(10):
    rx = last_x + random.randint(rock_spacing, rock_spacing + 400)
    rock_positions.append(rx)
    last_x = rx

current_question_index = 0
show_question = False
button_states = [False, False, False]
correct_count = 0
wrong_count = 0
distance_traveled = 0
quiz_trigger_distance = random.randint(900, 1200)
quiz_finished = False

font_question = pg.font.Font("./img/Press_Start_2P/PressStart2P-Regular.ttf", 16)
font_counter = pg.font.Font("./img/Press_Start_2P/PressStart2P-Regular.ttf", 12)
text_color = (152, 103, 64)
pressed_color = (156, 118, 79)
question_color = (0, 0, 139)

in_menu = True
running = True
button_down = False

buttons = []
for i in range(3):
    rect = answer_button.get_rect(center=(screen_w - 250, screen_h//2 - 100 + i*150))
    buttons.append(rect)

fade_alpha = 0
current_options = []

def draw_text(surface, text, font, color, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() > max_width and current_line != "":
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test_line
    lines.append(current_line)
    for i, line in enumerate(lines[:2]):  # max 2 lignes
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * font.get_height()))

def draw_quiz():
    global fade_alpha
    q = questions.questions[current_question_index]
    box_width = int(screen_w * 0.7)
    box_x = (screen_w - box_width) // 2
    draw_text(screen, q["text"], font_question, question_color,
              box_x, 50, box_width)
    for i, option in enumerate(current_options):
        rect = buttons[i]
        if button_states[i]:
            btn = answer_button_pressed.copy()
            option_surface = font_question.render(option, True, pressed_color)
            screen.blit(btn, rect)
            screen.blit(option_surface, (rect.centerx - option_surface.get_width()//2,
                                         rect.centery - option_surface.get_height()//2 + 2*factor))
        else:
            btn = answer_button.copy()
            if fade_alpha < 255:
                fade_alpha += 5
            btn.set_alpha(fade_alpha)
            option_surface = font_question.render(option, True, text_color)
            screen.blit(btn, rect)
            screen.blit(option_surface, (rect.centerx - option_surface.get_width()//2,
                                         rect.centery - option_surface.get_height()//2))

while running:
    clock.tick(FPS)
    screen.fill(color)
    keys = pg.key.get_pressed()
    moving = False
    current_frames = right_frames

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if in_menu:
            if event.type == pg.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                button_down = True
            if event.type == pg.MOUSEBUTTONUP:
                if button_down and button_rect.collidepoint(event.pos):
                    in_menu = False
                button_down = False
        elif show_question and not quiz_finished:
            if event.type == pg.MOUSEBUTTONDOWN:
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(event.pos):
                        button_states[i] = True
            if event.type == pg.MOUSEBUTTONUP:
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(event.pos) and button_states[i]:
                        chosen = current_options[i]
                        if chosen == questions.questions[current_question_index]["answer"]:
                            correct_count += 1
                        else:
                            wrong_count += 1
                        current_question_index += 1
                        if current_question_index >= len(questions.questions):
                            quiz_finished = True
                        else:
                            show_question = False
                            button_states = [False, False, False]
                            distance_traveled = 0
                            quiz_trigger_distance = random.randint(900, 1200)
                            fade_alpha = 0

    if in_menu:
        # fond du menu
        for x in range(0, screen_w, menu_bg_w):
            screen.blit(menu_bg, (x, 0))
        if button_down:
            screen.blit(play_button_pressed, button_rect)
        else:
            screen.blit(play_button, button_rect)

    else:
        # déplacement du dauphin
        if not show_question and not quiz_finished:
            if keys[pg.K_LEFT]:
                scroll_offset += char_speed
                distance_traveled += char_speed
                moving = True
                current_frames = left_frames
            if keys[pg.K_RIGHT]:
                scroll_offset -= char_speed
                distance_traveled += char_speed
                moving = True
                current_frames = right_frames
            if keys[pg.K_UP] and char_y > 0:
                char_y -= char_speed
                moving = True
            if keys[pg.K_DOWN] and char_y < screen_h - h:
                char_y += char_speed
                moving = True

            if distance_traveled >= quiz_trigger_distance:
                show_question = True
                current_options = questions.questions[current_question_index]["options"][:]
                random.shuffle(current_options)

        # animation
        if moving:
            frame_timer += 1
            if frame_timer >= frame_delay:
                frame_timer = 0
                frame_index = (frame_index + 1) % len(current_frames)
        else:
            frame_index = 0

        # rochers
        for i, rx in enumerate(rock_positions):
            x = rx + scroll_offset
            if -rocks.get_width() < x < screen_w + rocks.get_width():
                screen.blit(rocks, (x, screen_h - rocks.get_height()))
            if x < -rocks.get_width():
                max_rx = max(rock_positions)
                new_rx = max_rx + random.randint(rock_spacing, rock_spacing + 400)
                rock_positions[i] = new_rx

        # sable
        for x in range(-sand.get_width(), screen_w + sand.get_width(), sand.get_width()):
            screen.blit(sand, (x + scroll_offset % sand.get_width(), screen_h - sand.get_height()))

        # dauphin
        screen.blit(current_frames[frame_index], (char_x, char_y))

        # quiz ou fin
        if show_question and not quiz_finished:
            draw_quiz()
        elif quiz_finished:
            end_surface = font_question.render("Quiz terminé !", True, (0,0,0))
            screen.blit(end_surface, (screen_w//2 - end_surface.get_width()//2,
                                      screen_h//2))

        # compteur
        counter_surface = font_counter.render(f"Correctes: {correct_count} | Faux: {wrong_count}", True, (0,0,0))
        screen.blit(counter_surface, (20, 20))

    pg.display.flip()
