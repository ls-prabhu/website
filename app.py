from flask import Flask, render_template, request, redirect

app = Flask(__name__)

bookings_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    # --- THESE LINES MUST BE INDENTED (Press Tab) ---
    name = request.form.get('name')
    card = request.form.get('ration_no')
    
    if name and card:
        bookings_list.append({'name': name, 'card_no': card})
        return render_template('success.html', name=name)
    
    return redirect('/')
    # ------------------------------------------------

@app.route('/admin')
def admin():
    return render_template('admin.html', all_bookings=bookings_list)

if __name__ == '__main__':
    app.run(debug=True)
