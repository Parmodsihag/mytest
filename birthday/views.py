# i created this file
from django.http import HttpResponse
from django.http.response import FileResponse
from django.shortcuts import render
from docxtpl import DocxTemplate
import datetime
from docx2pdf import convert
import mimetypes
import os

def index(request):
    return render(request, 'index.html')

def make_my(name, from_location, to_name, amount, quote_number, today):
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
    tpl.save(f'birthday\\new\{name}.docx')

def remove_temp():
    print('hello harsh bhai')

def make_quotes(request):
    customer_name_g = request.GET.get('customer_name', 'name')
    from_name_g = request.GET.get('from_name', 'from')
    to_name_g = request.GET.get('to_name', 'to')
    amount_g = request.GET.get('amount', 'amount')
    quote_number_g = request.GET.get('quote_number', 'quote Number')
    make_my(customer_name_g, from_name_g, to_name_g, amount_g, quote_number_g, datetime.date.today())
    convert(f'birthday\\new\{customer_name_g}.docx',f'static\\birthday\{customer_name_g}.pdf')
    # return HttpResponse('<a href="birthday\\new\parmod.pdf" download onclick=remove_temp> Download</a>')
    # params = {'name':customer_name_g}
    # return render(request, 'final.html', params=params)
    
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


# if __name__ == '__main__':
#     make_my('parmod', 'dhansu', 'hisar', '5000', '536', datetime.date.today())