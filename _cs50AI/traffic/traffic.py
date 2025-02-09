import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import time
import math


from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1]) #what im doing --- boring stuff tbh

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model() #what im doing

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3.

    `labels` should be a list of integer labels, representing the categories for each of the
    corresponding `images`. -- this means

    """
    #learn to work with files
    #omg so i need to transform images !INTO ARRAYS
    number = 0
    images = []
    labels = []
    while True:
        folder = os.path.join(data_dir, str(number))


        if not os.path.exists(folder):
            break
        else:
            images_paths = [file.path for file in os.scandir(folder) if file.is_file()]
            for image_path in images_paths:

                # • The file path 'gtsrb-small/0/gtsrb-small/0/00015_00010. ppm' may be incorrect.
                img = cv2.imread(image_path) #, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
                #maybe i need to resize in a different way
                images.append(resized_image)
                labels.append(number)


        number += 1


    return (images, labels)





def get_model(filter_repeats=2, dense_layers=5, unitcount=300, features=35):
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([])

    expected_dimentions = IMG_WIDTH

    for _ in range(filter_repeats):

        if _ == 0:  # Only set input_shape in the first layer
            model.add(tf.keras.layers.Conv2D(features, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 1)))
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
            expected_dimentions //= 2

        elif expected_dimentions >= 4:
            model.add(tf.keras.layers.Conv2D(features, (3, 3), activation='relu')) # need to do a filter multiplyer?
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
            expected_dimentions //= 2

        else:
            print('no features left')
            print(filter_repeats)
            break

    model.add(tf.keras.layers.Flatten()),
    model.add(tf.keras.layers.Dropout(0.4))

    r = (8000 / 40000) ** (1/(dense_layers))
    for _ in range(dense_layers):
        model.add(tf.keras.layers.Dense(unitcount, activation='relu'))
        unitcount = math.floor(unitcount * r)
        # model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax'))


    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    # model.summary()

    return model


#this is my training function
# def train_model(filter_repeats, dense_layers, unitcount, features, x_train, y_train):
#     model = get_model(filter_repeats, dense_layers, unitcount, features) #what im doing

#     # Fit model on training data

#     start_time = time.time()
#     model.fit(x_train, y_train, epochs=10)
#     loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
#     end_time = time.time()
#     execution_time = end_time - start_time

#     return (loss, accuracy, execution_time)





if __name__ == "__main__":
    # Split data into training and testing sets
    main()

    # if len(sys.argv) not in [2, 3]:
    #     sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # # Get image arrays and labels for all image files
    # images, labels = load_data(sys.argv[1]) #what im doing --- boring stuff tbh

    # labels = tf.keras.utils.to_categorical(labels)
    # x_train, x_test, y_train, y_test = train_test_split(
    #     np.array(images), np.array(labels), test_size=TEST_SIZE
    # )

    # with open('output.txt', "a") as file:
    #     file.write(f"filters,layers,units,features,loss,accuracy,time\n")

    # #i should also change the
    # best_accuracy = 0

    # for filter_repeats in [2]:
    #     for dense_layers in [6, 7, 8]: # loss in 6 layers is less
    #         for unitcount in [250, 300, 350]: #250 is the best, bigger is worse
    #             for features in [40, 50]: # 20 is better than bigger, less than 40
    #                 with open("output.txt", "a") as file:
    #                     loss, accuracy, execution_time = train_model(filter_repeats, dense_layers, unitcount, features, x_train, y_train)
    #                     if accuracy > best_accuracy:
    #                         best_accuracy = accuracy
    #                     file.write(f"{str(filter_repeats)},{str(dense_layers)},{str(unitcount)},{str(features)},{str(loss)},{str(accuracy)},{str(execution_time)}\n")

    # # def get_model(filter_repeats=2, dense_layers=6, unitcount=300, features=35):

    # print(str(best_accuracy))



