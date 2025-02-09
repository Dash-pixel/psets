# Neural Network Optimization Log
in this project i searched for good configuration of the classification model -- ie the ones that are quick to achieve high accuracy on low (3) epoches -- (i recognise that it is not the best metric) -- realized that doing so algorithmically would save me time -- i will not have to rerun things myself if i change something -- i made a bunch of for loops to change the model a little (eg 1 layer or 2, 10 units or 40) and see what works best. Then i realized that this is essentially an optimization task - something that neural networks are best at. So next time i will task a neural network to optimize my image recognission model. i will also probably increase number of types of samples in classification task slowly.


## Starting Point

### Initial Model Configuration

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(10, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(10, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])
```

- Dataset: Small dataset.
- Initial performance:
  - Accuracy: **0.6339**
  - Loss: **1.0292**

### Observations and Changes

1. **Too many layers:** Removed one dense layer (10 units).

   - Result: Accuracy improved to **0.9762**, loss reduced to **0.1273**.

2. **Simplification hypothesis:** Kept the second dense layer but increased units.

   - Result: Accuracy further improved to **0.9851**, loss reduced to **0.0446**.

3. **Experimenting with single-layer changes:**

   - Removed the second dense layer and increased units in the remaining dense layer.
   - Result:
     - **150 units:** Accuracy = **0.9911**, Loss = **0.0275**
     - **500 units:** Accuracy = **0.9970**, Loss = **0.0061**
     - **1000 units:** No marginal improvement, accuracy remained **0.9970**, loss slightly increased (**0.0094**).

### Trade-offs and Insights

- Increasing units seems more effective than adding layers.
- Higher unit counts improve performance but hit diminishing returns around **500 units**.
- The current model may not generalize well for larger datasets or more training groups.

---

## Testing Multi-layer Configurations

### Experiments with Multiple Layers

- **3 layers of 500 units:**
  - Accuracy: **0.9762**, Loss: **0.1766**.
- **4 layers of 500 units:**
  - Accuracy: **0.9940**, Loss: **0.0113**.
- **6 layers of 500 units:**
  - Accuracy: **0.9970**, Loss: **0.0390**.

### Optimizing for Efficiency

- Reduced units per layer to **100** with **6 layers:**
  - Accuracy: **0.9940**, Loss: **0.0235**.
- Reduced to **5 layers with 100 units each:**
  - Accuracy: **1.0000**, Loss: **0.0032**.

### Key Insight

- Performance does not directly correlate with the number of layers. Doubling units often yields better results than doubling layers.

---

## Transition to Larger Dataset

### Initial Test with Larger Dataset

- Model: 500 units per layer, 6 layers.
- Results:
  - Accuracy: **0.9404**
  - Loss: **0.2818**
  - Speed: 23–51 seconds.

### Adjustments and Observations

1. **Decreased layers:**

   - Did not significantly improve speed, suggesting a bottleneck elsewhere.

2. **Increased units:**

   - Doubling units doubled the runtime but had no significant performance improvement.
   - Accuracy = **0.9356**, Loss = **0.3143**.

### Future Directions

- Explore kernel/filter adjustments for convolutional layers.
- Investigate the source of bottlenecks.
- Focus on identifying optimal unit-layer trade-offs for larger datasets.

---
after some time i decided to do some automatization to see what works and what doesnt
and also using multiplication by 2 rather then increasing linnearly
i also needed to print the timings of each step to best adapt it.
and adapt tensor flow to my hardware, since time turned out to be a big issue

i decided to run model many times, so that the input is better structured
and also decrease the number of echos for evaluation how good my model is at learning
i found easily parametizable things and decided that i will sqare the sizes

    model = tf.keras.models.Sequential([
        #image filters
        *([tf.keras.layers.Conv2D(10, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 1)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2))] * filter_repeats),

        tf.keras.layers.Flatten(),

        #dense layers
        *([tf.keras.layers.Dense(unitcount, activation='relu')] * dense_layers),

        #the end
        tf.keras.layers.Dense(3, activation='softmax')
    ])

  in my last adjustment on a big model
   333/333 - 2s - 7ms/step - accuracy: 0.9641 - loss: 0.1439
   wanna try to decrease the number of units towards the end

   def get_model(filter_repeats=2, dense_layers=6, unitcount=200, features=20):
   333/333 - 2s - 7ms/step - accuracy: 0.9650 - loss: 0.1754

   def get_model(filter_repeats=2, dense_layers=8, unitcount=200, features=20):
   333/333 - 3s - 8ms/step - accuracy: 0.9630 - loss: 0.1409

   def get_model(filter_repeats=2, dense_layers=5, unitcount=200, features=20):
   333/333 - 3s - 8ms/step - accuracy: 0.9489 - loss: 0.2576

   def get_model(filter_repeats=2, dense_layers=7, unitcount=200, features=20):
   333/333 - 2s - 6ms/step - accuracy: 0.9621 - loss: 0.1560

   def get_model(filter_repeats=2, dense_layers=10, unitcount=200, features=20):
   333/333 - 2s - 6ms/step - accuracy: 0.9533 - loss: 0.2248

   def get_model(filter_repeats=2, dense_layers=9, unitcount=200, features=20):
   333/333 - 2s - 6ms/step - accuracy: 0.9633 - loss: 0.1592


   so it seems that this is the best one
  def get_model(filter_repeats=2, dense_layers=6, unitcount=200, features=20):

  this seems to be the best i can do.
  2,4,300,35,0.1121153011918068,0.9727852940559387,260.3362979888916

  i did a lot of graphing on a small training set, i did a bunch of heat maps on the results and regressions
  just to see what works and what doesnt, i also used fewer epochs and based on that made decissions about a bigger model that would take a longer time to train. Feel like in the end the most optimized part of my neural network are the two layers of convolutional 2d -- this number of levels was consistent at producing best results. I am a lot less confident about number of dence layers, because more and fewer layers produce simmilar results. I also made a units number dependent on the number of layers, so it complicated things a little - i noticed that decreasing number of units towards the end had a positive effect on performance, so i decided to make it decrease steadily, hence the formula r = (8000 / 40000) ** (1/(dense_layers)), where each layer decreased by the same proportion. it is probably not an optimal way to do it and it also complicates the other components, but i had no intention to make model perfect. So i made a bunch of for loops that tried out different things and tried to find things that steadily decreased the losses, this was roughly the optima.

  convolutional layers 2d and max pooling repeats=2 , dense_layers=5, units in dence layers =300, features in convo2d=35):

  2,5,300,35 is probably best, decided to go with it
  333/333 - 6s - 17ms/step - accuracy: 0.9671 - loss: 0.1541
  ---
  i just realized that did not use dropouts to help with overfitting, but i already optimized for not overfitting, so i felt dissapointed and didnt want to add it. The neural networt does fine either way, about 0.97 on test data through the multiple trials, so i just went with it. I think i overcomplicated the model in general, but it works fine.

  this is its shape:
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ conv2d (Conv2D)                      │ (None, 28, 28, 35)          │             350 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ max_pooling2d (MaxPooling2D)         │ (None, 14, 14, 35)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ conv2d_1 (Conv2D)                    │ (None, 12, 12, 35)          │          11,060 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ max_pooling2d_1 (MaxPooling2D)       │ (None, 6, 6, 35)            │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ flatten (Flatten)                    │ (None, 1260)                │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense (Dense)                        │ (None, 300)                 │         378,300 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_1 (Dense)                      │ (None, 217)                 │          65,317 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_2 (Dense)                      │ (None, 157)                 │          34,226 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_3 (Dense)                      │ (None, 113)                 │          17,854 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_4 (Dense)                      │ (None, 81)                  │           9,234 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_5 (Dense)                      │ (None, 43)                  │           3,526 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
Dimensionality Reduction: Try smaller output sizes for intermediate layers, as too many parameters in dense layers may not generalize well.
Example: (300 → 128 → 43) instead of (300 → 217 → 157 → 113 → 81 → 43).

So i decided to give it a try even though my earlier trials with a big neural network and few dense layers failed, since the loss was decreasing with fewer returns.
this was my fast fix to keep the benefits from my earlier optimization struggles.
r = 2* (8000 / 40000) ** (1/(dense_layers))
dense_layers//2
maybe then i will even try to add something like a dropout?

immediatelly ive notised that the neural network was learning faster, yet it was related to overfitting,
and the generalizability was slightly lower than for my previous model.
333/333 - 4s - 12ms/step - accuracy: 0.9631 - loss: 0.2016

then its
- accuracy: 0.9236 - loss: 0.2721
333/333 - 5s - 15ms/step - accuracy: 0.9779 - loss: 0.0826 suggested


----------
with 0.3 dropout after each dense layer
333/333 - 3s - 10ms/step - accuracy: 0.9641 - loss: 0.1370


increasing the number of filters
333/333 - 3s - 10ms/step - accuracy: 0.9653 - loss: 0.1826

all are slightly higher than my original network.

this seems to be the stronger - dropout 0.4 after the filters
333/333 - 5s - 16ms/step - accuracy: 0.9749 - loss: 0.1072


oh no - just realized cs50 wants 3 color dimentions, but i selected 1 (ie made black and white)
that was my original design. now need to change it to 3 colors. actually if training to recognise road signs specifically, the neural network might be able learn stuff much faster, cus color is a fairly good indiactor.
