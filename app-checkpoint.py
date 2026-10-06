from flask import Flask, request, render_template_string
import pickle
import pandas as pd

app = Flask(__name__)

with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    result_class = ""

    cp = ""
    ca = ""
    thal = ""
    oldpeak = ""

    if request.method == "POST":

        cp = request.form["cp"]
        ca = request.form["ca"]
        thal = request.form["thal"]
        oldpeak = request.form["oldpeak"]

        patient_data = pd.DataFrame(
            [[float(cp), float(ca), float(thal), float(oldpeak)]],
            columns=["cp", "ca", "thal", "oldpeak"]
        )

        result = model.predict(patient_data)

        if result[0] == 1:
            prediction = "Heart Disease Detected"
            result_class = "danger"
        else:
            prediction = "No Heart Disease Detected"
            result_class = "success"

    return render_template_string("""

<!DOCTYPE html>
<html>

<head>

<title>Heart Disease Prediction</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #e8f5ff, #f8fbff);
    min-height: 100vh;
}

.header {
    background: linear-gradient(135deg, #0f766e, #0ea5a4);
    color: white;
    text-align: center;
    padding: 35px 20px;
}

.header h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

.header p {
    font-size: 16px;
    opacity: 0.9;
}

.container {
    width: 90%;
    max-width: 900px;
    margin: 40px auto;
}

.card {
    background: white;
    border-radius: 18px;
    padding: 35px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

.card h2 {
    color: #0f766e;
    margin-bottom: 10px;
}

.description {
    color: #666;
    margin-bottom: 30px;
}

.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
}

.field label {
    display: block;
    font-weight: bold;
    margin-bottom: 8px;
    color: #333;
}

.field input {
    width: 100%;
    padding: 13px;
    border: 1px solid #d1d5db;
    border-radius: 9px;
    font-size: 15px;
}

.field input:focus {
    outline: none;
    border-color: #0f766e;
}

.buttons {
    display: flex;
    gap: 12px;
    margin-top: 30px;
}

button {
    flex: 1;
    padding: 15px;
    border: none;
    border-radius: 10px;
    color: white;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

.predict {
    background: #0f766e;
}

.predict:hover {
    background: #115e59;
}

.clear {
    background: #64748b;
}

.clear:hover {
    background: #475569;
}

.result {
    margin-top: 30px;
    padding: 20px;
    text-align: center;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
}

.success {
    background: #dcfce7;
    color: #166534;
}

.danger {
    background: #fee2e2;
    color: #991b1b;
}

.footer {
    text-align: center;
    margin-top: 30px;
    color: #777;
    font-size: 13px;
}

@media (max-width: 650px) {

    .form-grid {
        grid-template-columns: 1fr;
    }

    .buttons {
        flex-direction: column;
    }

    .header h1 {
        font-size: 28px;
    }

    .card {
        padding: 25px;
    }
}

</style>

</head>


<body>

<div class="header">

    <h1>❤️ Heart Disease Prediction</h1>

    <p>Machine Learning Based Health Prediction System</p>

</div>


<div class="container">

<div class="card">

    <h2>Patient Information</h2>

    <p class="description">
        Enter the patient's medical information below to generate a prediction.
    </p>


    <form method="POST">

        <div class="form-grid">

            <div class="field">

                <label>Chest Pain (cp)</label>

                <input
                    type="number"
                    name="cp"
                    min="0"
                    max="3"
                    step="1"
                    placeholder="0 - 3"
                    value="{{ cp }}"
                    required
                >

            </div>


            <div class="field">

                <label>Major Vessels (ca)</label>

                <input
                    type="number"
                    name="ca"
                    min="0"
                    max="3"
                    step="1"
                    placeholder="0 - 3"
                    value="{{ ca }}"
                    required
                >

            </div>


            <div class="field">

                <label>Thalassemia (thal)</label>

                <input
                    type="number"
                    name="thal"
                    min="0"
                    max="7"
                    step="1"
                    placeholder="Enter value"
                    value="{{ thal }}"
                    required
                >

            </div>


            <div class="field">

                <label>ST Depression (oldpeak)</label>

                <input
                    type="number"
                    name="oldpeak"
                    step="0.1"
                    placeholder="e.g. 1.0"
                    value="{{ oldpeak }}"
                    required
                >

            </div>

        </div>


        <div class="buttons">

            <button type="submit" class="predict">
                🔍 Predict Heart Disease
            </button>

            <button
                type="button"
                class="clear"
                onclick="clearForm()">
                🗑️ Clear All
            </button>

        </div>

    </form>


    {% if prediction %}

        <div class="result {{ result_class }}">

            {{ prediction }}

        </div>

    {% endif %}

</div>


<div class="footer">

    Heart Disease Prediction System • Machine Learning Project

</div>

</div>


<script>

function clearForm() {

    document.querySelectorAll("input").forEach(function(input) {
        input.value = "";
    });

    document.querySelectorAll(".result").forEach(function(result) {
        result.remove();
    });

}

</script>

</body>

</html>

""",
    prediction=prediction,
    result_class=result_class,
    cp=cp,
    ca=ca,
    thal=thal,
    oldpeak=oldpeak
)


if __name__ == "__main__":
    app.run(debug=True)