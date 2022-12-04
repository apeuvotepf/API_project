
# API Project

This project uses the IMDd API in order to create a dash web application.

This application can be used to get the rate of a movie.

## Libraries installation

In order to use this project, you may have to install some libraries.

Please run each of the following commands in your python environment : 

```bash
pip install dash
```
```bash
pip install dash_bootstrap_components
```
```bash
pip install numpy
```
```bash
pip install python-dotenv
```
```bash
pip install requests
```

## Run the application

In order to run the application, you first need to have a key to access the IMDb API. Just create an account : https://imdb-api.com/ and then create a `.env` file with the following line : `API_KEY="YOUR_API_KEY"`.
The `.gitignore` file specified that you don't want to push `.env` files to GitHub so that your key isn't public.

You are now ready to launch the app ! 

Just run :

```bash
python dash-app/launch_app.py
```
