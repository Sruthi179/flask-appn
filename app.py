import pandas as pd
import numpy as np
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    s = np.array([1, 2, 3, 4, 5])
    df = pd.DataFrame(s)
    return df.to_html() 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080)) 
    app.run(host='0.0.0.0', port=port) 
