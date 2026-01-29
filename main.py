from pyscript import document

def compute_average(event=None):
    try:
        score1 = float(document.getElementById("score1").value)
        score2 = float(document.getElementById("score2").value)

        average = (score1 + score2) / 2

        if average >= 90:
            result = "Excellent"
        elif average >= 75:
            result = "Satisfactory"
        else:
            result = "Failed"

        document.getElementById("average").innerText = str(round(average, 2))
        document.getElementById("result").innerText = result

    except Exception:
        document.getElementById("average").innerText = "Error"
        document.getElementById("result").innerText = "Invalid input"


