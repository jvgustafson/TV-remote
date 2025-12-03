class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 5

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

    def volume_set(self, new_volume: int) -> None:
        """
        Method to set the volume of the Television object
        :param new_volume:
        """
        if not self.__status:
            return
        elif new_volume > Television.MAX_VOLUME or new_volume < Television.MIN_VOLUME:
            return

        if self.__muted:
            self.__muted = False
        self.__volume = new_volume

    def channel_set(self, new_channel: int) -> None:
        """
        Method to set the channel of the Television object
        :param new_channel:
        """
        if not self.__status:
            return
        elif new_channel > Television.MAX_CHANNEL or new_channel < Television.MIN_CHANNEL:
            return

        self.__channel = new_channel

    def volume_get(self) -> int:
        """
        Method to get the current volume of the Television object
        :return: volume value
        """
        return self.__volume

    def channel_get(self) -> int:
        """
        Method to get the current channel of the Television object
        :return: channel value
        """
        return self.__channel

    def isPowered(self) -> bool:
        """
        Method to check if the Television object is powered or not
        :return: true if on, false if off
        """
        return self.__status

    def isMuted(self) -> bool:
        """
        Method to check if the Television object is muted or not
        :return: true if muted, false if not muted
        """
        return self.__muted

    def __str__(self) -> str:
        """
        Method to format string for printing the Television object
        :return: Formated string of the Television object
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"