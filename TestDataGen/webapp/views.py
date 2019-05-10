# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pydbgen import pydbgen
from faker import Faker
fake = Faker()

def index(request):
    state = fake.address()
    myDB = pydbgen.pydb()
    dataFrameGen = myDB.gen_dataframe(10, fields= ['state'])
    template = loader.get_template('TestDataGen/index.html')
    return HttpResponse(template.render({'data':dataFrameGen},request))