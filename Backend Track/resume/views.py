from django.shortcuts import render
from . forms import MessageForm

def index(request):
    context = {}
    alert = 0
    if request.method == 'POST':
        alert = alert               
        form = MessageForm(request.POST)
        if form.is_valid():            
            form.save()
            alert = 1            
            context['message'] = "response saved successfully" 
            context['alert'] = alert                
    context['alert'] = alert        
    return render(request,'resume/index.html',context)    
    
