# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for hours managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 
    
def index():
    # form=crud.create(db.hours)
    filter_work = request.vars.w
    filter_user = request.vars.u
    if filter_work != None:
        rows=db(db.hours.work==filter_work).select(orderby=db.hours.work)
    elif filter_user != None:
        rows=db(db.hours.user==filter_user).select(orderby=db.hours.work)
    else:
        rows=db(db.hours.id>0).select(orderby=db.hours.work)
    # return dict(rows=rows,form=form)
    return dict(rows=rows)

def add():
    form=crud.create(db.hours,next=url('index'))
    return dict(form=form)

def edit():
    hours_id=request.args(0)
    hours=db.hours[hours_id]
    form=crud.update(db.hours,hours,next=url('index'))
    return dict(form=form)
