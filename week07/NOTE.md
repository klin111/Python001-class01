学习笔记

第7周内容： 


#1. 类属性与对象属性

python 2.2 后 新式类：

类的两大成员：属性和类


类属性：一份内存，节约内存

对象属性：每个对象都有各自的属性，

实例是用不同的内存的，

用__dict__  可以获取  类，实例里面定义的属性(变量)

看类相关的：

type()     ， id()   ，    a.__class__()  ,b.__class__()， c.__bases__  

dir(),


#2. 类属性的作用域


_name   ： 人为约定不可修改，其实可改。
__name  ： 私有属性， 其实也可以修改。 其实被解释器重命名了。class.__dict____name__ ： 魔术方法， 变量属性随着环境变化。 不是用有带有双下画线开头和结尾的方法都是魔术方法，魔术方法类似其他语言的接口。


#3. 类方法 描述器

   三种方法：

3.1. 普通方法： 至少一个self 参数，表示该方法的对象(实例)，只能被实例调用。 
def instance_method(self):
	pass

3.2. 类方法：至少一个cls参数，表示该方法的类。 直接使用类名.调用。  也可以被实例使用。
什么情况使用呢？ 1. 当函数操作需要调用类的时候，并返回类。或者当类需要构造函数的时候。2. 定义在父类中，提供给子类需要时调用。
@classmethod #它就是构造函数，在类中有且只有一个默认的__new__ 构造函数。
def  class_method(cls):
	pass

3.3. 静态方法：由类调用，无参数，
@staticmethod
def  static_method():
	pass

绑定方法：    先找实例方法->再找 类方法->父类方法。

三种方法在内存中都归属于类

@ ： 语法糖， 在原有的语法上，增加了新的方法，让它更好用。


__init__():  初始化函数，用来接受参数，实例化的时候会默认执行下面的代码。

__new__(): 构造函数，

#4. 静态方法描述器

类型转换，特定的判断，

可以讲静态方法赋值给变量使用。

#5-6. 描述器高级应用__getattribute__  和 __getattr()__

__getarrt()__
_getattribute__

异同：
都可以对实例属性进行获取拦截

，__getarrt()__， 适用于未定义的属性,即不存在的属性。
，_getattribute__，对所有属性的访问都会调用该方法， super().__getattribute__()

产生AtributeError ，函数_getattribute__， 类的实例的属性描述符

它们顺序问题，同时存在时，先调用getattribute,再调用getattr, 如果没有属性，则继续找__dict__

__getattr__    https://docs.python.org/3/reference/datamodel.html#object.__getattr__
__getattribute__ https://docs.python.org/3/reference/datamodel.html#object.__getattribute__


#7.  描述器原理&属性描述符

[getattr和getattribute]
用于拦截变量的赋值，拦截实例化之后的变量赋值。它们底层用描述器来实现的，即特定的协议，底层是描述符 ，即__get__,

即 属性描述符 property  类， 实现__get__,__set__,__delete__ 等方法.  
Property  用处：1. 把函数或方法伪装为属性；2. 把读与写分离；

__get__  https://docs.python.org/3/reference/datamodel.html#object.__get__
__set__  https://docs.python.org/3/reference/datamodel.html#object.__set__
__delete__  https://docs.python.org/3/reference/datamodel.html#object.__delete__
@property https://docs.python.org/3/library/functions.html#property


#8. 面向对象编程-继承


封装，继承，【多态，重载】


新势类，经典类

object 和 type 的关系 
• object 和 type 都属于 type 类 (class 'type') 
• type 类由 type 元类自身创建的。object 类是由元类 type 创建 
• object 的父类为空，没有继承任何类 
• type 的父类为 object 类 (class 'object')


类的继承
• 单一继承 
• 多重继承 
• 菱形继承（钻石继承） :  广度优先(新式类)，深度优先(经典类)
• 继承机制 MRO ： 
• MRO 的 C3 算法：

super() :当前类的父类，

class.mro()  :  看类的继承顺序

多重继承的顺序问题
有向无环图：DAG(Directed Acyclic Graph)  用于判断继承顺序
• DAG 原本是一种数据结构，因为 DAG 的拓扑结构带来的优异特性，经常被用于处 理动态规划、寻求最短路径的场景。
入度为零的优先找： 被依赖的类的数量为零。

当两个类入度都相等，从左边开始找。



#9. solid设计原则与设计模式&单例模式
 设计原则： 设计的规则，静态语言。

• 单一责任原则 The Single Responsibility Principle ：一个类只能有一个被修改的理由，即只有单一的功能；
• 开放封闭原则 The Open Closed Principle ： 对扩展是开放的，对修改是封闭的。即不改以前的代码，而是增加代码比如classmethod。继承一个类，再对其修改重构；
• 里氏替换原则 The Liskov Substitution Principle： 在重写子类时，子类的方法要完整的覆盖父类的方法。 
• 依赖倒置原则 The Dependency Inversion Principle： 高层的模块不能依赖 底层模块，而用抽象连接它们。
• 接口分离原则 The Interface Segregation Principle：模块之间互相交流的协议，


设计模式：前人总结的软件设计经验。
. 设计模式用于解决普遍性问题 
. 设计模式保证结构的完整性


单例模式： 程序实例化的时候，只能出现一个实例。

__init__ 和 __new__ 的区别： 
• __new__ 是实例创建之前被调用，返回该实例对象，是静态方法
• __init__ 是实例对象创建完成后被调用，是实例方法 
• __new__ 先被调用，__init__ 后被调用 
• __new__ 的返回值（实例）将传递给 __init__ 方法的第一个参数，__init__ 给这个 实例设置相关参数。

用装饰器 实现 单实例；
__new__ 实现 单实例；
import   实现单实例；

#10. 工厂模式

工厂模式：  用一个初始化类，去调用不同的类，进而创建了不同的类的实例。
简单(静态)工厂模式：


动态工厂模式： 用函数动态的去创建类；

#11. 元类

在类创建的时候，可以拦截来增加其他功能的。 元类比工厂模式更方便的来创建类。 一般用于框架中；


• 元类是关于类的类，是类的模板。 
• 元类是用来控制如何创建类的，正如类是创建对象的模板一样。 
• 元类的实例为类，正如类的实例为对象 
• 创建元类的两种方法
    	1. class 
    	2. type 
• type（类名，父类的元组（根据继承的需要，可以为空，包含属性的字典（名字和值））


#12-1. 抽象基类

用在普通应用中，

抽象基类（abstract base class，ABC）用来确保派生类实现了基类中的特定方法。 
• 使用抽象基类的好处： 
• 避免继承错误，使类层次易于理解和维护。 
• 无法实例化基类。 
• 如果忘记在其中一个子类中实现接口方法，要尽早报错。


#12-2. mixin模式

在程序运行过程中，重定义类的继承，即动态继承。
好处： 
• 可以在不修改任何源代码的情况下，对已有类进行扩展
• 进行组件的划分
