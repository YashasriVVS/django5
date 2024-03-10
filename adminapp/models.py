from django.db import models

# Create your models here.
class  Admin(models.Model):
    id =models.AutoField(primary_key=True)
    username= models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
       db_table ="admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id= models.AutoField(primary_key=True)
    coursecode= models.CharField(max_length=50,blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    #.department=models.CharField(max_length=50, blank=False)

    academicyear_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"), ("2021-22", "2021-22"))

    academicyear = models.CharField(max_length=20, blank=False,choices=academicyear_choices)

    semester_choices = (("ODD-semester", "ODD"), ("EVEN-semester", "EVEN"), ("Summer", "EVEN"))

    semester= models.CharField(blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)

    class Meta:
       db_table ="Course_table"

    def __str__(self):
        return self.coursecode



class Student(models.Model):
    id= models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100, blank=False)

    gender_choices = (("Female", "Female"), ("Male", "Male"), ("Others", "Others"))
    gender=models.CharField(max_length=200, blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department=models.CharField(max_length=50, blank=False,choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"),("M.Tech", "M.Tech"),("B.com", "B.com"))
    program=models.CharField(max_length=10, blank=False,choices=program_choices)

    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"), ("SUMMER", "SUMMER"))
    semester=models.CharField(max_length=20, blank=False,choices=semester_choices)

    year=models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact= models.CharField(max_length=200,blank=False,unique=True)

    class Meta:
       db_table ="Student_table"

    def __str__(self):
        return str(self.studentid)



class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gender_choices = (("Female", "Female"), ("Male", "Male"), ("Others", "Others"))
    gender = models.CharField(max_length=20, blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)

    qualification_choices=(("MD", "MD"), ("PHD", "PHD"), ("Dr.", "Dr."))
    qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)

    designation_choices = (("Prof.", "Professor"), ("Assoc. Prof", "Assoc Professor"), ("Asst. Prof", "Assistant professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "Faculty_table"

    def __str__(self):
        return str(self.facultyid)

