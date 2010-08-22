# -*- coding: utf-8 -*- 

from applications.init.modules.sets import *
is_phone = IS_MATCH('^(\+)?(\+\d{2}\-)?[\d\-]*(\#\d+)?$')

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db = db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
else:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB
## if no need for session
# session.forget()

#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import *
mail = Mail()                                  # mailer
auth = Auth(globals(),db)                      # authentication/authorization
crud = Crud(globals(),db)                      # for CRUD helpers using auth
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    from gluon.contrib.login_methods.gae_google_account import GaeGoogleAccount
    auth.settings.login_form = GaeGoogleAccount()

auth.settings.table_user = db.define_table('auth_user',    
    Field('first_name', length=512,default=''),
    Field('last_name', length=512,default=''),
    Field('email', length=512,default='',
          requires = [IS_EMAIL(),IS_NOT_IN_DB(db,'auth_user.email')]),
    Field('employed', 'date', label=T("Employed date")),
    Field('montly', 'integer', label=T("Montly wage")),
    Field('password', 'password', readable=False,
          label='Password',
          requires=CRYPT(auth.settings.hmac_key)),
    Field('registration_key', length=512,
          writable=False, readable=False,default=''),
    Field('reset_password_key', length=512,
          writable=False, readable=False, default=''))

mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         # your email
mail.settings.login = 'username:password'      # your credentials or None

auth.settings.hmac_key = 'sha512:79799e9f-a589-4faf-8a4a-ffa8e67a7674'   # before define_tables()
auth.define_tables()                           # creates all needed tables
auth.settings.mailer = mail                    # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s to reset your password'

#########################################################################
## If you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, uncomment and customize following
# from gluon.contrib.login_methods.rpx_account import RPXAccount
# auth.settings.actions_disabled=['register','change_password','request_reset_password']
# auth.settings.login_form = RPXAccount(request, api_key='...',domain='...',
#    url = "http://localhost:8000/%s/default/user/login" % request.application)
## other login methods are in gluon/contrib/login_methods
#########################################################################

crud.settings.auth = None                      # =auth to enforce authorization on crud

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('customers',
    Field('name','string'),
    Field('piva','string'),
    Field('email','string'),
    Field('address_num','string'),
    Field('address_road','string'),
    Field('address_city','string'),
    Field('address_county','string'),
    Field('address_zip','string'),
    Field('address_state','string'),
    Field('mobile','string'),
    Field('phone','string'),
    Field('fax','string'))
    
db.customers.name.label=T("Name")
db.customers.name.requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'customers.name')]
db.customers.piva.label=T("P IVA")
db.customers.piva.requires=IS_NOT_EMPTY()
db.customers.email.label=T("E-Mail")
db.customers.address_num.label=T("Street Number")
db.customers.address_road.label=T("Street")
db.customers.address_city.label=T("City")
db.customers.address_county.label=T("County")
db.customers.address_zip.label=T("ZIP Code")
db.customers.address_state.label=T("State")
db.customers.address_state.requires = IS_IN_SET(STATES,[T(x) for x in STATES])
db.customers.address_state.default = "Italy"
db.customers.mobile.label=T("Mobile")
db.customers.mobile.requires=is_phone
db.customers.phone.label=T("Phone")
db.customers.phone.requires=is_phone
db.customers.fax.label=T("Fax")
db.customers.fax.requires=is_phone



db.define_table('works',
    Field('name','string'),
    Field('customer',db.customers),
    Field('description','string'),
    Field('assign_date','date'),
    Field('due_to_date','date'),
    Field('status','string'),
    Field('value','integer'),
    Field('cost','integer'))
    
db.works.name.label=T("Name")
db.works.customer.label=T("Customer")
db.works.customer.requires=IS_IN_DB(db,'customers.id','customers.name')
db.works.description.label=T("Description")
db.works.assign_date.label=T("Assigned")
db.works.due_to_date.label=T("Due To")
db.works.status.label=T("Status")
db.works.status.requires = IS_IN_SET(STATUS,[T(x) for x in STATUS])
db.works.status.default = "Open"
db.works.value.label=T("Value")
db.works.cost.label=T("Cost")



db.define_table('hours',
    Field('work',db.works),
    Field('user',db.auth_user),
    Field('type','string'),
    Field('start','datetime'),
    Field('finish','datetime'),
    Field('note','string'))
    
db.hours.work.label=T("Work")
db.hours.work.requires=IS_IN_DB(db,'works.id','%(name)s')
db.hours.user.label=T("Worker")
db.hours.user.requires=IS_IN_DB(db,'auth_user.id','%(first_name)s %(last_name)s')
db.hours.type.requires = IS_IN_SET(TYPES,[T(x) for x in TYPES])
db.hours.type.default = "Coding"
db.hours.start.label=T("Starting time")
db.hours.finish.label=T("Finishing time")
db.hours.note.label=T("Notes")

###DEFAULT VALUES
#if not db(db.auth_group.id>0).count():
#    admin=auth.add_group('admin', 'can access to all actions')
#    auth.add_permission(admin, 'admin')
#    auth.add_permission(admin, 'manager')
#    auth.add_permission(admin, 'hr')
#    auth.add_permission(admin, 'crew')
#    manager=auth.add_group('manager', 'can access to managerial actions')
#    auth.add_permission(manager, 'manager')
#    auth.add_permission(manager, 'crew')
#    hr=auth.add_group('hr', 'can access to all human resources action')
#    auth.add_permission(hr, 'hr')
#    auth.add_permission(hr, 'crew')
#    crew=auth.add_group('crew', 'can access to all basic action')
#    auth.add_permission(crew, 'crew')
#if not db(db.auth_membership.id>0).count():
#    auth.add_membership(1, 1)
