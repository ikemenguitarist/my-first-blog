from django.shortcuts import render

def link_list(request):
    return render(request, 'curation/link_list.html',{})
