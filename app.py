import os   #To take api keys from .env
from google import genai
from dotenv import load_dotenv
from flask import Flask,request,jsonify

app=Flask(__name__)
client=genai.Client(api_key="AIzaSyDTKn9ud0q6AggUxvzdGPjR3pqE_ah6fx0")#Should not use api keys diretly like this so create dotenv and.env
load_dotenv()
api_key=os.getenv("API_KEY")
client=genai.Client(api_key=api_key)

@app.route("/home",methods=["GET"])
def home():
    return "Hello world!"
@app.route('/chat',methods=['POST'])
def chat():
    try:
        data=request.get_json() #Request library gets the jason we sent and store in data variable
        if 'prompt' not in data: #If no prompt parameter in the data we get then erro
            return jsonify(
                {"error":"Prompt not found in data"
                }),400
        prompt=data['prompt']
        response=client.models.generate_content(
             model="gemini-2.0-flash",
            contents=prompt
            )
        return jsonify({"ai_response":response.text}),200
    except Exception as e:
        return jsonify({
            "error":str(e)
        }),500
    
if(__name__)=='__main__': #For flask to understand this is flask app
    app.run(debug=True) #Debug by default will be false
#print(response.text) #Can have many contents like jason
