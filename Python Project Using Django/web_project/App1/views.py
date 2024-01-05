# from django.contrib.auth import authenticate, adminLogin
# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import studentInfo, adminUser,tenantUser
# from .form import tenantUserForm

# from . form import studentForm

# Create your views here.

def update(request,id):
    # student_set=studentInfo.objects.all
    student_update=studentInfo.objects.get(id=id)
    return render(request,'Update.html',{'students':student_update})

def add(request):
    if request.POST:
        name=request.POST.get('stu_name')
        classDetails=request.POST.get('stu_class')
        address=request.POST.get('stu_address')
        obj=studentInfo(name=name,classDetails=classDetails,address=address)
        obj.save()
    
   
    # if request.POST:
    #     frm = studentForm(request.POST)
    #     if frm.is_valid:
    #         frm.save()
    #     else:
    #         frm.studentForm()
    
    return render(request,'Add.html')

def list(request):
    student_set=studentInfo.objects.all
    print(student_set)
    return render(request,'List.html',{'students':student_set})

def delete(request,id):
    student_del=studentInfo.objects.get(id=id)
    student_del.delete()
    student_set=studentInfo.objects.all
    return render(request,'List.html',{'students':student_set})



def loginDetails(request):
    
    if request.method == 'POST':
        adminEmail=request.POST.get('adminEmail')
        print(adminEmail)
        adminPassword=request.POST.get('adminPassword')
        adminUser_set=adminUser.objects.all
        mydata = adminUser.objects.filter(adminEmail='adminEmail').values()
        if adminUser.objects.filter(adminEmail=adminEmail, adminPassword=adminPassword).values():
                print(mydata)
                return render(request, "rentalDashboard.html")
        else:
                 return render(request, "adminLogin.html")
        
       
        
    else:
        return render(request, 'adminLogin.html')                     
       

def signDetails(request):  
    if request.POST:
        adminUserName=request.POST.get('adminUserName')
        adminUserCountry=request.POST.get('adminUserCountry')
        adminUsernumber=request.POST.get('adminUsernumber')
        adminPassword=request.POST.get('adminPassword')
        adminConfirmPassword=request.POST.get('adminConfirmPassword')
        adminGender=request.POST.get('adminGender')
        adminEmail=request.POST.get('adminEmail')
        obj=adminUser(adminUserCountry=adminUserCountry,adminUserName=adminUserName,adminUsernumber=adminUsernumber,adminPassword=adminPassword,
                        adminConfirmPassword=adminConfirmPassword,adminGender=adminGender,adminEmail=adminEmail)
        obj.save()  
    return render(request,'adminSign.html')

def dashboardDetails(request):
    
    return render(request,'dashboard.html')
def rentalDashboard(request):
    
    return render(request,'rentalDashboard.html')
def about(request):
    
    return render(request,'about.html')



def rentaltypeDetail(request):
    tenantUser_set=tenantUser.objects.all
    print(tenantUser)
    return render(request,'rentaltypeDetail.html',{'tenantUser_set':tenantUser_set})
                   
       

def estateRegistrationlist(request):
    tenantUser_set=tenantUser.objects.all
    print(tenantUser)
    return render(request,'rentalDashboard.html',{'tenantUser_set':tenantUser_set})
                   
       

def estateRegistration(request):  
  
    if request.POST:
        tenantUserName=request.POST.get('tenantUserName')
        tenantUserProfile=request.POST.get('tenantUserProfile')
        tenantUserCountry=request.POST.get('tenantUserCountry')
        tenantUseremail=request.POST.get('tenantUseremail')
        tenantUsernumber=request.POST.get('tenantUsernumber')
        tenantadminUserAddress=request.POST.get('tenantadminUserAddress')
        monthRentDate=request.POST.get('monthRentDate')
        price=request.POST.get('price')
        agreementStartDate=request.POST.get('agreementStartDate')
        agreementEndDate=request.POST.get('agreementEndDate')
        rentalType=request.POST.get('rentalType')
        estatePic1=request.POST.get('estatePic1')
        estatePic2=request.POST.get('estatePic2')
        estatePic3=request.POST.get('estatePic3')
        estatePic4=request.POST.get('estatePic4')
        adminStatus=request.POST.get('adminStatus')
        foodService=request.POST.get('foodService')
        gymFacility=request.POST.get('gymFacility')
        
        obj1=tenantUser(tenantUserName=tenantUserName,tenantUserProfile=tenantUserProfile,tenantUserCountry=tenantUserCountry,
                      tenantUseremail=tenantUseremail,tenantUsernumber=tenantUsernumber,tenantadminUserAddress=tenantadminUserAddress,
                      monthRentDate=monthRentDate,price=price,agreementStartDate=agreementStartDate,agreementEndDate=agreementEndDate,
                      rentalType=rentalType,estatePic1=estatePic1,estatePic2=estatePic2,estatePic3=estatePic3,estatePic4=estatePic4,
                      adminStatus=adminStatus,foodService=foodService,gymFacility=gymFacility)
        obj1.save()  
        return render(request,'estateRegistration.html')
    else:
          return render(request,'estateRegistration.html')

