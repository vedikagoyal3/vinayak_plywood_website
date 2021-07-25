from django.shortcuts import render
from vp.forms import query_form
from django.contrib import messages
# Create your views here.


def main(request):
    form=query_form()
    forms=form

    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    # This iteration is necessary

    i=False
    if request.method=='POST':
        form=query_form(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Thanks,We will soon contact you')
            i=True
            return render(request,'home.html',{'forms':forms,'i':i})
        else:
            messages.error(request, 'Something went wrong please fill form again')
            i=True
            return render(request,'home.html',{'forms':forms,'i':i})

    i=False
    return render(request,'home.html',{'forms':form,'i':i})
