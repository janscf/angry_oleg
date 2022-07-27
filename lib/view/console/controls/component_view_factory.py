from typing import TYPE_CHECKING

from lib.game.components import ComponentType
from lib.view.console.controls.components.detector_view import DetectorView
from lib.view.console.controls.components.solid_body_view import SolidBodyView

if TYPE_CHECKING:
    from lib.game.components import ComponentState
    from lib.view.console.controls.components.component_state_view import ComponentStateView


class ComponentViewFactory:
    @staticmethod
    def create(component_state: 'ComponentState') -> 'ComponentStateView':
        if component_state.component_type == ComponentType.Detector:
            return DetectorView(component_state)
        if component_state.component_type == ComponentType.SolidBody:
            return SolidBodyView(component_state)
