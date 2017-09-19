#encoding: utf-8
import tensorflow as tf

flags = tf.app.flags

flags.DEFINE_string("model", "resnet50", "model name")

flags.DEFINE_integer("num_classes", 80, "the classes of the images")
flags.DEFINE_integer("width", 224, "the width of the input images")
flags.DEFINE_integer("height", 224, "the height of the images")
flags.DEFINE_integer("channel", 3, "the channel of the images")
flags.DEFINE_integer("train_samples", 10000, "the num of images in the training set")
flags.DEFINE_integer("val_samples", 1000, "the num of images in the validation set")


flags.DEFINE_integer("batch_size", 64, "batch size")
flags.DEFINE_integer("epoch", 50, "the num of training epoch")
flags.DEFINE_integer("drop_rate", 0.2, "dropout size")
flags.DEFINE_integer("embedding_dim", 200, "the embedding dimension")

flags.DEFINE_string("root_dir", "../image_classify/", "the root path")
flags.DEFINE_string("train_dir", "../data/ai_challenger_scene_train_20170904/little_train_images/", "the training data directory")
flags.DEFINE_string("val_dir", "../data/ai_challenger_scene_validation_20170908/little_val_images/", "the validation data directory")
#flags.DEFINE_string("batch_size", 64, "batch size")
#flags.DEFINE_string("batch_size", 64, "batch size")

FLAGS = flags.FLAGS