from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

def linear_interpolation(points, length):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    
    interpolated_x = np.linspace(min(x), max(x), length)
    interpolated_y = np.interp(interpolated_x, x, y)
    
    return list(zip(interpolated_x, interpolated_y))

def calculate_rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted) ** 2))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interpolate', methods=['POST'])
def interpolate_points():
    points = request.form.getlist('points[]')
    target_length = int(request.form['target_length'])
    
    points = [tuple(map(float, point.split(','))) for point in points]
    
    interpolated_points = linear_interpolation(points, target_length)
    
    # Calculate RMSE
    actual_y = np.array([p[1] for p in points])
    interpolated_y = np.array([p[1] for p in interpolated_points])
    
    # Ensure that interpolated_y has the same length as actual_y
    interpolated_y = interpolated_y[:len(actual_y)]
    
    rmse = calculate_rmse(actual_y, interpolated_y)
    
    return render_template('result.html', interpolated_points=interpolated_points, rmse=rmse)


if __name__ == '__main__':
    app.run(debug=True)
