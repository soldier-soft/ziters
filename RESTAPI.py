from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = {
    'items': [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]
}

# Endpoint to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data['items']})

# Endpoint to get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item is not None:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# Endpoint to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item_name = request.json.get('name')
    new_item = {'id': len(data['items']) + 1, 'name': new_item_name}
    data['items'].append(new_item)
    return jsonify({'item': new_item}), 201

# Endpoint to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item is not None:
        item['name'] = request.json.get('name')
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# Endpoint to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item is not None:
        data['items'].remove(item)
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
