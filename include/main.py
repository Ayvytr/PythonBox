from include.window import MainWindow


def main():
    try:
        MainWindow().show()
    except Exception as exception:
        print(exception)


if __name__ == '__main__':
    main()
