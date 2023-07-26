## LoProLife - Low Protein Life Management Web Application  
  
## Description  
LoProLife is a web application developed using Django framework, designed to assist parents and patients with Phenylketonuria (PKU) in managing and controlling their diet. The application enables users to track their phenylalanine consumption and other essential nutrients, automatically calculates daily intake, and provides insightful analytics and forecasting on the impact of various food products on phenylalanine levels.  
  
## Features  
* User Registration and Authentication: New users can sign up for an account, and existing users can log in securely to access their personalized profiles.  
  
* Product Tracking: Users can input the food products they consume daily, including their phenylalanine content, as well as other nutritional values.*  
  
* Daily Intake Calculation: LoProLife automatically calculates and displays the user's daily phenylalanine intake based on the tracked food products.  
  
* Anthropometric Data Management: Users can input and update their anthropometric data, such as height, weight, and age, to receive personalized diet recommendations.  
  
* Children Management: Parents or caregivers can manage multiple children or patients under one account, each with their own dietary tracking and analysis.  
  
* Analytics and Forecasting: The application provides insightful analytics, charts, and graphs to help users visualize their dietary patterns and phenylalanine consumption trends over time. It also offers forecasting on phenylalanine levels based on dietary changes.  
  
* Kid-Friendly Version: LoProLife offers a kid-friendly interface with food product recognition to make it engaging and easy for children with PKU to participate in tracking their diet.  
  
## Installation  
1. Clone the repository to your local machine using git clone **'https://github.com/your-username/LoProLife.git'**.  
2. Navigate to the project directory using **'cd LoProLife'**.  
3. Create a virtual environment using **'python -m venv venv'**.  
4. Activate the virtual environment:  
On Windows: **'venv\Scripts\activate'**
On macOS and Linux: **'source venv/bin/activate'**
5. Install the required packages using **'pip install -r requirements.txt'**.  
6. Run the database migrations using **'python manage.py migrate'**.****  
7. Create a superuser to access the admin interface using **'python manage.py createsuperuser'**.  
8. Start the development server using **'python manage.py runserver'**.
  
## Usage  
1. Access the application by visiting **'http://localhost:8000/'** in your web browser.  
2. Sign up for a new account or log in using your existing credentials.  
3. Start tracking your food product consumption by adding them to your daily intake.  
4. Optionally, input anthropometric data for personalized dietary analysis.  
5. View your daily phenylalanine intake, and utilize the analytics and forecasting tools for better diet management.  
6. Parents or caregivers can manage multiple children/patients by adding them to their accounts.  

## Technologies Used  
* Django (3.2.5)  
* Python (3.9.6)  
* HTML, CSS, JavaScript (Bootstrap framework for frontend)  

## License  
This project is licensed under the MIT License.  
  
## Acknowledgments  
Special thanks to the developers and contributors of Django and other open-source libraries that made this project possible.  
Please note that this is a fictional description of a hypothetical project. If you decide to create an actual project based on this description, you may need to add more details and modify it accordingly.