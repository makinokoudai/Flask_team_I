from flask import request,redirect,url_for,render_template,flash,session
from holiday import db
from holiday.models.mst_holiday import Holiday

holidaylist = session.query(Holiday.holiday).all()

print(holidaylist)