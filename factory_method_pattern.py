from abc import ABC, abstractmethod
import platform


# The product
class Component(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class WindowsPlayButton(Component):
    def render(self) -> str:
        return "Render Windows Play Button"

class WindowsTimeline(Component):
    def render(self) -> str:
        return "Render Windows Timeline"


class WindowsWindow(Component):
    def render(self) -> str:
        return "Render Windows Window"


class MacPlayButton(Component):
    def render(self) -> str:
        return "Render Mac Play Button"

class MacTimeline(Component):
    def render(self) -> str:
        return "Render Mac Timeline"


class MacWindow(Component):
    def render(self) -> str:
        return "Render Mac Window"


# The interface the client use so he can interact with the objects
class AbstractPlayerComponentFactory(ABC):
    @abstractmethod
    def create_component(self, component_type: str) -> Component:
        pass

# the concrete factory that implements the the create_component
class WindowsPlayerComponentFactory(AbstractPlayerComponentFactory):
    def create_component(self, component_type: str) -> Component:
        if component_type == "play_button":
            return WindowsPlayButton()
        if component_type == "timeline":
            return WindowsTimeline()
        if component_type == "window":
            return WindowsWindow()
        else:
            return None


class MacPlayerComponentFactory(AbstractPlayerComponentFactory):
    def create_component(self, component_type: str) -> Component:
        if component_type == "play_button":
            return MacPlayButton()
        if component_type == "timeline":
            return MacTimeline()
        if component_type == "window":
            return MacWindow()
        else:
            return None



# client code
def client(factory: AbstractPlayerComponentFactory) -> None:
    window = factory.create_component("window")
    timeline = factory.create_component("timeline")
    play_button = factory.create_component("play_button")

    print(window.render(), timeline.render(), play_button.render())




if __name__ == "__main__":
    current_os = platform.system()

    if current_os == "Windows":
        client(WindowsPlayerComponentFactory())
    elif current_os == "Darwin":
        client(MacPlayerComponentFactory())
    else:
        print("OS not supported")










