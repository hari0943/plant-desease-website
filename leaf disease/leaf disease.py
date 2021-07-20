from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask.globals import session
from werkzeug.utils import secure_filename
import demjson
from skimage import img_as_ubyte,color,io

from dbconnection import Db

app = Flask(__name__)
app.secret_key="leaf"
path1="C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\static\\images\\"
staticpath="C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\static\\"
fertilizerpath="C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\static\\fertilizer\\"
scanned_path = "C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\static\\scanned_img\\"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login',methods=['post'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    db = Db()
    res = db.selectOne("SELECT * FROM `login` WHERE `user_name`='"+username+"' AND `password`='"+password+"'")
    if res!=None:
        lid = res['login_id']
        type = res['type']
        session['lid'] = lid
        if type =="admin":
            return redirect(url_for('admin_home'))
        elif type=="subadmin":
            return redirect(url_for('subadmin_home'))
        elif type=="officer":
            return redirect(url_for('officer_home1'))
    else:
        return '<script>alert("invalid username or password")</script>'



@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')


@app.route('/add_subadmin')
def add_subadmin():
    return render_template('subadmin.html')

@app.route('/add_subadmin_add',methods=['post'])
def add_subadmin_add():
    name = request.form['textfield']
    dob = request.form['dob']
    email = request.form['textfield3']
    password = request.form['password']
    phone = request.form['textfield4']
    db = Db()
    db1 = Db()
    lid = db.insert("INSERT INTO `login`(`user_name`,`password`,`type`)VALUES('"+email+"','"+password+"','subadmin')")
    res = db1.insert("INSERT INTO `sub_admin`(`name`,`dob`,`email`,`phone`,`login_id`)VALUES('"+name+"','"+dob+"','"+email+"','"+phone+"','"+str(lid)+"')")
    if res>0:
        return '<script>alert("Added....");window.location="/admin_home";</script>'





@app.route('/view_leafdisease')
def view_leafdisease():
    db = Db()
    res=db.select("SELECT * FROM `leaf`")
    return render_template('admin_leaf.html',data=res)


    return render_template('admin_leaf.html')


@app.route('/view_noti')
def view_noti():
    db = Db()
    res=db.select("SELECT * FROM `notification`")
    return render_template('view_notification.html', data=res)


@app.route('/add_notification')
def add_notification():

    return render_template('admin_noti.html')

@app.route('/add_notification_add',methods=['post'])
def add_notification_add():
    subject=request.form['textfield']
    content=request.form['textfield2']
    db=Db()
    qry="INSERT INTO `notification`(`subject`,`content`,`date`)VALUES('"+subject+"','"+content+"',curdate())"
    print(qry)
    lid=db.insert(qry)
    if lid>0:
        return '<script>alert("Added....");window.location="/add_notification";</script>'


@app.route('/add_farmer')
def add_farmer():
    return render_template('admin_farmer.html')


@app.route('/view_farmer')
def view_farmer():
    db=Db()
    res=db.select("SELECT * FROM `farmer`")
    return render_template('admin_farmer.html', data=res)


@app.route('/admin_view_fertilizer')
def admin_view_fertilizer():
    db = Db()
    res=db.select("SELECT * FROM `fertilizer`")
    return render_template('admin_fertilaizer.html', data=res)



@app.route('/view_fertilizer')
def view_fertilizer():
    db = Db()
    res=db.select("SELECT * FROM `fertilizer`")
    return render_template('sub_viewferti.html', data=res)



@app.route('/view_feedback')
def view_feedback():
    db = Db()
    res=db.select("SELECT `feedback`.*,`farmer`.`name`,email,phone FROM `farmer`,`feedback` WHERE `feedback`.`farmer_id`=`farmer`.`login_id`")
    return render_template('admin__feadback.html', data=res)
   

@app.route('/password')
def password():
    db = Db()
    return render_template('admin_passward.html')


