import pygame
import random
import math
import Card

from pygame import mixer

# Initialize the pygame

pygame.init()
# pygame.display.list_modes()
# mixer.init()
# pygame.mixer.get_init()
# create the screen
screen = pygame.display.set_mode((800, 600))
#
# # Background
# background = pygame.image.load('2478865.jpg')
#
# # background sound
#
# pygame.mixer.music.load('background.wav')
# mixer.music.play(-1)
#
# Title and Icon
pygame.display.set_caption("Too Many Cats")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Create Deck
deck = Card.Deck()
deck.shuffle()
# deck.show()
# card = deck.draw()
# card.show()

# Init Player 1 and deal cards
player1 = Card.Player("Player1")
handnum = 3
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
                        return "Rainbow  Cat"
                    if self.name == "Taco Cat.jpg":
                        return "Taco Cat"
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

# Player 2 Card 1
button4 = Cardhand(player2.hand[0].img)
button4.rect.x = 50
button4.rect.y = 25
hand_player2_list.add(button4)

# Player 2 Card 2
button5 = Cardhand(player2.hand[1].img)
button5.rect.x = 175
button5.rect.y = 25
hand_player2_list.add(button5)

# Player 2 Card 3
button6 = Cardhand(player2.hand[2].img)
button6.rect.x = 300
button6.rect.y = 25
hand_player2_list.add(button6)

# Discard Pile
discard_top = Cardhand(discard_pile.hand[0].img)
discard_top.rect.x = 360
discard_top.rect.y = 230
discard_pile_list.add(discard_top)

# Deck Pile
deck_pile = Cardhand("Deck.jpg")
deck_pile.rect.x = 200
deck_pile.rect.y = 230
deck_list.add(deck_pile)

# Deck Pile
tonks = Cardhand("Deck.jpg")
tonks.rect.x = 480
tonks.rect.y = 230
tonks_list.add(tonks)


def update_player1(but1, but2, but3, handlisty):
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
    # player 1 Card 4
    try:
        but35 = Cardhand(player1.hand[3].img)
        but35.rect.x = 425
        but35.rect.y = 425
        handlisty.add(but35)
    except IndexError:
        but35 = None


def update_player2(but1, but2, but3, handlisty):
    handlisty.empty()
    # Player 1 Card 1
    try:
        but1 = Cardhand(player2.hand[0].img)
        but1.rect.x = 50
        but1.rect.y = 25
        handlisty.add(but1)
    except IndexError:
        but1 = None

    # Player 1 Card 2
    try:
        but2 = Cardhand(player2.hand[1].img)
        but2.rect.x = 175
        but2.rect.y = 25
        handlisty.add(but2)
    except IndexError:
        but2 = None

    # Player 1 Card 3
    try:
        but3 = Cardhand(player2.hand[2].img)
        but3.rect.x = 300
        but3.rect.y = 25
        handlisty.add(but3)
    except IndexError:
        but3 = None
    # player 1 Card 4
    try:
        but36 = Cardhand(player2.hand[3].img)
        but36.rect.x = 425
        but36.rect.y = 25
        handlisty.add(but36)
    except IndexError:
        but36 = None

def update_discard(but1, handlisty):
    handlisty.empty()
    # Player 1 Card 1
    try:
        but1 = Cardhand(discard_pile.hand[-1].img)
        but1.rect.x = 360
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
        return [True,score_player1,score_player2]
    else:
        return [False,score_player1,score_player2]

# Game Loop
running = True
turn_count = 0

print(x)
turn1 = True
turn2 = False
draw_turn = False
total_score_player1 = 0
total_score_player2 = 0

