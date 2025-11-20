class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to initialize the Television class
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to power on or off the Television object
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to mute or unmute the Television object
        """
        if not self.__status:
            return

        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase the channel of the Television object
        """
        if not self.__status:
            return

        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the channel of the Television object
        """
        if not self.__status:
            return

        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the volume of the Television object
        """
        if (not self.__status) or self.__volume == Television.MAX_VOLUME:
            return

        if self.__muted:
            self.__muted = False
        self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume of the Television object
        """
        if (not self.__status) or self.__volume == Television.MIN_VOLUME:
            return

        if self.__muted:
            self.__muted = False
        self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to format string for printing the Television object
        :return: Formated string of the Television object
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"