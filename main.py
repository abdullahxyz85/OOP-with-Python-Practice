MARS_MULTIPLE = 0.378

def main():
    earth_weight_str = input("Enter their weight on Earth: ")

    earth_weight = float(earth_weight_str)

    mars_weight = earth_weight * MARS_MULTIPLE

    print("The weight on Mars is:" + str(mars_weight))
if __name__ == '__main__':
    main()