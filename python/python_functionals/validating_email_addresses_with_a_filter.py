import re


# email_regex = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$')
# emails = [raw_input() for email in range(int(raw_input()))]
# print sorted(filter(lambda email: re.match(email_regex, email), emails))


def fun(s):
    email_regex = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$')
    return re.match(email_regex, s)
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return filter(fun, emails)


if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails

