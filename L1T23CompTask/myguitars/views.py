from django.shortcuts import render

def index(request):
    """
    This function, and all subsequent fn. in 
    this file requests and renders the named 
    html file.

    :param request built in function: Request
    :param html file, index.html: index.html page

    :returns: The rendered HTML file
    
    :rtype: Webpage,

    """
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