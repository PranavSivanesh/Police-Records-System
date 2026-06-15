from flask import Flask, render_template, request, redirect, url_for
import csv, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def read_csv(filename):
    if not os.path.exists(filename):
        return []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        return [row for row in reader if len(row) > 0]

def write_csv(filename, rows):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def get_next_id(filename):
    rows = read_csv(filename)
    if rows:
        return max(int(row[0]) for row in rows) + 1
    return 1
    
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<record_type>")
def view_records(record_type):
    if record_type == "criminals":
        filename = "Criminal.csv"
        template = "Criminals/criminals.html"
        key = "criminals"
    else:
        filename = "Officer.csv"
        template = "Officers/officers.html"
        key = "officers"
    
    records = read_csv(filename)
    return render_template(template, **{key: records})

@app.route("/<record_type>/delete", methods = ["GET", "POST"])
def delete_record(record_type):
    if record_type == "criminals":
        filename = "Criminal.csv"
        template = "Criminals/delete_criminal.html"
    else:
        filename = "Officer.csv"
        template = "Officers/delete_officer.html"
    
    if request.method == "POST":
        delete_id = request.form["ID"]
        rows = read_csv(filename)
        rows = [row for row in rows if row[0] != delete_id]
        write_csv(filename, rows)
        return redirect(url_for("view_records", record_type = record_type))
    return render_template(template)

@app.route("/<record_type>/search", methods = ["GET", "POST"])
def search_record(record_type):
    if record_type == "criminals":
        filename = "Criminal.csv"
        template = "Criminals/search_criminal.html"
    else:
        filename = "Officer.csv"
        template = "Officers/search_officers.html"

    results = []
    searched = False
    if request.method == "POST":
        search = request.form["name"]
        all_rows = read_csv(filename)
        results = [row for row in all_rows if row[1].lower() == search.lower()]
        searched = True
    return render_template(template, results = results, searched = searched)

@app.route("/criminals/add", methods = ["GET", "POST"])
def add_criminal():
    if request.method == "POST":
        id = get_next_id("Criminal.csv")
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        crime = request.form["crime"]
        place = request.form["place"]
        date = request.form["date"]
        rows = read_csv("Criminal.csv")
        rows.append([id,name,age,gender,crime,place,date])
        write_csv("Criminal.csv", rows)
        return redirect(url_for("view_records", record_type = "criminals"))
    return render_template("Criminals/add_criminal.html")


@app.route("/criminals/update", methods = ["GET", "POST"])
def update_criminal():
    updated_row=None
    criminal = None
    if request.method == "POST" and "ID" in request.form:
        id = int(request.form["ID"])
        rows = read_csv("Criminal.csv")
        for row in rows:
            if len(row)>0 and int(row[0]) == id:
                criminal = row
                break
        
    if request.method == "POST" and "update_id" in request.form:
        id = request.form["update_id"]
        name = request.form["name"] or request.form["orig_name"]
        age = request.form["age"] or request.form["orig_age"]
        gender = request.form["gender"] or request.form["orig_gender"]
        crime = request.form["crime"] or request.form["orig_crime"]
        place = request.form["place"] or request.form["orig_place"]
        date = request.form["date"] or request.form["orig_date"]

        rows = read_csv("Criminal.csv")

        for row in rows:
            if row[0] == id:
                row[1] = name
                row[2] = age
                row[3] = gender
                row[4] = crime
                row[5] = place
                row[6] = date

        write_csv("Criminal.csv", rows)

        updated_row =[id, name, age, gender, crime, place, date]
    return render_template("Criminals/update_criminal.html", criminal=criminal, updated = updated_row)

@app.route("/officers/add", methods = ["GET", "POST"])
def add_officer():
    if request.method == "POST":
        id = get_next_id("Officer.csv")
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        badge = request.form["badge"]
        rank = request.form["rank"]
        station = request.form["station"]
        rows = read_csv("Officer.csv")
        rows.append([id, name, age, gender, badge, rank, station])
        write_csv("Officer.csv", rows)
        return redirect(url_for("view_records", record_type = "officers"))
    return render_template("Officers/add_officers.html")

