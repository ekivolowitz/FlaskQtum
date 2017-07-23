import subprocess
import sys
import os

commandOptions = ["createcontract", "callcontract", "sendtocontract", "getaccountinfo", "listcontracts",
                  "reservebalance", "getstakinginfo", "gethexaddress", "fromhexaddress"]

def processCommand(command, arguments):
    # cli = os.getenv("HOME") + "/Desktop/qtum/src/qtum-cli"
    cli = "./qtum/src/qtum-cli"

    if command in commandOptions:
        _command = [cli, command]
        for x in arguments:
            _command.append(x)

        print("\n\n\n" + str(_command) + "\n\n\n")
        returnProcess = subprocess.run(_command, stdout=subprocess.PIPE)
        return str(returnProcess.stdout)
    raise Exception("ERROR: COMMAND NOT FOUND IN qtum-cli")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("ERROR: too few arguments. At least 3 required.")
    cli = sys.argv[1]
    args = sys.argv[2:]
    returnValue = processCommand(cli, args)
