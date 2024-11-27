from flask import Flask, render_template, request, redirect, url_for
from forms import MyForm
from trivia_class import Questions

app = Flask(__name__)
app.config["SECRET_KEY"] = "TommyShelby"


@app.route("/", methods=["GET", "POST"])
def home_page():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.decision.data == "TRYB VOLDEMORT":
                return redirect(
                    url_for("first_quiz_page")
                )

            # if form.quiz_type.data == "Multiple Choice":
            #     return redirect(url_for("first_quiz_page",
            #                             quantity=form.quantity.data,
            #                             category=form.category.data
            #                             )
            #                     )
            # else:
            #     return redirect(url_for("second_quiz_page",
            #                             quantity=form.quantity.data,
            #                             category=form.category.data
            #                             )
            #                     )
    return render_template("index.html", form=form)


@app.route("/quiz/multiple-choice")
def first_quiz_page():
    tool = Questions()
    data_1 = tool.get_questions()
    return render_template("quiz_first.html", data=data_1, name="Zadanie 1")


@app.route("/quiz/snake")
def second_quiz_page():
    # tool = Questions()
    # data_2 = tool.get_questions()
    return render_template("snake.html", name="Zadanie 2")

    # tool = Questions()
    # my_data = tool.get_questions(
    #     amount=5,
    #     category="Animals",
    #     quiz_type="boolean"
    # )
    # return render_template("quiz_second.html", data=my_data, name="Zadanie 2")

@app.route("/quiz/riddle")
def third_quiz_page():
    # tool = Questions()
    # data_2 = tool.get_questions()
    return render_template("riddle.html", name="Zadanie 3")


if __name__ == "__main__":
    app.run(debug=True)
