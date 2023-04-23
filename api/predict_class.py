#!/usr/bin/python3

import tensorflow as tf
import os

class Predict():
    def __init__(self):
        # Data location
        self.models_dir = os.path.join("..", "builder", "models")
        self.formula_name_model_path = os.path.join(self.models_dir, "formula-name-model")
        self.formula_model_path = os.path.join(self.models_dir, "formula-inorganic-organic-model")
        self.name_model_path = os.path.join(self.models_dir, "name-inorganic-organic-model")
        
        @tf.keras.utils.register_keras_serializable()
        def data_standardization(input_data): # CH3-CH=CH-CH(NO2)Br
            input_data = tf.strings.lower(input_data) # ch3-ch=ch-ch(no2)br
            input_data = tf.strings.regex_replace(input_data, "[^a-zà-ú]", ' ') # ch  ch ch ch no  br
            return tf.strings.regex_replace(input_data, "\s+", ' ') # ch ch ch ch no br
        
        # Load models
        self.formula_name_model = tf.keras.models.load_model(self.formula_name_model_path)
        self.formula_model = tf.keras.models.load_model(self.formula_model_path)
        self.name_model = tf.keras.models.load_model(self.name_model_path)
    
    def predict(self, example):
        category = -1
        
        # Predicts if it is "name" or "formula"
        if self.formula_name_model.predict([example])[0][0] * 100 < 50:
            # Formula
            if self.formula_model.predict([example])[0][0] * 100 < 50:
                # Inorganic formula
                category = 0
            else:
                # Organic formula
                category = 1
        else:
            # Name
            if self.name_model.predict([example])[0][0] * 100 < 50:
                # Inorganic name
                category = 2
            else:
                # Organic name
                category = 3
        
        return category
        
        
if __name__ == '__main__':
    print(Predict().predict("oxido"))