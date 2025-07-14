# CallSummarizeAI 📞🧠

A real-time call summarizer that listens to spoken conversations, transcribes them using Whisper, and generates bullet-point summaries with GPT.

---

## Features

- 🎧 Real-time or recorded call input
- 📝 Whisper-based transcription
- 🧠 GPT-generated summary
- 🗂️ JSON logs with timestamped input/summary pairs
- 🚀 Modular structure ready for scaling

---

## Why I Built This

After building a basic voice agent, I wanted to explore how AI could listen passively and provide insight rather than just respond. CallSummarizeAI is my attempt to think beyond chat — toward productivity, recall, and analysis.

This use case overlaps with what Krew is building — especially in terms of understanding conversation tone, automating routine communication, and optimizing messaging through analysis.

---

## Usage (WIP)

```bash
python main.py
```

> Note: Currently in scaffold mode. Working on audio capture + streaming transcription.

---

## Next Steps

- [ ] Add Twilio/Zoom audio ingestion
- [ ] Improve bullet summary formatting
- [ ] A/B test summary phrasing with prompt variations
