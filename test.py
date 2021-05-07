class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print()

student1=student('김주희',22)
student2=student('박주희',25)
student3=student('최주희',21)
student4=student('이주희',23)

student1.info()
student2.info()
student3.info()
student4.info()

