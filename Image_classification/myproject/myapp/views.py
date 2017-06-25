# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from myproject.myapp.getClass import Classification

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            url=newdoc.docfile.url
            obj = Classification()
            name = obj.imageClassification(newdoc.docfile.path)
            Predicted_image_name=name[0]

            # Redirect to the document list after POST
            return render(request,'abc.html',{"image_path" : url,"object_name" : Predicted_image_name})
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
