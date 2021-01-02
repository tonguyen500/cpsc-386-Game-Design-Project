import pygame
import random
import math
import Card

from pygame import mixer
import os

os.environ['SDL_AUDIODRIVER'] = 'alsa'
# Initialize the pygame

pygame.init()
mixer.init()
pygame.mixer.get_init()

# create the screen
WIDTH = 1000
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#
# Background
background = pygame.image.load('bkg.jpg')
background = pygame.transform.scale(background, (1000, 800))


#
# Title and Icon
pygame.display.set_caption("Too Many Cats")
# icon = pygame.image.load('spaceship.png')
# pygame.display.set_icon(icon)

# Create Deck
deck = Card.Deck()
deck.shuffle()
# deck.show()
# card = deck.draw()
# card.show()

# Init Player 1 and deal cards
player1 = Card.Player("Player1")
handnum = 8
for x in range(handnum):
    player1.draw(deck)
player1.showHand()
print("^^ player1 beginning")

# Init Player 2 and deal cards
player2 = Card.Player("Player2")
for x in range(handnum):
    player2.draw(deck)
player2.showHand()
print("^^ player2 beginning")
# deck.show()

# Init Discard Pile
discard_pile = Card.Player("Discard")
discard_pile.draw(deck)
discard_pile.showHand()
print("^^ discard beginning")

# Init Discard  Temp Pile
discard_temp_pile = Card.Player("Discard")

# Score
font = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.match_font('arial')

textX1 = 650
textY1 = 400

textX2 = 650
textY2 = 10

textX3 = 400
textY3 = 200

textX4 = 505
textY4 = 200

textX5 = 800
textY5 = 200
#
# Gamer over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
over_text = over_font.render("Game Over ", True, (255, 255, 255))


def show_score_player1(x, y):
    # render then blit
    score = font.render("Score Player 1: " + str(total_score_player1), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_score_player2(x, y):
    # render then blit
    score = font.render("Score Player 2: " + str(total_score_player2), True, (255, 255, 255))
    screen.blit(score, (x, y))


def deck_label(x, y):
    # render then blit
    label = font.render("Deck", True, (255, 255, 255))
    screen.blit(label, (x, y))

def discard_pile_label(x, y):
    # render then blit
    label = font.render("Discard Pile " , True, (255, 255, 255))
    screen.blit(label, (x, y))

def tonks_label(x, y):
    # render then blit
    label = font.render("Declare Tonks!!" , True, (255, 255, 255))
    screen.blit(label, (x, y))

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font2, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Cardhand(pygame.sprite.Sprite):
    def __init__(self, image_name):
        # parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # load image
        self.name = image_name
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image, (100, 150))
        #         set transparent color
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

    def handleEvent(self, event, pos):
        # pos is the mouse postion or tuple in x,y coords
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pos):
                    if self.name == "Beard Cat.jpg":
                        return "Beard Cat"
                    if self.name == "Watermelon Cat.jpg":
                        return "Watermelon Cat"
                    if self.name == "Potato Cat.jpg":
                        return "Potato Cat"
                    if self.name == "Rainbow Cat.jpg":
                        return "Rainbow Cat"
                    if self.name == "Taco Cat.jpg":
                        return "Taco Cat"
                    if self.name == "Grumpy Cat.jpg":
                        return "Grumpy Cat"
                    if self.name == "Deck.jpg":
                        return "Deck"


hand_player1_list = pygame.sprite.Group()
hand_player2_list = pygame.sprite.Group()
deck_list = pygame.sprite.Group()
discard_pile_list = pygame.sprite.Group()
tonks_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Player 1 Card 1
button = Cardhand(player1.hand[0].img)
button.rect.x = 50
button.rect.y = 425
hand_player1_list.add(button)

# Player 1 Card 2
button2 = Cardhand(player1.hand[1].img)
button2.rect.x = 175
button2.rect.y = 425
hand_player1_list.add(button2)

# Player 1 Card 3
button3 = Cardhand(player1.hand[2].img)
button3.rect.x = 300
button3.rect.y = 425
hand_player1_list.add(button3)

# Player 1 Card 4
button4 = Cardhand(player1.hand[3].img)
button4.rect.x = 425
button4.rect.y = 425
hand_player1_list.add(button4)

