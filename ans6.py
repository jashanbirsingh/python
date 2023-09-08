def extract_usernames_and_domains(emails):
    usernames = tuple(email.split('@')[0] for email in emails)
    domains = tuple(email.split('@')[1] for email in emails)
    return usernames, domains

def main():
    n = int(input("Enter the number of students: "))
    email_ids = []

    for i in range(n):
        email = input(f"Enter the email ID for student {i + 1}: ")
        email_ids.append(email)

    email_tuple = tuple(email_ids)
    usernames_tuple, domains_tuple = extract_usernames_and_domains(email_ids)

    print("Email IDs tuple:", email_tuple)
    print("Usernames tuple:", usernames_tuple)
    print("Domains tuple:", domains_tuple)
    
if __name__ == "__main__":
    main()
