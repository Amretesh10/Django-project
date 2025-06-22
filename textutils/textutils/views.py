# I am creating this file - 

from django.http import HttpResponse

from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello")

# def index(request):
#     return HttpResponse('''<h1>Aman</h1> <a href="https://youtu.be/JgDNFQ2RaLQ?si=Iw8Kkomqdu8S9q08"> Django CodeWithAman</a>''')

def index(request):
    params = {'name': 'Aman', 'place': 'Mars'}
    return render(request, 'index.html', params)

    # return HttpResponse("Home")
def ex1(request):    
    s = '''<h2>Navigation Bar</h2><br>
    <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django Code With Harry Bhai</a><br>
    <a href="https://www.facebook.com/">Facebook</a><br>
    <a href="https://www.flipkart.com/">Flipkart</a><br>
    <a href="https://www.hindustantimes.com/">News</a><br>
    <a href="https://www.google.com/">Google</a><br>
    '''
    return HttpResponse(s)

def index2(request):
    return render(request, 'index2.html')
   
def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcount = request.POST.get('charcount','off')
    
    # Check which checkbox is on
    print("Remove Punctuation:", removepunc)
    # print("Text:", djtext)
    
    if removepunc == 'on':
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return HttpResponse("remove punc")
        # return render(request,'analyze.html',params)
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
             analyzed = analyzed + char
            
        params = {'purpose':'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if charcount == 'on':
        count = 0
        for char in analyzed:
            count += 1  # You can add conditions here to skip spaces, etc.
    
        
        params = {'purpose':'Number of Character', 'analyzed_text': count}
        djtext = analyzed
        # return render(request,'analyze.html',params)
        
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and charcount!='on'):
        return HttpResponse("Please select any operation and try again")
    
    return render(request,'analyze.html',params)
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremover(request):
#     return HttpResponse("spaceremover <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("charcount")


