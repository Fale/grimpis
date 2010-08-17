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
    filter_customer = request.vars.c
    if filter_customer == None:
        rows=db(db.works.id>0).select(orderby=db.works.name)
    else:
        rows=db(db.works.customer==filter_customer).select(orderby=db.works.name)
    return dict(rows=rows)

@auth.requires_permission('manager')
def add():
    form=crud.create(db.works,next=url('index'))
    return dict(form=form)

@auth.requires_permission('manager')
def edit():
    works_id=request.args(0)
    works=db.works[works_id]
    form=crud.update(db.works,works,next=url('index'))
    return dict(form=form)
