# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for works managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 

@auth.requires_membership('hr')
def index():
    rows=db(db.auth_membership.id>0).select(orderby=db.auth_membership.id)
    return dict(rows=rows)

@auth.requires_membership('admin')
def add():
    form=crud.create(db.auth_membership,next=url('index'))
    return dict(form=form)

@auth.requires_membership('admin')
def edit():
    edit_id=request.args(0)
    edit=db.auth_membership[edit_id]
    form=crud.update(db.auth_membership,edit,next=url('index'))
    return dict(form=form)
