import pandas as pandas
import numpy as numpy
import sklearn
import joblid
from flask import flas, render_template, request app=Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediccion', methods=['GET','POST'])
def predict();
   if request.method =='POST':
       try:
           var_1=float(request.from['var_1'])
           var_2=float(reguest.from['var_2'])

           pred_args=[var_1,var_2]
           pred_arr=np.array(pred_args)
           prends=pred_arr.reshape(1,-1)
           modelo=open("./modelo.pkl","rb")
           modelo-clas=joblid.load(modelo)
           prediccion_modelo=modelo_clas.predict(prends)
           prediccion_modelo=round(float(prediccion_modelo), 2)
           if prediccion_momdelo == 1.0:
               prediccion_modelo = "Apeueba"
            else:
                prediccion_modelo = "No aprueba"
            except ValueError:
                return "Por favor entra nombre validos"
            return render_template('prediccion.html' ,prediccion=prediccion_modelo)
            if _name_=='_main_':
                app.run(debug=True)
                