from django.shortcuts import render, redirect



def wall(request):
    context = {

    }
    return render(request, 'wall.html', context)

def post_message(request):
    return redirect('/wall')

def post_comment(request):
    return redirect('/wall')