while running:
    #     RGB
    screen.fill((0, 0, 0))
    # mouse init
    pos = pygame.mouse.get_pos()
    #     # playerX += 0.1
    #     screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #     Player 1 turn 1
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True:
            if event.button == 1:

                for buttons in hand_player1_list:

                    if buttons.handleEvent(event, pos) == "Beard Cat":
                        print("beard works")
                        for x in player1.hand[:]:
                            if x.img == "Beard Cat.jpg":
                                player1.discard(x)
                                discard_temp_pile.hand.append(x)

                        discard_pile.showHand()
                        print("^^discard pile rn")
                        player1.showHand()
                        print("^^ player1 hand")

                        draw_turn = True

                        update_player1(button, button2, button3, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    if buttons.handleEvent(event, pos) == "Watermelon Cat":
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

                        update_player1(button, button2, button3, hand_player1_list)
                        update_discard(discard_top, discard_pile_list)

                    # if buttons.handleEvent(event, pos) == "Taco Cat":
                    #     print("taco works")
                    #     turn1 = False
                    #
                    # if buttons.handleEvent(event, pos) == "Rainbow Cat":
                    #     print("rain works")
                    #     turn1 = False
                    #
                    # if buttons.handleEvent(event, pos) == "Potato Cat":
                    #     print("potat works")
                    #     turn1 = False

        # Player 1 Draw time
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True and draw_turn == True:

            if event.button == 1:

                if discard_top.handleEvent(event, pos):
                    print("discard draw works")
                    # fix first turn later
                    player1.hand.append(discard_pile.hand[-1])
                    player1.showHand()
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)
                    discard_temp_pile.hand.clear()
                    print("player1 hand rn")
                    draw_turn = False
                    turn1 = False
                    update_player1(button, button2, button3, hand_player1_list)
                    update_discard(discard_top, discard_pile_list)

                if deck_pile.handleEvent(event, pos):
                    print("deck draw works")
                    player1.draw(deck)
                    for x in discard_temp_pile.hand:
                        discard_pile.hand.append(x)
                    discard_temp_pile.hand.clear()
                    player1.showHand()
                    print("player1 hand rn")
                    draw_turn = False
                    turn1 = False
                    update_player1(button, button2, button3, hand_player1_list)
                    update_discard(discard_top, discard_pile_list)
        # Player 2
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False:
            if event.button == 1:
                for buttons in hand_player2_list:
                    if buttons.handleEvent(event, pos) == "Beard Cat":
                        print("beard2 works")
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
                            update_player2(button4, button5, button6, hand_player2_list)
                            update_discard(discard_top, discard_pile_list)

                    if buttons.handleEvent(event, pos) == "Watermelon Cat":
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
                        update_player2(button4, button5, button6, hand_player2_list)
                        update_discard(discard_top, discard_pile_list)

                    # if buttons.handleEvent(event, pos) == "Taco Cat":
                    #     print("taco2 works")
                    #     turn1 = True
                    #
                    # if buttons.handleEvent(event, pos) == "Rainbow Cat":
                    #     print("rain2 works")
                    #     turn1 = True
                    #
                    # if buttons.handleEvent(event, pos) == "Potato Cat":
                    #     print("potat2 works")
                    #     turn1 = True
            # Player 2 Draw time
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False and draw_turn == True:

            if event.button == 1:

                if discard_top.handleEvent(event, pos):
                    print("discard draw works")
                    player2.hand.append(discard_pile.hand[-1])
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
                    update_player2(button4, button5, button6, hand_player2_list)
                    update_discard(discard_top, discard_pile_list)
                    turn_count += 1
                    print(turn_count)

                if deck_pile.handleEvent(event, pos):
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
                    update_player2(button4, button5, button6, hand_player2_list)
                    update_discard(discard_top, discard_pile_list)
                    turn_count += 1
                    print(turn_count)
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == True and turn_count >= 1:
            if event.button == 1:
                if tonks.handleEvent(event, pos):
                    round_score = calcScores(player1.hand,player2.hand)
                    if round_score[0] == True:
                        print("Player 1 Wins Round")
                        total_score_player2 += int(round(round_score[2] + 5.1, -1))
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")

                    elif round_score[0] == False:
                        print("Player 1 loses Round")
                        total_score_player1 += 20
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")
        if event.type == pygame.MOUSEBUTTONDOWN and turn1 == False and turn_count >= 1:
            if event.button == 1:
                if tonks.handleEvent(event, pos):
                    round_score = calcScores(player2.hand,player1.hand)
                    if round_score[0] == True:
                        print("Player 2 Wins Round")
                        total_score_player1 += int(round(round_score[2] + 5.1, -1))
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")

                    elif round_score[0] == False:
                        print("Player 2 loses Round")
                        total_score_player2 += 20
                        print(total_score_player1)
                        print("Player1 ^^")
                        print(total_score_player2)
                        print("Player2 ^^")

    # deck_img(deckX, deckY)
    # discard_pile_img(discardX, discardY)
    hand_player1_list.draw(screen)
    hand_player2_list.draw(screen)
    deck_list.draw(screen)
    discard_pile_list.draw(screen)
    tonks_list.draw(screen)
    #     show_score(textX,textY )
    # update screen
    pygame.display.update()
