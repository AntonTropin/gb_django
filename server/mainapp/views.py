from django.shortcuts import render

# Create your views here.

def main(requiest):
    return render(requiest, 'mainapp/index.html')

def support(requiest):
    return render(requiest, 'mainapp/support.html')
