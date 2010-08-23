# coding: utf8
# try something like

@auth.requires_login()
def index():
    return dict()

def user():
    return dict(form = auth())

#@auth.requires_permission('admin')
def data():
    return dict(form = crud())
