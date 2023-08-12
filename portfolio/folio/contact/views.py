from django.shortcuts import render

# Create your views here.
#view retounen paj fomile an
def contact_form(request) :
    return render(request,'contactPage.html')