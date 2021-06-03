import os
import urllib.parse as urlparse
from urllib.parse import parse_qs
from werkzeug.utils  import secure_filename
from flask import Flask,request,redirect,send_file,render_template

# Create and configure the app
app = Flask(__name__, template_folder='TemplateStudent')

#Search API
@app.route('/',methods=['GET'])
def search():
        if(request.method == 'GET'):
            # classParam = request.args.get('class')
            # idParam = request.args.get('id')
            # nameParam = request.args.get('name')
            # ageParam = request.args.get('age')
            # print(classParam,idParam,nameParam,ageParam)
            # if (classParam or idParam or nameParam or ageParam == 'none'):
            #     return render_template('studentSearch.html',idPa = idParam , namePa = nameParam , agePa = ageParam , classPa = classParam)        
            return render_template('student.html')

# If debug is disabled, the development server on local computer can be made available to the users on network by setting the host name as ...0.0.0.0....
if __name__ == "__main__":
    app.run(host='0.0.0.0')