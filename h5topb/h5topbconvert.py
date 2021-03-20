import tensorflow as tf

#model = tf.keras.models.load_model(sidewalk_weights.h5)
#tf.saved_model.save(model, sidewalk_weights.pb)


pre_model = tf.keras.models.load_model("sidewalk_weights2.h5")
pre_model.save("sidewalk_weights2.h5")
