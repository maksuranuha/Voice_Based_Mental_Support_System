# 🤗 TellAFriend - Advanced Multilingual AI Mental Health Companion

*The most sophisticated multilingual mental health support AI that speaks, listens, and responds in ANY language combination*
It enables empathetic, culturally-aware text + voice conversations in 30+ languages with real-time switching and mental health–focused support.

## ✨ User Interface & Features
### 🖥️ Initial Interface

https://github.com/user-attachments/assets/3e92cb9f-ff9c-4ac0-8f25-0b315fef6c16

- The clean and modern interface welcomes users with a dark, calming theme designed for sensitive conversations. From here, users can instantly start chatting or speaking in any supported language.
<img width="1909" height="976" alt="A_Initial" src="https://github.com/user-attachments/assets/b6e06a74-b62b-4c89-94b6-cac426fd41da" />

### 🌍 Multilingual Response Selection

- Users can choose their preferred response language from a simple dropdown. For example, the user may type in English but request the AI to respond in French, Arabic, or any other supported language—making cross-language mental health conversations seamless.
<img width="1919" height="947" alt="Response_In_French" src="https://github.com/user-attachments/assets/a3677888-26ce-4140-a0a2-88fda833cab1" />

### 🎙️ Voice Recording & Playback

- The interface provides a one-click recording feature for natural, voice-based conversations. Visual indicators show when recording is active, and responses are automatically played back in the selected language with emotion-aware, natural-sounding voices.
<img width="1919" height="1025" alt="Recording" src="https://github.com/user-attachments/assets/7c4b0efc-7027-4c10-8451-e551cc702579" />

👉 Together, these features create a safe, accessible, and truly multilingual support system, allowing users to express themselves in the way that feels most natural—through text or voice, in any language.

## 🌟 Revolutionary Features Overview

TellAFriend isn't just another chatbot - it's a **breakthrough multilingual AI companion** that provides mental health support with unprecedented language flexibility and communication modes.

### 🎯 **What Makes TellAFriend Unique:**

- **🗣️ FULL VOICE CONVERSATIONS**: Both user and AI can speak in any supported language
- **✍️ TEXT + VOICE HYBRID**: User types, AI responds with voice OR user speaks, AI responds with text
- **🌍 DYNAMIC LANGUAGE SWITCHING**: User speaks Spanish, AI responds in Urdu - ANY combination possible!
- **🔄 REAL-TIME LANGUAGE ADAPTATION**: Change languages mid-conversation seamlessly
- **🧠 CULTURALLY AWARE AI**: Responses adapt to cultural context and language nuances
- **🎙️ NATURAL VOICE SYNTHESIS**: High-quality, emotion-aware voice in 30+ languages

## 🚀 **Core Capabilities**

### 1. **Multilingual Voice-to-Voice Conversations**
```
👤 User (Spanish Audio): "Me siento muy triste hoy"
🤖 AI (English Audio): "I hear you're feeling very sad today. That's completely valid..."
```

### 2. **Cross-Language Communication**
```
👤 User (French Text): "Je me sens anxieux"
🤖 AI (German Voice): "Es tut mir leid zu hören, dass Sie sich ängstlich fühlen..."
```

### 3. **Dynamic Language Control**
- **Translation Dropdown**: Switch AI response language instantly
- **Auto-Detection**: AI automatically detects user's input language
- **Voice Language Matching**: AI voice matches selected language perfectly
- **Cultural Adaptation**: Responses culturally appropriate for target language

### 4. **Multiple Communication Modes**
| User Input | AI Response | Example Use Case |
|------------|-------------|------------------|
| 🎙️ Voice | 🔊 Voice | Natural conversation |
| ✍️ Text | 🔊 Voice | User prefers typing, wants to hear response |
| 🎙️ Voice | ✍️ Text | User speaks, prefers reading response |
| ✍️ Text | ✍️ Text | Traditional text chat |

## 🎛️ **Advanced Features**

### **🎵 Intelligent Voice Synthesis**
- **Emotion-Aware**: AI voice tone matches emotional context
- **Cultural Accent**: Native pronunciation for each language
- **Multilingual Model**: Seamless switching between language voices
- **High-Quality Audio**: Crystal clear 44.1kHz MP3 output

### **🧠 Smart Translation Engine**
- **Context Preservation**: Maintains emotional context across languages
- **Auto-Detection**: Automatically identifies 30+ languages
- **Cultural Sensitivity**: Adapts responses to cultural norms
- **Bidirectional**: Any language to any language translation

### **🎯 Mental Health AI Features**
- **Empathetic Responses**: Validates feelings without judgment
- **Cultural Awareness**: Understands cultural context of mental health
- **Crisis Recognition**: Identifies serious situations appropriately
- **Hope & Encouragement**: Provides gentle support and positivity
- **Language-Specific Support**: Mental health concepts explained culturally

