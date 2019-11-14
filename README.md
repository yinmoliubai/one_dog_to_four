# one_dog_to_four
一只狗变四只狗

通过对图片的切割与拼接，实现[一张狗狗照片切割后，竟变成了两只狗狗，随后又变成了四只](https://haokan.baidu.com/v?pd=wisenatural&vid=18424150096614689212)。


先导入库

    from functools import reduce
    import matplotlib.pyplot as ply
    %matplotlib inline

选一张狗狗图片

    im = ply.imread('dog.jpg')
    plt.imshow(im)
![dog.jpg](https://upload-images.jianshu.io/upload_images/14750449-7a41328898ab91a0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

选择将要处理的部位

    im2 = im[30:175,20:250]
    plt.imshow(im2)
![dog2.jpg](https://upload-images.jianshu.io/upload_images/14750449-3bb4ca3eff9803db.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

第一次纵向切割与拼接

    mim1 = []
    mim2 = []
    height = im2.shape[1]  // 44
    for i in range(0,44):
        if not i%2:
            mim1.append(im2[:,height*i:height*(i+1)])
        else:
            mim2.append(im2[:,height*i:height*(i+1)])


    def pinjie(x,y):
        hnp = np.hstack((x,y))
        return hnp
    plt.figure(figsize=(12,9))
    plt.subplot(2,1,1)
    im6 = reduce(pinjie,mim1)
    plt.imshow(im6)
    plt.subplot(2,1,2)
    im7 = reduce(pinjie,mim2)
    plt.imshow(im7)

    im8 = np.hstack((im6,im7))
    plt.imshow(im8)

![dog8.jpg](https://upload-images.jianshu.io/upload_images/14750449-a3ca049603a5db81.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

第二次横向切割与拼接


    lim1 = []
    lim2 = []
    weight = im8.shape[0] // 14
    for i in range(0,14):
        if not i%2:
            lim1.append(im8[weight*i:weight*(i+1),:])
        else:
            lim2.append(im8[weight*i:weight*(i+1),:])



    def pinjie(x,y):
        hnp = np.vstack((x,y))
        return hnp
    plt.figure()
    plt.subplot(2,1,1)
    im9 = reduce(pinjie,lim1)
    plt.imshow(im9)
    plt.subplot(2,1,2)
    im10 = reduce(pinjie,lim2)
    plt.imshow(im10)

最后拼接成一张图片

    im11 = np.hstack((im9,im10))
    plt.imshow(im11)

![dog11.jpg](https://upload-images.jianshu.io/upload_images/14750449-a933480715ece3fa.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
