# coding: utf8
from applications.init.modules.sets import *

is_phone = IS_MATCH('^(\+\d{2}\-)?[\d\-]*(\#\d+)?$')

try:
    db=DAL('gae')
    session.connect(request,response,db=db)
except:
    db=DAL("sqlite://dba.db")

db.define_table('auth_user',
    Field('first_name','string'),
    Field('last_name','string'),
    Field('email','string'),
    Field('employed','date'),
    Field('montly','integer'),
    Field('password','string'),
    Field('registration_key','string'),
    Field('reset_password_key','string'))

db.auth_user.first_name.label=T("Name")
db.auth_user.last_name.label=T("Surname")
db.auth_user.email.label=T("E-mail")
db.auth_user.email.requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'auth_user.email')]
db.auth_user.employed.label=T("Employed date")
db.auth_user.montly.label=T("Montly wage")
db.auth_user.password.label=T("Password")
db.auth_user.registration_key.label=T("Registration key")
db.auth_user.reset_password_key.label=T("Reset password key")
"""
success!
timestamp: 2010-08-07T17:52:30.549207
CREATE TABLE auth_group(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role CHAR(512),
    description TEXT
);
success!
timestamp: 2010-08-07T17:52:30.659899
CREATE TABLE auth_membership(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    group_id INTEGER REFERENCES auth_group(id) ON DELETE CASCADE
);
success!
timestamp: 2010-08-07T17:52:30.777639
CREATE TABLE auth_permission(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER REFERENCES auth_group(id) ON DELETE CASCADE,
    name CHAR(512),
    table_name CHAR(512),
    record_id INTEGER
);
success!
timestamp: 2010-08-07T17:52:30.873507
CREATE TABLE auth_event(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_stamp TIMESTAMP,
    client_ip CHAR(512),
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    origin CHAR(512),
    description TEXT
);
"""
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
db.customers.address_num.label=T("Number")
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
db.works.description.label=T("description")
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


from gluon.tools import Mail, Auth, Recaptcha

auth = Auth(globals(), db)
#from gluon.contrib.login_methods.gae_google_account import GaeGoogleAccount
#auth.settings.login_form = GaeGoogleAccount()
auth.settings.create_user_groups = False
## ask it to create all necessary tables
auth.define_tables()
auth.settings.mailer = mail

mail = Mail()
## specify your SMTP server
mail.settings.server = 'gae'
mail.settings.sender = 'uis@grimp.eu'
mail.settings.login = 'uis@Z27392'

from gluon.tools import Crud
crud = Crud(globals(),db)


###DEFAULT VALUES
#admin=auth.add_group('admin', 'can access to all actions')
#auth.add_permission(admin, 'admin')
#auth.add_permission(admin, 'manager')
#auth.add_permission(admin, 'hr')
#auth.add_permission(admin, 'crew')
#manager=auth.add_group('manager', 'can access to managerial actions')
#auth.add_permission(manager, 'manager')
#auth.add_permission(manager, 'crew')
#hr=auth.add_group('hr', 'can access to all human resources action')
#auth.add_permission(hr, 'hr')
#auth.add_permission(hr, 'crew')
#crew=auth.add_group('crew', 'can access to all basic action')
#auth.add_permission(crew, 'crew')