@app.route('/change_password',methods=['post'])
def change_password():
    c_password = request.form['cp']
    n_password = request.form['np']
    c_n_password = request.form['cnp']
    lid = session['lid']
    db = Db()
    db1 = Db()
    res = db.selectOne("SELECT * FROM `login` WHERE `password`='"+c_password+"' AND `login_id`='"+str(lid)+"'")
    if res!=None:
        if c_n_password==n_password:
            db1.update("UPDATE `login` SET `password`='"+n_password+"' WHERE `login_id`='"+str(lid)+"'")
            return '<script>alert("Updated...please login to continue........");window.location="/";</script>'
        else:
           return '<script>alert("Password mismatch....");window.location="/password";</script>'
    else:
        return '<script>alert("Wrong Current Password....");window.location="/password";</script>'

@app.route('/add_agriofficer')
def add_agriofficer():
    return render_template('add_agr_officer.html')

@app.route('/add_agrioffice_add',methods=['post'])
def add_agrioffice_add():
    name = request.form['textfield']
    dob = request.form['textfield2']
    place = request.form['textfield3']
    pin = request.form['textfield4']
    qualification = request.form['textfield5']
    experience= request.form['textfield6']
    mail = request.form['textfield7']
    phone = request.form['textfield8']
    image = request.files['fileField']
    image.save("C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\static\\officer\\"+image.filename)
    import random
    password=str(random.randint(0000,9999))
    path='/static/officer/'+image.filename
    db = Db()
    db1 = Db()
    lid = db.insert("INSERT INTO `login`(`user_name`,`password`,`type`)VALUES('"+mail+"','"+password+"','officer')")
    db1.insert("INSERT INTO `agriculture`(`name`,`dob`,`email`,`phone`,`login_id`,qualification,experience,`place`,`pin`,`image`)VALUES('"+name+"','"+dob+"','"+mail+"','"+phone+"','"+str(lid)+"','"+qualification+"','"+experience+"','"+place+"','"+pin+"','"+path+"')")

    return '<script>alert("Added....");window.location="/admin_home";</script>'

@app.route('/view_officer')
def view_officer():
    db=Db()
    res=db.select("SELECT * FROM `agriculture`")
    return render_template('admin_view officer.html', data=res)

@app.route('/view_officer_post',methods=['POST'])
def view_officer_post():
    s=request.form["s"]
    db=Db()
    res=db.select("SELECT * FROM `agriculture` where name like '%"+s+"%'")
    return render_template('admin_view officer.html', data=res)


@app.route('/ajax_view_officer/<id>')
def ajax_view_officer(id):
    db=Db()
    res=db.select("SELECT * FROM `agriculture` WHERE `name` LIKE '%"+id+"%'")
    if len(res)>0:
        return render_template('ajax_viewofficer.html', data=res)
    else:
        return 'no data'

@app.route('/remove_officer/<id>')
def remove_officer(id):
    db=Db()
    db1 = Db()
    print(id)
    res=db.delete("DELETE FROM `agriculture` WHERE `login_id`='"+id+"'")
    db1.delete("DELETE FROM `login` WHERE `login_id`='"+id+"'")
    return '<script>alert("Deleted....");window.location="/view_officer";</script>'

@app.route('/update_officer')
def update_officer():
    return render_template('admin_updateoffi.html')

@app.route('/update_sub')
def update_sub():
    return render_template('admin_update sub.html')

@app.route('/add_sub')
def add_sub():
    return render_template('admin_add sub.html')

@app.route('/view_sub')
def view_sub():
    db=Db()
    res=db.select("SELECT * FROM `sub_admin`")
    return render_template('admin_viewsub.html', data=res)

@app.route('/ajax_view_sub/<id>')
def ajax_view_sub(id):
    db=Db()
    res=db.select("SELECT * FROM `sub_admin` WHERE `name` LIKE '%"+id+"%'")
    return render_template('ajax_sub_admin.html', data=res)

@app.route('/remove_sub/<id>')
def remove_sub(id):
    db=Db()
    db1 = Db()
    res=db.delete("DELETE FROM `sub_admin` WHERE `subadmin_id`='"+str(id)+"'")

    return '<script>alert("Deleted....");window.location="/admin_home";</script>'




#####################subadmin  ###################################

@app.route('/subadmin_home')
def subadmin_home():
    return render_template('sub_adminhome.html')



