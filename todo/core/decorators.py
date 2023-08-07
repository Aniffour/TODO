from django.shortcuts import redirect


def notAuth(func):
    def check( self , *args , **kargs): 
        if args[0].user.is_authenticated:
            return redirect('home')
        else :
            return func(args[0] , *args , **kargs)
    return check