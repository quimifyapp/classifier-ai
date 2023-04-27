import tensorflow as tf


@tf.keras.utils.register_keras_serializable()
def data_standardization(input_data):  # CH3-CH=CH-CH(NO2)Br
    input_data = tf.strings.lower(input_data)  # ch3-ch=ch-ch(no2)br
    input_data = tf.strings.regex_replace(input_data, "[^a-zà-ú]", ' ')  # ch  ch ch ch no  br # TODO reconsider
    return tf.strings.regex_replace(input_data, "\s+", ' ')  # ch ch ch ch no br


class Model:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, text):
        return self.model.predict([text])[0][0]
