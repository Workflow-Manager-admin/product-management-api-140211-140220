from app import app

if __name__ == "__main__":
    # PUBLIC_INTERFACE
    # Start Flask app on 0.0.0.0:3001 for correct container binding
    app.run(host="0.0.0.0", port=3001)
