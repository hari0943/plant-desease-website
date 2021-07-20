import matplotlib
import csv
import os

# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])
path ="C:\\Users\\overlord\\Documents\\Plant Datasets\\New folder\\archive\\New Plant Diseases Dataset(Augmented)\\New Plant Diseases Dataset(Augmented)\\train\\"

header = 'homogeneity energy dissimilarity correlation contrast '

header += ' label'
header = header.split()

file = open('data.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)
genres = ["Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy", "Blueberry___healthy","Cherry_(including_sour)___healthy","Cherry_(including_sour)___Powdery_mildew","Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot","Corn_(maize)___Common_rust_","Corn_(maize)___healthy","Corn_(maize)___Northern_Leaf_Blight","Grape___Black_rot","Grape___Esca_(Black_Measles)","Grape___healthy","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)","Orange___Haunglongbing_(Citrus_greening)","Peach___Bacterial_spot","Peach___healthy","Pepper,_bell___Bacterial_spot","Pepper,_bell___healthy","Potato___Early_blight","Potato___healthy","Potato___Late_blight","Raspberry___healthy","Soybean___healthy","Squash___Powdery_mildew","Strawberry___healthy","Strawberry___Leaf_scorch","Tomato___Bacterial_spot","Tomato___Early_blight","Tomato___healthy","Tomato___Late_blight","Tomato___Leaf_Mold","Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite","Tomato___Target_Spot","Tomato___Tomato_mosaic_virus","Tomato___Tomato_Yellow_Leaf_Curl_Virus"]
print("__________", genres)
for g in genres:
    print("++++++++++++++++", g)
    for filename in os.listdir(path + g):
        songname = path + g + "\\" + filename


        # md = "D:\\2020 2021\\AISKIN DJANGO MANNARKAD\\aiskinexpert\\media\\" + cp.name
        md = path +g+"\\"+ filename
        import numpy as np
        from skimage import io, color, img_as_ubyte

        from skimage.feature import greycomatrix, greycoprops

        from sklearn.metrics.cluster import entropy

        # rgbImg = io.imread("D:\\2020 2021\\AISKIN DJANGO MANNARKAD\\aiskinexpert\\media\\" + cp.name)
        try:
            rgbImg = io.imread(path + g + "\\" + filename)
            grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

            distances = [1, 2, 3]
            angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
            properties = ['energy', 'homogeneity']

            glcm = greycomatrix(grayImg,
                                distances=distances,
                                angles=angles,
                                symmetric=True,
                                normed=True)

            feats = np.hstack([greycoprops(glcm, 'homogeneity').ravel() for prop in properties])
            feats1 = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])
            feats2 = np.hstack([greycoprops(glcm, 'dissimilarity').ravel() for prop in properties])
            feats3 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
            feats4 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])

            k = np.mean(feats)
            l = np.mean(feats1)
            m = np.mean(feats2)
            n = np.mean(feats3)
            o = np.mean(feats4)

            # test=np.array([[k,l,m,n,o]])

            test = [[k, l, m, n, o]]

            # y, sr = librosa.load("1-977-A-39.wav", mono=True)
            # to_append = f'{filename} {np.mean(chroma_stft)}  {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
            to_append = [k, l, m, n, o, g]

            #
            file = open('data.csv', 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append)
            print(songname)
        except:
            print("errror")
