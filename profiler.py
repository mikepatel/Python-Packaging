"""
Michael Patel
September 2021

Project description:

File description:

"""
################################################################################
# Imports
import os
from werkzeug.middleware.profiler import ProfilerMiddleware
from app import server


################################################################################
# Main
if __name__ == "__main__":
    # add profiler configurations
    server.config["PROFILE"] = True
    server.wsgi_app = ProfilerMiddleware(
        app=server.wsgi_app,
        restrictions=[10],
        profile_dir=os.path.join(os.getcwd(), "stats")
    )
    server.run(debug=True)
