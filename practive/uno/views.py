from django.shortcuts import render
from django.views.generic import View
from .consts import MessagesType
# Create your views here.

class Message(View):
   def get(self, request, message_type):
      data = {}
      try:
         message_type_obj = MessagesType[message_type]
      except:
         data['error'] = 'didnt have this message'
         render(request, 'message.html', data)
      
      message = request.GET.get('message','') #message in () means the message in url
      if not message:      #execute when the (?message=''), (?) or (?abc)...etc.
         data['error'] = 'text cannot be empty'
         return render(request, 'message.html', data)
      
      data['message'] = message
      data['message_type'] = message_type_obj
      return render(request, 'message.html', data)