from flask import Flask, render_template, request, jsonify
from database import get_db_connection
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Check if all fields are present
    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'Missing fields'}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert the data into the 'contacts' table
        cur.execute(
            "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True}), 200

    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
