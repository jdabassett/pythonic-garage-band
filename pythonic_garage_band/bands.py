

class Musician:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name}"

    def __repr__(self):
        return f"Name = {self.name}"

    def get_instrument(self)->str:
        return ""

    def play_solo(self)->str:
        return ""


class Guitarist(Musician):
    instrument="guitar"
    musician_type="guitarist"

    def __init__(self,name):
        super().__init__(name)

    def __str__(self) -> str:
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self) ->str:
        return f'{self.musician_type.title()} instance. Name = {self.name}'

    def get_instrument(self)->str:
        return f"{self.instrument}"

    def play_solo(self)->str:
        return "face melting guitar solo"



class Bassist(Musician):
    instrument="bass"
    musician_type="bassist"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self) -> str:
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self) ->str:
        return f'{self.musician_type.title()} instance. Name = {self.name}'

    def get_instrument(self)->str:
        return f"{self.instrument}"

    def play_solo(self)->str:
        return "bom bom buh bom"


class Drummer(Musician):
    instrument="drums"
    musician_type="drummer"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self) -> str:
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self) ->str:
        return f'{self.musician_type.title()} instance. Name = {self.name}'

    def get_instrument(self)->str:
        return f"{self.instrument}"

    def play_solo(self)->str:
        return "rattle boom crash"


class Keyboardist(Musician):
    def __int__(self,name:int):
        super().__init__(name)

    def __repr__(self):
        return """<ExceptionInfo TypeError("Can't instantiate abstract class Keyboardist with abstract method some_method_that_must_be_implemented_in_base_class") tblen=1>"""

class Band:
    instances=[]

    @classmethod
    def update_instances(cls,name):
        cls.instances.append(name)

    def __init__(self,name:str,members:list):
        self.name=name
        self.members=members
        self.update_instances(self.__repr__())

    def play_solos(self):
        list_solos = [member.play_solo() for member in self.members]
        return list_solos

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def to_list(cls):
        return cls.instances




