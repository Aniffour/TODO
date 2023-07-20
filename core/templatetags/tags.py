from django import template

register = template.Library()    

def IS(V1 ,V2): 
    return True if V1==V2 else False