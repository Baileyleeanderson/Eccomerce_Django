from django.shortcuts import render, HttpResponse, redirect

def index(request):
  if not 'all_totals' in request.session:
    request.session['all_totals'] = 0
  return render(request,'amadon/index.html')

def buy(request): 
  items = request.POST['select']
  request.session['counter'] = 0
  

  if request.POST['ids'] == '1015':
    request.session['total'] = 19.99 * int(items)
    request.session['counter'] += 1
    request.session['all_totals'] += request.session['total']
  elif request.POST['ids'] == '1020':
    request.session['total'] = 29.99 * int(items)
    request.session['counter'] += 1
    request.session['all_totals'] += request.session['total']
  elif request.POST['ids'] == '1030':
    request.session['total'] = 4.99 * int(items)
    request.session['counter'] += 1
    request.session['all_totals'] += request.session['total']
  elif request.POST['ids'] == '1040':
    request.session['total'] = 49.99 * int(items)
    request.session['counter'] += 1
    request.session['all_totals'] += request.session['total']
    
  return redirect('/amadon/checkout')

def checkout(request):
  return render(request,'amadon/amadon.html')

def clear(request):
  del request.session['total']
  return redirect('/')




