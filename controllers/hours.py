# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for hours managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 
    
def index():
    form=crud.create(db.hours)
    rows=db(db.hours.id>0).select(orderby=db.hours.work)
    return dict(rows=rows,form=form)

def add():
    form=crud.create(db.hours,next=url('index'))
    hours=db(db.hours.id>0).select(orderby=db.hours.work)
    return dict(hours=hours,form=form)

def edit():
    hours_id=request.args(0)
    hours=db.hours[hours_id]
    form=crud.update(db.hours,hours,next=url('index'))
    return dict(form=form)
