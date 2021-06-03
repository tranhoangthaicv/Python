import os
import urllib.parse as urlparse
from urllib.parse import parse_qs
from werkzeug.utils  import secure_filename
from flask import Flask,request,redirect,send_file,render_template

# Variable save the path to upload
UPLOAD_FOLDER = 'uploads/'

# Create and configure the app
app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Upload API
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            print(request.parameter_storage_class)
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads/', filename))
            print("saved file successfully")
        #send file name as parameter to downlad
            return redirect('/downloadfile/'+ filename)
    else:
        param = request.args.get('username')
        print(param)
        return render_template('upload_file.html',value=param)

# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download_file.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
     file_path = UPLOAD_FOLDER + filename
     return send_file(file_path, as_attachment=True, attachment_filename='')

# If debug is disabled, the development server on local computer can be made available to the users on network by setting the host name as ...0.0.0.0....
if __name__ == "__main__":
    app.run(host='0.0.0.0')