@app.route("/officers/update", methods = ["GET", "POST"])
def update_officers():
    updated_row = None
    officers = None
    if request.method == "POST" and "ID" in request.form:
        id = int(request.form["ID"])
        rows = read_csv("Officer.csv")
        for row in rows:
            if len(row)>0 and int(row[0]) == id:
                officers = row
                break
        
    if request.method == "POST" and "update_id" in request.form:
        id = request.form["update_id"]
        name = request.form["name"] or request.form["orig_name"]
        age = request.form["age"] or request.form["orig_age"]
        gender = request.form["gender"] or request.form["orig_gender"]
        badge = request.form["badge"] or request.form["orig_badge"]
        rank = request.form["rank"] or request.form["orig_rank"]
        station = request.form["station"] or request.form["orig_station"]

        rows = read_csv("Officer.csv")

        for row in rows:
            if row[0] == id:
                row[1] = name
                row[2] = age
                row[3] = gender
                row[4] = badge
                row[5] = rank
                row[6] = station

        write_csv("Officer.csv", rows)

        updated_row =[id, name, age, gender, badge, rank, station]
    return render_template("Officers/update_officers.html", officers=officers, updated = updated_row)

@app.route("/graphs/<graph_type>")
def show_graph(graph_type):
    plt.style.use('dark_background')
    plt.rcParams['figure.facecolor'] = '#14142b'
    plt.rcParams['axes.facecolor'] = '#14142b'
    plt.savefig("static/images/graph.png", facecolor = '#14142b')

    if graph_type == "crime_types":
        labels = ["Theft", "Assault", "Fraud", "Harassment", "Trafficking"]
        sizes = [35, 25, 20, 12, 8]
        plt.pie(sizes, labels = labels, autopct='%1.1f%%', textprops={'color' : 'white'})
        for autotext in plt.gca().texts:
            if '%' in autotext.get_text():
                autotext.set_color('black')
        plt.title("Most Common Crime Types in UAE")

    elif graph_type == "crime_rate":
        years = [2018, 2019, 2020, 2021, 2022, 2023]
        crime_rate = [4500, 4800, 3900, 4100, 4600, 4300]
        plt.plot(years, crime_rate, marker='o')
        plt.title("Crime Rate Over Years")
        plt.xlabel("Year")
        plt.ylabel("Number of Crimes")

    elif graph_type == "crime_emirate":
        emirates = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "RAK", "Fujairah", "UAQ"]
        crimes = [1200, 980, 650, 320, 280, 190, 150]
        plt.bar(emirates, crimes, color='blue')
        plt.title("Crimes by Emirate")
        plt.xlabel("Emirate")
        plt.ylabel("Number of Crimes")

    elif graph_type == "crime_women":
        categories = ["Harassment", "Domestic Violence", "Assault", "Trafficking"]
        cases = [320, 210, 180, 90]
        plt.bar(categories, cases, color='red')
        plt.title("Crimes Against Women")
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Cases")

    elif graph_type == "crime_senior":
        crimes = ["Fraud", "Theft", "Assault", "Neglect"]
        cases = [150, 200, 80, 120]
        plt.bar(crimes, cases, color='orange')
        plt.title("Crimes Against Senior Citizens")
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Cases")

    elif graph_type == "crime_age":
        rows = read_csv("Criminal.csv")
        ages = [int(row[2]) for row in rows]
        plt.hist(ages, bins=5)
        plt.title("Age Distribution of Criminals")
        plt.xlabel("Age")
        plt.ylabel("Number of Criminals")

    plt.savefig("static/images/graph.png")
    plt.close()

    titles = {
        "crime_types" : "Most Common Crime Types",
        "crime_rate" : "Crime Rate Over the Years",
        "crime_emirate": "Crimes by Emirate",
        "crime_women": "Crimes Against Women",
        "crime_senior": "Crimes Against Senior Citizens",
        "crime_age": "Age Distribution of Criminals"      
    }

    return render_template("graph.html", graph_type = graph_type, title=titles[graph_type])


if __name__ == "__main__":
    app.run(debug=True)