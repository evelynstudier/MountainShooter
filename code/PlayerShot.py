from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def _init_(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]