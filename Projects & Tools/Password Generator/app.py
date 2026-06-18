import random 
import string

def generate_password(length=12):
    characters = (
        string.ascii_letters +      # a-z A-Z
        string.digits              # 0-9
        # string.punctuation        # special chacters
    )

    password = "".join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(16)
print("Password Generate: ", password)

# Strong Password Generator (Guaranteed Requirements)
# At least 1 uppercase letter
# At least 1 lowercase letter
# At least 1 digit
# At least 1 special character

from flask import Flask, render_template, request
import secrets
import random
import string

app = Flask(__name__)

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password.extend(
        secrets.choice(all_characters)
        for _ in range(length - 4)
    )

    random.shuffle(password)

    return ''.join(password)


@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        length = int(request.form.get("length", 12))
        password = generate_strong_password(length)

    return render_template(
        "index.html",
        password=password
    )


if __name__ == "__main__":
    app.run(debug=True)