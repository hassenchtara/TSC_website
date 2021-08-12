from django.shortcuts import render
from .models import slide,produit
import random
L=slide.objects.all()
K=list(map(str,range(len(L))))
H=produit.objects.all()
F=[ i for i in H if i.Accueil ]
Fo=set('')
for i in range(5):
    Fo.add(random.choice(H))
def getcategory(q):
    s=set('')
    for i in q  :
        b = i.Category.replace(" ", "_")
        b = b.replace("'","_")
        s.add((b,i.Category))
    return s
def prods(q):
    N=[]
    for i in q :
        b = i.Category.replace(" ", "_")
        b = b.replace("'","_")
        N+=[(i,b)]
    return N

def getprod(name):
    for i in H :
        if str(i.name)==str(name) :
            return i
def getdescription(name):
    d=getprod(name).description
    N=d.split('///')
    A=[(i[:i.index(':')],i[i.index(':')+1:]) for i in N if ':' in i  ]
    B=[i for i in N if ':' not in i ]
    return (A,B)
def Accueil(request):
    context={'Accueil':'class=active','title':'Accueil','slides':zip(L,K) ,'id':K , 'produits': prods(F) ,'Categorys' : getcategory(F) , 'Fo':list(Fo) }
    return render(request,'Pages/Accueil.html',context)

def Services(request):
    context={'Services':'class=active','title':'Services', 'Fo':list(Fo) }
    return render(request,'Pages/Services.html',context)

def Produits(request):
    context={'Produits':'class=active','title':'Produits' , 'produits': prods(H) ,'Categorys' : getcategory(H) , 'Fo':list(Fo) }
    return render(request,'Pages/Produits.html',context)

def Contact(request):
    context={'Contact':'class=active','title':'Contact', 'Fo':list(Fo) }
    if request.method == "POST" :
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        print(email)
        return render(request,'Pages/emailFo.html',{})
    else:
        return render(request,'Pages/Contact.html',context)

def prod(request,name):
    context={'produit' : getprod(str(name)) ,'title': name  , 'list' : getdescription(name)[0] , 'description' : getdescription(name)[1] , 'Fo':list(Fo) }
    return render(request,'Pages/Prod.html', context)

def error_404_view(request,exception):
    context={'title': '404 error', 'Fo':list(Fo) }
    return render(request,'Pages/404.html',context)
