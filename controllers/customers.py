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
    form=crud.create(db.customers)
    rows=db(db.customers.id>0).select(orderby=db.customers.name)
    return dict(rows=rows,form=form)

@auth.requires_permission('manager')
def add():
    form=crud.create(db.customers,next=url('index'))
    return dict(form=form)

@auth.requires_permission('manager')
def edit():
    customers_id=request.args(0)
    customers=db.customers[customers_id]
    form=crud.update(db.customers,customers,next=url('index'))
    return dict(form=form)
