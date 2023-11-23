from flask import Flask

# create a flask server
app = Flask(__name__)


# add routes
@app.route("/", methods=["GET"])
def root():
  return "welcome to first webservice"


# start the application
app.run(host="0.0.0.0", port=9000)
