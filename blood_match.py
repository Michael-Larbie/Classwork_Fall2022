from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/mal126')
print(r.text)
donor = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/M6')
print(donor.text)
recipient = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6')
print(recipient.text)
print("M6 can give blood to F6")
post = {"Name": "mal126", "Match": "Yes"}
match = requests.post('http://vcm-7631.vm.duke.edu:5002/match_check',
                          json = post)
print(match.text)
