# coding: utf8
from applications.init.modules.sets import *

is_phone = IS_MATCH('^(\+\d{2}\-)?[\d\-]*(\#\d+)?$')

try:
    db=DAL('gae')
    session.connect(request,response,db=db)
except:
    db=DAL("sqlite://dba.db")
        
    passfield = auth.settings.password_field

db.define_table('auth_user',
    Field('first_name', length=128, label=T("Name")),
    Field('last_name', length=128, label=T("Surname")),
    Field('username', length=128, label=T("Username")),
    Field('email', length=512, label=T("E-mail")),
    Field('employed', 'date', label=T("Employed date")),
    Field('montly', 'integer', label=T("Montly wage")),
    Field('password', 'password', length=512, readable=False, label=T("Password")),
    Field('registration_key', length=512, writable=False, readable=False, label=T("Registration key")),
    Field('reset_password_key', length=512, writable=False, readable=False, label=T("Reset password key")),
    Field('registration_id', length=512, writable=False, readable=False, label=T("Registration ID")))
    
db.auth_user.username.requires = IS_NOT_IN_DB(db, 'auth_email.username')
db.auth_user.first_name.requires = IS_NOT_EMPTY()
db.auth_user.last_name.requires = IS_NOT_EMPTY()
#db.auth_user.password.requires = CRYPT(key=auth.settings.hmac_key)
#auth_user_table[passfield].requires = [CRYPT(key=auth.settings.hmac_key)]
db.auth_user.email.requires = IS_NOT_IN_DB(db, db.auth_user.email)
db.auth_user.registration_key.default = ''
auth.settings.table_user = db[auth.settings.table_user_name]
#db.auth_user.password.requires = [CRYPT(key=auth.settings.hmac_key)]
#auth.settings.table_user = db.auth_user

db.define_table( 'auth_group',
    Field('role', length=512, default='', label=auth.messages.label_role),
    Field('description', 'text', label=auth.messages.label_description),
    format = '%(role)s (%(id)s)')
db.auth_group.role.requires = IS_NOT_IN_DB(db, '%s.role' % auth.settings.table_group_name)
auth.settings.table_user = db.auth_group

db.define_table('auth_membership',
    Field('user_id', db.auth_user, label=auth.messages.label_user_id),
    Field('group_id', db.auth_group, label=auth.messages.label_group_id))
    
db.auth_membership.user_id.requires = IS_IN_DB(db, '%s.id' % db.auth_user, '%(first_name)s %(last_name)s (%(id)s)')
db.auth_membership.group_id.requires = IS_IN_DB(db, '%s.id' % db.auth_group, '%(role)s (%(id)s)')

"""
if not self.settings.table_permission_name in db.tables:
table = db.define_table(
    self.settings.table_permission_name,
    Field('group_id', self.settings.table_group,
            label=self.messages.label_group_id),
    Field('name', default='default', length=512,
            label=self.messages.label_name),
    Field('table_name', length=512,
            label=self.messages.label_table_name),
    Field('record_id', 'integer',
            label=self.messages.label_record_id),
    migrate=self.__get_migrate(
        self.settings.table_permission_name, migrate))
table.group_id.requires = IS_IN_DB(db, '%s.id' %
        self.settings.table_group_name,
        '%(role)s (%(id)s)')
table.name.requires = IS_NOT_EMPTY(error_message=self.messages.is_empty)
table.table_name.requires = IS_IN_SET(self.db.tables)
table.record_id.requires = IS_INT_IN_RANGE(0, 10 ** 9)
self.settings.table_permission = db[self.settings.table_permission_name]
if not self.settings.table_event_name in db.tables:
table  = db.define_table(
    self.settings.table_event_name,
    Field('time_stamp', 'datetime',
            default=self.environment.request.now,
            label=self.messages.label_time_stamp),
    Field('client_ip',
            default=self.environment.request.client,
            label=self.messages.label_client_ip),
    Field('user_id', self.settings.table_user, default=None,
            label=self.messages.label_user_id),
    Field('origin', default='auth', length=512,
            label=self.messages.label_origin),
    Field('description', 'text', default='',
            label=self.messages.label_description),
    migrate=self.__get_migrate(
        self.settings.table_event_name, migrate))
table.user_id.requires = IS_IN_DB(db, '%s.id' %
        self.settings.table_user_name,
        '%(first_name)s %(last_name)s (%(id)s)')
table.origin.requires = IS_NOT_EMPTY(error_message=self.messages.is_empty)
table.description.requires = IS_NOT_EMPTY(error_message=self.messages.is_empty)
self.settings.table_event = db[self.settings.table_event_name]
""""""
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
