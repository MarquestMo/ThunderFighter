import PIL.Image as Image

imgs = []
for i in range(0,510,11):
    pic_name = str(i)+'.jpg'
    temp = Image.open(pic_name)
    imgs.append(temp)
save_name = 'ALLgif.gif'
imgs[0].save(save_name, save_all=True, append_images=imgs, duration=0)
