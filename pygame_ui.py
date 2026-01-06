import pygame

from card import Card, Suit
from ui import GameUI, GameAction

class Button:
    def __init__(self, rect: pygame.Rect, label, bg_colour, fg_colour):
        self.rect = rect
        self.label = label
        self.bg_colour = bg_colour
        self.fg_colour = fg_colour

    def draw(self, surface: pygame.Surface, font: pygame.font.Font, hover = False):
        colour = tuple(min(255, c + 30) for c in self.bg_colour) if hover else self.bg_colour
        pygame.draw.rect(surface, colour, self.rect, border_radius=8)
        text_surf = font.render(self.label, True, self.fg_colour)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def contains(self, pos) -> bool:
        return self.rect.collidepoint(pos)

class PygameUI(GameUI):
    def __init__(self, cards_to_deal: int):
        super().__init__(cards_to_deal)
        pygame.init()
        self.size = (900, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Bank!")
        self.clock = pygame.time.Clock()

        #colours
        self.BG = (30, 30, 36)
        self.CARD_BORDER = (200, 200, 210)
        self.WHITE = (240, 240, 240)
        self.GREY = (170, 170, 180)
        self.GREEN = (52, 168, 83)
        self.RED = (234, 67, 53)
        self.YELLOW = (251, 188, 5)

        #fonts
        self.font_title = pygame.font.SysFont("arial", 36)
        self.font_body = pygame.font.SysFont("arial", 22)
        self.font_small = pygame.font.SysFont("arial", 18)
        self.font_card = pygame.font.SysFont("arial", 28, bold=True)

        #button setup
        w, h = self.size
        btn_w, btn_h = 160, 48
        gap = 24
        y = h - btn_h - 32
        center_x = w // 2
        self.lower_button = Button(pygame.Rect(center_x - btn_w - gap - btn_w // 2, y, btn_w, btn_h), "Lower", self.RED, (255, 255, 255))
        self.bank_button = Button(pygame.Rect(center_x - btn_w // 2, y, btn_w, btn_h), "Bank!", self.YELLOW, (0, 0, 0))
        self.higher_button = Button(pygame.Rect(center_x + gap + btn_w // 2, y, btn_w, btn_h), "Higher", self.GREEN, (255, 255, 255))

        self.game_state = {
            "current_card": None, 
            "cards_dealt": 0,
            "bank_score": 0,
            "total_score": 0,
        }

    #rendering helpers
    def draw_title(self, title):
        self.screen.fill(self.BG)
        text = self.font_title.render(title, True, self.WHITE)
        rect = text.get_rect(center=(self.size[0] // 2, 40))
        self.screen.blit(text, rect)

    def draw_stats(self):
        self.screen.blit(self.font_body.render(f"Card {self.game_state['cards_dealt']} / {self.cards_to_deal}", True, self.WHITE), (24, 16))
        self.screen.blit(self.font_body.render(f"Bank: {self.game_state['bank_score']}", True, self.WHITE), (24, 46))
        score_surf = self.font_body.render(f"Total: {self.game_state['total_score']}", True, self.WHITE)
        self.screen.blit(score_surf, (self.size[0] - score_surf.get_width() - 24, 16))

    def draw_card(self, card: Card, central_pos):
        card_rect = pygame.Rect(0, 0, 200, 280)
        card_rect.center = central_pos
        pygame.draw.rect(self.screen, self.WHITE, card_rect, border_radius=12)

        suit_symbols = {
            Suit.HEARTS: ("♥", (200, 0, 0)),
            Suit.DIAMONDS: ("♦", (200, 0, 0)),
            Suit.CLUBS: ("♣", (0, 0, 0)),
            Suit.SPADES: ("♠", (0, 0, 0)),
        }
        suit_symbol, suit_colour = suit_symbols[card.suit]

        #top-left --> rank
        self.screen.blit(self.font_small.render(card.rank.symbol, True, suit_colour), (card_rect.x + 10, card_rect.y + 10))

        #center --> symbol
        center = self.font_card.render(suit_symbol, True, suit_colour)
        center_rect = center.get_rect(center=card_rect.center)
        self.screen.blit(center, center_rect)

        #bottom-right --> rank
        br = self.font_small.render(card.rank.symbol, True, suit_colour)
        self.screen.blit(self.font_small.render(card.rank.symbol, True, suit_colour), (card_rect.right - br.get_width() - 10, card_rect.bottom - br.get_height() - 10))

    def draw_buttons(self, hover_pos=None):
        for button in (self.lower_button, self.bank_button, self.higher_button):
            button.draw(self.screen, self.font_body, hover=hover_pos and button.contains(hover_pos))

    def get_user_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                
            yield event

    #GameUI methods
    def display_welcome(self) -> None:
        while True:
            self.draw_title("Welcome to Bank!")
            instructions = [
                "Rules:",
                "- Predict if the next card is LOWER or HIGHER",
                "- Correct predictions DOUBLE your bank",
                "- Wrong predictions reset your bank to 0",
                "- Bank at any time to lock in your score",
                f"- Deck contains {self.cards_to_deal} cards in total",
                "Click anywhere to start",
            ]

            y = 120
            for line in instructions:
                surf = self.font_body.render(line, True, self.GREY)
                self.screen.blit(surf, (60, y))
                y += 28

            pygame.display.flip()
            self.clock.tick(60)

            for event in self.get_user_event():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return

    def display_game_state(self, current_card: Card, cards_dealt: int, bank_score: int, total_score: int) -> None:
        self.game_state["current_card"] = current_card
        self.game_state["cards_dealt"] = cards_dealt
        self.game_state["bank_score"] = bank_score
        self.game_state["total_score"] = total_score

    def get_action(self) -> GameAction:
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.draw_title("Make your move")
            self.draw_stats()
            self.draw_card(self.game_state["current_card"], (self.size[0] // 2, self.size[1] // 2 - 20))
            self.draw_buttons(mouse_pos)

            pygame.display.flip()
            self.clock.tick(60)

            for event in self.get_user_event():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.lower_button.contains(event.pos):
                        return GameAction.LOWER
                    if self.higher_button.contains(event.pos):
                        return GameAction.HIGHER
                    if self.bank_button.contains(event.pos):
                        return GameAction.BANK

    def display_bank_action_outcome(self, amount_banked: int) -> None:
        if amount_banked == 0:
            message = "But your bank was 0, so no points added..."
        else:
            message = f"Added {amount_banked} to your total."

        while True:
            self.draw_title("BANKED!")
            self.draw_stats()

            msg = self.font_body.render(message, True, self.WHITE)
            self.screen.blit(msg, (self.size[0] // 2 - msg.get_width() // 2, self.size[1] // 2))
            cont = self.font_small.render("Click to continue", True, self.GREY)
            self.screen.blit(cont, (self.size[0] // 2 - cont.get_width() // 2, self.size[1] - 32))

            pygame.display.flip()
            self.clock.tick(60)
            
            for event in self.get_user_event():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return

    def display_prediction_action_outcome(self, prediction: GameAction, is_correct: bool, current_card: Card, next_card: Card) -> None:
        if is_correct:
            title = "CORRECT!"
            colour = self.GREEN
        else:
            title = "WRONG!"
            colour = self.RED

        while True:
            self.draw_title(title)
            self.draw_stats()

            #draw cards side by side
            cx = self.size[0] // 2 - 120
            nx = self.size[0] // 2 + 120
            cy = self.size[1] // 2 - 20
            self.draw_card(current_card, (cx, cy))
            self.draw_card(next_card, (nx, cy))

            prediction_text = self.font_body.render(f"You predicted: {prediction.value}", True, colour)
            self.screen.blit(prediction_text, (self.size[0] // 2 - prediction_text.get_width() // 2, cy + 170))

            cont = self.font_small.render("Click to continue", True, self.GREY)
            self.screen.blit(cont, (self.size[0] // 2 - cont.get_width() // 2, self.size[1] - 32))

            pygame.display.flip()
            self.clock.tick(60)

            for event in self.get_user_event():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return

    def display_game_over(self, final_score: int, new_high_score: bool) -> None:
        self.draw_game_over_screen(final_score, new_high_score)
        pygame.display.flip()

    def ask_play_again(self) -> bool:
        yes_button = Button(pygame.Rect(self.size[0] // 2 - 170, self.size[1] - 100, 150, 48), "Play Again", self.GREEN, (255, 255, 255))
        no_button = Button(pygame.Rect(self.size[0] // 2 + 20, self.size[1] - 100, 150, 48), "Quit", self.RED, (255, 255, 255))

        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            self.draw_game_over_screen(self.game_state["total_score"], False)
            yes_button.draw(self.screen, self.font_body, hover=yes_button.contains(mouse_pos))
            no_button.draw(self.screen, self.font_body, hover=no_button.contains(mouse_pos))

            pygame.display.flip()
            self.clock.tick(60)

            for event in self.get_user_event():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if yes_button.contains(event.pos):
                        return True
                    if no_button.contains(event.pos):
                        return False

    def draw_game_over_screen(self, final_score: int, new_high_score: bool):
        self.draw_title("Game Over!")
        score_text = self.font_title.render(f"Final Score: {final_score}", True, self.WHITE)
        self.screen.blit(score_text, (self.size[0] // 2 - score_text.get_width() // 2, 180))

        if new_high_score:
            hs = self.font_body.render("New High Score!", True, self.YELLOW)
            self.screen.blit(hs, (self.size[0] // 2 - hs.get_width() // 2, 240))
        hint = self.font_small.render("Choose an option below", True, self.GREY)
        self.screen.blit(hint, (self.size[0] // 2 - hint.get_width() // 2, 280))
