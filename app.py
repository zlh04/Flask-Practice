from flask import Flask, render_template, request

#assigns the vairable app to flask version of that class which is main in this case
app = Flask(__name__)

#when user navigates to just / then give them home page which is...
#@ is a python decorator
#decorators create a function that can be used in other functions by just using @functionName
#good way to add something before or after normal functions
#decorator: wraps or additional functionality to funciton it is used to decorate
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/change")
def change():
    return render_template('change.html')

@app.route("/append", methods=['POST'])
def append():
    vmName = request.form['vmName']
    vmOwner = request.form['owner']
    comments = request.form['comments']
    exclude = request.form['exclude']
    #add get table here and append table with inputs defined as variables above.
    VMinfo= vmName, vmOwner, comments, exclude
    return VMinfo

if __name__ == "__main__":
    app.run()