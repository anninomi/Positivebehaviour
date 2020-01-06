from django.shortcuts import render, redirect
from form_fba.forms import FbaForm
from form_fba.models import Fba
# Create your views here.


def std(request):
    if request.method == "POST":
        form = FbaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = FbaForm()
    return render(request, 'fbaindex.html', {'form': form})


def view(request):
    form_fba = Fba.objects.all()
    return render(request, "view.html", {'form_fba': form_fba})

def delete(request, id):
    form_fba = Fba.objects.get(id=id)
    form_fba.delete()
    return redirect("/view")

def edit(request, id):
    form_fba = Fba.objects.get(id=id)
    return redirect(request, 'edit.html', {'form_fba': form_fba})
