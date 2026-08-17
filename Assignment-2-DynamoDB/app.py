from flask import Flask, request, redirect, render_template_string
import boto3
from decimal import Decimal

app = Flask(__name__)

# Uses the EC2 IAM Role automatically
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("linkding-dynamodb")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DynamoDB CRUD App</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
            background: #f4f4f4;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        button {
            cursor: pointer;
        }
        .item {
            border: 1px solid #ddd;
            padding: 15px;
            margin-top: 15px;
            border-radius: 8px;
        }
    </style>
</head>
<body>

<div class="container">

<h1>DynamoDB Bookmark Manager</h1>

<h2>Create Bookmark</h2>

<form action="/create" method="post">
    <input name="id" placeholder="ID" required>
    <input name="title" placeholder="Title" required>
    <input name="rating" type="number" placeholder="Rating" required>
    <input name="tags" placeholder="Tags (comma separated)" required>

    <label>
        Favorite:
        <input name="favorite" type="checkbox">
    </label>

    <button type="submit">Create</button>
</form>

<hr>

<h2>Bookmarks</h2>

{% for item in items %}

<div class="item">

<b>ID:</b> {{ item.id }} <br>
<b>Title:</b> {{ item.title }} <br>
<b>Rating:</b> {{ item.rating }} <br>
<b>Favorite:</b> {{ item.is_favorite }} <br>
<b>Tags:</b> {{ item.tags }} <br>
<b>Metadata:</b> {{ item.metadata }} <br>

<br>

<a href="/edit/{{ item.id }}">Edit</a>

<form action="/delete/{{ item.id }}" method="post" style="display:inline">
    <button type="submit">Delete</button>
</form>

</div>

{% endfor %}

</div>

</body>
</html>
"""


@app.route("/")
def index():
    response = table.scan()
    items = response.get("Items", [])
    return render_template_string(HTML, items=items)


@app.route("/create", methods=["POST"])
def create():

    item = {
        "id": request.form["id"],
        "title": request.form["title"],
        "rating": Decimal(request.form["rating"]),
        "is_favorite": "favorite" in request.form,
        "tags": [
            x.strip()
            for x in request.form["tags"].split(",")
        ],
        "metadata": {
            "source": "EC2",
            "category": "Cloud Computing"
        }
    }

    table.put_item(Item=item)

    return redirect("/")


@app.route("/edit/<id>")
def edit(id):

    response = table.get_item(
        Key={"id": id}
    )

    item = response.get("Item")

    if not item:
        return "Item not found", 404

    return f"""
    <h1>Update Bookmark</h1>

    <form action="/update/{id}" method="post">

        Title:
        <input name="title"
               value="{item.get('title', '')}">
        <br><br>

        Rating:
        <input name="rating"
               type="number"
               value="{item.get('rating', 0)}">
        <br><br>

        Tags:
        <input name="tags"
               value="{','.join(item.get('tags', []))}">
        <br><br>

        <button type="submit">Update</button>

    </form>
    """


@app.route("/update/<id>", methods=["POST"])
def update(id):

    table.update_item(
        Key={"id": id},

        UpdateExpression="SET title=:t, rating=:r, tags=:g",

        ExpressionAttributeValues={
            ":t": request.form["title"],
            ":r": Decimal(request.form["rating"]),
            ":g": [
                x.strip()
                for x in request.form["tags"].split(",")
            ]
        }
    )

    return redirect("/")


@app.route("/delete/<id>", methods=["POST"])
def delete(id):

    table.delete_item(
        Key={"id": id}
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
