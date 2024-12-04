# Ex.05 Design a Website for Server Side Processing
## Date:3.12.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lamp Power Calculator</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Quicksand', sans-serif;
            background: #ffec40;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .circle-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background: #fff;
            padding: 40px;
            border-radius: 50%;
            width: 500px;
            height: 500px;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
            text-align: center;
            position: relative;
        }
        h1 {
            font-family: 'Fredoka One', cursive;
            font-size: 2.5em;
            color: #ff6347;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        label {
            font-size: 1.5em;
            color: #ff6347;
            font-weight: bold;
            margin-bottom: 10px;
            display: block;
        }
        input[type="number"] {
            width: 80%;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            border: 2px solid #ff6347;
            background-color: #fff3cd;
            font-size: 1.2em;
            color: #333;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
        }
        button {
            width: 80%;
            padding: 15px;
            background-color: #ff6347;
            border: none;
            border-radius: 15px;
            color: white;
            font-size: 1.5em;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #ff4500;
            transform: scale(1.1);
        }
        .result {
            margin-top: 20px;
            padding: 20px;
            background-color: #ffec40;
            border-radius: 10px;
            font-size: 1.6em;
            color: #ff6347;
            font-weight: bold;
            display: none;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
        }
        .highlight {
            color: #ff4500;
            font-weight: bold;
        }
        .footer {
            margin-top: 20px;
            font-size: 1.2em;
            color: #ff6347;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>

    <div class="circle-container">
        <div>
            <h1>Lamp Power Calculator</h1>
            <form id="powerForm">
                <label for="intensity">Intensity (I) in Amperes:</label>
                <input type="number" id="intensity" required step="any" placeholder="Enter intensity">
                
                <label for="resistance">Resistance (R) in Ohms:</label>
                <input type="number" id="resistance" required step="any" placeholder="Enter resistance">
                
                <button type="button" onclick="calculatePower()">Calculate Power</button>
            </form>

            <div id="result" class="result">
                Power (P): <span id="power" class="highlight"></span> Watts
            </div>
        </div>

        <div class="footer">
            <p>G.T. Gowtham | Ref. No: 24901330</p>
        </div>
    </div>

    <script>
        function calculatePower() {
            var intensity = parseFloat(document.getElementById('intensity').value);
            var resistance = parseFloat(document.getElementById('resistance').value);
            
            if (!isNaN(intensity) && !isNaN(resistance)) {
                var power = Math.pow(intensity, 2) * resistance;
                document.getElementById('power').innerText = power.toFixed(2);
                document.getElementById('result').style.display = 'block';
            } else {
                alert("Please enter valid numbers for intensity and resistance.");
            }
        }
    </script>

</body>
</html>


urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lamp_power_calculator, name='lamp_power_calculator'),
    path('calculate/', views.calculate_power, name='calculate_power'),
]


views.py
from django.shortcuts import render
from django.http import JsonResponse

def lamp_power_calculator(request):
    """Renders the Lamp Power Calculator page."""
    return render(request, 'lamp_power_calculator.html')

def calculate_power(request):
    """Handles the power calculation request."""
    if request.method == 'GET':
        intensity = float(request.GET.get('intensity', 0))
        resistance = float(request.GET.get('resistance', 0))
        power = intensity**2 * resistance
        return JsonResponse({'power': round(power, 2)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


```
## SERVER SIDE PROCESSING:
![alt text](<VS CODE FOR FINAL EX 5.png>)

## HOMEPAGE:
![alt text](<THIS IS OK.png>)

## RESULT:
The program for performing server side processing is completed successfully.