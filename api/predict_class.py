#!/usr/bin/python3

import tensorflow as tf
import os

class Predict():
    def __init__(self):
        # Data location
        self.models_dir = os.path.join("..", "builder", "models")
        self.formula_name_path = os.path.join(self.models_dir, "formula-name-model")
        
        @tf.keras.utils.register_keras_serializable()
        def data_standardization(input_data): # CH3-CH=CH-CH(NO2)Br
            input_data = tf.strings.lower(input_data) # ch3-ch=ch-ch(no2)br
            input_data = tf.strings.regex_replace(input_data, "[^a-zà-ú]", ' ') # ch  ch ch ch no  br
            return tf.strings.regex_replace(input_data, "\s+", ' ') # ch ch ch ch no br
        
        # Load models
        self.model_formula_name = tf.keras.models.load_model(self.formula_name_path)
        
    def predict(self, example):
        first_category = "formula"
        second_category = "name"
        
        prediction = self.model_formula_name.predict([example])[0][0] * 100
        category = first_category if prediction < 50 else second_category
        
        return category
        
        
if __name__ == '__main__':
    print(Predict().predict("oxido"))