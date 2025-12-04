from gui import *
from PyQt6.QtWidgets import *
from television import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, tv: Television) -> None:
        """
        Method to initialize the main window
        :param tv: television object to be initialized in main
        """
        super().__init__()
        self.setupUi(self)
        self.tv = tv

        # widget connects
        self.button_power.clicked.connect(lambda: self.togglePower())
        self.button_mute.clicked.connect(lambda: self.toggleMute())
        self.button_volume_up.clicked.connect(lambda: self.increaseVolume())
        self.button_volume_down.clicked.connect(lambda: self.decreaseVolume())
        self.button_channel_up.clicked.connect(lambda: self.increaseChannel())
        self.button_channel_down.clicked.connect(lambda: self.decreaseChannel())
        self.slider_volume.valueChanged.connect(lambda: self.setVolume())
        self.slider_channel.valueChanged.connect(lambda: self.setChannel())

    def togglePower(self) -> None:
        """
        Method to toggle power of tv object when the power button is pressed,
        sliders are disabled and the tv screen is black when the tv is off
        """
        self.tv.power()

        if self.tv.isPowered():
            self.slider_volume.setEnabled(True)
            self.slider_channel.setEnabled(True)
            self.stacked_widget_screen.setCurrentIndex(self.tv.channel_get())
        else:
            self.slider_volume.setEnabled(False)
            self.slider_channel.setEnabled(False)
            self.stacked_widget_screen.setCurrentIndex(0)

    def toggleMute(self) -> None:
        """
        Method to toggle mute on tv object when the mute button is pressed,
        the volume slider and buttons are disabled when the tv is on and muted
        """
        self.tv.mute()

        if not self.tv.isPowered():
            return
        if self.tv.isMuted():
            self.slider_volume.setEnabled(False)
            self.button_volume_up.setEnabled(False)
            self.button_volume_down.setEnabled(False)
        else:
            self.slider_volume.setEnabled(True)
            self.button_volume_up.setEnabled(True)
            self.button_volume_down.setEnabled(True)

    def increaseVolume(self) -> None:
        """
        Method to increase the volume of the tv object when the increase volume button is pressed,
        also adjusts the volume slider accordingly
        """
        self.tv.volume_up()
        self.slider_volume.setValue(self.tv.volume_get())

    def decreaseVolume(self) -> None:
        """
        Method to decrease the volume of the tv object when the decrease volume button is pressed,
        also adjusts the volume slider accordingly
        """
        self.tv.volume_down()
        self.slider_volume.setValue(self.tv.volume_get())

    def increaseChannel(self) -> None:
        """
        Method to increase the channel of the tv object when the increase channel button is pressed,
        also adjusts the channel slider and screen display accordingly
        """
        self.tv.channel_up()
        if not self.tv.isPowered():
            return
        self.slider_channel.setValue(self.tv.channel_get())
        self.stacked_widget_screen.setCurrentIndex(self.tv.channel_get())

    def decreaseChannel(self) -> None:
        """
        Method to decrease the channel of the tv object when the decrease channel button is pressed,
        also adjusts the channel slider and screen display accordingly
        """
        self.tv.channel_down()
        if not self.tv.isPowered():
            return
        self.slider_channel.setValue(self.tv.channel_get())
        self.stacked_widget_screen.setCurrentIndex(self.tv.channel_get())

    def setVolume(self) -> None:
        """
        Method to set the volume of the tv object to the value of the volume slider
        """
        self.tv.volume_set(self.slider_volume.value())

    def setChannel(self) -> None:
        """
        Method to set the channel of the tv object to the value of the channel slider,
        also adjusts the screen display accordingly
        """
        self.tv.channel_set(self.slider_channel.value())
        self.stacked_widget_screen.setCurrentIndex(self.tv.channel_get())