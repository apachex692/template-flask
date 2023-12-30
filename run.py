# Author: Sakthi Santhosh
# Created on: 30/12/2023
def main():
    from app import create_app

    app_handler = create_app()

    app_handler.run(host="127.0.0.1", debug=True, port=5000, threaded=True)


if __name__ == "__main__":
    main()
