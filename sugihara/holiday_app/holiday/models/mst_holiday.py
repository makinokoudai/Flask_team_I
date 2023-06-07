from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'new_holiday'
    holiday = db.Column(db.Date,primary_key=True)
    holiday_text = db.Column(db.VARCHAR(20))
   
    def __init__(self,holiday=None,holiday_text=None):
        self.holiday = holiday
        self.holiday_text = holiday_text
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Holiday holiday{} holiday_text:{}>'.format(self.holiday,self.holiday_text)