# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for works managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 
    
@auth.requires_permission('crew')
def index():
    form=crud.create(db.partners)
    rows=db(db.partners.out==0).select(orderby=db.partners.name)
    return dict(rows=rows,form=form)

@auth.requires_permission('manager')
def add():
    form=crud.create(db.partners,next=url('index'))
    return dict(form=form)

@auth.requires_permission('manager')
def edit():
    row_id=request.args(0)
    row=db.partners[row_id]
    form=crud.update(db.partners,row,next=url('index'))
    return dict(form=form)
