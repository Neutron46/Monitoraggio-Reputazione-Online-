import os
import torch
from datasets import load_dataset
from src.model import load_sentiment_model

def monitor_sentiment(dataset_name="emotion", sample_size=10):
    """
    Il sistema carica un modello di sentiment, un dataset, e successivamente svolge un monitoraggio iniziale. 
    """
    try:
        tokenizer, model = load_sentiment_model()
        print("Modello caricato con successo per il monitoraggio.")
    except Exception as e:
        print(f"Errore nel caricamento del modello: {e}")
        return

    try:
        dataset = load_dataset(dataset_name)
        print(f"Dataset '{dataset_name}' caricato con successo per il monitoraggio.")
        if 'test' not in dataset:
            print("Il dataset è privo della suddivisione 'test'. Di conseguenza, si utilizzerà la suddivisione 'train', sebbene ciò possa non essere ottimale per una valutazione accurata.")
            split_name = 'train'
        else:
            split_name = 'test'
        sample = dataset[split_name].shuffle().select(range(sample_size))
    except Exception as e:
        print(f"Errore nel caricamento del dataset '{dataset_name}': {e}")
        return

    results = []
    for example in sample:
        text = example['text']  # Prendiamo per buono che il dataset abbia una colonna 'text'
        inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        probabilities = outputs.logits.softmax(dim=-1)
        predicted_label = torch.argmax(probabilities).item()
        labels = ['negative', 'neutral', 'positive']  # Fissiamo queste come etichette
        sentiment = labels[predicted_label]
        results.append({"text": text, "sentiment": sentiment})
        print(f"Testo: '{text}' - Sentiment: {sentiment}")

if __name__ == "__main__":
    monitor_sentiment(dataset_name="emotion", sample_size=10)
