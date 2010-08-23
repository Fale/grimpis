# coding: utf8

def url(f,args=[]):
    return URL(r=request,f=f,args=args)

def button(text,action,args=[]):
    return SPAN('[',A(text,_href=URL(r=request,f=action,args=args)),']')
    
def limage(text,action,args=[]):
    return A(IMG(_src=URL(r=request,c='static',f='images/' + text)),_href=URL(r=request,f='action',args=args))

def loCimage(text,action,args=[]):
    return IMG(_src=URL(r=request,c='static',f='images/' + text), _onClick="jQuery('#" + action + "').slideToggle()")
