from flask import Flask, request, jsonify, render_template
from lxml import etree

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    xml_data = request.form['xml']
    try:
        # set parser to allow loading external entities
        parser = etree.XMLParser(load_dtd=True, no_network=True)
        root = etree.fromstring(xml_data, parser)
        json_data = etree_to_dict(root)
        return jsonify(json_data)
    except Exception as e:
        return jsonify({"error": str(e)})

def etree_to_dict(t):
    return {t.tag: [etree_to_dict(child) for child in t.iterchildren()] or t.text}

if __name__ == "__main__":
    app.run(debug=True)