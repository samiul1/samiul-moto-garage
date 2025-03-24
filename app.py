from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garage.db'
db = SQLAlchemy(app)

# Database Model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bike_model = db.Column(db.String(100), nullable=False)
    problem = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="Pending")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        bike_model = request.form['bike_model']
        problem = request.form['problem']
        phone = request.form['phone']
        email = request.form['email']
        booking_date = request.form['booking_date']

        new_booking = Booking(name=name, bike_model=bike_model, problem=problem, 
                              phone=phone, email=email, booking_date=booking_date)
        db.session.add(new_booking)
        db.session.commit()

        flash('✅ বুকিং সফলভাবে সম্পন্ন হয়েছে!', 'success')
        return redirect(url_for('home'))

    return render_template('booking.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
