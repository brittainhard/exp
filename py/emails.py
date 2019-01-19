def num_unique_emails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    valid = set()
    for x in emails:
        email, domain = x.split("@")
        email = "".join(email.split("+")[0].split("."))
        print(email)
        valid.add(email + "@" + domain)
    print(valid)
    return len(valid)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(num_unique_emails(emails))
