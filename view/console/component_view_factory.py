from typing import TYPE_CHECKING

from lib.game.enums import ComponentType

if TYPE_CHECKING:
    from lib.game.state import ComponentState
    from view.console.components import ComponentView


class ComponentViewFactory:
    @staticmethod
    def create(component_state: 'ComponentState') -> 'ComponentView':
        if component_state.component_type == ComponentType.Detector:
            from view.console.components.detector_view import DetectorView
            return DetectorView(component_state)

        if component_state.component_type == ComponentType.SolidBody:
            from view.console.components.solid_body_view import SolidBodyView
            return SolidBodyView(component_state)
