from flask import Flask, render_template

app = Flask(__name__)


# ---------------------------------------------------
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#--------------------------------------------------

@app.route('/value')
@app.route('/value/<string:username>')
def value(username=None):
    return render_template('value.html', username=username)


#-------------------------------------------
@app.route('/comtrol')
@app.route('/comtrol/<int:num>')
def control(num=0):
    articles = []
    for i in range(1, num + 1):
        articles.append({
            'title': '文章%d标题' % i,
            'content': ('文章%d的内容' % i) * i,
        })
    return render_template('control.html', num=num, articles=articles)


# --------------------------------------------------
@app.route('/include_nav')
def include_nav():
    return render_template('include_nav.html')

    # ------------------------------------------------
    if __name__ == '__main__':
        app.run()
