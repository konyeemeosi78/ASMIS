import bcrypt

password = b"P@ssword"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

email = request.form.get("email") 
password = request.form.get("password").encode("utf-8")

if bcrypt.checkpw(password, hashed):
    print("Password match")
    return redirect(url_for("user_profile"))
else:
    print("No match")
    flash("Invalid credentials", "warning")