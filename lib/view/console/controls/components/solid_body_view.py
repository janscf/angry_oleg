from lib.game.components.solid_body import SolidBodyState
from lib.view.console.controls.components.component_state_view import ComponentStateView
from lib.view.console.screen import Screen


class SolidBodyView(ComponentStateView[SolidBodyState]):
    POSITION_MESSAGE = 'Ваши координаты: {}'

    def show_state(self):
        Screen.display(self.POSITION_MESSAGE.format(str(self.state.position)))