@app.route('/sub_view_profile')
def sub_view_profile():
    lid=session["lid"]
    db = Db()
    res = db.selectOne("SELECT * FROM `sub_admin` where login_id='"+str(lid)+"'")
    return render_template('sub_view profile.html',data=res)





@app.route('/sub_fertilizer')
def sub_fertilizer():
    # print("hhh")
    # lid=session["lid"]
    db = Db()
    res = db.select("SELECT * FROM `fertilizer` ")
    return render_template('sub_viewferti.html',data=res)


@app.route('/ajax_sub_ferti/<id>')
def ajax_sub_ferti (id):
    db=Db()
    res=db.select("SELECT * FROM `agriculture` WHERE `name` LIKE '%"+id+"%'")
    if len(res)>0:
        return render_template('ajax_sub_ferti.html', data=res)

@app.route('/remove_ferti/<id>')
def remove_ferti(id):
    db = Db()
    print(id)
    res = db.delete("DELETE FROM `fertilizer` WHERE `fertilizer_id`='" + str(id) + "'")
    return '<script>alert("Deleted....");window.location="/subadmin";</script>'


@app.route('/add_leaf')
def add_leaf():
    return render_template('sub_leaf disease.html')


@app.route('/add_leaf_vaue',methods=['post'])
def add_leaf_vaue():
    name=request.form['textfield']
    photo=request.files['imageField']
    discriptiont=request.form['textfield3']
    disease=request.form['textfield4']
    photo.save(path1+photo.filename)
    path="/static/images/"+photo.filename
    db=Db()
    qry="INSERT INTO `leaf`(`name`,`phtoto`,`discreption`,`disease`)VALUES('"+name+"','"+path+"','"+discriptiont+"','"+disease+"')"
    print(qry)
    db.insert(qry)

    return '<script>alert("Added....");window.location="/subadmin";</script>'

@app.route('/subadmin')
def subadmin():
    return render_template('sub_adminhome.html')


@app.route('/view_leaf')
def view_leaf():
    db = Db()
    res=db.select("SELECT * FROM `leaf`")
    return render_template('sub_viewleaf.html', data=res)

@app.route('/view_leafpost',methods=['POST'])
def view_leafpost():
    s=request.form["s"]
    db = Db()
    res=db.select("SELECT * FROM `leaf` where name like '%"+s+"%'")
    return render_template('sub_viewleaf.html', data=res)    

@app.route('/deleteleaf/<lid>')
def deleteleaf(lid):
    db = Db()


    qry="DELETE FROM `leaf` WHERE `leaf_id`='"+lid+"'"
    print(qry)
    db.delete(qry)

    return '<script>alert("Leaf deleted....");window.location="/view_leaf";</script>'

    


@app.route('/fertilizer')
def fertilizer():
    db = Db()
    res=db.select("SELECT * FROM `fertilizer`")
    return render_template('sub_viewferti.html', data=res)


@app.route('/ajax_view_ferti/<id>')
def ajax_view_ferti(id):
    db=Db()
    res=db.select("SELECT * FROM `fertilizer` WHERE `name` LIKE '%"+id+"%'")
    return render_template('ajax_sub_ferti.html', data=res)

@app.route('/add_fertilizer')
def add_fertilizer():
    return render_template("sub_fertilizer.html")

@app.route('/add_fertilizer_post',methods=['post'])
def add_fertilizer_post():
    name=request.form['textfield']
    pic=request.files['oo']
    discreption=request.form['textfield3']
    pic.save(fertilizerpath+pic.filename)
    path="/static/fertilizer/"+pic.filename
    db=Db()
    qry="INSERT INTO `fertilizer`(`name`,`pic`,`descrription`)VALUES('"+name+"','"+path+"','"+discreption+"')"
    print(qry)
    lid=db.insert(qry)
    if lid>0:
        return '<script>alert("Added....");window.location="/subadmin";</script>'
    return render_template('sub_fertilizer.html')

@app.route('/add_tips')
def add_tips():
    return render_template("sub_add tips.html")

