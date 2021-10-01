
from django.http import HttpResponse
from django.shortcuts import render
from docxtpl import DocxTemplate
import mimetypes
import os

def index(request):
    return render(request, 'index.html')


def make_my(name, from_location, to_name, amount, quote_number, today, contact_number, save_to):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tpl = DocxTemplate(f"{BASE_DIR}/birthday/my_temp.docx")
    context = {
                'customer_name': name,
                'from_point': from_location,
                'to_point': to_name,
                'amount': amount,
                'mydate': today,
                'quote_no': quote_number,
                'contact_num' : contact_number
     }
    tpl.render(context)
    tpl.save(save_to)




def make_quotes(request):

    customer_name_g = request.GET.get('customer_name', 'name')
    from_name_g = request.GET.get('from_name', 'from')
    to_name_g = request.GET.get('to_name', 'to')
    amount_g = request.GET.get('amount', 'amount')
    quote_number_g = request.GET.get('quote_number', 'quote Number')
    contact_number_g = request.GET.get('contact_number', 'contact_number')
    date_g = request.GET.get('mydate', 'mydate')

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #make file
    file_path_to_save = BASE_DIR + '/static/birthday/' +f'{customer_name_g}.docx'
    make_my(customer_name_g, from_name_g, to_name_g, amount_g, quote_number_g, date_g, contact_number_g, file_path_to_save)
    # Define text file name
    filename = f'{customer_name_g}.docx'
    # Define the full file path
    filepath = BASE_DIR +'/static/birthday/' + filename
    # Open the file for reading conten
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    os.remove(file_path_to_save)
    # Return the response value
    return response
