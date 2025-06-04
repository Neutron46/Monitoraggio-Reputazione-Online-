import unittest
from src.model import load_sentiment_model, predict_sentiment

# Definiamo una classe di test ereditata da unittest.TestCase
# Tutti i metodi in questa classe il cui nome inizia con 'test_' saranno automaticamente eseguiti come test unitari.

class TestSentimentModel(unittest.TestCase):
    # Questo test unitario assicura che il modello e il tokenizer vengano caricati correttamente.
    def test_model_loading(self):
        # Carica il tokenizer e il modello
        tokenizer, model = load_sentiment_model()
        # Verifica che il tokenizer non sia nullo
        self.assertIsNotNone(tokenizer)
        # Verifica che il modello non sia nullo
        self.assertIsNotNone(model)

    # Questo test verifica la predizione del sentiment
    def test_sentiment_prediction(self):
        # Carica tokenizer e modello
        tokenizer, model = load_sentiment_model()
        # Definisce le frasi di test
        texts = ["This is fantastic!", "This is horrible!"]
        # Chiama la funzione predict_sentiment con le frasi, il modello e il tokenizer
        sentiments = predict_sentiment(texts, tokenizer, model)
        # Verifica che la lunghezza della sentiment list sia la stessa della lista di input
        self.assertEqual(len(sentiments), len(texts))
        # Verifica che il primo esito sia positivo
        self.assertEqual(sentiments[0], 'positive')
        # Verifica che il secondo esito sia negativo
        self.assertEqual(sentiments[1], 'negative')

if __name__ == '__main__':
    unittest.main()