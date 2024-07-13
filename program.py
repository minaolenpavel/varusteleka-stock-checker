#import message_sender
import scrapper

def Main():
    item = scrapper.get_stock("https://www.varusteleka.com/en/product/sarma-tst-general-purpose-pouch-zip-s/61190", "M05 Snow Camo")
    print(item)

if __name__ == "__main__":
    Main()