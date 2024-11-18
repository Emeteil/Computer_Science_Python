import sys

emails_dict = {
    "gryffindor.com": [
        "andrei_serov",
        "alexander_pushkin",
        "elena_belova",
        "k_stepanov"
    ],
    "hufflepuff.com": [
        "alena.semyonova",
        "ivan.polekhin",
        "marina_abrabova"
    ],
    "hogwarts.com": [
        "sergei.zharkov",
        "julia_lyubimova",
        "vitaliy.smirnoff"
    ],
    "slytherin.com": [
        "ekaterina_ivanova",
        "glebova_nastya"
    ],
    "ravenclaw.com": [
        "john.doe",
        "mark.zuckerberg",
        "helen_hunt"
    ]
}

def main():
    emails = set()
    
    for domain, names in emails_dict.items():
        for name in names:
            emails.add(f"{name}@{domain}")
    
    print(*emails, sep = "\n")

if __name__ == "__main__":
    main()