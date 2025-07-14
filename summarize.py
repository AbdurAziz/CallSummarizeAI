from transformers import pipeline

# Load summarization pipeline using facebook/bart-large-cnn
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    try:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Summary generation error: {e}")
        return "Summary unavailable."

