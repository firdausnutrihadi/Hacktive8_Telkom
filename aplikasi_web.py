import flask
from markupsafe import escape
from flask import render_template
from flask import request

app=flask.Flask(__name__)

@app.route("/")
def Hello():
    return "Hello Telkom"
    
@app.route("/hello")
def Hello_wolrd():
    return "Hello Telkooooooom"

@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return "User %s" % escape(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post %d" % post_id

@app.route("/jakarta")
def jakarta():
    return render_template("jakarta.html")

@app.route('/gambar', methods=['POST', 'GET'])
def upload_picture():
    if request.method == "POST":
        # prediksi gambar kucing atau anjing
        f = request.files['gambar']
        f.save('gambar.jpg')
        return "Sudah disimpan gambarnya"
    return render_template("gambar.html")

@app.route("/me")
def me_api():
    return {
        "username": "haha",
        "theme": "dark",
        "image": "kucing.jpg",
    }

if __name__ == "__main__":
    app.run(debug=True)