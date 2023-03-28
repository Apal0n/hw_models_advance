from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year

    class Meta:
        abstract = True
        ordering = ['name', ]


class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField(max_length=20)
    work_experience = models.DateField()

    def __str__(self):
        return self.position


class Passport(models.Model):
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=9)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self, inn):
        self.inn = inn
        if inn[0] == '1':
            return "Female"
        elif inn[0] == '2':
            return "Male"


class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)
    employees = models.ManyToManyField(Employee, related_name='work_projects', through='Membership')

    def __str__(self):
        return f"Название проекта {self.project_name}"


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f"Работник {self.employee} в проекте {self.work_project}"


class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()
