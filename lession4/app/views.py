from django.shortcuts import render
from django.views.generic import View
# Create your views here.\
    

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Test(View):
    def get(self, request):
        memvalue = request.GET.get('memvalue', '1')
        cputhread = request.GET.get('cputhread', '1')
        cpucore = request.GET.get('cpucore', '1') 
        return render(request, 'test.php')