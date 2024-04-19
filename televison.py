class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        self.__status = not self.__status

    def mute(self) -> None:
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        When the tv is on.
        This is where the channel is by one channel at a time.
        else: is when the maximun chanel is hit it goes back up to minimum chanel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This is when the channel is being turned down by one channle at a time.
        If the channel reaches the min channel then the television will go back up to
        the max channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """ this is when the tv is turned on and the volume is unmuted
        the volume goes up  by one till it reaches its max volume"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This is when the televison is turned on and the volume is unmuted
        the volume goes down till it reaches its minimum value.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Here we have set  the values of the television."""
        if self.__muted:
            return (f'Power = {self.__status}, '
                    f'Channel = {self.__channel}, '
                    f'Volume = {Television.MIN_VOLUME}')
        else:
            return (f'Power = {self.__status}, '
                    f'Channel = {self.__channel}, '
                    f'Volume = {self.__volume}')