## 🌐 **Complete Language Matrix**

TellAFriend supports **FULL VOICE + TEXT** in all these languages:

| **European** | **Asian** | **Middle Eastern** | **Others** |
|--------------|-----------|-------------------|------------|
| 🇬🇧 English | 🇨🇳 Chinese (Mandarin) | 🇸🇦 Arabic | 🇮🇳 Hindi |
| 🇪🇸 Spanish | 🇯🇵 Japanese | 🇹🇷 Turkish | 🇵🇰 Urdu |
| 🇫🇷 French | 🇰🇷 Korean | 🇮🇷 Persian | 🇧🇩 Bengali |
| 🇩🇪 German | 🇹🇭 Thai | 🇮🇱 Hebrew | 🇳🇬 Yoruba |
| 🇮🇹 Italian | 🇻🇳 Vietnamese | | 🇿🇦 Afrikaans |
| 🇵🇹 Portuguese | 🇮🇩 Indonesian | | 🇰🇪 Swahili |
| 🇷🇺 Russian | 🇲🇾 Malay | | |
| 🇳🇱 Dutch | 🇵🇭 Filipino | | |
| 🇵🇱 Polish | | | |
| 🇨🇿 Czech | | | |

*Plus 20+ additional languages with full voice and text support!*

## 🚀 **Quick Start Guide**

### **Prerequisites**
- Python 3.8+
- Modern web browser with microphone access
- Stable internet connection
- API keys (instructions below)

### **Installation**

1. **Clone & Navigate**
   ```bash
   git clone https://github.com/yourusername/tellafriend.git
   cd tellafriend
   ```

2. **Virtual Environment Setup**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   
   Create `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here  
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

5. **Launch Application**
   ```bash
   python backend.py
   ```

6. **Start Conversing!**
   
   Visit `http://127.0.0.1:5000` and start talking in any language!

## 🏗️ **Technical Architecture**

### **Project Structure**
```
TellAFriend/
├── 📁 src/
│   ├── 📄 transcribe.py          # 🎙️ AssemblyAI speech-to-text
│   ├── 📄 tts.py                 # 🔊 ElevenLabs text-to-speech  
│   └── 📄 voice_translator.py    # 🌍 Google Translate integration
├── 📄 backend.py                 # 🚀 Flask server + AI logic
├── 📄 index.html                 # 🎨 Interactive web interface
├── 📄 requirements.txt           # 📦 Python dependencies
├── 📄 .env                       # 🔑 Environment variables
├── 📄 README.md                  # 📖 This documentation
└── 📁 venv/                      # 🐍 Virtual environment
```

### **Core Components**

#### **🧠 AI Mental Health Engine (`mental_support_ai`)**
- **Model**: Google Gemini 1.5 Flash
- **Capabilities**: 
  - Multilingual empathetic responses
  - Cultural context awareness
  - Crisis situation recognition
  - Emotional validation in native language

#### **🎙️ Speech Processing (`transcribe.py`)**
- **Service**: AssemblyAI Universal Speech Recognition
- **Features**:
  - Real-time audio transcription
  - 30+ language automatic detection
  - High accuracy for emotional speech
  - Background noise reduction

#### **🔊 Voice Synthesis (`tts.py`)**
- **Service**: ElevenLabs Multilingual TTS
- **Features**:
  - Emotion-aware voice synthesis
  - Native accents for each language
  - High-quality 44.1kHz audio
  - Streaming audio generation

#### **🌍 Translation Engine (`voice_translator.py`)**
- **Service**: Google Translate
- **Features**:
  - Auto-language detection
  - 30+ language pairs
  - Context-aware translation
  - Cultural adaptation

## 🎯 **API Endpoints Reference**

### **💬 Mental Health Chat**
```http
POST /chat
Content-Type: application/json

{
  "message": "I'm feeling overwhelmed today"
}

Response:
{
  "response": "I hear that you're feeling overwhelmed...",
  "success": true
}
```

### **🌍 Real-time Translation**
```http
POST /translate  
Content-Type: application/json

{
  "text": "Je me sens triste",
  "target_language": "english"
}

Response:
{
  "translated_text": "I feel sad",
  "success": true
}
```

### **🎙️ Speech-to-Text Transcription**
```http
POST /transcribe
Content-Type: multipart/form-data

Files: audio: [recorded_audio.wav]

Response:
{
  "transcription": "Hello, I need someone to talk to",
  "success": true
}
```

### **🔊 Text-to-Speech Generation**
```http
POST /tts
Content-Type: application/json

{
  "text": "I'm here to listen and support you"
}

Response: [Audio Stream - MP3 Format]
```

