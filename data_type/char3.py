'''
学校人事管理系统
基本人员ADT设计
ADT Person：
    Person(self,strname,strsex,tuple birthday,str ident)#构造
    id(self)#解析
    name(self)
    sex(self)
    birthday(self)
    age(self)
    <(self,Person another)
    details(self)
    set_name(self,str name)#修改
学生
ADT Student(Person):
    Student(self,strname,strsex,tuple birthday,str department)#构造
    department(self)#院系
    en_year(sefl)#入学年度
    scores(self）#成绩单
    set_course(self,str course_name)
    set_score(self,str course_name,int score)
教职工
ADT staff(Person):
    Staff(self,strname,strsex,tuple birthday,tuple entry_date)
    department(self)
    salary(self)
    entry_date(self)
    position(self)
    set_salary(self,int amount)
'''
import datetime


# 首先定义异常类
class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person:
    _num = 0  # 实例计数

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and isinstance(ident, str) and sex in ('男', '女')):
            raise PersonTypeError
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError
        self._name = name  # 设置成私有变量的一个好处是只能够通过方法访问，而且无法通过属性赋值修改
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonTypeError
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError
        return self._id < another._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return ' '.join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ','.join(('编号' + self._id,
                         '姓名' + self._name,
                         '性别' + self._sex,
                         '出生日期' + str(self._birthday)))


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        # super().__init__(name, sex, birthday,Student._id_gen())
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        if not isinstance(department, str):
            raise PersonValueError
        self._enroll_date = datetime.date.today()
        self._courses = {}
        self._department = department

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('NO THIS COURSE SELECTED')
        if score not in range(0, 101):
            raise PersonValueError('SCORE REEOR')
        self._courses[course_name] = score

    def scores(self):
        return [(coursename, self._courses[coursename]) for coursename in self._courses]

    def details(self):
        return ','.join((Person.details(self),
                         '入学日期' + str(self._enroll_date),
                         '学院' + self._department,
                         '课程记录' + str(self.scores())))
