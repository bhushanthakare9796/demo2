import pickle
import json
import config
import numpy as np

class BostanHousing():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT
        
    def load_model(self):
         with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

         with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def get_predicted(self):
        self.load_model()
        array = np.zeros(len(self.json_data['columns']))
        array[0]=self.CRIM
        array[1]=self.ZN
        array[2]=self.INDUS
        array[3]=self.CHAS
        array[4]=self.NOX
        array[5]=self.RM
        array[6]=self.AGE
        array[7]=self.DIS
        array[8]=self.RAD
        array[9]=self.TAX
        array[10]=self.PTRATIO
        array[11]=self.B
        array[12]=self.LSTAT

        predicted_price  = self.model.predict([array])
        print("predicted_price of House in Bostan is :",predicted_price)
        return predicted_price