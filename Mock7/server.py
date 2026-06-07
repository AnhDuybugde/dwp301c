"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template_string, request

from EmotionDetection import emotion_detector


app = Flask(__name__)

PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Emotion Detection</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 40px; background: #f5f7fb; }
      main { max-width: 760px; background: white; padding: 28px; border-radius: 8px; }
      textarea { width: 100%; min-height: 120px; margin: 12px 0; }
      button { padding: 10px 18px; font-weight: 700; }
      .error { color: #b00020; font-weight: 700; }
      .result { color: #154734; font-weight: 700; }
    </style>
  </head>
  <body>
    <main>
      <h1>Emotion Detection</h1>
      <form action="/emotionDetector" method="get">
        <label for="textToAnalyze">Enter text to analyze</label>
        <textarea id="textToAnalyze" name="textToAnalyze">{{ text }}</textarea>
        <button type="submit">Run Emotion Detection</button>
      </form>
      {% if error %}
        <p class="error">{{ error }}</p>
      {% endif %}
      {% if result %}
        <p class="result">{{ result }}</p>
      {% endif %}
    </main>
  </body>
</html>
"""


@app.route("/")
def index():
    """Render the home page."""
    return render_template_string(PAGE_TEMPLATE, text="", error="", result="")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and render the emotion detection result."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response.get("status_code") == 400:
        return render_template_string(
            PAGE_TEMPLATE,
            text=text_to_analyze,
            error="Invalid text! Please try again.",
            result="",
        ), 400

    result = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return render_template_string(
        PAGE_TEMPLATE,
        text=text_to_analyze,
        error="",
        result=result,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