### **🔍 Health Check**
```http
GET /test

Response:
{
  "status": "Backend is running!",
  "endpoints": ["/chat", "/translate", "/transcribe", "/tts"],
  "success": true
}
```

## 🎮 **User Experience Features**

### **🎨 Modern Interface**
- **Dark Theme**: Eye-friendly design for sensitive conversations
- **Responsive**: Perfect on mobile, tablet, and desktop
- **Voice Indicators**: Visual feedback for recording and playback
- **Language Switcher**: Dropdown for instant language changes
- **Auto Voice Toggle**: Smart voice response activation

### **🎙️ Voice Interaction**
- **One-Click Recording**: Press and hold to record
- **Real-time Feedback**: Visual recording indicators
- **Automatic Playback**: AI responses play automatically
- **Volume Control**: Adjustable audio levels
- **Background Compatible**: Works while multitasking

### **📱 Accessibility**
- **Screen Reader Support**: Full accessibility compliance
- **Keyboard Navigation**: Complete keyboard control
- **High Contrast**: Readable for visual impairments
- **Text Alternatives**: Every voice feature has text backup

## 🔧 **Configuration & Customization**

### **🎛️ Advanced Settings**

#### **Voice Configuration (tts.py)**
```python
# Customize voice settings
voice_id = "NYkjXRso4QIcgWakN1Cr"  # Default multilingual voice
model_id = "eleven_multilingual_v2"   # High-quality model
output_format = "mp3_44100_128"       # Crystal clear audio
```

#### **AI Personality (backend.py)**
```python
# Customize AI response style
prompt = """You are a compassionate, warm multilingual mental health support AI.
- Always respond in the SAME LANGUAGE the user used
- Validate feelings without judgment  
- Offer gentle encouragement and hope
- Be culturally sensitive and appropriate
"""
```

#### **Language Extensions**
Add new languages by updating the language codes dictionary:
```python
language_codes = {
    'new_language': 'code',  # Add your language here
    # ... existing languages
}
```

## 🔐 **API Keys & Setup**

### **1. 🧠 Google Gemini AI**
```bash
# Visit: https://makersuite.google.com/app/apikey
# 1. Create Google account
# 2. Enable Gemini API
# 3. Generate API key
# 4. Add to .env: GEMINI_API_KEY=your_key
```

### **2. 🎙️ AssemblyAI Speech Recognition**  
```bash
# Visit: https://www.assemblyai.com/
# 1. Sign up for free account
# 2. Navigate to API keys section
# 3. Copy your API key
# 4. Add to .env: ASSEMBLYAI_API_KEY=your_key
```

### **3. 🔊 ElevenLabs Voice Synthesis**
```bash  
# Visit: https://elevenlabs.io/
# 1. Create account (free tier available)
# 2. Go to Profile → API Keys
# 3. Generate new API key
# 4. Add to .env: ELEVENLABS_API_KEY=your_key
```
##  Live Demo & Voice Samples

Want to hear TellAFriend in action? Check out our demo below:

<video controls width="720">
  <source src="Demo/demo_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Voice Samples**:  
- `Demo/spanish_support_example.mp3` – Empathetic Spanish reply  
- `Demo/arabic_transformation.wav` – Arabic response to English input  
...and more in the `Demo/` folder.

## 🌟 **Real-World Usage Scenarios**

### **Scenario 1: Multilingual Therapy Session**
```
👤 User (Arabic Voice): "أشعر بالقلق الشديد اليوم"
🤖 AI (English Voice): "I understand you're feeling very anxious today. That's completely valid..."
```

### **Scenario 2: Cultural Code-Switching**
```
👤 User (Spanish Text): "Mi familia no entiende mi depresión"
🤖 AI (Spanish Voice): "Entiendo que es difícil cuando la familia no comprende..."
```

### **Scenario 3: Learning & Support**
```
👤 User (English Voice): "Can you explain anxiety in simple terms?"
🤖 AI (User's Native Language): [Explains in user's preferred language]
```

## 🛡️ **Privacy & Security**

### **🔒 Data Protection**
- **No Storage**: Conversations are not stored permanently
- **Encrypted Transit**: All API calls use HTTPS
- **Temporary Files**: Audio files deleted after processing
- **API Key Security**: Environment variables for sensitive data

### **🏥 Mental Health Safety**
- **Crisis Detection**: Identifies serious mental health situations
- **Resource Provision**: Provides crisis hotline information
- **Professional Disclaimer**: Clear boundaries about AI limitations
- **Cultural Sensitivity**: Respects cultural mental health concepts

## 🤝 **Contributing to TellAFriend**

We welcome contributors! Here's how to get involved:

### **🚀 Development Setup**
```bash
# 1. Fork the repository
git fork https://github.com/maksuranuha/tellafriend.git

# 2. Create feature branch  
git checkout -b feature/amazing-new-feature

# 3. Make your changes
# 4. Test thoroughly
# 5. Submit pull request
```

