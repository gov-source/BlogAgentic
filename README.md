# BlogAgentic 🤖✍️

A multi-agent content generation system built with LangGraph that autonomously creates, translates, and optimizes blog content across multiple languages.

## 🎯 What It Does

- **Intelligent Content Creation**: AI agents generate structured blog posts from topics
- **Multi-Language Translation**: Automatic translation to Hindi, French, and more
- **Agent Orchestration**: Uses LangGraph for coordinated multi-agent workflows
- **RESTful API**: FastAPI backend for easy integration

## 🏗️ Architecture
```
User Input → Topic Creation Agent → Content Generation Agent → Translation Router → Language-Specific Agents → Final Output
```

Built with:
- **LangGraph**: Agent orchestration and state management
- **LangChain**: LLM integration
- **FastAPI**: High-performance API
- **Claude/OpenAI**: Content generation

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- API key for Claude/OpenAI/Groq

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/BlogAgentic.git
cd BlogAgentic

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

### Run the API
```bash
uvicorn app:app --reload
```

API will be available at `http://localhost:8000`

### Example Request
```bash
curl -X POST "http://localhost:8000/blogs" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "AI Agents",
    "current_language": "hindi"
  }'
```

## 📁 Project Structure
```
BlogAgentic/
├── app.py                 # FastAPI application
├── src/
│   ├── nodes/
│   │   └── graphnodes.py # LangGraph node definitions
│   ├── states/
│   │   └── blogstate.py  # State schemas
│   └── graph/
│       └── workflow.py    # Graph construction
├── requirements.txt
└── README.md
```

## 🔧 Configuration

Edit `.env`:
```env
ANTHROPIC_API_KEY=your_key_here
# or
OPENAI_API_KEY=your_key_here
```

## 🛣️ Roadmap

- [ ] Add support for 10+ languages
- [ ] Implement content quality scoring
- [ ] Add SEO optimization agent
- [ ] Web interface for content generation
- [ ] Batch processing for multiple topics
- [ ] Custom styling and tone agents

## 🤝 Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Areas to contribute:**
- New language translation agents
- Content quality improvements
- Performance optimizations
- Documentation improvements
- Bug fixes

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Anthropic Claude](https://www.anthropic.com)

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/YOUR_USERNAME/BlogAgentic](https://github.com/YOUR_USERNAME/BlogAgentic)

---

**⭐ If this project helps you, please star it!**
