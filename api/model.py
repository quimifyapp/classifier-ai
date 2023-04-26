#!/usr/bin/python3

import os
import tensorflow as tf


class Model:
    def __init__(self):
        # Data location
        self.models_dir = os.path.join("..", "builder", "models") # TODO parameter
        self.formula_name_model_path = os.path.join(self.models_dir, "formula-name-model")
        self.formula_inorganic_organic_model_path = os.path.join(self.models_dir, "formula-inorganic-organic-model")
        self.name_inorganic_organic_model_path = os.path.join(self.models_dir, "name-inorganic-organic-model")

        @tf.keras.utils.register_keras_serializable()
        def data_standardization(input_data):  # CH3-CH=CH-CH(NO2)Br
            input_data = tf.strings.lower(input_data)  # ch3-ch=ch-ch(no2)br
            input_data = tf.strings.regex_replace(input_data, "[^a-zà-ú]", ' ')  # ch  ch ch ch no  br # TODO reconsider
            return tf.strings.regex_replace(input_data, "\s+", ' ')  # ch ch ch ch no br

        # Load models
        self.formula_name_model = tf.keras.models.load_model(self.formula_name_model_path)
        self.formula_inorganic_organic_model = tf.keras.models.load_model(self.formula_inorganic_organic_model_path)
        self.name_inorganic_organic_model = tf.keras.models.load_model(self.name_inorganic_organic_model_path)

    def formula_or_name(self, text):
        return self.formula_name_model.predict([text])[0][0]

    def formula_inorganic_or_organic(self, text):
        return self.formula_inorganic_organic_model.predict([text])[0][0]

    def name_inorganic_or_organic(self, text):
        return self.name_inorganic_organic_model.predict([text])[0][0]

    def classify(self, text):  # TODO improve
        category = -1

        # Predicts if it is "name" or "formula"
        if self.formula_name_model.predict([text])[0][0] * 100 < 50:
            # Formula
            if self.formula_inorganic_organic_model.predict([text])[0][0] * 100 < 50:
                # Inorganic formula
                category = 0
            else:
                # Organic formula
                category = 1
        else:
            # Name
            if self.name_inorganic_organic_model.predict([text])[0][0] * 100 < 50:
                # Inorganic name
                category = 2
            else:
                # Organic name
                category = 3

        return category


if __name__ == '__main__':
    print(Model().predict("oxido"))
