from flask import Flask
from optparse import OptionParser
from digiez_api import app


if __name__ == "__main__":
    # Run with docker
    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug", default=False,
                      action="store_true", help="Use debug option")
    options, args = parser.parse_args()
    # app.run(debug=options.debug, host='0.0.0.0',
    #         port=5001)
    app.run(debug=True, port=5001)
