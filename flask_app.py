from flask import Flask
import qtum_cli

app = Flask(__name__)

@app.route('/')
def run_qtum_cli():
    arguments = []
    command = input("Select command from " + str(qtum_cli.commandOptions) + ": ")
    with open("args", 'r') as f:
        arguments.append(f.readline())
    otherArgs = input("Other arguments delimited by a space: ")
    otherArgs = otherArgs.split(" ")
    arguments.extend(otherArgs)

    return str(qtum_cli.processCommand(command, arguments))