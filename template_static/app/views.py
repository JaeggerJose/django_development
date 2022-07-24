from django.shortcuts import render
from django.views.generic import View
import datetime

from pytz import UTC
# Create your views here.

class Index(View):
    def get(self, request):
        data = {}
        data['count'] = 20
        data['time'] = datetime.datetime.now()
        data['cut_str'] = "Hello-boy!" 
        data['first_big'] = "hello wrold"
        data['result'] = True
        data['ifnow'] = None
        data['dict_list'] =[{'name':'zh', 'age':139},{'name':'max','age':22}]
        data['float_num'] = 2.657384
        data['array'] = range(10)
        data['html_str'] = '<div style="background-color:red;width:50px;height:50px"></div>'
        data['url_str'] = 'bitte schau www.google.com'
        data['feature'] =  data['time'] + datetime.timedelta(hours=1)
        return render(request, 'index.html', data)