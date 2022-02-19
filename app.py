#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS Reg")
        pred = model.predict([[float(rates)]])
        print(pred)
        s1 = "Predicted DBS Share price based on Linear Regression is : " + str(pred)
        model = joblib.load("DBS Reg")
        pred = model.predict([[float(rates)]])
        print(pred)
        s2 = "Predicted DBS Share price based on Linear Regression is : " + str(pred)
        model = joblib.load("DBSDT")
        pred = model.predict([[float(rates)]])
        print(pred)
        s3 = "Predicted DBS Share price based on Linear Regression is : " + str(pred)
        model = joblib.load("MLPRegressor")
        pred = model.predict([[float(rates)]])
        return(render_template("index.html",results1=s1,results2=s2,results3=s3))
    else:
        return(render_template("index.html",results1="Predicted Price 1",results2="Predicted Price 2",results3="Predicted Price 3"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




