# shopping-cart
Shopping Cart Project for OPIM 243

## Let's get rolling

Fork this repo! Then, clone or download to your github desktop.

Then, navigate to the command line (or GitBash, etc) and activate a new virtual environment with conda. After you have done this, make sure that you
```sh
pip install requirements.txt
```

## Load the .env

Make sure that the .env has environment variables adjusted so the program works properly. You should adjust the tax rate and email address if you wish (do not tinker with sendgrid API key):
```sh
TAX_RATE = ".0875" # or change if you want
MY_EMAIL_ADDRESS = "tsp16@georgetown.edu" # here is my email for testing!
```

## Run it!

Try to run the script (after having the virtual environment made + activated, requirements.txt "pipped," adjusting the .env, and navigating to the repo in your directory!)
```sh
python shopping_cart.py
```

## Extra challenges that were completed

In this project, I chose to do the extra challenges that follow:

Setting the tax rate as an environment variable

Adjusting items to being priced per item or "priced-per" (like bananas)

Sending an optional email receipt

