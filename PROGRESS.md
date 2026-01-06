# Assister - AI Voice Assistant App

> A proof-of-concept Android app for managing daily tasks through natural conversation

**Project Started:** January 6, 2026  
**Last Updated:** January 6, 2026

---

## 📋 Project Overview

Assister is a voice-enabled AI assistant Android app that allows users to:
- Set reminders through natural conversation
- Write and manage notes
- Add calendar events
- General task management via voice commands

The app uses an **agentic AI architecture** powered by **LangGraph** for intelligent task routing and execution.

---

## 🛠️ Technology Stack

### Mobile App (Frontend)
| Component | Technology | Status |
|-----------|------------|--------|
| Framework | **Flet** (Python) | ⏳ Not Started |
| Voice Input | SpeechRecognition | ⏳ Not Started |
| Voice Output | pyttsx3 / gTTS | ⏳ Not Started |
| Local Storage | SQLite | ⏳ Not Started |

### Backend (AI Agent)
| Component | Technology | Status |
|-----------|------------|--------|
| API Framework | **FastAPI** | ⏳ Not Started |
| AI Framework | **LangGraph** + LangChain | ⏳ Not Started |
| LLM Provider | TBD (OpenAI/Bedrock/Ollama) | ⏳ Not Started |
| Database | SQLite / PostgreSQL | ⏳ Not Started |

---

## 🎯 Features Roadmap

### Phase 1: Foundation (MVP)
- [ ] Project structure setup
- [ ] Basic Flet app with chat UI
- [ ] FastAPI backend skeleton
- [ ] LangGraph agent with basic routing
- [ ] Text-based interaction (no voice yet)

### Phase 2: Core Features
- [ ] Reminder Tool (create, list, delete reminders)
- [ ] Notes Tool (create, read, update, delete notes)
- [ ] Calendar Tool (add events, view schedule)
- [ ] Persistent storage for all data

### Phase 3: Voice Integration
- [ ] Voice input (speech-to-text)
- [ ] Voice output (text-to-speech)
- [ ] Wake word detection (optional)
- [ ] Continuous conversation mode

### Phase 4: Polish & Deployment
- [ ] Android APK build
- [ ] UI/UX improvements
- [ ] Error handling & edge cases
- [ ] Performance optimization

---

## 📁 Project Structure (Planned)

```
Assister/
├── app/                      # Flet mobile app
│   ├── main.py              # App entry point
│   ├── screens/             # UI screens
│   │   ├── chat.py          # Main chat interface
│   │   ├── settings.py      # Settings screen
│   │   └── history.py       # Conversation history
│   ├── services/            # App services
│   │   ├── api_client.py    # Backend API client
│   │   ├── voice.py         # Voice processing
│   │   └── storage.py       # Local storage
│   └── components/          # Reusable UI components
│
├── backend/                  # FastAPI + LangGraph backend
│   ├── main.py              # FastAPI entry point
│   ├── agent/               # LangGraph agent
│   │   ├── graph.py         # Agent graph definition
│   │   ├── state.py         # Agent state
│   │   └── nodes.py         # Graph nodes
│   ├── tools/               # Agent tools
│   │   ├── reminders.py     # Reminder management
│   │   ├── notes.py         # Notes management
│   │   └── calendar.py      # Calendar management
│   ├── models/              # Data models
│   └── database/            # Database layer
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── PROGRESS.md              # This file
```

---

## 📝 Development Log

### January 6, 2026
- [x] Project initialized
- [x] Technology stack decided (Flet + FastAPI + LangGraph)
- [x] Progress tracking document created
- [ ] **NEXT:** Set up project structure and dependencies

---

## 🔗 Resources & References

- [Flet Documentation](https://flet.dev/docs/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Flet Android Packaging](https://flet.dev/docs/guides/python/packaging-android/)

---

## ❓ Open Questions / Decisions Needed

1. **LLM Provider:** Which LLM to use? (OpenAI, AWS Bedrock, local Ollama?)
2. **Deployment:** Cloud backend or on-device processing?
3. **Voice API:** Native Android speech APIs or cloud-based (Google Cloud Speech)?
4. **Authentication:** Will the app need user accounts?

---

## 🐛 Known Issues

*No issues reported yet.*

---

## 💡 Ideas / Future Enhancements

- Smart notification scheduling
- Integration with external calendars (Google Calendar)
- Multi-language support
- Habit tracking feature
- Daily summaries and insights
