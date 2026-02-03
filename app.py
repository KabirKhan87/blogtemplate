from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/menu.html')
def menu():
    return render_template('menu.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404.html')
def error_404():
    return render_template('404.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run()