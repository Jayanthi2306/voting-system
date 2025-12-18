from voting_system import VotingSystem

system = VotingSystem()

system.add_candidate(1, "Alice")
system.add_candidate(2, "Bob")

while True:
    print("\nVoting System")
    print("1. Register Voter")
    print("2. Cast Vote")
    print("3. View Results")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vid = input("Voter ID: ")
        name = input("Name: ")
        print("Registered" if system.register_voter(vid, name) else "Already Exists")

    elif choice == "2":
        vid = input("Voter ID: ")
        cid = int(input("Candidate ID: "))
        print("Vote Cast" if system.cast_vote(vid, cid) else "Invalid / Duplicate Vote")

    elif choice == "3":
        print(system.get_results())

    elif choice == "0":
        break
