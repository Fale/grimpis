# -*- coding: utf-8 -*- 

#########################################################################
## This is the controller for works managment
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
######################################################################### 

#@auth.requires_permission('hr')
def index():
    rows=db(db.auth_group.id>0).select(orderby=db.auth_group.id)
    return dict(rows=rows)

#@auth.requires_permission('admin')
def add():
    form=crud.create(db.auth_group,next=url('index'))
    return dict(form=form)

#@auth.requires_permission('admin')
def edit():
    edit_id=request.args(0)
    edit=db.auth_group[edit_id]
    form=crud.update(db.auth_group,edit,next=url('index'))
    return dict(form=form)
