from django.shortcuts import render

# Create your views here.
def home(request):
    """
    This function requests and renders the named 
    html file.

    :param request built in function: Request
    :param html file, home.html: home.html page

    :returns: The rendered HTML file
    
    :rtype: Webpage,

    """
    return render(request, 'home.html')