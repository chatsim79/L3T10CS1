from django.shortcuts import render
# Create your viedef index(request):
def main(request):
    """
    This function, requests and renders the named 
    html file

    :param request: request command
    :param main.html: html file to be rendered.

    :rtype: returns rendered html
    """    
    return render(request, "main.html")