"""ของขวัญและขโมย"""
def main():
    """หาโขมย"""
    N, K, T = map(int, input().split())
    person = 1
    find_thief = 1
    while True:
        if person == T:
            print(find_thief)
            break

        person = (person + K) % N

        if person == 1:
            print(find_thief)
            break

        find_thief += 1
main()
