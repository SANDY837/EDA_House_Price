from flask import Flask, render_template, request, redirect, url_for,Response
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import numpy as np

app = Flask(__name__)
df=pd.read_csv(r"D:\excel_files_ml\Raw_Housing_Prices3.csv")

# Replace 'your_database_info' with your MySQL database connection details
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sandy83$",
    database="EDA_HOUSE_PRICE"
)
cursor = db.cursor()

def create_users_table():
    # Create the 'users' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EDA_HOUSE_PRICE.users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            email  VARCHAR(255)  NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email=request.form['email']
    password = request.form['password']

    create_users_table()

    try:
        # Insert user data into the 'users' table
        cursor.execute("INSERT INTO users (name,email, password) VALUES (%s,%s,%s)", (username, email,password))
        db.commit()
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    except mysql.connector.IntegrityError:
        # Handle duplicate username (user already exists)
        return "Username already taken. Please choose another username."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            # If the user exists in the database, consider it a successful login
            return  redirect('/home')
        else:
            return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# for sale price
def generate_plot1():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Sale Price'],kde=True, color='orange')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot2():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Sale Price'],palette="Paired")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

# for flat area
def generate_plot3():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Flat Area (in Sqft)'],kde=True,color='green')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot4():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Flat Area (in Sqft)'],palette="Set1")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

# for Lot Area (in Sqft)


def generate_plot7():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Lot Area (in Sqft)'],kde=True,color='red')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot8():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Lot Area (in Sqft)'],palette='Accent_r')
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

# for Area of the House from Basement (in Sqft)
def generate_plot9():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Area of the House from Basement (in Sqft)'],kde=True,color='yellow')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot10():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Area of the House from Basement (in Sqft)'],palette="Oranges")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


# for Basement Area (in Sqft)
def generate_plot11():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Basement Area (in Sqft)'],kde=True,color='purple')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot12():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Basement Area (in Sqft)'],palette="PRGn")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def generate_plot13():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Age of House (in Years)'],kde=True,color='green')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot14():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Age of House (in Years)'],palette="PuBu_r")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def generate_plot15():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Living Area after Renovation (in Sqft)'],kde=True,color='black')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot16():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Living Area after Renovation (in Sqft)'],palette="Spectral")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def generate_plot17():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.distplot(df['Lot Area after Renovation (in Sqft)'],kde=True,color='orange')
    plt.xlabel("Sale Price Bins")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    return plot_url1

def generate_plot18():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(4, 4))
    sns.boxplot(df['Lot Area after Renovation (in Sqft)'],palette="YlGn")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2



@app.route('/univariate')
def univariate():
    plot_url1 = generate_plot1()
    plot_url2 = generate_plot2()
    plot_url3 = generate_plot3()
    plot_url4 = generate_plot4()
    plot_url7 = generate_plot7()
    plot_url8 = generate_plot8()
    plot_url9 = generate_plot9()
    plot_url10 = generate_plot10()
    plot_url11 = generate_plot11()
    plot_url12 = generate_plot12()
    plot_url13 = generate_plot13()
    plot_url14 = generate_plot14()
    plot_url15 = generate_plot15()
    plot_url16 = generate_plot16()
    plot_url17 = generate_plot17()
    plot_url18 = generate_plot18()
    return render_template('univariate.html', plot_url1=plot_url1, plot_url2=plot_url2,plot_url3=plot_url3,plot_url4=plot_url4,plot_url7=plot_url7,plot_url8=plot_url8,plot_url9=plot_url9,plot_url10=plot_url10,plot_url11=plot_url11, plot_ur112=plot_url12,plot_url13=plot_url13,plot_url14=plot_url14,plot_url15=plot_url15,plot_url16=plot_url16,plot_url17=plot_url17,plot_url18=plot_url18)



# univariate analysis on categorical columns

def categorica1():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Bedrooms'].value_counts().plot(kind='bar',color='green')
    plt.xlabel("No of Bedrooms")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica2():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Bedrooms'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


# for No of Bathrooms
def categorica3():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Bathrooms']=round(df['No of Bathrooms'])
    df['No of Bathrooms'].value_counts().plot(kind='bar',color='yellow')
    plt.xlabel("No of Bathrooms")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica4():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Bathrooms'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

