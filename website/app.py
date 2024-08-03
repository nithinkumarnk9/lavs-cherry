from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.secret_key='supersecretkey'

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route('/category1.html')
def category1():
    return render_template('category1.html')
@app.route('/category2')
def category2():
    return render_template('category2.html')
@app.route('/category3.html')
def category3():
    return render_template('category3.html')
@app.route('/category4.html')
def category4():
    return render_template('category4.html')
@app.route('/category5.html')
def category5():
    return render_template('category5.html')
@app.route('/category6.html')
def category6():
    return render_template('category6.html')
@app.route('/search')
def search():
    query= request.args.get('query')
    return render_template('search_results.html',query=query)
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
         #Process login form data here
         username=request.form['username']
         password=request.form['password']
    #Add your authentication logic here
         if username == 'admin' and password == 'admin':
        #Dummy authentication
                    flash('Login successful!','success')
         return redirect(url_for('home'))
         return render_template('login.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        #Proccess signup form data here
        username=request.form['username']
        password=request.form['password']
        #Add your user registration logic here
        flash('Signup successful', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')
@app.route('/categories')
def categories():
    categories=["categories 1","categories 2", "categories 3","categories 4"]
    return render_template('categories.html', categories=categories)

if __name__ == "__main__":
    app.run(debug=True)