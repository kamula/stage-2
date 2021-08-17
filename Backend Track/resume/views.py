from django.shortcuts import render
from . forms import MessageForm

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()        
    return render(request,'resume/index.html')
