from random import randint

### ORIGINAL CODE

# dice_images = ["1️⃣","2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])

### Modified code to always generate the error
# dice_images = ["1️⃣","2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# # dice_num = randint(1, 6)
# dice_num = 6
# print(dice_images[dice_num])

### FIXED CODE
dice_images = ["1️⃣","2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_images[dice_num])