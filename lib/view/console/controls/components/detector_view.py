from lib.game.components.detector import DetectorState
from lib.view.console.controls.components.component_state_view import ComponentStateView
from lib.view.console.screen import Screen


class DetectorView(ComponentStateView[DetectorState]):
    DETECTOR_MESSAGE = 'В направлении {direction} что-то есть, уровень сигнала {level}'

    def show_state(self):
        for target in self.state.targets:
            message = self.DETECTOR_MESSAGE.format(
                level=target.signal_level,
                direction=target.direction,
            )
            Screen.display(message)
