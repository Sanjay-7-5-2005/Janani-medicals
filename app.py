import os
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

mail = Mail(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        try:
            # Get form data
            phone = request.form.get('phone')
            address = request.form.get('address')
            remarks = request.form.get('remarks', '')
            
            if not phone or not address:
                return jsonify({'error': 'Phone number and address are required.'}), 400

            # Handle file upload
            if 'prescription' not in request.files:
                return jsonify({'error': 'No file part'}), 400
            
            file = request.files['prescription']
            
            if file.filename == '':
                return jsonify({'error': 'No selected file'}), 400
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Construct Email
                recipient = os.getenv('RECIPIENT_EMAIL')
                msg = Message(f"New Order from {phone}", recipients=[recipient])
                msg.body = f"""
New Order Received:

Phone Number: {phone}
Delivery Address: {address}
Remarks: {remarks}

Please find the prescription attached.
"""
                # Attach file
                with app.open_resource(filepath) as fp:
                    msg.attach(filename, file.content_type, fp.read())
                
                # Send Email
                mail.send(msg)
                
                # Cleanup
                os.remove(filepath)
                
                return jsonify({'success': 'Order placed successfully!'}), 200
            else:
                return jsonify({'error': 'Invalid file type. Allowed: png, jpg, jpeg, gif'}), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('order.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
