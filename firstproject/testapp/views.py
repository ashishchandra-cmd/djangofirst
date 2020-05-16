from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def div(request):
    val1=int(request.GET["num1"])
    val2 =int( request.GET["num2"])
    # res=val1/val2
    try:
        res=val1/val2
    except ZeroDivisionError:
        res='infinity'    

    return render(request,"result.html",{"results":res})
