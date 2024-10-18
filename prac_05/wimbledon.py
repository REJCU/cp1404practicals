import csv

FILENAME = "wimbledon.csv"
NUM_OF_COUNTRIES = 1
NUM_OF_CHAMPIONS = 2



def main():
    records = get_results(FILENAME)
    champion_to_count, countries = winning_results(records)
    display_results(champion_to_count, countries)


def get_results(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def winning_results(records):
    champions_to_add = {}
    countries = set()
    for record in records:
        countries.add(record[NUM_OF_COUNTRIES])
        try:
            champions_to_add[record[NUM_OF_CHAMPIONS]] += 1
        except KeyError:
            champions_to_add[record[NUM_OF_CHAMPIONS]] = 1
    return champions_to_add, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))




main()