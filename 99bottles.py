def main():
    for bottles in range(99, 0, -1):
        print(f"{bottles} bottles of beer on the wall!")
        print(f"{bottles} bottles of beer! You take one down, pass it around!")

        if bottles - 1 == 1:
            print("1 bottle of beer on the wall!\n")
        else:
            print(f"{bottles - 1} bottles of beer on the wall!\n")
if __name__ == "__main__":
    main()
