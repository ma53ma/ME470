import tensorflow as tf

#model = tf.keras.models.load_model(sidewalk_weights.h5)
#tf.saved_model.save(model, sidewalk_weights.pb)


pre_model = tf.keras.models.load_model(r"C:\Users\scott\OneDrive\Documents\GitHub\ME470\h5topb\sidewalk_weights.h5")
pre_model.save(r"C:\Users\scott\OneDrive\Documents\GitHub\ME470\h5topb\sidewalk_weights.h5")
