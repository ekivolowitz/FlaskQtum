import subprocess
import sys
import os

def processCommand(command, arguments):
    # cli = os.getenv("HOME") + "/Desktop/qtum/src/qtum-cli"
    cli = "./qtum/src/qtum-cli"
    commandOptions = ["createcontract", "callcontract", "sendtocontract", "getaccountinfo", "listcontracts",
        "reservebalance", "getstakinginfo", "gethexaddress", "fromhexaddress"]

    if command in commandOptions:
        commands = [cli, command]
        for x in arguments:
            commands.append(x)
        returnProcess = subprocess.run(commands, stdout=subprocess.PIPE)
        return returnProcess.stdout
    raise Exception("ERROR: COMMAND NOT FOUND IN qtum-cli")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("ERROR: too few arguments. At least 3 required.")
    cli = sys.argv[1]
    args = sys.argv[2:]
    returnValue = processCommand(cli, args)
