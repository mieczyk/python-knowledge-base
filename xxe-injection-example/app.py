from flask import Flask, request, jsonify, render_template
from lxml import etree


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/convert', methods=['POST'])
def convert():
    xml_data = bytes(request.form['xml'], encoding="utf8")

    try:
        # Create a custom parser that uses DTD for parsing and allows
        # network access for related files (e.g. external entities).
        parser = etree.XMLParser(load_dtd=True, no_network=False)

        # Parse an XML string received in the POST request using the custom parser.
        root = etree.fromstring(xml_data, parser)

        # Convert to JSON and render the HTML template.
        json_data = {root.tag: xml_to_dict(root)}

        return jsonify(json_data)
    except Exception as e:
        return jsonify({"error": str(e)})


def xml_to_dict(element: etree.Element):
    """
    Traverses the XML document and builds a dict object from it.
    """
    if len(element) == 0:  # element has no children
        return element.text

    result = {}

    for child in element:
        child_data = xml_to_dict(child)

        if child.tag not in result:
            result[child.tag] = child_data
        else:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]

    return result


if __name__ == "__main__":
    app.run(debug=True)
