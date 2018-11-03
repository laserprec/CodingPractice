# 929. Unique Email Addresses

# Every email consists of a local name and a domain name, separated by the @ sign.

# For example, in alice@leetcode.com, alice is the local name, 
# and leetcode.com is the domain name.

# Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods ('.') between some characters in the local name
#  part of an email address, mail sent there will be forwarded to 
#  the same address without dots in the local name.  For example, 
#  "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the 
#  same email address.  (Note that this rule does not apply for 
#  domain names.)

# If you add a plus ('+') in the local name, everything after the 
# first plus sign will be ignored. This allows certain emails to be 
# filtered, for example m.y+name@email.com will be forwarded to 
# my@email.com.  (Again, this rule does not apply for domain names.)

# Example 1:

# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    s = set()
    for email in emails:
        domain_start = email.find("@")
        domain_name = email[domain_start + 1:]
        username = email[:domain_start]
        # find +
        valid_index = username.find("+")
        username = username[:valid_index]
        # remove all .
        username = username.replace(".", "")
        s.add(username + domain_name)
    return len(s)