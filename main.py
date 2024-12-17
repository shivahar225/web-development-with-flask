from flask import Flask

app = Flask(__name__)


#@app.route('/')
#def hellow_world():
    #return '<h1 style="text-align:center">hellow, world</h1>' \
     #      '<p>this is paragraph</p>'\
     #      '<img src=<div style=""width:480px"><iframe allow="fullscreen" frameBorder="0" height="640" src="https://giphy.com/embed/oEZfuntI6g3VMinO5y/video" width="480"></iframe></div>"width=200 />'

#if __name__ == "__main__":
#    app.run()

@app.route("/")
def say_bye():
    return '<u><em><b>Bye</b></em></u>'


if __name__ == "__main__":
    app.run()

#@app.route("/username/<name>")
#def greet(name):
 #   return f"f Hello {name}!"
#@app.route("/<name>")
#def greet(name):
  #  return f" Hello there {name + '12'}!"

#@app.route("/username/<name>/<int:number>")
#def greet(name,number):
 #   return f"f Hello {name} you are {number} old!"


#if __name__ == "__main__":
 #   app.run(debug=True)

#greet()


