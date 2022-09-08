import csv


def main():
    with open('authorsbig.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name'])
        for i in range(100):
            writer.writerow({'name': f'Author {i}'})


if __name__ == '__main__':
    main()
