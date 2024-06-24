from flask import Flask, render_template, send_file, redirect
import psycopg2
import io

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Database connection details
DB_NAME = 'alvo_db'
DB_USER = 'alvo'
DB_PASSWORD = 'alvo'
DB_HOST = 'localhost'
DB_PORT = '5432'

def get_data():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT id_company, company_name, url, logo FROM company")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

@app.route('/logo/<int:company_id>')
def logo(company_id):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT logo FROM company WHERE id_company = %s", (company_id,))
    image_data = cur.fetchone()[0]
    cur.close()
    conn.close()
    return send_file(io.BytesIO(image_data), mimetype='image/png')

@app.route('/url/<int:company_id>')
def url(company_id):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT url FROM company WHERE id_company = %s", (company_id,))
    url = cur.fetchone()[0]
    print ("url=")
    cur.close()
    conn.close()
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
