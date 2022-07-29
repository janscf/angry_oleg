from lib.game.enums import SignalLevel
from lib.game.state.components import DetectorState
from view.console.components import ComponentView
from view.console.controls import DirectionLabel
from view.console.screen import Screen


class _Texts:
    NO_TARGETS_MESSAGE = 'Вы не чувствуете ничего необычного.'
    DETECTOR_MESSAGE = 'В направлении на {direction} что-то есть.'
    SIGNAL_MESSAGE = {
        SignalLevel.Low: 'Вы едва ощущаете это.',
        SignalLevel.Average: 'Это явно чувствуется.',
        SignalLevel.High: 'Вы совершенно уверены в этом.',
    }


class DetectorView(ComponentView[DetectorState]):
    def render(self, state: DetectorState):
        messages = []
        if state.targets:
            for target in state.targets:
                direction_label = DirectionLabel(target.direction)
                messages.append(_Texts.DETECTOR_MESSAGE.format(direction=direction_label))
                messages.append(_Texts.SIGNAL_MESSAGE[target.signal_level])
        else:
            messages.append(_Texts.NO_TARGETS_MESSAGE)

        return Screen.join(messages)
