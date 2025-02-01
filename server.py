"""import librries"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app= Flask("Emotion Detector")

@app.route("/emotionDetector")

def emotionDetector():
    """Analyzes the emotion in a given text and returns the results."""
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return "Invlid input! Please try again!"
    else:
        return f"For the given statement, the system response is  'anger': {anger},' disgust': {disgust},' fear': {fear},' joy': {joy},' sadness': {sadness}. The dominant emotion is  {dominant_emotion}"

@app.route("/")
def render_index_page():
    """Renders the main index page (the HTML form)."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
