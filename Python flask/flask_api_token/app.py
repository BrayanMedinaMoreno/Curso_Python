from flask import Flask,jsonify

app = Flask(__name__)




@app.route("/hola", methods=["GET"])
def hola():
    return jsonify({"message" : "endpoint desde hola"})


if __name__ == "__main__":
    app.run(debug=True,port=5000)
    
#https://www.youtube.com/watch?v=M-Q37rNGJ-0&ab_channel=RoCode
    