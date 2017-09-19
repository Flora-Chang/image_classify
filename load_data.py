from keras.preprocessing.image import ImageDataGenerator
from util import FLAGS
import numpy as np
from PIL import Image

#preprocessing the image to match the ImageNet
def pre_function(x):
    #switch RGB to GBR
    image = x[:, :, ::-1]
    image = np.array(image, dtype="float64")
    #substract ImageNet mean pixel
    image[:, :, 0] -= 103.939
    image[:, :, 1] -= 116.779
    image[:, :, 2] -= 123.68
    return image

train_datagen = ImageDataGenerator(rescale=1.,
                                     #shear_range=0.1,
                                     #zoom_range=0.1,
                                     #rotation_range=10.,
                                     #width_shift_range=0.1,
                                     #height_shift_range=0.1,
                                     horizontal_flip=False,
                                     vertical_flip=False,
                                     #preprocessing_function=pre_function,
                                    )

val_datagen = ImageDataGenerator(rescale=1.,
                                 #preprocessing_function=pre_function，
                                 )

train_generator = train_datagen.flow_from_directory(FLAGS.train_dir,
                                                    target_size=(FLAGS.width, FLAGS.height),
                                                    batch_size=FLAGS.batch_size,
                                                    shuffle=True,
                                                    class_mode="categorical",)
validation_generator = val_datagen.flow_from_directory(FLAGS.val_dir,
                                                       target_size=(FLAGS.width, FLAGS.height),
                                                       batch_size=FLAGS.batch_size,
                                                       shuffle=False,
                                                       class_mode="categorical",
                                                       #save_to_dir="../data/visualizasion",
                                                       #save_prefix="pre"
                                                        )





