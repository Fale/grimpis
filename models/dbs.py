# coding: utf8
from applications.init.modules.states import *

is_phone = IS_MATCH('^(\+\d{2}\-)?[\d\-]*(\#\d+)?$')

try:
    db=DAL("sqlite://dba.db")
except:
    db=DAL('gae')
    session.connect(request,response,db=db)

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
db.customers.address_state.requires = IS_IN_SET(STATES)
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
    Field('value','integer'),
    Field('cost','integer'))
    
db.works.name.label=T("Name")
db.works.customer.label=T("Customer")
db.works.customer.requires=IS_IN_DB(db,'customers.id','customers.name')
db.works.description.label=T("description")
db.works.assign_date.label=T("Assigned")
db.works.due_to_date.label=T("Due To")
db.works.value.label=T("Value")
db.works.cost.label=T("Cost")



db.define_table('users',
    Field('user','string'),
    Field('name','string'),
    Field('surname','string'),
    Field('employed','date'),
    Field('montly','integer'))

db.users.name.label=T("Name")
db.users.surname.label=T("Surname")
db.users.employed.label=T("Employed date")
db.users.montly.label=T("Montly wage")



db.define_table('hours',
    Field('work',db.works),
    Field('user',db.users),
    Field('start','datetime'),
    Field('finish','datetime'),
    Field('note','string'))
    
db.hours.work.label=T("Work")
db.hours.work.requires=IS_IN_DB(db,'works.id','%(name)s')
db.hours.user.label=T("Worker")
db.hours.user.requires=IS_IN_DB(db,'users.id','%(name)s %(surname)s')
db.hours.start.label=T("Starting time")
db.hours.finish.label=T("Finishing time")
db.hours.note.label=T("Notes")
