from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4b7BK3m6?@localhost/flaskproject'

db= SQLAlchemy(app)

class Meeting(db.Model):
    __tablename__ = 'meetings'
    id = db.Column(db.Integer, primary_key= True)
    meeting_subject = db.Column(db.String(40))
    date = db.Column(db.String(40))
    s_time = db.Column(db.String(40))
    e_time = db.Column(db.String(40))
    participants = db.Column(db.String(40))

    def __init__(self, meeting_subject, date, s_time, e_time, participants):
        self.meeting_subject = meeting_subject
        self.date = date
        self.s_time = s_time
        self.e_time = e_time
        self.participants = participants
    
    def toString(self):
        return f"Meeting id: {self.id}\nSubject: {self.meeting_subject}\nDate: {self.date}\nStart time:{self.s_time}\nEnding time {self.e_time}\nParticipants {self.participants}\n "
    



@app.get("/")
def home():
    query_result = db.session.query(Meeting)
    return render_template('index.html', query = query_result.order_by(Meeting.id))

@app.route('/api/submitMeeting', methods = ['POST'])
def submit_meeting():
    meeting_subject = request.form['meeting_subject']
    date = request.form['date']
    s_time = request.form['s_time']
    e_time = request.form['e_time']
    participants = request.form['participants']

    meeting = Meeting(meeting_subject, date, s_time, e_time, participants)
    db.session.add(meeting)
    db.session.commit()

    query_result = db.session.query(Meeting)

    return render_template('index.html', query=query_result.order_by(Meeting.id))

@app.route('/api/editMeeting', methods=["POST"])
def update_meeting():
    meeting_id = request.form['meeting_id']
    wanted_meeting = db.session.query(Meeting).filter(Meeting.id==meeting_id)[0]

    if request.form['meeting_subject'] != "":
        wanted_meeting.meeting_subject = request.form['meeting_subject']
    if request.form['date'] != "":
        wanted_meeting.date = request.form['date']
    if request.form['s_time'] != "":
        wanted_meeting.s_time = request.form['s_time']
    if request.form['e_time'] != "":
        wanted_meeting.e_time = request.form['e_time']
    if request.form['participants'] != "":
        wanted_meeting.participants = request.form['participants']

    db.session.commit()


    query_result = db.session.query(Meeting)
    
    return  render_template('index.html', query=query_result.order_by(Meeting.id))
    
@app.route('/api/deleteMeeting', methods= ["GET"])
def delete_meeting():
    meeting_id = request.args.get('meeting_id')
    query = db.session.query(Meeting).filter(Meeting.id==meeting_id)[0]
    db.session.delete(query)
    db.session.commit()


    query_result = db.session.query(Meeting)
    return render_template('index.html',  query=query_result.order_by(Meeting.id))

if __name__ == "__main__":
    app.run(debug=True)