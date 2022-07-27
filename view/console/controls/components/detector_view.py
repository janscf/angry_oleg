from lib.game.enums import SignalLevel
from lib.game.state.components import DetectorState
from view.console.controls.components.component_state_view import ComponentStateView
from view.console.controls.direction_label import DirectionLabel
from view.console.screen import Screen


class DetectorView(ComponentStateView[DetectorState]):
    NO_TARGETS_MESSAGE = 'Вы не чувствуете ничего необычного.'
    DETECTOR_MESSAGE = 'В направлении на {direction} что-то есть.'
    SIGNAL_MESSAGE = {
        SignalLevel.Low: 'Вы едва ощущаете это.',
        SignalLevel.Average: 'Это явно чувствуется.',
        SignalLevel.High: 'Вы совершенно уверены в этом.',
    }

    def show_state(self):
        if self.state.targets:
            for target in self.state.targets:
                direction_label = DirectionLabel(target.direction)
                message = self.DETECTOR_MESSAGE.format(direction=direction_label)
                Screen.display(message)
                Screen.display(self.SIGNAL_MESSAGE[target.signal_level])
        else:
            Screen.display(self.NO_TARGETS_MESSAGE)