# Player 1 Card 5
button5 = Cardhand(player1.hand[4].img)
button5.rect.x = 550
button5.rect.y = 425
hand_player1_list.add(button5)

# Player 1 Card 6
button6 = Cardhand(player1.hand[5].img)
button6.rect.x = 675
button6.rect.y = 425
hand_player1_list.add(button6)

# Player 1 Card 7
button7 = Cardhand(player1.hand[6].img)
button7.rect.x = 800
button7.rect.y = 425
hand_player1_list.add(button7)

# Player 2 Card 1
buttontwo = Cardhand(player2.hand[0].img)
buttontwo.rect.x = 50
buttontwo.rect.y = 25
hand_player2_list.add(buttontwo)

# Player 2 Card 2
buttontwo2 = Cardhand(player2.hand[1].img)
buttontwo2.rect.x = 175
buttontwo2.rect.y = 25
hand_player2_list.add(buttontwo2)

# Player 2 Card 3
buttontwo3 = Cardhand(player2.hand[2].img)
buttontwo3.rect.x = 300
buttontwo3.rect.y = 25
hand_player2_list.add(buttontwo3)

# Player 2 Card 4
buttontwo4 = Cardhand(player2.hand[3].img)
buttontwo4.rect.x = 425
buttontwo4.rect.y = 25
hand_player2_list.add(buttontwo4)

# Player 2 Card 5
buttontwo5 = Cardhand(player2.hand[4].img)
buttontwo5.rect.x = 550
buttontwo5.rect.y = 25
hand_player2_list.add(buttontwo5)

# Player 2 Card 6
buttontwo6 = Cardhand(player2.hand[5].img)
buttontwo6.rect.x = 675
buttontwo6.rect.y = 25
hand_player2_list.add(buttontwo6)

# Player 2 Card 7
buttontwo7 = Cardhand(player2.hand[6].img)
buttontwo7.rect.x = 800
buttontwo7.rect.y = 25
hand_player2_list.add(buttontwo7)

# Discard Pile
discard_top = Cardhand(discard_pile.hand[0].img)
discard_top.rect.x = 500
discard_top.rect.y = 230
discard_pile_list.add(discard_top)

# Deck Pile
deck_pile = Cardhand("Deck.jpg")
deck_pile.rect.x = 350
deck_pile.rect.y = 230
deck_list.add(deck_pile)

# Deck Pile
tonks = Cardhand("Deck.jpg")
tonks.rect.x = 800
tonks.rect.y = 230
tonks_list.add(tonks)


def update_player1(but1, but2, but3, but4, but5, but6, but7, handlisty):
    handlisty.empty()
    # Player 1 Card 1
    try:
        but1 = Cardhand(player1.hand[0].img)
        but1.rect.x = 50
        but1.rect.y = 425
        handlisty.add(but1)
    except IndexError:
        but1 = None

    # Player 1 Card 2
    try:
        but2 = Cardhand(player1.hand[1].img)
        but2.rect.x = 175
        but2.rect.y = 425
        handlisty.add(but2)
    except IndexError:
        but2 = None

    # Player 1 Card 3
    try:
        but3 = Cardhand(player1.hand[2].img)
        but3.rect.x = 300
        but3.rect.y = 425
        handlisty.add(but3)
    except IndexError:
        but3 = None

    # Player 1 Card 4
    try:
        but4 = Cardhand(player1.hand[3].img)
        but4.rect.x = 425
        but4.rect.y = 425
        handlisty.add(but4)
    except IndexError:
        but4 = None

    # Player 1 Card 5
    try:
        but5 = Cardhand(player1.hand[4].img)
        but5.rect.x = 550
        but5.rect.y = 425
        handlisty.add(but5)
    except IndexError:
        but5 = None

    # Player 1 Card 6
    try:
        but6 = Cardhand(player1.hand[5].img)
        but6.rect.x = 675
        but6.rect.y = 425
        handlisty.add(but6)
    except IndexError:
        but6 = None

    # Player 1 Card 7
    try:
        button7 = Cardhand(player1.hand[6].img)
        button7.rect.x = 800
        button7.rect.y = 425
        handlisty.add(button7)
    except IndexError:
        but7 = None

    # player 1 Card 8
    try:
        but8 = Cardhand(player1.hand[7].img)
        but8.rect.x = 425
        but8.rect.y = 425
        handlisty.add(but8)
    except IndexError:
        but8 = None


