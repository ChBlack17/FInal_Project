from flask import Flask, render_template, request, url_for, redirect
import giphypop
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)

#API Key from Giphy
giphy = os.environ['GIPHY_PUBLIC_API']

@app.route('/')
def index():
	return render_template('results_true.html') 

@app.route('/results')
def results():
    for result in results:
    	print(result.media_url)
    	print(result.url)
 
@app.route('/about')
def about():
    return render_template('about_page.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


# Need to use translate to turn search term into gif image



# You've decided to:

# Create a new Flask web app where users can search for GIFs by a specific term
# Search the Giphy API using the giphypop (Links to an external site.) library
# Display the results to the user using thumbnails with links to the full GIF url
# Use Git and Github for version control, and Heroku to host the website




