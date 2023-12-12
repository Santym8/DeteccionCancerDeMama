from django.shortcuts import render
from .forms import DataForm
from keras.models import load_model
import joblib

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            model = load_model("app/data/model.h5")
            min_max_scaler = joblib.load("app/data/min_max_scaler.save")

            data = form.to_np().reshape(1, -1)
            data = min_max_scaler.transform(data)

            prediction = model.predict(data).round()
            prediction = "Cancer Negativo" if prediction == 0 else "Cancer Positivo"
            return render(request, 'index.html', 
                          {'form': form, 'prediction': prediction})
            
    form = DataForm()
    return render(request, 'index.html', {'form': form})