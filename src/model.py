import tensorflow as tf
from tensorflow.python.keras import layers, losses


class Model:

    @staticmethod
    @tf.keras.utils.register_keras_serializable()
    def data_standardization(input_data):  # "CH3-CH=CH-CH(NO2)Br"
        input_data = tf.strings.lower(input_data)  # "ch3-ch=ch-ch(no2)br"
        return tf.strings.regex_replace(input_data, r".", r"\0 ")  # "c h 3 - c h = c h - c h ( n o 2 ) b r"

    def __init__(self, model_path=None, max_features=None, embedding_dim=None):
        if model_path is not None:
            self.model = tf.keras.models.load_model(model_path)
        elif max_features is not None and embedding_dim is not None:
            self.model = tf.keras.Sequential([
                layers.Embedding(max_features + 1, embedding_dim),
                layers.Dropout(0.2),
                layers.Dense(256, activation="relu"),
                layers.GlobalAveragePooling1D(),
                layers.Dropout(0.2),
                layers.Dense(1),
            ])

            self.model.compile(
                optimizer="adam",
                metrics=tf.metrics.BinaryAccuracy(threshold=0.0),
                loss=losses.BinaryCrossentropy(from_logits=True),
            )

    def predict(self, text):
        return self.model.predict([text], verbose=0)[0][0]

    def get(self):
        return self.model

    @staticmethod
    def cleanup():
        # Otherwise there's a memory leak
        tf.keras.backend.clear_session()
