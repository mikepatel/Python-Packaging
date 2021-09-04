"""
Michael Patel
September 2021

Project description:

File description:

"""
################################################################################
# Imports
from werkzeug.middleware.profiler import ProfilerMiddleware
from app import server


################################################################################
# Main
if __name__ == "__main__":
    # add profiler configurations
    server.config["PROFILE"] = True
    server.wsgi_app = ProfilerMiddleware(server.wsgi_app, restrictions=[10])
    server.run(debug=True)
