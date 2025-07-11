from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Voiceover API is running!"

@app.route("/api/voiceover", methods=["POST"])
def voiceover():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "টেক্সট দিন"}), 400

    try:
        tts = gTTS(text=text, lang="bn")
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return send_file(mp3_fp, mimetype="audio/mpeg", as_attachment=True, download_name="voiceover.mp3")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
