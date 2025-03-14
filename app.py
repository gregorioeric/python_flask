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

if __name__ == "__main__":
    app.run(debug=True)