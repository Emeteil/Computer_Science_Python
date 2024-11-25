string = """
5
Jack captain
Alice woman
Charlie man
Bob child
Julia woman
""".strip()

priorities = [
    ["woman", "child"],
    ["man"],
    ["captain"]
]

def main():
    string_split = string.split("\n")
    n = int(string_split[0])
    
    peoples = [
        tuple(i.split())
        for i in
        string_split[1:n + 1]
    ]
    
    evacuation = []
    
    for L in priorities:
        for people in peoples:
            if people[1] in L:
                evacuation.append(people[0])
    
    print(*evacuation, sep = "\n")

if __name__ == "__main__":
    main()