# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = "Grimp IS"
response.subtitle = T('Grimp Informative System')
response.version = "0.3"

##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Index'), False, URL(request.application,'default','index'), []),
    (T('Customers'), False, URL(request.application,'customers','index'), []),
    (T('Works'), False, URL(request.application,'works','index'), []),
    (T('Users'), False, URL(request.application,'users','index'), []),
    (T('Groups'), False, URL(request.application,'groups','index'), []),
    (T('Membership'), False, URL(request.application,'membership','index'), []),
    (T('Hours'), False, URL(request.application,'hours','index'), [])
    ]

##########################################
## this is here to provide shortcuts
## during development. remove in production 
##
## mind that plugins may also affect menu
##########################################

#response.menu+=[
#    (T('Edit'), False, URL('admin', 'default', 'design/%s' % request.application),
#     [
#            (T('Controller'), False, 
#             URL('admin', 'default', 'edit/%s/controllers/%s.py' \
#                     % (request.application,request.controller=='appadmin' and
#                        'default' or request.controller))), 
#            (T('View'), False, 
#             URL('admin', 'default', 'edit/%s/views/%s' \
#                     % (request.application,response.view))),
#            (T('Layout'), False, 
#             URL('admin', 'default', 'edit/%s/views/layout.html' \
#                     % request.application)),
#            (T('Stylesheet'), False, 
#             URL('admin', 'default', 'edit/%s/static/base.css' \
#                     % request.application)),
#            (T('DB Model'), False, 
#             URL('admin', 'default', 'edit/%s/models/db.py' \
#                     % request.application)),
#            (T('Menu Model'), False, 
#             URL('admin', 'default', 'edit/%s/models/menu.py' \
#                     % request.application)),
#            (T('Database'), False, 
#             URL(request.application, 'appadmin', 'index')),
#            ]
#   ),
#  ]