def update_player2(but1, but2, but3, but4, but5, but6, but7, handlisty):
    handlisty.empty()
    # Player 2 Card 1
    try:
        but1 = Cardhand(player2.hand[0].img)
        but1.rect.x = 50
        but1.rect.y = 25
        handlisty.add(but1)
    except IndexError:
        but1 = None

    # Player 2 Card 2
    try:
        but2 = Cardhand(player2.hand[1].img)
        but2.rect.x = 175
        but2.rect.y = 25
        handlisty.add(but2)
    except IndexError:
        but2 = None

    # Player 2 Card 3
    try:
        but3 = Cardhand(player2.hand[2].img)
        but3.rect.x = 300
        but3.rect.y = 25
        handlisty.add(but3)
    except IndexError:
        but3 = None

    # Player 1 Card 4
    try:
        but4 = Cardhand(player2.hand[3].img)
        but4.rect.x = 425
        but4.rect.y = 25
        handlisty.add(but4)
    except IndexError:
        but4 = None

    # Player 1 Card 5
    try:
        but5 = Cardhand(player2.hand[4].img)
        but5.rect.x = 550
        but5.rect.y = 25
        handlisty.add(but5)
    except IndexError:
        but5 = None

    # Player 2 Card 6
    try:
        but6 = Cardhand(player2.hand[5].img)
        but6.rect.x = 675
        but6.rect.y = 25
        handlisty.add(but6)
    except IndexError:
        but6 = None

    # Player 2 Card 7
    try:
        but7 = Cardhand(player2.hand[6].img)
        but7.rect.x = 800
        but7.rect.y = 25
        handlisty.add(but7)
    except IndexError:
        but7 = None

    # player 2 Card 8
    try:
        but82 = Cardhand(player2.hand[7].img)
        but82.rect.x = 925
        but82.rect.y = 25
        handlisty.add(but82)
    except IndexError:
        but82 = None


def update_discard(but1, handlisty):
    handlisty.empty()
    # Player 1 Card 1
    try:
        but1 = Cardhand(discard_pile.hand[-1].img)
        but1.rect.x = 500
        but1.rect.y = 230
        handlisty.add(but1)
    except IndexError:
        but1 = None


def calcScores(caller, opponent):
    score_player1 = 0
    score_player2 = 0
    for x in caller:
        score_player1 += x.value
    for x in opponent:
        score_player2 += x.value
    print(score_player1)
    print(score_player2)
    if score_player1 < score_player2:
        return [True, score_player1, score_player2]
    else:
        return [False, score_player1, score_player2]


def round_down(num, divisor):
    solution = num - (num % divisor)
    if solution < 10:
        return 10
    else:
        return solution


