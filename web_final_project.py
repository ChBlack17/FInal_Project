from flask import Flask, render_template, request
import giphypop
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)

#API Key from Giphy
giphy = os.environ['GIPHY_PUBLIC_API']

@app.route('/')
def index():
	name = request.values.get('name')
	greeting = "Hello {}".format(name)
	return render_template('results.html', greeting=greeting) 

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])

from forms import SearchForm

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()

@app.route('/results')
def results():
    for result in results:
    	print(result.media_url)
    	print(result.url)
 
# @app.route('/about')
# def about():
#    return render_template('about_page.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


# Need to use translate to turn search term into gif image



# You've decided to:

# Create a new Flask web app where users can search for GIFs by a specific term
# Search the Giphy API using the giphypop (Links to an external site.) library
# Display the results to the user using thumbnails with links to the full GIF url
# Use Git and Github for version control, and Heroku to host the website