@app.route('/add_tipsadd', methods=['post'])
def add_tipsadd():
    subject = request.form['textfield']
    content= request.form['textfield2']
    db = Db()
    qry = "INSERT INTO `tips`(`subject`,`content`)VALUES('" + subject+ "','" + content+ "')"
    print(qry)
    db.insert(qry)
    return '<script>alert("Added....");window.location="/subadmin";</script>'


@app.route('/view_tips')
def view_tips():
    db = Db()
    res = db.select("SELECT * FROM `tips`")
    return render_template('sub_viewtips.html', data=res)

    return render_template('sub_viewtips.html')

@app.route('/remove_tips/<id>')
def remove_tips(id):
    db=Db()
    print(id)
    res=db.delete("DELETE FROM `tips` WHERE `tips_id`='"+str(id)+"'")
    return '<script>alert("Deleted....");window.location="/view_tips";</script>'


@app.route('/complaint')
def complaint():
    db = Db()
    res = db.select("SELECT `complaints`.*,`farmer`.`name`,email,phone FROM `farmer`,`complaints` WHERE `complaints`.`farmer_id`=`farmer`.`login_id`")
    return render_template('sub_complaints.html', data=res)

@app.route('/complaint_post_subadmin',methods=['post'])
def complaint_post_subadmin():
    froms=request.form["from"]
    to=request.form["to"]
    db = Db()
    res = db.select("SELECT `complaints`.*,`farmer`.`name`,email,phone FROM `farmer`,`complaints` WHERE `complaints`.`farmer_id`=`farmer`.`login_id` and date between '"+froms+"' and '"+to+"'")
    return render_template('sub_complaints.html', data=res)

@app.route('/reply/<id>')
def reply(id):
    db = Db()
    res = db.select("SELECT * FROM `complaints` WHERE `complaints_id`='"+id+"'")
    return render_template('agri_addreply.html', cid=id)

@app.route('/reply_add',methods=['post'])
def reply_add():
    db = Db()
    cid=request.form['cid']
    reply=request.form['textfield']
    db.update("UPDATE `complaints` SET `replay`='"+reply+"' WHERE`complaints_id`='"+cid+"'")
    return redirect("/complaint")


@app.route('/log_out')
def log_out():
    return render_template('login.html')


#####################officer  ###################################


@app.route('/officer_home1')
def officer_home1():
    return render_template('agriofficer_homepage.html')

@app.route('/offview_profile')
def offview_profile():
    db = Db()
    lid=session["lid"]
    print(lid)
    res = db.selectOne("SELECT * FROM `agriculture` WHERE login_id='"+str(session["lid"])+"'")
    print(res)
    return render_template('agriofficer_viewprofile.html', data=res)

    #return render_template('agriofficer_viewprofile.html')


@app.route('/view_doubts')
def view_doubts():
    db = Db()
    res = db.select("SELECT `doubts`.*,`farmer`.`name` FROM `farmer`,`doubts` WHERE `doubts`.`farmer_id`=`farmer`.`login_id`")
    return render_template('agriculture_doubts.html', data=res)
     #return render_template('agriculture_doubts.html')



@app.route('/add_reply/<id>')
def add_reply(id):
    return render_template('offereplay.html',did=id)


@app.route('/reply_add_o',methods=['post'])
def reply_add_o():
    db = Db()
    cid=request.form['cid']
    reply=request.form['textfield']
    db.update("UPDATE `doubts` SET `replay`='"+reply+"' WHERE`doubts_id`='"+cid+"'")
    return redirect("/view_doubts")

##################pablic##########################################

@app.route('/view_notification')
def view_notification ():
    db = Db()
    res=db.select("SELECT * FROM `notification`")
    return render_template('pablic_noti.html', data=res)
    
@app.route('/delnoti/<id>')
def delnoti(id):
    db=Db()
    db1 = Db()
    res=db.delete("DELETE FROM notification WHERE `noti_id`='"+str(id)+"'")

    return '<script>alert("Deleted....");window.location="/view_noti";</script>'


@app.route('/view_pabdisease')
def view_pabdisease():
    db = Db()
    res=db.select("SELECT * FROM `leaf`")
    return render_template('pablic_disease.html', data=res)


