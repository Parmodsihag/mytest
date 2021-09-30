# i created this file
from django.http import HttpResponse
from django.shortcuts import render
from docxtpl import DocxTemplate
import datetime
from docx2pdf import convert
import mimetypes
import os

def index(request):
    return render(request, 'index.html')

def make_my(name, from_location, to_name, amount, quote_number, today, save_to):
    try:
        tpl = DocxTemplate("birthday\my_temp.docx")
        context = {
                'customer_name': name,
                'from_point': from_location,
                'to_point': to_name,
                'amount': amount,
                'mydate': today,
                'quote_no': quote_number
        }
        tpl.render(context)
        tpl.save(save_to)
    except:
        print('odifusfdoihgisudfhgoiudsfhgiuggdguvydsuiygfuiyd')


def make_quotes(request):
    try:
        customer_name_g = request.GET.get('customer_name', 'name')
        from_name_g = request.GET.get('from_name', 'from')
        to_name_g = request.GET.get('to_name', 'to')
        amount_g = request.GET.get('amount', 'amount')
        quote_number_g = request.GET.get('quote_number', 'quote Number')

        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #make file
        file_path_to_save = BASE_DIR + '/static/birthday/' +f'{customer_name_g}.docx'
        make_my(customer_name_g, from_name_g, to_name_g, amount_g, quote_number_g, datetime.date.today(), file_path_to_save)
        convert(file_path_to_save, BASE_DIR + '/static/birthday/' +f'{customer_name_g}.pdf')
        # Define text file name
        filename = f'{customer_name_g}.pdf'
        # Define the full file path
        filepath = BASE_DIR +'/static/birthday/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    except:
        return HttpResponse('hello')
