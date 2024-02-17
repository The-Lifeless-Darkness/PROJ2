import pygame


class Button:
    """
    Button on pygame screen
    """
    def __init__(self,
                 text,
                 x,
                 y,
                 width,
                 height,
                 background_color,
                 background_hover_color,
                 text_color,
                 text_hover_color,
                 onclick=lambda: None,
                 font_size=32):
        """
        Initializes button
        :param text: text of button
        :param x: X coordinate of button
        :param y: Y coordinate of button
        :param width: width of button
        :param height: height of button
        :param background_color:  background color of button
        :param background_hover_color: background color of button when hovered
        :param text_color: color of text on button
        :param text_hover_color: color of text on button when hovered
        :param onclick: click handler of button
        :param font_size: font size of text on button
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = background_color
        self.hover_color = background_hover_color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, font_size)
        self.text_surf = self.font.render(self.text, True, text_color)
        self.text_surf_hover = self.font.render(self.text, True, text_hover_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.onclick = onclick
        self.pressed = False

    def draw(self, screen) -> None:
        """
        Draws button on passed screen
        :param screen: screen to draw on
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.hover_color, self.rect, 0, 10)
            screen.blit(self.text_surf_hover, self.text_rect)
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                self.onclick()
                self.pressed = True
        else:
            self.pressed = False
            pygame.draw.rect(screen, self.color, self.rect, 0, 10)
            screen.blit(self.text_surf, self.text_rect)