@app.route('/view_pabfertilizer')
def view_pabfertilizer():
    db = Db()
    res=db.select("SELECT * FROM `fertilizer`")
    return render_template('pablic_fertilizer.html', data=res)

@app.route('/pablic_home')
def pablic_home():
    return render_template('public_home.html')


##################farmer##########################################
@app.route('/and_reg',methods=['POST'])
def and_reg():
    r ={}
    name=request.form['name']
    dob=request.form['dob']
    gender=request.form['gender']
    place=request.form['place']
    pin=request.form['pin']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']
    db=Db()
    db1=Db()
    lid=db.insert("INSERT INTO `login`(`user_name`,`password`,`type`)VALUES('"+email+"','"+password+"','farmer')")
    res=db1.insert("INSERT INTO `farmer`(`name`,`dob`,`gender`,`place`,`pin`,`email`,`phone`,`login_id`)VALUES('"+name+"','"+dob+"','"+gender+"','"+place+"','"+pin+"','"+email+"','"+phone+"','"+str(lid)+"')")
    
    if res>0:
        r['status'] = "1"
    else:
        r['status'] = "0"
    return demjson.encode(r)


@app.route('/and_login',methods=['POST'])
def and_login():
    r ={}
    username=request.form['username']
    password=request.form['password']
    db=Db()
    res=db.selectOne("SELECT * FROM `login` WHERE `user_name`='"+username+"' AND `password`='"+password+"'")
    if res!=None:
        r['status'] = "1"
        r['lid'] = res['login_id']
    else:
        r['status'] = "0"
    return demjson.encode(r)



@app.route('/and_viewprofile',methods=['POST'])
def and_viewprofile():
    r ={}
    db = Db()
    lid=request.form['lid']

    res = db.selectOne("SELECT * FROM `farmer` WHERE login_id='"+lid+"'")
    if res!=None:
        r['status'] = "1"
        r['name'] = res['name']
        r['dob'] = res['dob']
        r['gender'] = res['gender']
        r['place'] = res['place']
        r['pin'] = res['pin']
        r['email'] = res['email']
        r['phone'] = res['phone']
    else:
        r['status'] = "0"
    return demjson.encode(r)

@app.route('/and_view_leafdisease',methods=['POST'])
def and_view_leafdisease():
    r ={}
    db = Db()

    res = db.select("SELECT *FROM `leaf`")
    if len(res)>0:
        r['status'] = "1"
        r['data'] = res

    else:
        r['status'] = "0"
    return demjson.encode(r)


@app.route('/and_view_notification', methods=['POST'])
def and_view_notification():
    r = {}
    db = Db()

    res = db.select("SELECT *FROM `notification`")
    if len(res) > 0:
        r['status'] = "1"
        r['data'] = res

    else:
        r['status'] = "0"
    return demjson.encode(r)

@app.route('/and_view_fertilizer', methods=['POST'])
def and_view_fertilizer():
    r = {}
    db = Db()

    res = db.select("SELECT *FROM `fertilizer`")
    if len(res) > 0:
        r['status'] = "1"
        r['data'] = res

    else:
        r['status'] = "0"
    return demjson.encode(r)

@app.route('/and_view_tips', methods=['POST'])
def and_view_tips():
    r = {}
    db = Db()

    res = db.select("SELECT *FROM `tips`")
    print(res)
    if len(res) > 0:
        r['status'] = "ok"

        r['result'] = res

    else:
        r['status'] = "no"
    return demjson.encode(r)

@app.route('/and_compliant',methods=['POST'])
def and_compliant():
    r ={}
    com=request.form['complaint']
    fid = request.form['lid']

    db=Db()
    db1=Db()
    res=db.insert("INSERT INTO `complaints`(`farmer_id`,`date`,`replay`,`complaints`)VALUES('"+fid+"',curdate(),'pending','"+com+"')")
    if res>0:
        r['status'] = "1"
    else:
        r['status'] = "0"
    return demjson.encode(r)


