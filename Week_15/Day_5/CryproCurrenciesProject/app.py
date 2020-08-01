from app import app, routes


@app.shell_context_processor
def shell_context():
    return {
        'routes': routes
    }


if __name__ == "__main__":
    app.run(debug=True)
