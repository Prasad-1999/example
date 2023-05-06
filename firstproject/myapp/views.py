from django.shortcuts import render
from django.http import HttpResponse


# def demo(request):
#     return HttpResponse("This is Helloworld app")

def demo(request):
    c = ""
    if request.method == "POST":
        n1 = eval(request.POST.get("a"))
        n2 = eval(request.POST.get("b"))
        opr = request.POST.get("opr")
        if opr == "+":
            c = n1+n2
        elif opr == "-":
            c = n1-n2
        elif opr == "*":
            c = n1*n2
        elif opr == "/":
            c = n1/n2
    return render(request, 'cal.html', {'c': c})
