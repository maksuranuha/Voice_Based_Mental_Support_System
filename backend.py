from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.voice_translator import simple_translator
from src.tts import voice
from src.transcribe import transcribe_audio
import io

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

def mental_support_ai(text):
    try:
        print(f"[DEBUG] Generating AI response for: '{text}'")
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""You are a compassionate, warm multilingual mental health support AI. The user just shared: "{text}"

CRITICAL: Always respond in the SAME LANGUAGE the user used. Detect their language and respond accordingly.

Your response should:
- Greet warmly if the user greets you (Hello -> Hello back, Hi -> Hi back)
- Acknowledge what they specifically said
- Validate their feelings without judgment
- Offer gentle encouragement and hope
- Be warm, human-like, and conversational
- Keep it around 2-3 sentences, not too long
- Speak as if you're a caring friend who truly understands

Always respond in the user's native language with empathy and cultural sensitivity.

Respond directly to them:"""
        
        response = model.generate_content(prompt)
        support_text = response.text.strip()
        
        print(f"[DEBUG] AI Response generated: '{support_text}'")
        return support_text
        
    except Exception as e:
        print(f"[ERROR] Error generating support: {e}")
        return "I hear you. Your feelings are valid, and you're not alone."

@app.route('/chat', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        user_message = data['message']
        print(f"[DEBUG] Received chat message: '{user_message}'")
        
        ai_response = mental_support_ai(user_message)
        
        print(f"[DEBUG] Sending response: '{ai_response}'")
        return jsonify({
            'response': ai_response,
            'success': True
        })
    except Exception as e:
        print(f"[ERROR] Chat endpoint error: {e}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data['text']
        target_language = data['target_language']
        
        print(f"[DEBUG] Translating '{text}' to {target_language}")
        
        translated_text = simple_translator(text, target_language)
        
        print(f"[DEBUG] Translation result: '{translated_text}'")
        return jsonify({
            'translated_text': translated_text,
            'success': True
        })
    except Exception as e:
        print(f"[ERROR] Translation error: {e}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/transcribe', methods=['POST'])
def transcribe_audio_endpoint():
    try:
        print("[DEBUG] Transcribe endpoint called")
        
        # Check if audio file is in the request
        if 'audio' not in request.files:
            print("[ERROR] No audio file provided")
            return jsonify({
                'error': 'No audio file provided',
                'success': False
            }), 400
        
        audio_file = request.files['audio']
        print(f"[DEBUG] Audio file received: {audio_file.filename}, size: {audio_file.content_length}")
        
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            audio_file.save(tmp_file.name)
            tmp_file_path = tmp_file.name
        
        print(f"[DEBUG] Audio saved to: {tmp_file_path}")
        
        try:
            # Transcribe the audio using your transcribe function
            print("[DEBUG] Starting transcription...")
            transcription = transcribe_audio(tmp_file_path)
            print(f"[DEBUG] Transcription result: '{transcription}'")
            
            # Clean up the temporary file
            os.unlink(tmp_file_path)
            
            if transcription and transcription.strip():
                return jsonify({
                    'transcription': transcription,
                    'success': True
                })
            else:
                print("[ERROR] Empty transcription result")
                return jsonify({
                    'error': 'No speech detected in audio',
                    'success': False
                }), 400
                
        except Exception as transcribe_error:
            print(f"[ERROR] Transcription failed: {transcribe_error}")
            # Clean up the temporary file in case of error
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
            
            return jsonify({
                'error': f'Failed to transcribe audio: {str(transcribe_error)}',
                'success': False
            }), 500
            
    except Exception as e:
        print(f"[ERROR] Audio upload error: {e}")
        return jsonify({
            'error': 'Failed to process audio file',
            'success': False
        }), 500
    
@app.route('/tts', methods=['POST'])
def text_to_speech():
    try:
        data = request.get_json()
        text = data['text']
        
        print(f"[DEBUG] TTS request for: '{text}'")
        
        audio_gen = voice(text)
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            for chunk in audio_gen:
                tmp_file.write(chunk)
            tmp_file_path = tmp_file.name
        
        print(f"[DEBUG] TTS audio generated: {tmp_file_path}")
        
        def cleanup_file():
            try:
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
                    print(f"[DEBUG] Cleaned up TTS file: {tmp_file_path}")
            except:
                pass
        
        # Schedule cleanup after sending file
        response = send_file(
            tmp_file_path, 
            as_attachment=False, 
            download_name='response.mp3',
            mimetype='audio/mpeg'
        )
        
        # Clean up file after a delay to ensure it's sent
        import threading
        def delayed_cleanup():
            import time
            time.sleep(2)  # Wait 2 seconds before cleanup
            cleanup_file()
        
        threading.Thread(target=delayed_cleanup).start()
        
        return response
        
    except Exception as e:
        print(f"[ERROR] TTS error: {e}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

# Test endpoint to check if everything is working
@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({
        'status': 'Backend is running!',
        'endpoints': ['/chat', '/translate', '/transcribe', '/tts'],
        'success': True
    })

@app.route('/')
def serve_html():
    return send_file('index.html')

if __name__ == '__main__':
    print("[DEBUG] Starting TellAFriend backend...")
    print("[DEBUG] Available endpoints: /, /chat, /translate, /transcribe, /tts, /test")
    app.run(debug=True, port=5000)