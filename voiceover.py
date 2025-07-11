from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gtts import gTTS
import io
import os


from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from gtts import gTTS
import io

app = Flask(__name__)
CORS(app)  # <-- এই লাইনটি যোগ করো

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)






# word to voice


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "✅ Voiceover API is running!"

@app.route("/api/voiceover", methods=["POST"])
def voiceover():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "Empty text"}), 400

        tts = gTTS(text, lang='bn')  # ইংরেজি হলে lang='en'
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return send_file(mp3_fp, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
