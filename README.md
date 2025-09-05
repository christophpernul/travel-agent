# travel-agent

A travel agent that can help you find places to eat, drink or see.

## Technical setup

The dependencies can be installed with `uv sync`.
The agent is built using `openai` and `agents` frameworks and uses `gpt-4o-mini` as an LLM model.

### Quick Start

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Test the setup:**
   ```bash
   python test_setup.py
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:7860` to access the Gradio interface.

### Project Structure

```
tennis-booking-assistant/
├── src/
│   ├── agent/           # AI agent logic
│   ├── booking/         # STC booking system integration
│   ├── data/           # Court data and user preferences
│   ├── interface/      # Gradio web interface
│   └── main.py         # Application entry point
├── run.py              # CLI launcher
├── test_setup.py       # Setup verification
└── pyproject.toml      # Project configuration
```

## Assistant Purpose