# -*- coding: utf-8 -*-
"""Fashion MNIST Mini Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13MX02ttrR7hWNDe09NxtCzk3BOD4xdAI

Milan Gandhi; C Format; CSC 590

Some problems I encountered were (initially) several implementation bugs or other issues with forgetting certain layers, steps, values, or mismatching values in the model building and testing phases. However, I rectified this after some time. Another problem I ran into was the false perception that the model was performing well, when in reality, it was simply an error with the output variable. 

Another issue I initially faced, but quickly overcome, was the use of improper optimizers and metrics that did not produce desirable results. As such, the loss and accuracy figures were well, well below desired figures. 


Outcomes from the chosen modifications(s): 
During the training phases of 1, 5, and 25 epochs (and more in some cases), I observed an interesting pattern as the epochs got higher. The accuracy improved, but it seemed to do so with diminishing returns, and the accuracy and loss started to plateau as the accuracy approached 100 (or 1.0) and the loss approached 0.00. This observation held true for all epochs of greater than 1, and was especially noticeable at higher numbers. 

Additionally, I also tested other activation functions. However, I noticed that none of the ones tested - Sigmoid, Serialize, Linear - gave improved results from relu. Such activation function, loss function, and optimizer function changes are topics that I would like to continue to explore in the future.
"""

import tensorflow as tf 
mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
                                    
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dense(64),
])

predictions = model(x_train[:20]).numpy()
tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:20], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)