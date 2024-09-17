from flask import Flask, render_template, request, jsonify
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Parse JSON data from the request body
    data = request.get_json()
    
    # Ensure the data is in the correct format
    if not data:
        return jsonify({'success': False, 'error': 'Invalid JSON format'}), 400

    # Extract form fields
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Validate form fields
    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'All fields are required'}), 400

    try:
        # Connect to the PostgreSQL database
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert form data into the 'contacts' table
        cur.execute(
            "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return a JSON response
        return jsonify({'success': True}), 200

    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