@app.route('/and_view_reply',methods=['POST'])
def and_view_reply():
    r ={}
    db = Db()
    lid=request.form['lid']

    res = db.select("SELECT * FROM `complaints` WHERE `farmer_id`='"+lid+"'")
    if len(res)>0:
        r['status'] = "1"
        r['data'] = res

    else:
        r['status'] = "0"
    return demjson.encode(r)


@app.route('/and_senddoubts',methods=['POST'])
def and_senddoubts():
    r ={}
    doubts=request.form['doubts']
    fid = request.form['lid']


    db=Db()
    db1=Db()
    res=db.insert("INSERT INTO doubts(`farmer_id`,`date`,`replay`,`doubts`)VALUES('"+fid+"',curdate(),'pending','"+doubts+"')")
    if res>0:
        r['status'] = "1"
    else:
        r['status'] = "0"
    return demjson.encode(r)

@app.route('/and_sendfeedback',methods=['POST'])
def and_sendfeedback():
    r ={}
    feedback=request.form['feedback']
    fid = request.form['lid']


    db=Db()
    res=db.insert("INSERT INTO `feedback`(`farmer_id`,`date`,`feedback`)VALUES('"+fid+"',curdate(),'"+feedback+"')")
    if res>0:
        r['status'] = "1"
    else:
        r['status'] = "0"
    return demjson.encode(r)

@app.route('/and_view_doubt_reply',methods=['POST'])
def and_view_doubt_reply():
    r ={}
    db = Db()
    lid=request.form['lid']

    res = db.select("SELECT * FROM `doubts` WHERE `farmer_id`='"+lid+"'")
    if len(res)>0:
        r['status'] = "1"
        r['data'] = res

    else:
        r['status'] = "0"
    return demjson.encode(r)



def lks(p):
    import tensorflow as tf
    import sys
    import os

    # Disable tensorflow compilation warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    #import tensorflow as tf
    import tensorflow.compat.v1 as tf
    # image_path = sys.argv[1]
    # image_path="C:\\Users\\ELCOT-Lenovo\\Documents\\images\\sign_dataset\\test\\A\\color_0_0016"
    # Read the image_data
    image_data = tf.gfile.FastGFile(p, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\logs\\output_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("C:\\Users\\overlord\\Desktop\\Backup\\leaf disease\\logs\\output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            return human_string


@app.route('/and_detect',methods=['post'])
def android_scanner():

    photo = request.files['file']
    db = Db()
    # lid = request.form['lid']
    # filename = 'scanned' + lid + '.jpg'
    filename = photo.filename
    r={}
    if photo is not None:
        fn = photo.filename
        if fn != '':
            photo.save(scanned_path + filename)
            lks(scanned_path+filename)

            ####predcition

            import numpy as np
        #     from skimage import io, color, img_as_ubyte
        #
            from skimage.feature import greycomatrix, greycoprops
            from sklearn.metrics.cluster import entropy

            rgbImg = io.imread(scanned_path + filename)
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

            test = [[k, l, m, n, o]]
        #
        #
            attribut = []
            lables = []

            import  pandas as pd
        #
            balance_data = pd.read_csv(r'C:\Users\overlord\Desktop\Backup\leaf disease\data.csv', sep=',', header=None)
            X = balance_data.values[1:, :5]
            Y = balance_data.values[1:, 5]
        #
        #
            from sklearn.ensemble import RandomForestClassifier
            rnd = RandomForestClassifier()
            rnd.fit(X, Y)
        #
            k = rnd.predict(np.array(test))

            print(k,"Final result")
            # l=int(k[0])
            #8
            # l=l+1

            db=Db()
            res=db.selectOne("SELECT * FROM `leaf` WHERE `disease`='"+k[0]+"'")
            print(res)
            if res is not None:
                r['status']='1'
                r['name']=res['name']
                r['photo']=res['phtoto']
                r['descr']=res['discreption']
                r['dis']=res['disease']

                # return jsonify(status='1',name=res['name'], photo=res['phtoto'],descr=res['discreption'], dis=res['disease'])
            else:   
                r['status']='0'
    else:
        r['status']='0'

    print(r)
    return demjson.encode(r)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
