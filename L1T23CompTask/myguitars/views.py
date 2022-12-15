from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def bacchus(request):
    return render(request, 'bacchus.html')

def ebmm(request):
    return render(request, 'ebmm.html')

def prs(request):
    return render(request, 'prs.html')

def rk(request):
    return render(request, 'rk.html')

def strat(request):
    return render(request, 'strat.html')

def gower(request):
    return render(request, 'gower.html')

def slo(request):
    return render(request, 'slo.html')

def vids(request):
    return render(request, 'vids.html')