# for No of Floors
def categorica5():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Floors'].value_counts().plot(kind='bar',color='red')
    plt.xlabel("No of Floors")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica6():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Floors'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def categorica7():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Waterfront View'].value_counts().plot(kind='bar',color='black')
    plt.xlabel("Waterfront View")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica8():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Waterfront View'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def categorica9():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Times Visited'].value_counts().plot(kind='bar',color='pink')
    plt.xlabel("No of Times Visited")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica10():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['No of Times Visited'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def categorica11():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Condition of the House'].value_counts().plot(kind='bar',color='yellow')
    plt.xlabel("Condition of the House")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica12():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Condition of the House'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2


def categorica13():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Overall Grade'].value_counts().plot(kind='bar',color='orange')
    plt.xlabel("Overall Grade")
    plt.ylabel("Count")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2
def categorica14():
    sns.set(style="whitegrid")
    plt.figure(figsize=(5, 5))
    df['Overall Grade'].value_counts().plot(kind='pie',autopct='%0.1f%%')
    

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2






@app.route('/uni_categorical')
def uni_categorical():
    plot_ur1=categorica1()
    plot_ur2=categorica2()
    plot_ur3=categorica3()
    plot_ur4=categorica4()
    plot_ur5=categorica5()
    plot_ur6=categorica6()
    plot_ur7=categorica7()
    plot_ur8=categorica8()
    plot_ur9=categorica9()
    plot_ur10=categorica10()
    plot_ur11=categorica11()
    plot_ur12=categorica12()
    plot_ur13=categorica13()
    plot_ur14=categorica14()
    

    return render_template('uni_categorical.html',plot_ur1=plot_ur1,plot_ur2=plot_ur2,plot_ur3=plot_ur3
                           ,plot_ur4=plot_ur4,plot_ur5=plot_ur5,plot_ur6=plot_ur6,plot_ur7=plot_ur7,plot_ur8=plot_ur8,plot_ur9=plot_ur9,plot_ur10=plot_ur10,plot_ur11=plot_ur11,plot_ur12=plot_ur12,plot_ur13=plot_ur13,plot_ur14=plot_ur14)



def categorical1():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df, x='Sale Price', y='Flat Area (in Sqft)',color='yellow')
    plt.xlabel("Sale Price")
    plt.ylabel("Flat Area (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical2():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Lot Area (in Sqft)',color='red')
    plt.xlabel("Sale Price")
    plt.ylabel("Lot Area (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical3():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Area of the House from Basement (in Sqft)',color='orange')
    plt.xlabel("Sale Price")
    plt.ylabel("Area of the House from Basement (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical4():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Basement Area (in Sqft)',color='pink')
    plt.xlabel("Sale Price")
    plt.ylabel("Basement Area (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical5():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Age of House (in Years)',color='green')
    plt.xlabel("Sale Price")
    plt.ylabel("Age of House (in Years)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical6():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Living Area after Renovation (in Sqft)',color='black')
    plt.xlabel("Sale Price")
    plt.ylabel("Living Area after Renovation (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

def categorical7():
    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df,x='Sale Price',y='Lot Area after Renovation (in Sqft)',color='pink')
    plt.xlabel("Sale Price")
    plt.ylabel("Lot Area after Renovation (in Sqft)")

    # Save the plot to a BytesIO object to display in the Flask app
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image in base64 to embed in the HTML
    plot_url2 = base64.b64encode(img.getvalue()).decode()
    return plot_url2

@app.route('/bivariate')
def bivariate():
    plot_u1=categorical1()
    plot_u2=categorical2()
    plot_u3=categorical3()
    plot_u4=categorical4()
    plot_u5=categorical5()
    plot_u6=categorical6()
    plot_u7=categorical7()


    return render_template('bivariate.html',plot_u1=plot_u1,plot_u2=plot_u2,plot_u3=plot_u3,
                           plot_u4=plot_u4,plot_u5=plot_u5,plot_u6=plot_u6,plot_u7=plot_u7)






if __name__ == '__main__':
    app.run(debug=True)


