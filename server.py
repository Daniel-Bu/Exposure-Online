import warnings
from app import app

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        app.run(debug=False, host="0.0.0.0", port=8000)
