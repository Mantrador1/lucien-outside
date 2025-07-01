# Έλεγχος αν το API_KEY είναι ορισμένο
if (-not $env:API_KEY -or $env:API_KEY -eq "") {
    Write-Host "❌ ERROR: Η μεταβλητή περιβάλλοντος API_KEY δεν είναι ορισμένη ή είναι κενή."
    Write-Host "Παρακαλώ πρόσθεσε το API_KEY στο αρχείο .env ή όρισε το χειροκίνητα με:"
    Write-Host '$env:API_KEY="το_κλειδί_σου_εδώ"'
    exit 1
} else {
    Write-Host "✅ Το API_KEY έχει οριστεί σωστά."
}

# Εκκίνηση Flask server
Write-Host "🚀 Εκκίνηση Flask server..."
python main.py
