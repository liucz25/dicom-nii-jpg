from model import *
from data import *
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print(time.asctime(time.localtime(time.time())))

data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(2,'data/membrane/trainlcz','image','label',data_gen_args,save_to_dir = None)

model = unet()

model_checkpoint = ModelCheckpoint('unet_membranelcz.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=1200,epochs=1,callbacks=[model_checkpoint])
testGene = testGenerator("data/membrane/testlcz")
results = model.predict_generator(testGene,30,verbose=1)
saveResult("data/membrane/testlcz",results)
print(time.asctime(time.localtime(time.time())))