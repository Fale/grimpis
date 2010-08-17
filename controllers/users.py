# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for works managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 
    
def index():
    form=crud.create(db.users)
    rows=db(db.users.id>0).select(orderby=db.users.name)
    return dict(rows=rows,form=form)

def add():
    form=crud.create(db.users,next=url('index'))
    return dict(form=form)

def edit():
    users_id=request.args(0)
    users=db.users[users_id]
    form=crud.update(db.users,users,next=url('index'))
    return dict(form=form)
