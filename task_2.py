from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, c_for_counting):
        self.c_for_counting = c_for_counting

    @property
    def c_for_counting(self):
        return self.__c_for_counting

    @c_for_counting.setter
    def c_for_counting(self, c_for_counting):
        if c_for_counting > 3:
            self.__c_for_counting = 3
        elif c_for_counting < 1:
            self.__c_for_counting = 1
        else:
            self.__c_for_counting = c_for_counting

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def fabric_consumption(self):
        return self.c_for_counting / 6.5 + 0.5


class Suit(Clothes):
    def fabric_consumption(self):
        return self.c_for_counting * 2 + 0.3


if __name__ == "__main__":
    coat = Coat(5)
    suit = Suit(5)

    print(coat.fabric_consumption(), suit.fabric_consumption())
