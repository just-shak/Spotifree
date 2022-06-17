
@app.route("/profile", methods= "POST")
@login_required
def profile():
    if form.validate_on_submit():
        if "music" in request.form:
            return redirect("/music_search")
        elif "playlist" in request.form:
            return redirect("/playlist")
        else "spotifriends" in request.form:
            return redirect ("/spotifriends")
    else : 
        return render_template("profile.html")