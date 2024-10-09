from PIL import Image, ImageEnhance, ImageFilter

with Image.open('./Images/Bird.jfif') as picture:
    picture.show()
    black_white=picture.convert('L')
    # black_white.show()
    black_white.save('./Images/Bird_bw.png')

    mirror =picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save('./Images/Bird_mirror.png')
    blur=picture.filter(ImageFilter.GaussianBlur(20))
    blur.save('./Images/Bird_blur.png')

    contrast=ImageEnhance.Contrast(picture)
    contrast.enhance(2).save('./Images/Bird_contrast.png')

    color=ImageEnhance.Color(picture).enhance(2).save('./Images/Bird_color.png')
    picture.save('./Images/Bird.png')
    # picture.save('./Images/Bird.jpg')
    # picture.save('./Images/Bird.bmp')
    # picture.save('./Images/Bird.tiff')
    # picture.save('./Images/Bird.webp')
    # picture.save('./Images/Bird.ico')
    # picture.save('./Images/Bird.gif')
    # picture.save('./Images/Bird.pdf')