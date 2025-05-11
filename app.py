from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = []
# streamlit

@app.route("/")
def home():    
    return render_template("index.html", send=users)

@app.route("/cadastro", methods=["POST"])
def cadastro():
    data = request.form.to_dict()
    # data2 = request.get_json()
    # print(data2)
    if "nome" not in data:
        return render_template("index.html")

    users.append(data)
    print(data)
    return render_template("index.html", send=users)

@app.route('/edit')
def edit():
    return render_template('edit_user.html')

@app.route('/listUsers')
def list_users():
    return render_template('list_user.html')

@app.route('/api/listUsers')
def list_users():
    return render_template('list_user.html')

if __name__ == "__main__":
    app.run(debug=True)