### **🎯 Contribution Areas**
- **New Language Support**: Add more languages
- **Voice Improvements**: Better voice synthesis
- **UI/UX Enhancements**: Improve user interface
- **AI Responses**: Enhance mental health support
- **Mobile Apps**: iOS/Android applications
- **Documentation**: Improve guides and docs

### **📋 Development Guidelines**
- Follow PEP 8 style guide
- Add comprehensive comments
- Test all language combinations
- Ensure accessibility compliance
- Update documentation
- Respect mental health sensitivity

## 📊 **Performance & Scalability**

### **⚡ Response Times**
- **Text Chat**: < 2 seconds
- **Voice Transcription**: 3-5 seconds  
- **Voice Generation**: 2-4 seconds
- **Translation**: < 1 second
- **Total Voice-to-Voice**: 8-12 seconds

### **🔄 Scalability Features**
- **Async Processing**: Non-blocking API calls
- **File Cleanup**: Automatic temporary file management
- **Error Recovery**: Graceful failure handling
- **Rate Limiting**: Built-in API rate management

## 🌍 **Global Impact & Use Cases**

### **🎯 Target Users**
- **Multilingual Communities**: Immigrant support
- **Language Learners**: Mental health in native language  
- **Cultural Minorities**: Culturally-aware support
- **Global Organizations**: Employee mental health
- **Healthcare Providers**: Multilingual patient support

### **🏥 Professional Applications**
- **Therapy Preparation**: Pre-session anxiety support
- **Cultural Bridge**: Between therapist and patient
- **Crisis First Aid**: Immediate multilingual support
- **Educational Tool**: Mental health awareness
- **Accessibility Aid**: For hearing/speech impaired

## 🆘 **Mental Health Resources**

⚠️ **IMPORTANT**: TellAFriend provides supportive conversation but is not a replacement for professional mental health care.

### **🚨 Crisis Resources**
- **International**: [findahelpline.com](https://findahelpline.com)
- **US**: 988 Suicide & Crisis Lifeline
- **UK**: 116 123 Samaritans
- **Canada**: 1-833-456-4566
- **Australia**: 13 11 14 Lifeline

### **🌐 Global Mental Health Support**
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: [iasp.info](https://iasp.info)
- **Mental Health America**: [mhanational.org](https://mhanational.org)
- **World Health Organization**: [who.int/mental-health](https://who.int/mental-health)

## 📈 **Roadmap & Future Features**

### **🔮 Coming Soon**
- [ ] **Mobile Apps**: Native iOS and Android apps
- [ ] **Group Support**: Multilingual group chat rooms
- [ ] **AI Therapists**: Specialized therapy AI models
- [ ] **Emotion Recognition**: Facial/voice emotion analysis  
- [ ] **Personalization**: Learning user preferences
- [ ] **Integration**: WhatsApp, Telegram, Discord bots

### **💡 Innovation Pipeline**
- [ ] **AR/VR Support**: Immersive therapy sessions
- [ ] **Wearable Integration**: Apple Watch, Fitbit support
- [ ] **Family Features**: Support for family members
- [ ] **Professional Tools**: Therapist dashboard
- [ ] **Research Platform**: Anonymous usage insights

## 📄 **License & Legal**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **📝 Terms of Use**
- Free for personal and educational use
- Commercial use requires attribution
- No warranty for medical outcomes
- Users must be 13+ years old
- Comply with local mental health regulations

## 🙏 **Acknowledgments & Credits**

### **🏢 Technology Partners**
- **Google**: Gemini AI and Translation services
- **AssemblyAI**: Speech recognition technology
- **ElevenLabs**: Voice synthesis platform
- **Flask Community**: Web framework support

### **👥 Community**
- **Mental Health Advocates**: Guidance and feedback
- **Translators**: Language accuracy verification
- **Beta Testers**: Cross-cultural testing
- **Open Source Contributors**: Code improvements

### **❤️ Special Thanks**
- Mental health professionals who provided guidance
- Multilingual community for language testing
- Accessibility advocates for inclusive design
- Crisis counselors for safety recommendations

## 🌟 **Why TellAFriend Matters**

In a world where **1 in 4 people** experience mental health challenges, language barriers shouldn't prevent anyone from getting support. TellAFriend breaks down these barriers by providing:

- **🌍 Universal Access**: Support in your native language
- **🤖 24/7 Availability**: Always there when you need to talk
- **🎭 Cultural Sensitivity**: Understands cultural context
- **🔒 Safe Space**: Judgment-free, confidential environment
- **🚀 Innovative Technology**: Cutting-edge AI for better support

---

**⭐ Star this project if it made a difference in your life or cou
