from typing import TYPE_CHECKING

from lib.game.enums import ComponentType
from view.console.controls.components.detector_view import DetectorView
from view.console.controls.components.solid_body_view import SolidBodyView

if TYPE_CHECKING:
    from lib.game.state import ComponentState
    from view.console.controls.components.component_state_view import ComponentStateView


class ComponentViewFactory:
    @staticmethod
    def create(component_state: 'ComponentState') -> 'ComponentStateView':
        if component_state.component_type == ComponentType.Detector:
            return DetectorView(component_state)
        if component_state.component_type == ComponentType.SolidBody:
            return SolidBodyView(component_state)
