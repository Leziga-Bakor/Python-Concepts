class A:
    __count = 0

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count


def main():
    
    a = A()
    print(a.get_count())

    a.__count = 42
    print(a.get_count())

    print(a.__count)

    a.set_count(50)
    print(a.get_count())

    print(a.__dict__)


if __name__ == "__main__":
    main()