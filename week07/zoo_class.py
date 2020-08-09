"""
定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。


"""

from abc import ABC ,abstractmethod

class Animal(ABC):
    shape1={'small':1,'middle':2,'big':3}
    kind=['carnivorous','herbivorous']
    shape=['small','middle','big']
    character=['ferocious','docile']
    
    @abstractmethod
    def __init__(self,kind,shape,character):
        super().__init__()
        self.kind=kind
        self.shape=shape
        self.character=character
    
    def is_pet(self):
        if self.shape>= 2 and kind == 'carnivorous' and character=='ferocious':
            self.is_pet=False
        else:
            self.is_pet=True

class Cat(Animal):
    voice='miao'
    def __init__(self, name,kind, shape, character):
        self.name=name
        super().__init__(kind, shape, character)
        if super().is_pet:
            self.is_pet=True
        else:
            self.is_pet=False

class Zoo():
    def __init__(self,name):
        self.name=name
        self.animal=[]

    def add_animal(self,animal):
        if animal in self.animal:
            print('had a same  animal ')
        else:
            self.animal.append(animal)
    @property
    def animals(self):
        for a in self.animal:
            print(f'{a.__class__.__name__}: {a.name}, id: {id(a)}')


def getattr(zoo, animal):
    if animal in zoo.animal:
        print(f"本动物园已经有{animal}这种动物了.")
        return True
    else:
        print(f"本动物园还没有{animal}这种动物.")
        return False


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2=Cat('small_cat','carnivorous','small','docile')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    z.animal
