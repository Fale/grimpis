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
    form=crud.create(db.auth_user)
    rows=db(db.auth_user.id>0).select(orderby=db.auth_user.last_name)
    return dict(rows=rows,form=form)

@auth.requires_permission('crew')
def add():
    form=crud.create(db.auth_user,next=url('index'))
    return dict(form=form)

@auth.requires_permission('crew')
def edit():
    edit_id=request.args(0)
    edit=db.auth_user[edit_id]
    form=crud.update(db.auth_user,edit,next=url('index'))
    return dict(form=form)
