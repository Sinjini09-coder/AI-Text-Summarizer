from app.models.summarizer_model import summarizer_pipeline

def generate_summary(text: str):
    summary = summarizer_pipeline(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']