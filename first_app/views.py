from django.shortcuts import render, HttpResponse, redirect # add render to import statement, add redirect to import statement
from django.http import JsonResponse


# Create your views here.

def index(request):
    if 'visits' not in request.session:  
      print("key 'visits' does NOT exist")
      request.session['visits'] = 1 
    else:
      print('key exists!')
      request.session['visits'] += 1

    if 'counter' not in request.session:    
        request.session['counter'] = 0 
    
    return render (request, 'index.html')



def destroy_session(request):
    try:
     del request.session['visits']
     del request.session['counter']
    except KeyError as e:
     print('error : ',e)
    # If either key doesn't exist, we'll just ignore the error
     #pass
    return redirect('/')


# NINJA BONUS
def increm_sess_two(request):
    request.session['counter'] += 2 
    return redirect("/")

# SENSEI BONUS
def specify_increment(request):
    if int(request.POST['visits'])>0:
            request.session['counter'] += int(request.POST['visits']) 
    return redirect("/")



