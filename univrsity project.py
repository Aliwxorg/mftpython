class masters():
    location="tehran"
    _income=4200
    _income_model="contract"
    def __init__(self,name,family,lesson,id):
        self.name=name
        self.family=family
        self.lesson = lesson
        self._id=id
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i teach {self.lesson} and i live in {self.location} ")
    def secret_info(self):
        print(f"my income is {self._income} and my income model is {self._income_model} and my id is{self._id}")

# e1=masters("ali","asadi","math",98101)
# e1.info()
# e1.secret_info()

class masters_free(masters):
    location="another city"
    _income=1000
    _income_model="per hour"
    def __init__(self,name,family,lesson,id,hour,income):
        self.name=name
        self.family=family
        self.lesson = lesson
        self._id=id
        self.hour=hour
        self.income=income
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i teach {self.lesson} and i live in {self.location} ")
    def secret_info(self):
        print(f"my income is {self._income +(self.hour*self.income) } and my income model is {self._income_model} and my id is{self._id}")

# e1=masters_free("ali","asadi","math",98101,22,100)
# e1.info()
# e1.secret_info()

class masters_high(masters_free):
    location = "foreign countries"
    _income = 3000
    _income_model = "per hour"
    def __init__(self,name,family,lesson,id,hour,income):
        self.name=name
        self.family=family
        self.lesson = lesson
        self._id=id
        self.hour=hour
        self.income=income
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i teach {self.lesson} and i live in {self.location} ")
    def secret_info(self):
        print(f"my income is {self._income +(self.hour*self.income) } and my income model is {self._income_model} and my id is{self._id} ")

# e1=masters_high("ali","asadi","math",98101,22,100)
# e1.info()
# e1.secret_info()

class employee():
    location="tehran"
    income=3500
    income_model="contract"
    def __init__(self,name,family,part,id,num):
        self.name=name
        self.family=family
        self.part = part
        self.id=id
        self.num = num
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i work in  {self.part} and i live in {self.location} ")
    def secret_info(self):
        print(f"my income is {self.income} and my income model is {self.income_model} and my id is{self.id}  and my num is {self.num}")

# e1=employee("ali","asadi","education of material and metallurgy",98101,"09334706265")
# e1.info()
# e1.secret_info()


class employee_free(employee):
    location="tehran"
    _income=2000
    _income_model="per_hour"
    def __init__(self,name,family,part,hour,income,id,num):
        self.name=name
        self.family=family
        self.part = part
        self.hour=hour
        self.income=income
        self.id=id
        self.num = num
        
        
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i work in  {self.part} and i live in {self.location} ")
    def secret_info(self):
        print(f"my income is {self._income +( self.hour* self.income) } and my income model is {self.income_model} and my id is{self.id}  and my num is {self.num}")

e1=employee_free("ali","asadi","IT management",7,200,327,"09334706265")
e1.info()
e1.secret_info()

class faculty_boss():
    location="tehran"
    income=6000
    income_model="contract"
    def __init__(self,name,family,faculty,id,num):
        self.name=name
        self.family=family
        self.faculty = faculty
        self.id=id
        self.num = num
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i manage {self.faculty} ")
    def secret_info(self):
        print(f"my income is {self.income} ,and my id is {self.id} and my num is {self.num}")

# e1=faculty_boss("ali","asadi","material and metallurgy","98101")
# e1.info()
# e1.secret_info()

class university_boss():
    university="ELM V SANAT UNIVERSITY"
    n_employee=1200
    def __init__(self,name,family,num):
        self.name=name
        self.family=family
        self.num=num
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i manage {self.university} and my phone number is {self.num}")

# e1=university_boss("ali","asadi","09334706265")
# e1.info()

class student_tehran():
    location="tehran"
    university = "ELM V SANAT UNIVERSITY"
    def __init__(self,name,family,field,id,sex,num):
        self.name=name
        self.family=family
        self.field=field
        self.id=id
        self.sex=sex
        self.num=num
    def info(self):
        print(f"my name is {self.name} and my family is {self.family} and i study {self.field} in {self.university} and i live in {self.location}")
    def secret_info(self):
        print(f"my sex is {self.sex} and my id is {self.id} and my phone number is {self.num}")

# e1=student_tehran("ali","asadi","electrical engineering","98101","boy","09334706265")
# e1.info()
# e1.secret_info()



class student_city(student_tehran):
    location="another cities"
    university = "ELM V SANAT UNIVERSITY"
    def __init__(self,name,family,field,id,sex,num):
        self.name=name
        self.family=family
        self.field=field
        self.id=id
        self.sex=sex
        self.num=num

# e1=student_city("ali","asadi","electrical engineering","98101","boy","09334706265")
# e1.info()
# e1.secret_info()






