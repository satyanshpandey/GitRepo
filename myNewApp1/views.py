from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer , userSerializersModelData
from django.contrib.auth.models import User

# for ignoring dajngo csrf validation i'm using decorator 
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def EmployeeListViews(request):
    if request.method == 'GET':
        employeeDataFromModel = Employee.objects.all()
        serializedData = EmployeeSerializer(employeeDataFromModel , many=True)
        newData = serializedData.data
        print("data from satya new data: ",newData)
        # return HttpResponse("this is newData: ",newData,status=200)
        return JsonResponse(newData ,safe=False, status = 200)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        print("\n\n\n this is json_DatA____from__parser: ===>>>>---------",jsonData, "tttttttype: " , type(jsonData))
        # okay ,  now i have converted request data into dict data type , now i have to convert it into : serialized datat type :
        serializer = EmployeeSerializer(data = jsonData)
        print("\n\n\n\n this is request data after serialized form: ",serializer)
        if serializer.is_valid():
            serializer.save()
            
        
            return JsonResponse({"addingEmployee":"Added Successfully"},safe=False)
        else:
            return JsonResponse(serializer.errors , safe=False)

def GetEmployees(request):
    employees = Employee.objects.all()
    serializedData = EmployeeSerializer(employees , many=True)
    serializedData = serializedData.data
    print("Serialized data by serializeerrrr: -----------------------> ",serializedData)
    print("Employees from saatyansh pandey ji : ---->",employees)
    # return HttpResponse("this is emplyee details on browser bro's , ", employees)
    return JsonResponse(serializedData , safe=False , status=200)


def printAllusers(request):
    employee = User.objects.all()
    serialisedUser_data = userSerializersModelData(employee , many=True)
    print("this is serialized normal data without converting into JJSSOONN JSON type: ---->>>>>>>>>>>>>>>>> ",serialisedUser_data)
    new__user____serializedDataFrom_userModel = serialisedUser_data.data
    print("this is the UUUSer---->Data>>>>>>>> ",new__user____serializedDataFrom_userModel)
    return JsonResponse(new__user____serializedDataFrom_userModel , safe=False , status=200)
