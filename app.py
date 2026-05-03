from flask import Flask, request, redirect, render_template
from models import db, URL
import shortuuid

app = Flask(__name__)

# SQLite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    if request.method == 'POST':
        original_url = request.form.get('url')

        if original_url:
            short_id = shortuuid.uuid()[:6]

            new_url = URL(
                original_url=original_url,
                short_id=short_id
            )
            db.session.add(new_url)
            db.session.commit()

            short_url = request.host_url + short_id

    return render_template('index.html', short_url=short_url)


@app.route('/<short_id>')
def redirect_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first()

    if not url:
        return "URL not found", 404

    return redirect(url.original_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)