from django.shortcuts import redirect,render
from django.views import View
from account .models import Contact,Staff 
from .models import Students
from .forms import StudentForm,Students
from django.contrib import messages


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
# class Form(View):
#     def get(self,request):
#         return render(request,'form.html',{'form':std1})
class Enquiry(View):
    def get(self,request):
        customer = Contact.objects.all()
        return render(request,'enquiry.html',{'form':customer})

class Staffs(View):
    def get(self,request):
        customer=Staff.objects.all()
        return render(request,'staff.html',{'customer':customer})

class Student(View):
    def get(self,request):
        student=Students.objects.all()
        return render(request,'student.html',{'form':student})           

class Form(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'form.html',{'form':std1})
    def post(self,request):    
        if request.method == 'POST':
            std1 = StudentForm(request.POST)  
            if std1.is_valid():
               std1.save()
               student=Students.objects.all()
               return render(request,'student.html',{'form':student})
            else:
               print("form is not valid")  
            return redirect("student")        
        
class Show(View):
    def get(self,request):
        student=Students.objects.all()
        return render(request,'student.html',{'form':student})   


class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Students.objects.filter(student_id=edit1)
        return render(request,'edit.html',{'forms':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Students.objects.filter(student_id=edit1).exists():
                if request.POST.get('student_address'):
                    Students.objects.filter(student_id=edit1).update(Student_address=request.POST['student_address'])
                if request.POST.get('student_place'):
                    Students.objects.filter(student_id=edit1).update(Student_place=request.POST['student_place'])
                if request.POST.get('student_name'):
                    print(request.POST.get('student_name'))
                    Students.objects.filter(student_id=edit1).update(Student_name=request.POST['student_name'])
                if request.POST.get('student_email'):
                    Students.objects.filter(student_id=edit1).update(Student_email=request.POST['student_email'])
                if request.POST.get('student_phone'):
                    Students.objects.filter(student_id=edit1).update(Student_phone=request.POST['student_phone'])
                student=Students.objects.all()
                return render(request,'student.html',{'form':student})    
  
      
class EditProfile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1) 
        return render(request,'editprofile.html',{'forms':edit})
    def post(self,request):
        edit1=request.session['name']
        if request.method =='POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name']) 
                if request.POST['email']:
                    if Staff.objects.filter(email=edit1).exists():
                        edit=Staff.objects.filter(email=edit1)
                        return render(request,'editprofile.html',{'forms':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email']) 
                        request.session['email']=request.POST['email']        
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])      
                customer=Staff.objects.filter(name=request.session['name'])
                return render(request,'profile.html',{'customer':customer})            

class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Students.objects.filter(student_id=delete).delete()
        student=Students.objects.all()
        return render(request,'student.html',{'form':student})


class Forgot(View):
    def get(self,request):
        return render(request,'forgot.html')
    def post(self,request):
        if request.method == "POST":
            emails=request.POST['email']
            passwords=request.POST['password']
            if Staff.objects.filter(email=emails).exists():
                Staff.objects.filter(email=emails).update(password=passwords)
                return render(request,"signin.html")
            else:
                messages.error(request,"invalid email")
                return render(request,"forgot.html")    


class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer = Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})    