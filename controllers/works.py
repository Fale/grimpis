# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for works managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 
    
def index():
    form=crud.create(db.works)
    rows=db(db.works.id>0).select(orderby=db.works.name)
    return dict(rows=rows,form=form)

def add():
    form=crud.create(db.works,next=url('index'))
    works=db(db.works.id>0).select(orderby=db.works.name)
    return dict(works=works,form=form)

def edit():
    works_id=request.args(0)
    works=db.works[works_id]
    form=crud.update(db.works,works,next=url('index'))
    return dict(form=form)