def show_go_screen():
    # background sound
    mixer.music.stop()
    pygame.mixer.music.load('Music&Sounds/Meow Song Choir.wav')
    mixer.music.play(-1)

    draw_text(screen, "Too Many Cats", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Click on hand to discard. Then draw from deck or discard pile "
                      "in middle.", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, " Don't look at other player's cards!", 22, WIDTH / 2, (HEIGHT + 50) / 2)
    draw_text(screen, " Press any key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                mixer.music.stop()
                # background sound
                pygame.mixer.music.load('Music&Sounds/にゃー.wav')
                mixer.music.play(-1)


# Game Loop
meow_Sound = mixer.Sound('Music&Sounds/Meow.wav')
meow_Sound.set_volume(.2)
deal_Sound = mixer.Sound('Music&Sounds/deal.wav')
win_Sound = mixer.Sound('Music&Sounds/win.wav')
win_Sound.set_volume(.2)
lose_Sound = mixer.Sound('Music&Sounds/dun.wav')
lose_Sound.set_volume(.4)

running = True
game_over = True
turn_count = 0

turn1 = True
turn2 = False
draw_turn = False
total_score_player1 = 0
total_score_player2 = 0

while running:
    if game_over:


        screen.fill(BLACK)

        show_go_screen()
        game_over = False


        # reset
        deck.__init__()
        deck.build()
        deck.shuffle()
        # Init Player 1 and deal cards
        player1 = Card.Player("Player1")
        handnum = 7
        for x in range(handnum):
            player1.draw(deck)
        player1.showHand()
        print("^^ player1 beginning")

        # Init Player 2 and deal cards
        player2 = Card.Player("Player2")
        for x in range(handnum):
            player2.draw(deck)
        player2.showHand()
        print("^^ player2 beginning")
        # deck.show()

        # Init Discard Pile
        discard_pile = Card.Player("Discard")
        discard_pile.draw(deck)
        discard_pile.showHand()
        print("^^ discard beginning")

        # Init Discard  Temp Pile
        discard_temp_pile = Card.Player("Discard")

        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
        # update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6, buttontwo7,
        #                hand_player2_list)
        hand_player2_list.empty()
        update_discard(discard_top, discard_pile_list)

        turn_count = 0

        turn1 = True
        turn2 = False
        draw_turn = False
        total_score_player1 = 0
        total_score_player2 = 0

    #     RGB
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # pygame.display.flip()
    # mouse init
    pos = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #     Player 1 turn 1
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True and draw_turn == False:
            if event.button == 1:

                for buttons in hand_player1_list:

                    if buttons.handleEvent(event, pos) == "Beard Cat":
                        print("beard works")
                        meow_Sound.play()
                        for x in player1.hand[:]:
                            if x.img == "Beard Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Watermelon Cat":
                        meow_Sound.play()
                        print("water works")
                        for x in player1.hand[:]:
                            if x.img == "Watermelon Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")

                        player1.showHand()
                        print("^^player 1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)

                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Taco Cat":
                        meow_Sound.play()
                        for x in player1.hand[:]:
                            if x.img == "Taco Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Rainbow Cat":
                        meow_Sound.play()
                        for x in player1.hand[:]:
                            if x.img == "Rainbow Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Potato Cat":
                        meow_Sound.play()
                        for x in player1.hand[:]:
                            if x.img == "Potato Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Grumpy Cat":
                        meow_Sound.play()
                        for x in player1.hand[:]:
                            if x.img == "Grumpy Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

        # Player 1 Draw time
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True and draw_turn == True:

            if event.button == 1:

                if discard_top.handleEvent(event, pos):
                    deal_Sound.play()
                    print("discard draw works")
                    # fix first turn later
                    player1.hand.append(discard_pile.hand[-1])
                    player1.showHand()
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)

                    print("player1 hand rn")
                    draw_turn = False
                    turn1 = False
                    update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                    update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6, buttontwo7,
                                   hand_player2_list)
                    update_discard(discard_top, discard_pile_list)
                    hand_player1_list.empty()

                if deck_pile.handleEvent(event, pos):
                    deal_Sound.play()
                    print("deck draw works")
                    player1.draw(deck)
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)

                    player1.showHand()
                    print("player1 hand rn")
                    draw_turn = False
                    turn1 = False
                    update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                    update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6, buttontwo7,
                                   hand_player2_list)
                    update_discard(discard_top, discard_pile_list)
                    hand_player1_list.empty()
        # Player 2
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False and draw_turn == False:
            if event.button == 1:
                for buttons in hand_player2_list:
                    if buttons.handleEvent(event, pos) == "Beard Cat":
                        meow_Sound.play()
                        for x in player2.hand[:]:
                            if x.img == "Beard Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                            discard_pile.showHand()
                            print("^^discard pile rn")
                            print()

                            player2.showHand()
                            print("player 2 hand")
                            print()

                            draw_turn = True
                            update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                           buttontwo7, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Watermelon Cat":
                        meow_Sound.play()
                        print("water works")
                        for x in player2.hand[:]:
                            if x.img == "Watermelon Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        print()

                        player2.showHand()
                        print("^^player 2 hand")
                        print()

                        draw_turn = True
                        update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                       buttontwo7, hand_player2_list)
                        update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Taco Cat":
                        meow_Sound.play()
                        for x in player2.hand[:]:
                            if x.img == "Taco Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                            discard_pile.showHand()
                            print("^^discard pile rn")
                            print()

                            player2.showHand()
                            print("player 2 hand")
                            print()

                            draw_turn = True
                            update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                           buttontwo7, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Rainbow Cat":
                        meow_Sound.play()
                        for x in player2.hand[:]:
                            if x.img == "Rainbow Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                            discard_pile.showHand()
                            print("^^discard pile rn")
                            print()

                            player2.showHand()
                            print("player 2 hand")
                            print()

                            draw_turn = True
                            update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                           buttontwo7, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)

                    elif buttons.handleEvent(event, pos) == "Potato Cat":
                        meow_Sound.play()
                        for x in player2.hand[:]:
                            if x.img == "Potato Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                            discard_pile.showHand()
                            print("^^discard pile rn")
                            print()

                            player2.showHand()
                            print("player 2 hand")
                            print()

                            draw_turn = True
                            update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                           buttontwo7, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)
                    elif buttons.handleEvent(event, pos) == "Grumpy Cat":
                        meow_Sound.play()
                        for x in player2.hand[:]:
                            if x.img == "Grumpy Cat.jpg":
                                player2.discard(x)
                                discard_temp_pile.hand.append(x)

                            discard_pile.showHand()
                            print("^^discard pile rn")
                            print()

                            player2.showHand()
                            print("player 2 hand")
                            print()

                            draw_turn = True
                            update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                           buttontwo7, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)
            # Player 2 Draw time
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False and draw_turn == True:

            if event.button == 1:

                if discard_top.handleEvent(event, pos):
                    deal_Sound.play()
                    print("discard draw works")
                    player2.hand.append(discard_pile.hand[-1])
                    player2.showHand()
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)

                    print("^^player 2 hand")
                    print()
                    discard_pile.showHand()
                    print("discard pile rn")
                    print()
                    draw_turn = False
                    turn1 = True
                    update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6, buttontwo7,
                                   hand_player2_list)
                    update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                    hand_player2_list.empty()
                    update_discard(discard_top, discard_pile_list)
                    turn_count += 1
                    print(turn_count)

                if deck_pile.handleEvent(event, pos):
                    deal_Sound.play()
                    print("deck draw works")
                    player2.draw(deck)
                    player2.showHand()
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)
                    discard_temp_pile.hand.clear()
                    print("^^player 2 hand")
                    print()
                    discard_pile.showHand()
                    print("discard pile rn")
                    print()
                    draw_turn = False
                    turn1 = True
                    update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6, buttontwo7,
                                   hand_player2_list)
                    update_discard(discard_top, discard_pile_list)
                    update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                    hand_player2_list.empty()
                    turn_count += 1
                    print(turn_count)

        # Calling Tonks Player 1
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True and turn_count >= 1 and draw_turn == False:
            if event.button == 1:
                if tonks.handleEvent(event, pos):
                    round_score = calcScores(player1.hand, player2.hand)
                    # If player 1 calls Tonks correct
                    if round_score[0] == True:
                        win_Sound.play()
                        print("Player 1 Wins Round")
                        total_score_player2 += int((round_down(round_score[2],10)))
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")
                        # reset
                        deck.__init__()
                        deck.build()
                        deck.shuffle()
                        # Init Player 1 and deal cards
                        player1 = Card.Player("Player1")
                        handnum = 7
                        for x in range(handnum):
                            player1.draw(deck)
                        player1.showHand()
                        print("^^ player1 beginning")

                        # Init Player 2 and deal cards
                        player2 = Card.Player("Player2")
                        for x in range(handnum):
                            player2.draw(deck)
                        player2.showHand()
                        print("^^ player2 beginning")
                        # deck.show()

                        # Init Discard Pile
                        discard_pile = Card.Player("Discard")
                        discard_pile.draw(deck)
                        discard_pile.showHand()
                        print("^^ discard beginning")

                        # Init Discard  Temp Pile
                        discard_temp_pile = Card.Player("Discard")

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                       buttontwo7, hand_player2_list)
                        update_discard(discard_top, discard_pile_list)
                        hand_player2_list.empty()
                        turn_count = 0
                        draw_turn = False
                        turn1 = True

                    # if Player 1 calls tonks wrong
                    elif round_score[0] == False:
                        lose_Sound.play()
                        print("Player 1 loses Round")
                        total_score_player1 += 20
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")

                        # reset
                        deck.__init__()
                        deck.build()
                        deck.shuffle()
                        # Init Player 1 and deal cards
                        player1 = Card.Player("Player1")
                        handnum = 7
                        for x in range(handnum):
                            player1.draw(deck)
                        player1.showHand()
                        print("^^ player1 beginning")

                        # Init Player 2 and deal cards
                        player2 = Card.Player("Player2")
                        for x in range(handnum):
                            player2.draw(deck)
                        player2.showHand()
                        print("^^ player2 beginning")
                        # deck.show()

                        # Init Discard Pile
                        discard_pile = Card.Player("Discard")
                        discard_pile.draw(deck)
                        discard_pile.showHand()
                        print("^^ discard beginning")

                        # Init Discard  Temp Pile
                        discard_temp_pile = Card.Player("Discard")

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                       buttontwo7, hand_player2_list)
                        hand_player2_list.empty()
                        update_discard(discard_top, discard_pile_list)
                        turn_count = 0
                        draw_turn = False
                        turn1 = True

        # calling tonks player 2
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False and turn_count >= 1 and draw_turn == False:
            if event.button == 1:
                if tonks.handleEvent(event, pos):
                    round_score = calcScores(player2.hand, player1.hand)

                    # if player 2 calls tonks correct
                    if round_score[0] == True:
                        win_Sound.play()
                        print("Player 2 Wins Round")
                        total_score_player1 += int(round_down(round_score[2],10))
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")
                        # reset
                        deck.__init__()
                        deck.build()
                        deck.shuffle()
                        # Init Player 1 and deal cards
                        player1 = Card.Player("Player1")
                        handnum = 7
                        for x in range(handnum):
                            player1.draw(deck)
                        player1.showHand()
                        print("^^ player1 beginning")

                        # Init Player 2 and deal cards
                        player2 = Card.Player("Player2")
                        for x in range(handnum):
                            player2.draw(deck)
                        player2.showHand()
                        print("^^ player2 beginning")
                        # deck.show()

                        # Init Discard Pile
                        discard_pile = Card.Player("Discard")
                        discard_pile.draw(deck)
                        discard_pile.showHand()
                        print("^^ discard beginning")

                        # Init Discard  Temp Pile
                        discard_temp_pile = Card.Player("Discard")

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                       buttontwo7, hand_player2_list)
                        update_discard(discard_top, discard_pile_list)
                        hand_player1_list.empty()
                        turn_count = 0
                        draw_turn = False
                        turn1 = False

                    # If player 2 calls Tonks wrong
                    elif round_score[0] == False:
                        lose_Sound.play()
                        print("Player 2 loses Round")
                        total_score_player2 += 20
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")

                        # reset
                        deck.__init__()
                        deck.build()
                        deck.shuffle()
                        # Init Player 1 and deal cards
                        player1 = Card.Player("Player1")
                        handnum = 7
                        for x in range(handnum):
                            player1.draw(deck)
                        player1.showHand()
                        print("^^ player1 beginning")

                        # Init Player 2 and deal cards
                        player2 = Card.Player("Player2")
                        for x in range(handnum):
                            player2.draw(deck)
                        player2.showHand()
                        print("^^ player2 beginning")
                        # deck.show()

                        # Init Discard Pile
                        discard_pile = Card.Player("Discard")
                        discard_pile.draw(deck)
                        discard_pile.showHand()
                        print("^^ discard beginning")

                        # Init Discard  Temp Pile
                        discard_temp_pile = Card.Player("Discard")

                        update_player1(button, button2, button3, button4, button5, button6, button7, hand_player1_list)
                        update_player2(buttontwo, buttontwo2, buttontwo3, buttontwo4, buttontwo5, buttontwo6,
                                       buttontwo7, hand_player2_list)
                        update_discard(discard_top, discard_pile_list)
                        hand_player1_list.empty()
                        turn_count = 0
                        draw_turn = False
                        turn1 = False

        # Game over
        if total_score_player2 >= 50 or total_score_player1 >= 50:
            game_over = True

    hand_player1_list.draw(screen)
    hand_player2_list.draw(screen)
    deck_list.draw(screen)
    discard_pile_list.draw(screen)
    tonks_list.draw(screen)
    show_score_player1(textX1, textY1)
    show_score_player2(textX2, textY2)
    deck_label(textX3,textY3)
    discard_pile_label(textX4,textY4)
    tonks_label(textX5,textY5)
    # update screen
    pygame.display.update()
