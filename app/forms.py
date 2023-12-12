from django import forms
import numpy as np

class DataForm(forms.Form):
    radius = forms.FloatField(label='Radio', required=True)
    texture = forms.FloatField(label='Textura', required=True)
    perimeter = forms.FloatField(label='Perimetro', required=True)
    area = forms.FloatField(label='Area', required=True)
    smoothness = forms.FloatField(label='Suavidad', required=True)
    compactness = forms.FloatField(label='Compactibilidad', required=True)
    concavity = forms.FloatField(label='Concavidad', required=True)
    concave_points = forms.FloatField(label='Puntos Concavos', required=True)
    symmetry = forms.FloatField(label='Simetria', required=True)
    fractal_dimension = forms.FloatField(label='Dimension Fractal', required=True)

    radius_2 = forms.FloatField(label='Radio', required=True)
    texture_2 = forms.FloatField(label='Textura', required=True)
    perimeter_2 = forms.FloatField(label='Perimetro', required=True)
    area_2 = forms.FloatField(label='Area', required=True)
    smoothness_2 = forms.FloatField(label='Suavidad', required=True)
    compactness_2 = forms.FloatField(label='Compactibilidad', required=True)
    concavity_2 = forms.FloatField(label='Concavidad', required=True)
    concave_points_2 = forms.FloatField(label='Puntos Concavos', required=True)
    symmetry_2 = forms.FloatField(label='Simetria', required=True)
    fractal_dimension_2 = forms.FloatField(label='Dimension Fractal', required=True)

    radius_3 = forms.FloatField(label='Radio', required=True)
    texture_3 = forms.FloatField(label='Textura', required=True)
    perimeter_3 = forms.FloatField(label='Perimetro', required=True)
    area_3 = forms.FloatField(label='Area', required=True)
    smoothness_3 = forms.FloatField(label='Suavidad', required=True)
    compactness_3 = forms.FloatField(label='Compactibilidad', required=True)
    concavity_3 = forms.FloatField(label='Concavidad', required=True)
    concave_points_3 = forms.FloatField(label='Puntos Concavos', required=True)
    symmetry_3 = forms.FloatField(label='Simetria', required=True)
    fractal_dimension_3 = forms.FloatField(label='Dimension Fractal', required=True)

    def to_np(self):
        data = [[
            self.cleaned_data['radius'], 
            self.cleaned_data['texture'], 
            self.cleaned_data['perimeter'], 
            self.cleaned_data['area'], 
            self.cleaned_data['smoothness'], 
            self.cleaned_data['compactness'], 
            self.cleaned_data['concavity'], 
            self.cleaned_data['concave_points'], 
            self.cleaned_data['symmetry'], 
            self.cleaned_data['fractal_dimension'], 
            self.cleaned_data['radius_2'], 
            self.cleaned_data['texture_2'], 
            self.cleaned_data['perimeter_2'], 
            self.cleaned_data['area_2'], 
            self.cleaned_data['smoothness_2'], 
            self.cleaned_data['compactness_2'], 
            self.cleaned_data['concavity_2'], 
            self.cleaned_data['concave_points_2'], 
            self.cleaned_data['symmetry_2'], 
            self.cleaned_data['fractal_dimension_2'], 
            self.cleaned_data['radius_3'], 
            self.cleaned_data['texture_3'], 
            self.cleaned_data['perimeter_3'], 
            self.cleaned_data['area_3'], 
            self.cleaned_data['smoothness_3'], 
            self.cleaned_data['compactness_3'], 
            self.cleaned_data['concavity_3'], 
            self.cleaned_data['concave_points_3'], 
            self.cleaned_data['symmetry_3'], 
            self.cleaned_data['fractal_dimension_3']
        ]]
       
        return np.array(data, dtype="float32")
       

        
    

   

