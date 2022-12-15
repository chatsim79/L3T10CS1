from django.shortcuts import render
# Create your viedef index(request):
def main(request):
    return render(request, "main.html")