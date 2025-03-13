from flask import Flask

hello = Flask("hello")
@hello.route("/" , methods = ["GET"])
def say_hello() :

    return f"HELLO"

if __name__ == "__main__" :

    hello.run(debug = True , port=5000)
